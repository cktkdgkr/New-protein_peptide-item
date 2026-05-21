"""Export Phase D digests into Excel (.xlsx) + Word (.docx).

CLI usage:
    python scripts/export_report.py --mode round --iter 1 --date 20260521
    python scripts/export_report.py --mode round --iter 2 --date 20260521
    python scripts/export_report.py --mode round --iter 3 --date 20260521
    python scripts/export_report.py --mode consolidated --date 20260521

For --mode round:
    Writes iterations/iter_NN/digest.xlsx + .docx
    Mirrors to reports/digest_round_NN_<date>.xlsx + .docx
    Round 1 also writes reports/digest_<date>.xlsx + .docx (backward compat).

For --mode consolidated:
    Writes reports/consolidated_digest_<date>.xlsx + .docx.

Sources of truth:
    - Score / confidence / business_model / lifecycle: per-round CSV (or candidates_history.csv).
    - Narrative blocks (Top 3, signals, risks, next actions): hardcoded per-round
      dictionaries reflecting the markdown digests as of 2026-05-21.
"""
from __future__ import annotations

import argparse
import csv
import sys
from collections import defaultdict
from pathlib import Path
from statistics import mean, pstdev

from openpyxl import Workbook
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.utils import get_column_letter

from docx import Document
from docx.enum.table import WD_ALIGN_VERTICAL
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
from docx.shared import Cm, Pt, RGBColor

ROOT = Path("/home/user/New-protein_peptide-item/protein-item-discovery")

# ---------------------------------------------------------------------------
# Style constants
# ---------------------------------------------------------------------------

HEAD_FILL = PatternFill("solid", fgColor="1F4E78")
HEAD_FONT = Font(name="맑은 고딕", bold=True, color="FFFFFF", size=11)
SUBHEAD_FILL = PatternFill("solid", fgColor="D9E1F2")
SUBHEAD_FONT = Font(name="맑은 고딕", bold=True, size=11)
BODY_FONT = Font(name="맑은 고딕", size=10)
WRAP = Alignment(wrap_text=True, vertical="top")
CENTER = Alignment(wrap_text=True, vertical="center", horizontal="center")
BORDER = Border(*(Side(style="thin", color="BFBFBF") for _ in range(4)))

SHORTLIST_FILL = PatternFill("solid", fgColor="FFF2CC")
SCORE_FILLS = {
    5: PatternFill("solid", fgColor="63BE7B"),
    4: PatternFill("solid", fgColor="B7E1A1"),
    3: PatternFill("solid", fgColor="FFEB84"),
    2: PatternFill("solid", fgColor="FAB58B"),
    1: PatternFill("solid", fgColor="F8696B"),
}
CONFIDENCE_FILLS = {
    "H": PatternFill("solid", fgColor="C6EFCE"),
    "M": PatternFill("solid", fgColor="FFEB9C"),
    "L": PatternFill("solid", fgColor="F4CCCC"),
}


def style_header_row(ws, row_num, ncols):
    for c in range(1, ncols + 1):
        cell = ws.cell(row=row_num, column=c)
        cell.fill = HEAD_FILL
        cell.font = HEAD_FONT
        cell.alignment = CENTER
        cell.border = BORDER


def apply_body_style(ws, row_num, ncols, fill=None):
    for c in range(1, ncols + 1):
        cell = ws.cell(row=row_num, column=c)
        cell.font = BODY_FONT
        cell.alignment = WRAP
        cell.border = BORDER
        if fill:
            cell.fill = fill


def set_col_widths(ws, widths):
    for idx, w in enumerate(widths, start=1):
        ws.column_dimensions[get_column_letter(idx)].width = w


def set_cell_bg(cell, hex_color):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement("w:shd")
    shd.set(qn("w:val"), "clear")
    shd.set(qn("w:color"), "auto")
    shd.set(qn("w:fill"), hex_color)
    tcPr.append(shd)


def add_table(doc, headers, rows, col_widths_cm=None,
              header_bg="1F4E78", header_color=RGBColor(0xFF, 0xFF, 0xFF),
              row_bgs=None):
    table = doc.add_table(rows=len(rows) + 1, cols=len(headers))
    table.style = "Light Grid Accent 1"
    table.autofit = False
    for i, h in enumerate(headers):
        cell = table.cell(0, i)
        cell.text = ""
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run = p.add_run(h)
        run.bold = True
        run.font.size = Pt(10)
        run.font.color.rgb = header_color
        run.font.name = "맑은 고딕"
        set_cell_bg(cell, header_bg)
        cell.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
    for r, row in enumerate(rows, start=1):
        for c, value in enumerate(row):
            cell = table.cell(r, c)
            cell.text = ""
            p = cell.paragraphs[0]
            run = p.add_run(str(value) if value is not None else "")
            run.font.size = Pt(9.5)
            run.font.name = "맑은 고딕"
            cell.vertical_alignment = WD_ALIGN_VERTICAL.TOP
            if row_bgs and r - 1 < len(row_bgs) and row_bgs[r - 1]:
                set_cell_bg(cell, row_bgs[r - 1])
    if col_widths_cm:
        for i, w in enumerate(col_widths_cm):
            for r in range(len(rows) + 1):
                table.cell(r, i).width = Cm(w)
    return table


def add_heading(doc, text, level=1, color=RGBColor(0x1F, 0x4E, 0x78)):
    h = doc.add_paragraph()
    run = h.add_run(text)
    run.bold = True
    run.font.name = "맑은 고딕"
    if level == 0:
        run.font.size = Pt(20); run.font.color.rgb = color
    elif level == 1:
        run.font.size = Pt(15); run.font.color.rgb = color
        h.paragraph_format.space_before = Pt(14)
        h.paragraph_format.space_after = Pt(6)
    elif level == 2:
        run.font.size = Pt(12); run.font.color.rgb = color
        h.paragraph_format.space_before = Pt(10)
    else:
        run.font.size = Pt(11)


def add_para(doc, text, size=10.5, italic=False, bold=False):
    p = doc.add_paragraph()
    run = p.add_run(text)
    run.font.size = Pt(size)
    run.font.name = "맑은 고딕"
    run.italic = italic
    run.bold = bold
    return p


def score_bar(score):
    score = int(score)
    return "█" * score + "░" * (5 - score) + f" {score}/5"


# ---------------------------------------------------------------------------
# CSV readers
# ---------------------------------------------------------------------------

def read_csv_rows(path: Path) -> list[dict]:
    rows = []
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            rows.append(row)
    return rows


def round_csv_path(iter_n: int) -> Path:
    if iter_n == 1:
        return ROOT / "data" / "candidates.csv"
    return ROOT / f"iterations/iter_{iter_n:02d}/data/candidates.csv"


# ---------------------------------------------------------------------------
# Per-round narrative content (hardcoded from md digests)
# ---------------------------------------------------------------------------

ROUND_META = {
    1: {
        "run_id": "20260521-A",
        "focus": "broad_scan",
        "exec_summary": (
            "이번 회차는 단백질·펩타이드 의약 모달리티(SC 항체, ADC, AOC, radioligand, mRNA, GLP-1 peptide)의 "
            "시장 신호 18개를 수집하고, 그로부터 사업화 후보 14개를 도출해 6축 정량 스코어링한 뒤 short-list "
            "7개를 확정했다. 핵심 발견: 빅파마 모달리티 트렌드는 모두 항체·핵산·펩타이드의 결합(conjugation)·"
            "합성(ligation)·후처리(modification) 효소 수요로 수렴하며, 임상 부담 없는 process enzyme "
            "화이트스페이스가 가장 크다."
        ),
        "top3": [
            ("1 (tie)", "item_002", "Engineered mTG (ADC site-specific conjugation)", 4.20,
             "ADC $13.5B + Lonza Visp 2배 확장 + Hzymes가 'enzyme cost'를 산업 통설로 지적 → cost-down 변이체 직접 수요."),
            ("1 (tie)", "item_008", "Peptiligase / OaAEP1 C247A (green peptide ligation)", 4.20,
             "Bachem·PolyPeptide GLP-1 캐파 2배 + Vinnova green chem + OaAEP1 C247A 140× 효율 입증 (PMC11607802)."),
            ("3", "item_007", "Engineered RNA ligase (AOC/ASO splint-ligation)", 4.10,
             "Novartis–Avidity $12B AOC 인수 + Codexis ECO Synthesis 빅파마 첫 수주 = 시장 형성기 + 백색공간 가장 큼."),
        ],
        "delta_vs_prev": "R1은 기준선 (이전 라운드 없음). 14개 후보 평균 가중합 3.50, top-5 SD 0.095.",
    },
    2: {
        "run_id": "20260521-B",
        "focus": "deferred_and_boost",
        "exec_summary": (
            "R2는 R1에서 보류·[추정]이던 5개 영역(TPD reagents / PETase·cutinase / non-PH20 hyaluronidase / "
            "radioligand enzymatic conjugation / mRNA aux 효소)을 표적 스캔해 fresh signal 18개를 추가하고, "
            "부활 후보 2건 + 신규 후보 8건(item_015~022)을 정식 카드화했다. 누적 활성 후보 23개. R1 14개에 "
            "business_model(L/K/C/S/H)·lifecycle 사후 부여 + 모든 6축 점수에 confidence H/M/L 태그 적용. "
            "가장 결정적인 R2 신호: (1) EfHyl8 학계 보고 (JAFC 2025) — non-PH20 SC 확산 효소의 첫 명시적 후보, "
            "(2) ARV-471 FDA 승인 (2026.5.1) + DUBTAC 모달리티화 — TPD 시약 시장의 본격 commercial 진입."
        ),
        "top3": [
            ("1", "item_008", "Peptiligase / OaAEP1 C247A", 4.30,
             "FDA Research-Grade Peptide guidance(2026.1 enforce) → 효소적 ligation이 cGMP 부담 완화 수단으로 가시화. T 3→4. (R1 1위 유지, +0.10)"),
            ("2", "item_002", "Engineered mTG (ADC site-specific)", 4.20,
             "ADC $13.5B + Lonza Visp 2배 확장 — R2 변동 없음 (R1 1위→2위, 점수 동일)."),
            ("3 (tie)", "item_021", "cGMP Sortase A · OaAEP1 (radioligand) [NEW]", 4.10,
             "AZ–Fusion $2.4B 클로징 + Aktis Phase 0 + Research-Grade Peptide guidance의 직접 수혜. R2 신규 진입."),
        ],
        "delta_vs_prev": (
            "R1 → R2 |delta| 최대 0.25 (item_006 T7 RNAP −0.25, CleanCap M6 압박). "
            "+0.10: item_008. R1 14개 외 신규/부활 9개는 R2 첫 스코어. Top-5 SD 0.095→0.117. quality-gate 미발동."
        ),
    },
    3: {
        "run_id": "20260521-C",
        "focus": "quantitative_validation_and_ip_fto",
        "exec_summary": (
            "R3는 R2 23개 후보 전체에 (a) 단가·시장·로열티 정량화, (b) IP/FTO 매핑(Halozyme MDASE vs PL8, "
            "Codexis ligase 청구항, mTG cluster Araris, EnzyPep vs OaAEP1, NEB FCE, NBE SMAC), (c) CDMO RFI "
            "공개 신호(Lonza·Samsung·WuXi·Aldevron·Bachem) 3축을 집중 검증. 신규/병합/드롭 0, 23/23 카드 보강. "
            "가장 결정적 R3 신호: Lonza Advanced Synthesis Synaffix 통합(2026-02-19) — EndoS2 enzymatic glycan "
            "remodel + click이 빅 CDMO ADC GMP 라인 표준 step으로 진입한 공식 confirmation. 점수 변동: 23개 중 "
            "단 2건 — item_002 +0.10 (IP 3→4, M→H), item_021 +0.15 (W 4→5, NBE SMAC carve-out). confidence "
            "M→H 상향 7건 / 5개 후보(모두 short-list)."
        ),
        "top3": [
            ("1 (tie)", "item_002", "Engineered mTG (ADC)", 4.30,
             "Lonza Synaffix 통합 + Samsung-Araris 펀드 + Ajinomoto AJICAP enzyme-free carve-out → IP 3→4 (M→H). +0.10."),
            ("1 (tie)", "item_008", "Peptiligase / OaAEP1 C247A", 4.30,
             "EnzyPep S8 vs OaAEP1 C13 fold carve-out 자명, IP·T·F 모두 H 도달. Top 1 안정화 (변동 0)."),
            ("3", "item_021", "cGMP Sortase A / OaAEP1 (radioligand)", 4.25,
             "NBE SMAC = ADC 한정 → radioligand white-space 확인, W 4→5. RLT $4.8B 2030 정량. +0.15."),
        ],
        "delta_vs_prev": (
            "R2 → R3 |delta| 최대 0.15 (item_021 W 4→5). +0.10: item_002 (IP 3→4). 나머지 21개 raw 변동 0. "
            "confidence M→H 7건 / 5개 후보 (item_002·005·007·008·021, 모두 short-list). "
            "Top-5 SD 0.117→0.136. quality-gate 미발동."
        ),
    },
}


# Fresh signals per round (Top 5 for R2/R3; full 18 for R1).
SIGNALS_R1_TOP5 = [
    ("1",
     "Halozyme 2025 매출 $1.4B(+38%), 로열티 +52% — BMS Opdivo SC EU·argenx VYVGART SC EU·Roche Ocrevus/Tecentriq SC 동시 출시",
     "prnewswire",
     "SC 전환은 빅파마 표준 — hyaluronidase 단일 효소 시장 최대, IP 분쟁(Halozyme vs Merck) 발목."),
    ("2",
     "ADC $13.5B / 15품목 — Gilead–Tubulis $3.15B + Lonza Visp bioconjugation 2배 확장(200명 신규)",
     "bioworld, gilead.com, fiercepharma",
     "차세대 site-specific conjugation 효소(mTG, Sortase, FGE, EndoS2)가 차별화. CDMO 캐파가 효소 채택 견인."),
    ("3",
     "Novartis–Avidity $12B AOC 인수(2025.10) + Codexis ECO Synthesis 빅파마 첫 수주",
     "bioanalysis-zone, SEC 8-K",
     "AOC·olig CDMO enzymatic ligation 시장 형성 — Codexis 외 백색공간 매우 큼."),
    ("4",
     "mRNA 임상 600+ / IVT 효소 시장 $1.8B(2025)→$3.9B(2034); engineered T7 RNAP (low-dsRNA, co-trans cap) Mol Ther 2026",
     "PMC12932865, dataintelo",
     "T7 RNAP·capping enzyme 단일 효소 최대 시장이나 NEB/Aldevron/Trilink 혼잡."),
    ("5",
     "Bachem Vista 1톤/yr SPPS + PolyPeptide €100M 확장 + Vinnova green GLP-1 + OaAEP1 C247A 140× 효율",
     "bachem.com, dcatvci, PMC11607802",
     "GLP-1 시대가 enzymatic peptide ligation을 push — green chem 정책 추가 견인."),
]

SIGNALS_R2_TOP5 = [
    ("1",
     "ARV-471 (vepdegestrant) FDA 승인 (2026.5.1) — oral PROTAC 첫 신약",
     "Biochempeg PROTAC, Promega TPD",
     "PROTAC QC·screening enzyme 시장의 임상→시판 단계 본격 진입. item_018·019·023 직접 동력."),
    ("2",
     "EfHyl8 (E. faecalis PL8 hyaluronate lyase) — JAFC 2025",
     "JAFC2025 EfHyl8, ScienceDirect2025, Springer2024 HylP",
     "비PH20 fold·메커니즘 → Halozyme/Alteogen IP 우회 명분. item_015의 IP=4(H), W=4(H) 핵심 근거."),
    ("3",
     "FCE::T7RNAP fusion + 2′-O-MTase one-pot Cap-1 (NEB·Takara·KACTUS GMP) vs TriLink CleanCap M6",
     "TriLink2025 CleanCap, NEB M2081, KACTUS DMF038029",
     "enzymatic capping이 chemical analog와 cost race. item_006 강등·item_016 신설 직접 원인."),
    ("4",
     "AstraZeneca–Fusion $2.4B 2026 Q1 클로징 + Ac-225 supply 통합 + Aktis Phase 0 + PeptiDream 두번째 program",
     "AZ2024 Fusion, BioSpace2025 PeptiDream",
     "radiopharma 공정 throughput 압박 → cGMP enzymatic conjugation 채택. item_021 신규 진입 직접 동력."),
    ("5",
     "Carbios Wankai JV (50 kt/년) + 프랑스 €1,000/톤 sensitive-contact 보너스 (2025.9) + Epoch Biodesign $50M+",
     "Carbios2025 Wankai, TechCrunch2025 Epoch, Crystals2026 CtCut",
     "PETase·LCC variant의 의약 PET 포장재 ESG incentive. item_020 부활·신설 근거."),
]

SIGNALS_R3_TOP5 = [
    ("1",
     "Lonza Advanced Synthesis Synaffix 통합 (2026-02-19) + dpADC 확장 — EndoS2 glycan remodel + click + HydraSpace가 ADC GMP 표준 step",
     "Lonza2026 AS, ADCReview2026, Synaffix2026 dpADC (H)",
     "빅 CDMO가 enzymatic conjugation을 ADC 표준 플랫폼으로 채택 — item_005·002·003·021 동시 수혜. R3 단일 최대 신호."),
    ("2",
     "Halozyme MDASE = PH20 (GH56, EC 3.2.1.35), EfHyl8 = PL8 (EC 4.2.2.1) — fold·메커니즘·EC 완전 다름; Merck IPR 7건",
     "Halozyme rHuPH20 patent, Halozyme2025 lawsuit, FiercePharma2025 (H)",
     "item_015 EfHyl8 IP=4(H) 회피 자명; Merck IPR 결과는 비PH20 진입장벽 추가 하락 잠재."),
    ("3",
     "EnzyPep peptiligase = subtilisin BPN' Y217 (S8 serine), OaAEP1 = C13 asparaginyl — US10883132B2가 OaAEP1을 직접 위협하지 않음",
     "US10883132B2 Fresenius, US11795488B2, Nature Comm Chem 2024 (H)",
     "item_008 IP=4(M→H), T=4(M→H). Top 1 (4.30) 자리 안정화."),
    ("4",
     "Codexis–Merck $37.8M Supply Assurance (2025-10) + Q1 2024 Roche dsDNA ligase $6.0M + Bachem TIDES 2025 co-presentation",
     "SEC 8-K Codexis 2025Q3, Codexis Q1-2025 (H)",
     "item_007 RNA ligase의 빅파마 직접 라이선싱 매출 검증; ECO Synthesis 사업화 정량 근거 강화."),
    ("5",
     "Alteogen ALT-B4 = 2% net sales royalty 확정 (Keytruda SC, upfront $20M + milestones $432M, peak $15.2B by 2030)",
     "Alteogen royalty 2%, Biospectator2024, Fierce Pharma (H)",
     "비PH20 후발주자(item_015) 협상 ceiling 정량화 — mid-single-digit 대비 보수적 baseline."),
]

ROUND_SIGNALS = {
    1: SIGNALS_R1_TOP5,
    2: SIGNALS_R2_TOP5,
    3: SIGNALS_R3_TOP5,
}

ROUND_RISKS = {
    1: [
        ("데이터 부족", "[추정] 태그 다수 — T7 RNAP $3.9B(2034) 단일 출처, hyaluronidase non-PH20 효능, AOC enzymatic 채택률, GMP peptide ligase·PAM 수요 추정 근거 약함."),
        ("경계 사례", "item_001 hyaluronidase (결합제형 트랙), item_010 IdeS (imlifidase 치료제 존재; QC·연구만), item_013 prime editor (in-vivo 분리; research·ex-vivo만)."),
        ("가정 의존", "mTG/Sortase/EndoS2 채택은 ADC CDMO의 enzymatic conjugation 전환 가정 필요; GMP enzyme $5~30k/g 다수 [추정]."),
        ("IP 분쟁", "Halozyme vs Merck (Keytruda SC), Codexis ECO 청구항, NBE/Boehringer SMAC, EnzyPep peptiligase — FTO 분석 선행 필요."),
        ("누락 가능성", "TPD E3 ligase·PETase는 Phase B에서 제외 — 다음 회차 재검토 권장."),
    ],
    2: [
        ("R1 유지 영역 단가 [추정]", "GMP enzyme $5~30k/g 가정의 출처 다수가 [추정]. R3 정량화 필요."),
        ("IP 분쟁", "Halozyme vs Merck, NBE/Boehringer SMAC, EnzyPep peptiligase, Codexis ECO — FTO 미해결."),
        ("EfHyl8 (item_015)", "SC 확산 효능을 학술적으로 명시했으나 정량 비교 데이터(vs rHuPH20) 미발표. IP 우회 명분만으로는 사업화 불충분."),
        ("FCE::T7RNAP fusion (item_016)", "linker engineering 난이도 미검증. fusion 구성 IP 약함. 공급사 매우 혼잡 (W=2)."),
        ("TPD cascade", "item_018 + item_019 + item_023 3단 계층이 동일 고객을 두고 SKU 자기잠식 위험. R3에서 패키지화 vs 단품 결정 필요."),
        ("item_021 vs item_003/008", "효소 자체 동일, 응용·grade만 다름 → R3에서 통합/carve-out 결정."),
        ("item_006 추가 강등 가능성", "CleanCap M6 채택률 가속 시 M=4→3 추가 강등 → 4번째 OUT 후보 모니터링."),
        ("TPD 시장 $402M", "단일 출처 (AnalystView) — 교차검증 필요."),
    ],
    3: [
        ("EfHyl8 정량 미확보", "specific activity (U/mg), kcat, SC diffusion vs rHuPH20 — full-text 403 차단. PL8 fold carve-out은 명확하나 효능 정량은 R4 과제."),
        ("item_016 FCE fusion IP risk", "NEB Faustovirus 4국가 청구 + H3C2 fusion 자체 청구. linker engineering·Cap-2·dual MTase만 carve-out 가능. IP 3→2 강등 risk 약하게 존재."),
        ("cGMP enzyme 단가 catalog 부재", "mTG/Sortase A/OaAEP1/EndoS2/RNA ligase 모두 quote-only. R3에서도 추정($2~30k/g) 유지."),
        ("WebFetch 403 차단", "SEC EDGAR, PR newswire, PubMed 1차 fetch 4건 모두 실패. WebSearch 요약본 다중 출처 교차로 보완."),
        ("FTO opinion 필요", "R3 IP carve-out은 명세 단계. 변호사 검토 필요 (item_002 mTG, item_021 sortase, item_008 peptiligase)."),
        ("TPD trio cannibalization", "item_018+019+023의 cross-cannibalization risk ~30-50% 추정 — 별도 카드 유지하나 모니터링."),
        ("빅파마 신딜 모니터링", "Halozyme vs Merck IPR 결과 (예정 2026), Keytruda SC FDA 결정 후속, AZ-Alteogen 후속 deal — R4 watch."),
    ],
}

# Short-list cards per round (definition / biz / score / risk / next).
ROUND_SHORTLIST_CARDS = {
    1: [
        {"rank": "1 (tie)", "id": "item_002", "name": "Engineered mTG (ADC site-specific conjugation)",
         "definition": "Streptomyces mTG 변이체로 항체 LLQG-tag glutamine과 amine payload를 isopeptide 결합 → 균일 DAR2/4 ADC 효소적 제조.",
         "biz": "ADC CDMO(Lonza Visp, Samsung Bio, WuXi XDC, AGC, Catalent) + ADC biotech 대상 GMP enzyme kit + Q-tag 설계 + DAR 보증 라이선스. [추정] enzyme $5~15k/g, upfront $1~5M + 로열티 0.5~2%.",
         "biz_model": "K / L",
         "score": {"M": 5, "F": 4, "R": 5, "W": 3, "IP": 3, "T": 4}, "weighted": 4.20,
         "risk": "Hzymes·Ajinomoto·Zedira의 cluster 특허 회피 필요; CDMO의 chemical→enzymatic 전환 가정 의존.",
         "next": "Lonza/Samsung Bio/WuXi XDC에 enzymatic conjugation 채택 의향 RFI; mTG cluster 특허 FTO 분석."},
        {"rank": "1 (tie)", "id": "item_008", "name": "Peptiligase / OaAEP1 C247A — green enzymatic peptide ligation",
         "definition": "Asparaginyl endopeptidase (butelase-1 family) variant — SPPS fragment 2~3개를 효소 ligation해 GLP-1·인슐린·radioligand peptide(32~40mer)를 저용매·고수율로 제조.",
         "biz": "Bachem, PolyPeptide, Lonza Peptides, CordenPharma, Sumitomo, GLP-1 biosimilar 개발사 대상 cGMP enzyme + 공정 라이선스 (EnzyTag/EnzyPep 대안). [추정] enzyme $2~10k/g, upfront $2~10M.",
         "biz_model": "L / K",
         "score": {"M": 5, "F": 4, "R": 5, "W": 3, "IP": 4, "T": 3}, "weighted": 4.20,
         "risk": "EnzyPep peptiligase IP 청구항 회피 필요; cGMP 라이선스 셋업 3~4년.",
         "next": "OaAEP1 C247A vs EnzyPep peptiligase IP 비교; PolyPeptide/Bachem 파트너십 RFI."},
        {"rank": "3", "id": "item_007", "name": "Engineered RNA ligase (splint-ligation, AOC/ASO 합성)",
         "definition": "T4 RNA ligase 2 (Rnl2) 또는 RtcB variant로 splint DNA 가이드 하에 oligo fragment를 결합 → 긴 siRNA/AOC를 fragment ligation으로 저비용 합성.",
         "biz": "올리고 CDMO(Nitto Avecia, GenScript, Bachem oligo, Cytiva)·RNA 치료제 개발사에 cGMP enzyme + ECO Synthesis 스타일 워크플로 라이선스. [추정] enzyme $3~12k/g, upfront $1~5M.",
         "biz_model": "L / K",
         "score": {"M": 4, "F": 4, "R": 5, "W": 4, "IP": 4, "T": 3}, "weighted": 4.10,
         "risk": "Codexis ECO 핵심 청구항 범위; AOC enzymatic 채택률 [추정] 의존.",
         "next": "Codexis ECO Synthesis 특허 청구항 분석; Novartis Avidity 인수 후 oligo CDMO RFI."},
        {"rank": "4", "id": "item_006", "name": "Engineered T7 RNAP variant (low-dsRNA, co-trans capping)",
         "definition": "thumb·finger 변이로 abortive·dsRNA 부산물을 줄이고 co-transcriptional cap1 효율을 높인 directed-evolution T7 RNAP.",
         "biz": "Moderna, Pfizer, BioNTech, CureVac + IVT 효소 supply(Aldevron, Trilink, Maravai, Thermo, NEB)에 cGMP enzyme 직판/라이선스. [추정] $5~30k/g, 시장 $1.8B→$3.9B (2034).",
         "biz_model": "K",
         "score": {"M": 5, "F": 4, "R": 5, "W": 2, "IP": 3, "T": 4}, "weighted": 4.05,
         "risk": "NEB/Aldevron/Trilink/Thermo/Promega 시장 매우 혼잡; academic 특허 다수.",
         "next": "T7 RNAP 차세대 변이체 IP 매핑; mRNA 빅파마 cGMP enzyme spec RFI."},
        {"rank": "5 (tie)", "id": "item_003", "name": "Engineered Sortase A variant (Ca-independent, high-kcat)",
         "definition": "eSrtA 7M/2A-9 등 directed-evolution variant — Ca²⁺ 없이 LPETG motif와 oligoglycine을 isopeptide 결합 → ADC/AOC/radioligand peptide conjugation.",
         "biz": "ADC·AOC·radioligand CDMO + Actithera·Nuclidium 등 radiopharma 스타트업에 enzyme + tag 설계 컨설팅 패키지 (NBE SMAC 대안). [추정] $3~10k/g, upfront $0.5~3M.",
         "biz_model": "L / K",
         "score": {"M": 4, "F": 4, "R": 5, "W": 3, "IP": 3, "T": 4}, "weighted": 3.95,
         "risk": "eSrtA 7M academic IP 풍부 — 차세대 evolution 필수; NBE/Boehringer SMAC 경쟁.",
         "next": "차세대 Sortase IP whitespace 분석; radiopharma 스타트업 RFI."},
        {"rank": "5 (tie)", "id": "item_005", "name": "EndoS2 glycosynthase mutant (Fc glycan remodel)",
         "definition": "S. pyogenes EndoS2 D184M 등 transglycosylation-enhanced glycosynthase — 항체 N297 glycan trim → 균일 G2/G2S2/afucosylated G2 결합 (ADCC 강화, biosimilar 균질화).",
         "biz": "항체·ADC CDMO + Fc engineering biotech + biosimilar 개발사(Celltrion, Sandoz)에 cGMP enzyme + oxazoline donor 패키지 (GlycoConnect 대안).",
         "biz_model": "K / L",
         "score": {"M": 4, "F": 4, "R": 5, "W": 3, "IP": 3, "T": 4}, "weighted": 3.95,
         "risk": "Genovis·Synaffix·NEB 시장 점유; donor sugar 공급망 구축 필요.",
         "next": "EndoS2 변이체 IP 매핑; biosimilar 개발사 glycoform 균질화 수요 RFI."},
        {"rank": "7", "id": "item_009", "name": "Engineered Peptide Amidating Enzyme (PAM, bifunctional)",
         "definition": "PHM (Cu monooxygenase) + PAL (lyase) bifunctional 재조합 효소 — peptide-Gly의 C-terminal glycine을 α-amide로 전환 (GLP-1·calcitonin·oxytocin·radioligand peptide 활성 필수).",
         "biz": "GLP-1 biosimilar + peptide CDMO + radioligand peptide 제조사에 cGMP recombinant PAM 직접 공급. cGMP supplier 사실상 부재 — 화이트스페이스 가장 깨끗.",
         "biz_model": "K / S",
         "score": {"M": 4, "F": 2, "R": 5, "W": 5, "IP": 4, "T": 2}, "weighted": 3.75,
         "risk": "Cu·ascorbate 진핵 발현·capex 큼; cGMP 셋업 4~5년.",
         "next": "Unigene/BELLUS PAM 특허 만료 상태 확인; GMP 발현(P. pastoris/CHO) capex 추정."},
    ],
    2: [
        {"rank": "1", "id": "item_008", "name": "Peptiligase / OaAEP1 C247A — green enzymatic peptide ligation",
         "definition": "Asparaginyl endopeptidase (butelase-1 family) variant — SPPS fragment 효소 ligation으로 GLP-1·인슐린·radioligand peptide 제조.",
         "biz": "Bachem, PolyPeptide, Lonza Peptides, CordenPharma, Sumitomo + GLP-1 biosimilar 개발사 대상 cGMP enzyme + 공정 라이선스. FDA Research-Grade Peptide 2026.1 enforce → T 3→4.",
         "biz_model": "L / K",
         "score": {"M": 5, "F": 4, "R": 5, "W": 3, "IP": 4, "T": 4}, "weighted": 4.30,
         "risk": "EnzyPep peptiligase IP 청구항 회피 필요. R3에서 carve-out 분석 필요.",
         "next": "OaAEP1 C247A vs EnzyPep US10883132B2 청구항 비교 — R3 IP/FTO 1순위."},
        {"rank": "2", "id": "item_002", "name": "Engineered mTG (ADC site-specific)",
         "definition": "Streptomyces mTG 변이체로 항체 LLQG-tag glutamine과 amine payload를 isopeptide 결합 → 균일 DAR2/4 ADC.",
         "biz": "ADC CDMO(Lonza Visp, Samsung Bio, WuXi XDC, AGC, Catalent) + ADC biotech 대상 GMP enzyme + Q-tag 설계 + DAR 보증 라이선스.",
         "biz_model": "K / L",
         "score": {"M": 5, "F": 4, "R": 5, "W": 3, "IP": 3, "T": 4}, "weighted": 4.20,
         "risk": "Ajinomoto/Hzymes/Zedira cluster 특허 회피 필요. R3 FTO 분석 1순위.",
         "next": "mTG cluster FTO 분석; Lonza·Samsung·WuXi XDC RFI."},
        {"rank": "3 (tie)", "id": "item_007", "name": "Engineered RNA ligase (splint, AOC/ASO)",
         "definition": "T4 Rnl2 / RtcB variant로 splint DNA 가이드 fragment ligation → 긴 siRNA·AOC 저비용 합성.",
         "biz": "올리고 CDMO·RNA 치료제 개발사에 cGMP enzyme + ECO Synthesis 워크플로 라이선스.",
         "biz_model": "L / K",
         "score": {"M": 4, "F": 4, "R": 5, "W": 4, "IP": 4, "T": 3}, "weighted": 4.10,
         "risk": "Codexis ECO 핵심 청구항; AOC enzymatic 채택률 추정.",
         "next": "Codexis ECO 청구항 분석; Novartis-Avidity 후속 oligo CDMO RFI."},
        {"rank": "3 (tie)", "id": "item_021", "name": "cGMP Sortase A / OaAEP1 (radioligand peptide-chelator) [NEW]",
         "definition": "cGMP-grade Sortase A LPXTG + OaAEP1 C247A NGL → DOTA/HEHA/NETA chelator를 peptide ligand에 site-specific 결합, ⁶⁴Cu/¹⁷⁷Lu/²²⁵Ac 라벨링.",
         "biz": "Radiopharma CDMO + Actithera·Nuclidium·PeptiDream·AZ-Fusion에 cGMP enzyme + chelator-tag 설계 패키지.",
         "biz_model": "K / L",
         "score": {"M": 4, "F": 4, "R": 5, "W": 4, "IP": 4, "T": 3}, "weighted": 4.10,
         "risk": "item_003/008과 효소 자체 동일 — carve-out 결정 필요. NBE SMAC 청구항 범위 확인 필요.",
         "next": "NBE SMAC WO2014140317A1 청구항 ADC 한정 확인 → radioligand white-space 검증."},
        {"rank": "5 (tie)", "id": "item_003", "name": "Engineered Sortase A (Ca-independent)",
         "definition": "eSrtA 7M/2A-9 directed-evolution variant — Ca²⁺ 없이 LPETG/GGGG isopeptide 결합.",
         "biz": "ADC·AOC·radioligand CDMO + radiopharma 스타트업에 enzyme + tag 설계.",
         "biz_model": "L / K",
         "score": {"M": 4, "F": 4, "R": 5, "W": 3, "IP": 3, "T": 4}, "weighted": 3.95,
         "risk": "academic IP 풍부 — 차세대 evolution 필수; NBE/Boehringer SMAC 경쟁.",
         "next": "차세대 Sortase IP whitespace + commodity화 추세 확인."},
        {"rank": "5 (tie)", "id": "item_005", "name": "EndoS2 glycosynthase mutant",
         "definition": "S. pyogenes EndoS2 D184M class — Fc N297 균일 glycan 결합(ADCC 강화·biosimilar 균질화).",
         "biz": "항체·ADC CDMO + biosimilar 개발사에 cGMP enzyme + oxazoline donor 패키지 (GlycoConnect 대안).",
         "biz_model": "K / L",
         "score": {"M": 4, "F": 4, "R": 5, "W": 3, "IP": 3, "T": 4}, "weighted": 3.95,
         "risk": "Genovis·Synaffix·NEB 시장 점유; donor sugar 공급망 구축 필요.",
         "next": "Lonza Synaffix 통합 후 GMP step 표준화 흐름 확인 (R3)."},
        {"rank": "7", "id": "item_017", "name": "Inorganic pyrophosphatase (IVT helper, GMP non-animal) [NEW]",
         "definition": "Yeast/E. coli PPase — T7 RNAP IVT의 PPi 피드백 억제 해제 → RNA yield +15-25%.",
         "biz": "Captive/Catalog OEM — Hzymes DMF 채택 검증, non-animal source GMP-IVT 시장 진입.",
         "biz_model": "C",
         "score": {"M": 4, "F": 5, "R": 5, "W": 2, "IP": 2, "T": 4}, "weighted": 3.90,
         "risk": "Whitespace 약함(W=2) — non-animal differentiator만 entry point. IP=2.",
         "next": "Hzymes 등 기존 yeast PPase 공급사 catalog 단가 비교."},
    ],
    3: [
        {"rank": "1 (tie)", "id": "item_002", "name": "Engineered mTG (ADC site-specific)",
         "definition": "Streptomyces mTG 변이체로 항체 LLQG-tag / RKAA-tag glutamine과 amine payload를 isopeptide 결합 → 균일 DAR2/4 ADC.",
         "biz": "ADC CDMO(Lonza·Samsung·WuXi XDC)에 GMP mTG enzyme + Q-tag/RKAA-tag 설계 패키지. Ajinomoto AJICAP은 enzyme-free chemical(Lys248)로 비충돌, Araris RKAA-peptide 카브아웃 명확.",
         "biz_model": "K / L",
         "score": {"M": 5, "F": 4, "R": 5, "W": 3, "IP": 4, "T": 4}, "weighted": 4.30,
         "risk": "Zedira/Hzymes commodity mTG와의 차별화 필요; US11786603 narrow-specificity 변이체 white-space 검증 필요.",
         "next": "Lonza Synaffix RFI; Araris RKAA-tag carve-out variant 후속 IP 매핑."},
        {"rank": "1 (tie)", "id": "item_008", "name": "Peptiligase / OaAEP1 C247A",
         "definition": "OaAEP1 (C13 asparaginyl, cysteine) + Peptiligase (subtilisin BPN' Y217, S8 serine) — SPPS fragment 효소 ligation으로 GLP-1·radioligand peptide 제조.",
         "biz": "Bachem CEPS·PolyPeptide·EnzyTag·Sumitomo 대상 cGMP enzyme + 공정 라이선스. EnzyPep US10883132B2 청구항이 OaAEP1을 직접 위협하지 않음 — carve-out 자명.",
         "biz_model": "L / K",
         "score": {"M": 5, "F": 4, "R": 5, "W": 3, "IP": 4, "T": 4}, "weighted": 4.30,
         "risk": "라이선스 ceiling 정량 부재(quote-only); cGMP 셋업 3~4년 유지.",
         "next": "Codexis-Merck Supply Assurance 모델 모방, Bachem CEPS RFI."},
        {"rank": "3", "id": "item_021", "name": "cGMP Sortase A / OaAEP1 (radioligand peptide-chelator)",
         "definition": "cGMP-grade Sortase A LPXTG + OaAEP1 C247A NGL로 DOTA/DOTAGA/NETA chelator를 peptide ligand에 site-specific 결합, ⁶⁴Cu/¹⁷⁷Lu/²²⁵Ac 라벨링.",
         "biz": "Radiopharma CDMO + Actithera·Nuclidium·PeptiDream·AZ-Fusion에 cGMP enzyme. NBE SMAC WO2014140317A1 = ADC 한정 → radioligand white-space 확인.",
         "biz_model": "K / L",
         "score": {"M": 4, "F": 4, "R": 5, "W": 5, "IP": 4, "T": 3}, "weighted": 4.25,
         "risk": "cGMP DMF 등록 3~4년 소요; USPTO 10556024 chelator-tag carve-out 추가 검증 필요.",
         "next": "AZ-Fusion / Aktis cGMP enzymatic conjugation RFI; chelator-tag 변이체 IP whitespace."},
        {"rank": "4", "id": "item_007", "name": "Engineered RNA ligase (splint, AOC/ASO)",
         "definition": "T4 Rnl2 / RtcB variant로 splint DNA 가이드 fragment ligation → 긴 siRNA·AOC 저비용 합성.",
         "biz": "올리고 CDMO·RNA 치료제 개발사에 cGMP enzyme + ECO Synthesis 워크플로 라이선스. Codexis-Merck $37.8M + Roche $6.0M 라이선스 매출 검증.",
         "biz_model": "L / K",
         "score": {"M": 4, "F": 4, "R": 5, "W": 4, "IP": 4, "T": 3}, "weighted": 4.10,
         "risk": "ECO Synthesis 진영 dominance; variant 청구항 carve-out 가능 but 정확 USPTO 번호 미확정.",
         "next": "Codexis ECO 패밀리 USPTO 검색; AOC enzymatic 채택률 R4 추적."},
        {"rank": "5 (tie)", "id": "item_003", "name": "Engineered Sortase A (Ca-independent)",
         "definition": "Caltech eSrtA 7M / 2A-9 directed-evolution variant — US10202593B2.",
         "biz": "ADC·AOC·radioligand CDMO + radiopharma 스타트업에 enzyme + tag 설계 dual track.",
         "biz_model": "L / K",
         "score": {"M": 4, "F": 4, "R": 5, "W": 3, "IP": 3, "T": 4}, "weighted": 3.95,
         "risk": "commodity화 추세 — Sortase A는 academic 풍부, 차세대 evolution 필수.",
         "next": "R4: commodity vs premium variant 단가 비교."},
        {"rank": "5 (tie)", "id": "item_005", "name": "EndoS2 glycosynthase mutant",
         "definition": "S. pyogenes EndoS2 D184M class — 항체 N297 glycan trim → 균일 G2 결합.",
         "biz": "Lonza Synaffix 통합으로 ADC GMP 표준 step 진입. carve-out 변이체(D184M·EndoF/H) catalog 또는 Synaffix 라이선스 대안.",
         "biz_model": "K / L",
         "score": {"M": 4, "F": 4, "R": 5, "W": 3, "IP": 3, "T": 4}, "weighted": 3.95,
         "risk": "Genovis/Synaffix 시장 점유 — donor sugar 공급망 구축 필요.",
         "next": "R4: Lonza Synaffix L primary 격상 검토; biosimilar 개발사 RFI."},
        {"rank": "7", "id": "item_017", "name": "Inorganic pyrophosphatase (IVT helper)",
         "definition": "Yeast PPase — T7 RNAP IVT의 PPi 피드백 억제 해제 → RNA yield +15-25%.",
         "biz": "Captive/Catalog OEM — Hzymes yeast PPase FDA DMF #036853 채택 확정. GMP-IVT $361.9M→$923M 정량.",
         "biz_model": "C",
         "score": {"M": 4, "F": 5, "R": 5, "W": 2, "IP": 2, "T": 4}, "weighted": 3.90,
         "risk": "Whitespace 약함(W=2); IP=2.",
         "next": "Hzymes 외 differentiator (catalytic 변이체) IP 매핑."},
    ],
}

ROUND_NEXT_ACTIONS = {
    1: [
        "TPD E3 ligase / E1 / E2 / deubiquitinase 시약 시장 — PROTAC screening 효소 시장 규모·CRO 채택 신호 보강.",
        "Radioligand peptide-chelator 효소적 conjugation — GMP enzymatic 채택 가능성을 PeptiDream·Aktis·Fusion 공정에서 추적.",
        "mRNA 보조 효소 — capping enzyme(vaccinia/faustovirus), polyA polymerase, RNase H/III 정제용 변이체의 cGMP 시장 신호.",
        "non-PH20 hyaluronidase — leech-derived, chondroitinase 변이체, 세균 hyaluronate lyase의 SC 확산 잠재력 검증.",
        "PETase·MHETase·cutinase의 의약품 PET 포장재 ESG 적용 — 의약 인접성 검증.",
    ],
    2: [
        "EfHyl8 vs rHuPH20 SC 확산 정량 비교 + Halozyme MDASE IP 회피 분석.",
        "mTG cluster 특허(Ajinomoto AJICAP/Hzymes/Zedira/Araris) FTO 분석.",
        "Codexis ECO Synthesis 핵심 청구항 + item_021 radioligand sortase 경쟁자 매핑.",
        "EnzyPep peptiligase US10883132B2 vs OaAEP1 C247A IP claim 비교.",
        "FCE::T7RNAP fusion 발현·활성 균형 학술 검증 + NEB 패밀리 특허 상태.",
        "TPD reagent 시장 $402M 출처 교차검증 + DUBTAC 시약 시장 sizing.",
    ],
    3: [
        "EfHyl8 specific activity(U/mg), kcat, SC diffusion zone(cm²·hr⁻¹) 정량 — R4 1순위.",
        "CDMO RFI 가설 검증(Lonza Visp·Samsung Bio·WuXi XDC IR call 모니터링 또는 컨퍼런스 발표 추적).",
        "item_016 FCE::T7RNAP fusion 패밀리 청구항 심층 분석(NEB H3C2 fusion 청구 범위 확정).",
        "PAM(item_009) cGMP supplier 신호 보강 — white-space 최고이나 검증 데이터 부족.",
        "AI-designed enzyme(item_014) customer case 6~12개월 누적 후 재검토(RFdiffusion3 오픈소스 후 신호 추적).",
        "Halozyme vs Merck IPR 7건 결과 모니터링 — 일부 MDASE 청구항 무효화 시 비PH20 진입장벽 추가 하락.",
    ],
}

# ---------------------------------------------------------------------------
# Per-round Excel builder
# ---------------------------------------------------------------------------

def build_round_xlsx(iter_n: int, date: str, out_path: Path):
    out_path.parent.mkdir(parents=True, exist_ok=True)
    meta = ROUND_META[iter_n]
    scoring = read_csv_rows(round_csv_path(iter_n))
    signals = ROUND_SIGNALS[iter_n]
    risks = ROUND_RISKS[iter_n]
    shortlist_cards = ROUND_SHORTLIST_CARDS[iter_n]
    next_actions = ROUND_NEXT_ACTIONS[iter_n]
    has_bm_lifecycle = iter_n >= 2  # R2/R3 csv has business_model_*, lifecycle, confidence_*

    wb = Workbook()

    # ---- Sheet 1: 요약 ----
    ws = wb.active
    ws.title = "1.요약"
    ws["A1"] = f"Protein/Peptide Item Discovery — Round {iter_n} Digest 2026-05-21"
    ws["A1"].font = Font(name="맑은 고딕", bold=True, size=16, color="1F4E78")
    ws.row_dimensions[1].height = 28
    ws["A2"] = f"run_id: {meta['run_id']}   |   focus: {meta['focus']}   |   scope SSOT: scope/inclusion.md · scope/exclusion.md"
    ws["A2"].font = Font(name="맑은 고딕", italic=True, size=10, color="595959")

    ws["A4"] = "▣ Executive Summary"
    ws["A4"].font = SUBHEAD_FONT
    ws.merge_cells("A5:F9")
    ws["A5"] = meta["exec_summary"]
    ws["A5"].alignment = WRAP
    ws["A5"].font = BODY_FONT

    ws["A11"] = "▣ Top 3 Short-list"
    ws["A11"].font = SUBHEAD_FONT
    headers = ["순위", "id", "아이템", "가중합", "한 줄 추천 사유"]
    for i, h in enumerate(headers, start=1):
        ws.cell(row=12, column=i, value=h)
    style_header_row(ws, 12, len(headers))
    for r, (rank, cid, name, sc, why) in enumerate(meta["top3"], start=13):
        ws.cell(row=r, column=1, value=rank)
        ws.cell(row=r, column=2, value=cid)
        ws.cell(row=r, column=3, value=name)
        ws.cell(row=r, column=4, value=sc)
        ws.cell(row=r, column=5, value=why)
        apply_body_style(ws, r, 5, fill=SHORTLIST_FILL)
        ws.row_dimensions[r].height = 48

    base = 13 + len(meta["top3"]) + 1
    ws.cell(row=base, column=1, value=f"▣ R{iter_n-1 if iter_n > 1 else 0}→R{iter_n} delta 요약" if iter_n > 1 else "▣ Round 1 (기준선)").font = SUBHEAD_FONT
    ws.merge_cells(start_row=base+1, start_column=1, end_row=base+3, end_column=5)
    ws.cell(row=base+1, column=1, value=meta["delta_vs_prev"]).alignment = WRAP
    ws.cell(row=base+1, column=1).font = BODY_FONT

    set_col_widths(ws, [12, 12, 38, 10, 58])

    # ---- Sheet 2: 시장 신호 ----
    ws2 = wb.create_sheet("2.시장신호")
    cols = ["#", "신호", "출처", "함의"]
    for i, h in enumerate(cols, start=1):
        ws2.cell(row=1, column=i, value=h)
    style_header_row(ws2, 1, len(cols))
    for r, row in enumerate(signals, start=2):
        for c, v in enumerate(row, start=1):
            ws2.cell(row=r, column=c, value=v)
        apply_body_style(ws2, r, len(cols))
        ws2.row_dimensions[r].height = 60
    set_col_widths(ws2, [5, 65, 28, 50])
    ws2.freeze_panes = "A2"

    # ---- Sheet 3: 후보 long-list ----
    ws3 = wb.create_sheet("3.후보longlist")
    if has_bm_lifecycle:
        cols = ["id", "아이템", "class (EC)", "inclusion_bucket", "biz_primary", "biz_secondary", "lifecycle", "rank", "shortlist"]
    else:
        cols = ["id", "아이템", "class (EC)", "inclusion_bucket", "rank", "shortlist"]
    for i, h in enumerate(cols, start=1):
        ws3.cell(row=1, column=i, value=h)
    style_header_row(ws3, 1, len(cols))
    sorted_sc = sorted(scoring, key=lambda r: int(r["rank"]))
    for r, row in enumerate(sorted_sc, start=2):
        if has_bm_lifecycle:
            values = [row["id"], row["item_name"], row["class"], row["inclusion_bucket"],
                      row.get("business_model_primary", ""), row.get("business_model_secondary", ""),
                      row.get("lifecycle", ""), int(row["rank"]),
                      "✓" if row["shortlist"] == "1" else ""]
        else:
            values = [row["id"], row["item_name"], row["class"], row["inclusion_bucket"],
                      int(row["rank"]), "✓" if row["shortlist"] == "1" else ""]
        for c, v in enumerate(values, start=1):
            ws3.cell(row=r, column=c, value=v)
        fill = SHORTLIST_FILL if row["shortlist"] == "1" else None
        apply_body_style(ws3, r, len(cols), fill=fill)
        ws3.row_dimensions[r].height = 38
    if has_bm_lifecycle:
        set_col_widths(ws3, [10, 50, 32, 22, 11, 11, 22, 6, 9])
    else:
        set_col_widths(ws3, [10, 50, 32, 22, 6, 9])
    ws3.freeze_panes = "A2"

    # ---- Sheet 4: 스코어링 ----
    ws4 = wb.create_sheet("4.스코어링")
    if has_bm_lifecycle:
        cols = ["rank", "id", "아이템", "M", "cM", "F", "cF", "R", "cR", "W", "cW", "IP", "cIP", "T", "cT",
                "가중합", "delta", "shortlist", "biz", "lifecycle"]
    else:
        cols = ["rank", "id", "아이템", "M", "F", "R", "W", "IP", "T", "가중합", "shortlist"]
    for i, h in enumerate(cols, start=1):
        ws4.cell(row=1, column=i, value=h)
    style_header_row(ws4, 1, len(cols))
    axes = [("market", "confidence_market"), ("feasibility", "confidence_feasibility"),
            ("regulatory", "confidence_regulatory"), ("whitespace", "confidence_whitespace"),
            ("ip", "confidence_ip"), ("time", "confidence_time")]
    for r, row in enumerate(sorted_sc, start=2):
        ws4.cell(row=r, column=1, value=int(row["rank"]))
        ws4.cell(row=r, column=2, value=row["id"])
        ws4.cell(row=r, column=3, value=row["item_name"])
        col = 4
        for key, conf_key in axes:
            s = int(row[key])
            cell = ws4.cell(row=r, column=col, value=s)
            cell.alignment = CENTER
            cell.font = Font(name="맑은 고딕", size=10, bold=True)
            cell.fill = SCORE_FILLS[s]
            cell.border = BORDER
            col += 1
            if has_bm_lifecycle:
                conf = row.get(conf_key, "")
                cc = ws4.cell(row=r, column=col, value=conf)
                cc.alignment = CENTER
                cc.font = Font(name="맑은 고딕", size=9, bold=True)
                if conf in CONFIDENCE_FILLS:
                    cc.fill = CONFIDENCE_FILLS[conf]
                cc.border = BORDER
                col += 1
        # weighted
        cell = ws4.cell(row=r, column=col, value=float(row["weighted_score"]))
        cell.alignment = CENTER
        cell.font = Font(name="맑은 고딕", size=10, bold=True)
        cell.number_format = "0.00"
        cell.border = BORDER
        col += 1
        if has_bm_lifecycle:
            delta_val = row.get("delta_from_prev", "")
            try:
                delta_f = float(delta_val) if delta_val else 0.0
            except ValueError:
                delta_f = 0.0
            cell = ws4.cell(row=r, column=col, value=delta_f if delta_val else "")
            cell.alignment = CENTER
            cell.font = Font(name="맑은 고딕", size=10, bold=True,
                             color=("C00000" if delta_f < 0 else ("006100" if delta_f > 0 else "595959")))
            cell.number_format = "+0.00;-0.00;0.00"
            cell.border = BORDER
            col += 1
        # shortlist
        cell = ws4.cell(row=r, column=col, value="✓" if row["shortlist"] == "1" else "")
        cell.alignment = CENTER
        cell.font = Font(name="맑은 고딕", size=12, bold=True, color="C00000")
        cell.border = BORDER
        col += 1
        if has_bm_lifecycle:
            bm = (row.get("business_model_primary", "") +
                  (f"/{row.get('business_model_secondary')}" if row.get("business_model_secondary") else ""))
            ws4.cell(row=r, column=col, value=bm)
            col += 1
            ws4.cell(row=r, column=col, value=row.get("lifecycle", ""))
            col += 1
        # body cells for non-score columns
        for cc in (1, 2, 3):
            cell = ws4.cell(row=r, column=cc)
            cell.font = BODY_FONT
            cell.alignment = WRAP
            cell.border = BORDER
        if has_bm_lifecycle:
            for cc in (col - 2, col - 1):
                cell = ws4.cell(row=r, column=cc)
                cell.font = BODY_FONT
                cell.alignment = WRAP
                cell.border = BORDER
        if row["shortlist"] == "1":
            for cc in (1, 2, 3):
                cell = ws4.cell(row=r, column=cc)
                if cell.fill.fgColor.rgb in (None, "00000000"):
                    cell.fill = SHORTLIST_FILL
        ws4.row_dimensions[r].height = 38
    if has_bm_lifecycle:
        set_col_widths(ws4, [6, 10, 40, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 8, 8, 9, 11, 24])
    else:
        set_col_widths(ws4, [6, 10, 50, 7, 7, 7, 7, 7, 7, 9, 10])
    ws4.freeze_panes = "C2"

    # gauges / weights note
    note_row = len(sorted_sc) + 4
    ws4.cell(row=note_row, column=1, value="가중치 / 산식 / 색상").font = SUBHEAD_FONT
    notes = [
        "가중치: M 0.25 / F 0.20 / R 0.20 / W 0.15 / IP 0.10 / T 0.10",
        "weighted_score = Σ(score_i × weight_i), 5점 만점",
        "셀 색(점수): 5(진녹) → 4(연녹) → 3(노랑) → 2(주황) → 1(빨강)",
    ]
    if has_bm_lifecycle:
        notes.append("confidence: H(연녹) / M(노랑) / L(연주황). cM~cT 컬럼은 각 축의 confidence 태그.")
    for i, n in enumerate(notes, start=1):
        ws4.cell(row=note_row + i, column=1, value=n).font = BODY_FONT

    # ---- Sheet 5: Short-list 상세 ----
    ws5 = wb.create_sheet("5.ShortList상세")
    cols = ["rank", "id", "아이템", "biz_model", "정의", "사업화 시나리오",
            "M", "F", "R", "W", "IP", "T", "가중합", "위험·미지수", "다음 액션"]
    for i, h in enumerate(cols, start=1):
        ws5.cell(row=1, column=i, value=h)
    style_header_row(ws5, 1, len(cols))
    for r, item in enumerate(shortlist_cards, start=2):
        ws5.cell(row=r, column=1, value=item["rank"])
        ws5.cell(row=r, column=2, value=item["id"])
        ws5.cell(row=r, column=3, value=item["name"])
        ws5.cell(row=r, column=4, value=item["biz_model"])
        ws5.cell(row=r, column=5, value=item["definition"])
        ws5.cell(row=r, column=6, value=item["biz"])
        for c, k in enumerate(["M", "F", "R", "W", "IP", "T"], start=7):
            s = item["score"][k]
            cell = ws5.cell(row=r, column=c, value=s)
            cell.alignment = CENTER
            cell.font = Font(name="맑은 고딕", size=10, bold=True)
            cell.fill = SCORE_FILLS[s]
            cell.border = BORDER
        cell = ws5.cell(row=r, column=13, value=item["weighted"])
        cell.alignment = CENTER
        cell.font = Font(name="맑은 고딕", size=10, bold=True)
        cell.number_format = "0.00"
        cell.border = BORDER
        ws5.cell(row=r, column=14, value=item["risk"])
        ws5.cell(row=r, column=15, value=item["next"])
        for c in (1, 2, 3, 4, 5, 6, 14, 15):
            cell = ws5.cell(row=r, column=c)
            cell.font = BODY_FONT
            cell.alignment = WRAP
            cell.border = BORDER
            cell.fill = SHORTLIST_FILL
        ws5.row_dimensions[r].height = 120
    set_col_widths(ws5, [10, 10, 32, 10, 50, 60, 5, 5, 5, 5, 5, 5, 8, 38, 38])
    ws5.freeze_panes = "C2"

    # ---- Sheet 6: Round 차이 / 위험 ----
    ws6 = wb.create_sheet("6.Round차이·위험")
    ws6["A1"] = f"▣ R{iter_n-1 if iter_n > 1 else 0}→R{iter_n} 차이 / Quality-gate" if iter_n > 1 else "▣ Round 1 기준선 / Quality-gate"
    ws6["A1"].font = SUBHEAD_FONT
    ws6.merge_cells("A2:B4")
    ws6["A2"] = meta["delta_vs_prev"]
    ws6["A2"].alignment = WRAP
    ws6["A2"].font = BODY_FONT
    ws6["A2"].border = BORDER

    ws6["A6"] = "▣ 위험·미지수"
    ws6["A6"].font = SUBHEAD_FONT
    for i, h in enumerate(["영역", "내용"], start=1):
        ws6.cell(row=7, column=i, value=h)
    style_header_row(ws6, 7, 2)
    for r, (area, content) in enumerate(risks, start=8):
        ws6.cell(row=r, column=1, value=area)
        ws6.cell(row=r, column=2, value=content)
        apply_body_style(ws6, r, 2)
        ws6.row_dimensions[r].height = 50

    next_start = 8 + len(risks) + 2
    ws6.cell(row=next_start, column=1, value=f"▣ 다음 라운드 (R{iter_n+1}) 제안 / focus 영역").font = SUBHEAD_FONT
    for i, action in enumerate(next_actions, start=1):
        ws6.cell(row=next_start + i, column=1, value="•")
        ws6.cell(row=next_start + i, column=2, value=action)
        apply_body_style(ws6, next_start + i, 2)
        ws6.cell(row=next_start + i, column=1).alignment = CENTER
        ws6.row_dimensions[next_start + i].height = 36
    set_col_widths(ws6, [22, 110])

    # ---- Sheet 7: 메타 ----
    ws7 = wb.create_sheet("7.메타")
    weighted_scores = [float(r["weighted_score"]) for r in scoring]
    top5_scores = sorted(weighted_scores, reverse=True)[:5]
    sd_val = pstdev(top5_scores) if len(top5_scores) > 1 else 0.0
    meta_rows = [
        ("run_id", meta["run_id"]),
        ("실행일", "2026-05-21 (UTC)"),
        ("focus", meta["focus"]),
        ("후보 수 (활성)", str(len(scoring))),
        ("Short-list 수", str(sum(1 for r in scoring if r["shortlist"] == "1"))),
        ("평균 가중합", f"{mean(weighted_scores):.3f}"),
        ("Top-5 가중합", ", ".join(f"{s:.2f}" for s in top5_scores)),
        ("Top-5 평균 / SD", f"{mean(top5_scores):.3f} / {sd_val:.3f}"),
        ("Quality-gate", "미발동 (Top-5 SD < 0.15, |delta| < 1.0)" if iter_n > 1 else "미적용 (R1 기준선)"),
        ("입력 파일",
         f"iterations/iter_{iter_n:02d}/pipeline/{{01,02,03}}_*.md, {round_csv_path(iter_n).relative_to(ROOT)}, state/run_state.json"
         if iter_n > 1 else "pipeline/{01,02,03}_*.md, data/candidates.csv, state/run_state.json"),
    ]
    for i, h in enumerate(["항목", "값"], start=1):
        ws7.cell(row=1, column=i, value=h)
    style_header_row(ws7, 1, 2)
    for r, (k, v) in enumerate(meta_rows, start=2):
        ws7.cell(row=r, column=1, value=k).font = Font(name="맑은 고딕", bold=True, size=10)
        ws7.cell(row=r, column=2, value=v).font = BODY_FONT
        ws7.cell(row=r, column=1).alignment = WRAP
        ws7.cell(row=r, column=2).alignment = WRAP
        ws7.cell(row=r, column=1).border = BORDER
        ws7.cell(row=r, column=2).border = BORDER
        ws7.row_dimensions[r].height = 28
    set_col_widths(ws7, [22, 110])

    wb.save(out_path)


# ---------------------------------------------------------------------------
# Per-round Word builder
# ---------------------------------------------------------------------------

def build_round_docx(iter_n: int, date: str, out_path: Path):
    out_path.parent.mkdir(parents=True, exist_ok=True)
    meta = ROUND_META[iter_n]
    scoring = read_csv_rows(round_csv_path(iter_n))
    signals = ROUND_SIGNALS[iter_n]
    risks = ROUND_RISKS[iter_n]
    shortlist_cards = ROUND_SHORTLIST_CARDS[iter_n]
    next_actions = ROUND_NEXT_ACTIONS[iter_n]
    has_bm = iter_n >= 2

    doc = Document()
    for section in doc.sections:
        section.left_margin = Cm(2.0)
        section.right_margin = Cm(2.0)
        section.top_margin = Cm(2.0)
        section.bottom_margin = Cm(2.0)

    add_heading(doc, f"Protein/Peptide Item Discovery — Round {iter_n} Digest 2026-05-21", level=0)
    add_para(doc, f"run_id: {meta['run_id']}   |   focus: {meta['focus']}   |   scope SSOT: scope/inclusion.md · scope/exclusion.md",
             size=9.5, italic=True)

    # 1 요약
    add_heading(doc, f"1. Round {iter_n} 한 페이지 요약")
    add_para(doc, meta["exec_summary"])
    add_heading(doc, "Top 3 Short-list", level=2)
    add_table(
        doc,
        headers=["순위", "id", "아이템", "가중합", "한 줄 사유"],
        rows=[(r, cid, n, f"{s:.2f}", w) for r, cid, n, s, w in meta["top3"]],
        col_widths_cm=[1.5, 1.6, 5.5, 1.3, 7.1],
        row_bgs=["FFF2CC"] * len(meta["top3"]),
    )
    add_heading(doc, f"R{iter_n-1 if iter_n > 1 else 0}→R{iter_n} delta 요약" if iter_n > 1 else "R1 기준선", level=2)
    add_para(doc, meta["delta_vs_prev"])

    # 2 시장 신호
    add_heading(doc, "2. 시장 신호 (Top 5)")
    add_table(
        doc,
        headers=["#", "신호", "출처", "함의"],
        rows=signals,
        col_widths_cm=[0.8, 7.5, 2.8, 5.9],
    )

    # 3 후보 long-list
    add_heading(doc, "3. 후보 Long-list")
    sorted_sc = sorted(scoring, key=lambda r: int(r["rank"]))
    rows = []
    bgs = []
    for row in sorted_sc:
        if has_bm:
            rows.append((
                int(row["rank"]),
                row["id"],
                row["item_name"][:50] + ("…" if len(row["item_name"]) > 50 else ""),
                row["inclusion_bucket"],
                row.get("business_model_primary", "") + ("/" + row.get("business_model_secondary", "") if row.get("business_model_secondary") else ""),
                row.get("lifecycle", "").replace("_", " "),
                "✓" if row["shortlist"] == "1" else "",
            ))
        else:
            rows.append((
                int(row["rank"]),
                row["id"],
                row["item_name"][:60] + ("…" if len(row["item_name"]) > 60 else ""),
                row["inclusion_bucket"],
                "✓" if row["shortlist"] == "1" else "",
            ))
        bgs.append("FFF2CC" if row["shortlist"] == "1" else None)
    if has_bm:
        add_table(
            doc,
            headers=["rank", "id", "아이템", "분류", "biz", "lifecycle", "SL"],
            rows=rows,
            col_widths_cm=[1.0, 1.7, 6.0, 2.3, 1.5, 3.4, 1.1],
            row_bgs=bgs,
        )
    else:
        add_table(
            doc,
            headers=["rank", "id", "아이템", "분류", "SL"],
            rows=rows,
            col_widths_cm=[1.0, 1.7, 9.5, 2.5, 1.3],
            row_bgs=bgs,
        )

    # 4 스코어링
    add_heading(doc, "4. 6축 스코어링")
    add_para(doc, "가중치: M 0.25 / F 0.20 / R 0.20 / W 0.15 / IP 0.10 / T 0.10. 가중합 5점 만점.",
             size=10, italic=True)
    score_rows = []
    score_bgs = []
    for row in sorted_sc:
        if has_bm:
            score_rows.append((
                int(row["rank"]),
                row["id"],
                f"{row['market']} ({row.get('confidence_market', '?')})",
                f"{row['feasibility']} ({row.get('confidence_feasibility', '?')})",
                f"{row['regulatory']} ({row.get('confidence_regulatory', '?')})",
                f"{row['whitespace']} ({row.get('confidence_whitespace', '?')})",
                f"{row['ip']} ({row.get('confidence_ip', '?')})",
                f"{row['time']} ({row.get('confidence_time', '?')})",
                f"{float(row['weighted_score']):.2f}",
                row.get("delta_from_prev", "0.00") or "0.00",
                "✓" if row["shortlist"] == "1" else "",
            ))
        else:
            score_rows.append((
                int(row["rank"]),
                row["id"],
                row["market"], row["feasibility"], row["regulatory"],
                row["whitespace"], row["ip"], row["time"],
                f"{float(row['weighted_score']):.2f}",
                "✓" if row["shortlist"] == "1" else "",
            ))
        score_bgs.append("FFF2CC" if row["shortlist"] == "1" else None)
    if has_bm:
        add_table(
            doc,
            headers=["rank", "id", "M(c)", "F(c)", "R(c)", "W(c)", "IP(c)", "T(c)", "가중합", "Δ", "SL"],
            rows=score_rows,
            col_widths_cm=[0.8, 1.5, 1.4, 1.4, 1.4, 1.4, 1.4, 1.4, 1.3, 1.0, 0.8],
            row_bgs=score_bgs,
        )
    else:
        add_table(
            doc,
            headers=["rank", "id", "M", "F", "R", "W", "IP", "T", "가중합", "SL"],
            rows=score_rows,
            col_widths_cm=[1.0, 1.7, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 1.3, 0.9],
            row_bgs=score_bgs,
        )

    # 5 short-list 상세
    add_heading(doc, "5. Short-list 상세")
    for item in shortlist_cards:
        add_heading(doc, f"#{item['rank']} {item['id']} — {item['name']}  [{item['biz_model']}]", level=2)
        add_para(doc, f"정의: {item['definition']}")
        add_para(doc, f"사업화: {item['biz']}")
        bar_lines = "  ".join(f"{k} {score_bar(item['score'][k])}" for k in ["M", "F", "R", "W", "IP", "T"])
        p = doc.add_paragraph()
        run = p.add_run(bar_lines + f"   →   가중합 {item['weighted']:.2f}")
        run.font.name = "Consolas"
        run.font.size = Pt(9)
        add_para(doc, f"위험: {item['risk']}", size=10)
        add_para(doc, f"다음 액션: {item['next']}", size=10)

    # 6 round 차이 / 위험
    add_heading(doc, "6. Round 차이 / 위험")
    add_table(
        doc,
        headers=["영역", "내용"],
        rows=risks,
        col_widths_cm=[3.2, 13.8],
    )

    # 7 다음 라운드 제안
    add_heading(doc, f"7. 다음 라운드 (R{iter_n+1}) 제안" if iter_n < 3 else "7. R4+ 제안 / open questions")
    for a in next_actions:
        doc.add_paragraph(a, style="List Bullet")

    # 8 메타
    add_heading(doc, "8. 메타")
    weighted_scores = [float(r["weighted_score"]) for r in scoring]
    top5_scores = sorted(weighted_scores, reverse=True)[:5]
    sd_val = pstdev(top5_scores) if len(top5_scores) > 1 else 0.0
    meta_rows = [
        ("run_id", meta["run_id"]),
        ("실행일", "2026-05-21 (UTC)"),
        ("focus", meta["focus"]),
        ("후보 수 (활성)", str(len(scoring))),
        ("Short-list 수", str(sum(1 for r in scoring if r["shortlist"] == "1"))),
        ("Top-5 가중합", ", ".join(f"{s:.2f}" for s in top5_scores)),
        ("Top-5 평균 / SD", f"{mean(top5_scores):.3f} / {sd_val:.3f}"),
        ("Quality-gate", "미발동" if iter_n > 1 else "미적용 (R1 기준선)"),
    ]
    add_table(doc, headers=["항목", "값"], rows=meta_rows, col_widths_cm=[3.5, 13.5])

    doc.save(out_path)


# ---------------------------------------------------------------------------
# Consolidated builders
# ---------------------------------------------------------------------------

CONSOLIDATED_META = {
    "exec_summary": (
        "3라운드 동안 단백질·펩타이드 process/formulation/diagnostic 효소 시장에서 누적 활성 후보 23개"
        "(R1 14 → R2 +8 신규 +1 부활 = 23 → R3 23 유지)를 발굴·평가하고 누적 short-list 7개(★★★ 5 + ★★ 2)"
        "를 확정했다. R3 short-list 7명 전원이 R2 멤버와 동일 — ranking 수렴 강함. "
        "공통 패러다임: 빅파마 modality 트렌드는 모두 결합(conjugation)·합성(ligation)·후처리(modification) 효소 "
        "수요로 수렴하며, 임상 부담 없는 process enzyme이 가장 큰 화이트스페이스를 보유한다. "
        "R3 결정적 결론: Lonza Synaffix 통합(2026-02-19) = enzymatic ADC conjugation 빅 CDMO 표준 채택 확정; "
        "EfHyl8 PL8 vs Halozyme PH20 IP 회피 자명; EnzyPep S8 vs OaAEP1 C13 carve-out 자명; "
        "NBE SMAC = ADC 한정, radioligand white-space 확인."
    ),
    "top3": [
        ("1 (tie)", "item_002", "Engineered mTG (ADC)", 4.30, "★★★",
         "3라운드 연속 short-list 1·2위. Lonza+Samsung+Araris 자본 흐름 + AJICAP carve-out 명확."),
        ("1 (tie)", "item_008", "Peptiligase / OaAEP1 C247A", 4.30, "★★★",
         "3라운드 연속 Top 1 또는 공동 1위. EnzyPep vs OaAEP1 fold carve-out 자명 + FDA Research-Grade Peptide 2026.1 enforce."),
        ("3", "item_021", "cGMP Sortase A / OaAEP1 (radioligand)", 4.25, "★★",
         "R2 신규 등장 → R3에서 +0.15 상승. NBE SMAC carve-out + RLT $4.8B 2030."),
    ],
    "shortlist_history": {
        # id : {iter: weighted, ...}
        "item_002": {1: 4.20, 2: 4.20, 3: 4.30},
        "item_003": {1: 3.95, 2: 3.95, 3: 3.95},
        "item_005": {1: 3.95, 2: 3.95, 3: 3.95},
        "item_006": {1: 4.05, 2: 3.80, 3: 3.80},  # R1 only short-list
        "item_007": {1: 4.10, 2: 4.10, 3: 4.10},
        "item_008": {1: 4.20, 2: 4.30, 3: 4.30},
        "item_009": {1: 3.75, 2: 3.75, 3: 3.75},  # R1 only short-list
        "item_017": {2: 3.90, 3: 3.90},
        "item_021": {2: 4.10, 3: 4.25},
    },
    "shortlist_membership": {
        # id : (R1, R2, R3) booleans
        "item_002": (True, True, True),
        "item_003": (True, True, True),
        "item_005": (True, True, True),
        "item_006": (True, False, False),
        "item_007": (True, True, True),
        "item_008": (True, True, True),
        "item_009": (True, False, False),
        "item_017": (False, True, True),
        "item_021": (False, True, True),
    },
    "names": {
        "item_002": "Engineered mTG (ADC)",
        "item_003": "Engineered Sortase A (Ca-independent)",
        "item_005": "EndoS2 glycosynthase mutant",
        "item_006": "Engineered T7 RNAP (low-dsRNA, capping)",
        "item_007": "Engineered RNA ligase (splint)",
        "item_008": "Peptiligase / OaAEP1 C247A",
        "item_009": "Engineered Peptide Amidating Enzyme (PAM)",
        "item_017": "Inorganic pyrophosphatase (IVT helper)",
        "item_021": "cGMP Sortase A / OaAEP1 (radioligand)",
    },
    "recommendations": {
        "immediate": [
            ("1", "item_002", "Engineered mTG (ADC)", "★★★", 4.30, "K/L",
             "Lonza Synaffix·Samsung·WuXi XDC ADC CDMO에 GMP mTG + Q-tag/RKAA-tag 패키지. ADC $32.66B 2035."),
            ("2", "item_017", "Inorganic pyrophosphatase", "★★", 3.90, "C",
             "Yeast non-animal PPase OEM, Hzymes DMF #036853 채택. GMP-IVT $923M 2034."),
            ("3", "item_005", "EndoS2 glycosynthase", "★★★", 3.95, "K/L",
             "Lonza Synaffix 통합 ADC GMP 표준 step. carve-out 변이체 catalog 또는 Synaffix 대안."),
        ],
        "mid_term": [
            ("1", "item_008", "Peptiligase / OaAEP1 C247A", "★★★", 4.30, "L/K",
             "EnzyPep S8 vs OaAEP1 C13 carve-out 자명. Bachem CEPS·PolyPeptide·EnzyTag. FDA RGP 2026.1 enforce."),
            ("2", "item_007", "Engineered RNA ligase", "★★★", 4.10, "L/K",
             "Codexis-Merck $37.8M + Roche $6.0M 라이선스 매출 검증. AOC 시장 형성기."),
            ("3", "item_003", "Engineered Sortase A", "★★★", 3.95, "L/K",
             "Caltech eSrtA US10202593B2 + commodity화. ADC + radioligand fork."),
        ],
        "long_term": [
            ("1", "item_021", "cGMP Sortase A / OaAEP1 (radioligand)", "★★", 4.25, "K/L",
             "RLT $4.8B 2030 + AZ-Fusion $2.4B. NBE SMAC = ADC 한정. cGMP DMF 등록 3~4년."),
            ("2", "item_015", "EfHyl8 PL8 (non-PH20)", "(R4 priority)", 3.40, "K/L",
             "PL8 vs PH20 IP 회피 자명. Merck IPR 7건 + Alteogen 2% royalty ceiling. specific activity R4 확보 후."),
            ("3", "item_009", "Engineered PAM", "★ (R1)", 3.75, "K/S",
             "GLP-1·radioligand C-term amide 필수, cGMP supplier 부재 = 화이트스페이스 최고. 진핵 발현 capex 큼."),
            ("4", "item_004", "FGE (aldehyde-tag)", "(등급 외)", 3.65, "K/S",
             "Lonza dpADC 발표로 간접 PoC. dual-payload ADC 상용화 가속 시 격상."),
        ],
    },
    "open_questions": [
        "EfHyl8 (item_015) vs rHuPH20 SC diffusion 정량 — specific activity (U/mg), kcat, diffusion zone (cm²·hr⁻¹).",
        "cGMP enzyme catalog 실제 단가 — mTG·sortase·OaAEP1·EndoS2·RNA ligase 모두 quote-only.",
        "Codexis ligase variant 청구항 정확 USPTO/EPO 번호.",
        "item_002 mTG cluster FTO opinion (Ajinomoto AJICAP / Zedira / Hzymes / Araris RKAA / US11786603).",
        "item_021 radioligand sortase — NBE SMAC + USPTO 10556024 chelator-tag carve-out 검증.",
        "item_008 peptiligase/OaAEP1 — US10883132B2 (Fresenius) vs US11795488B2 carve-out 검증.",
        "item_016 FCE::T7RNAP fusion NEB Faustovirus 4국가 패밀리 청구항 심층 분석.",
        "Halozyme vs Merck IPR 7건 결과 (예정 2026) — 비PH20 진입장벽.",
        "Keytruda SC FDA 결정 후속 영향 — Alteogen 2% royalty 시장 성숙도.",
        "AZ-Alteogen 후속 deal — non-PH20 SC 라이선스 확장 신호.",
    ],
    "r4_triggers": [
        "신규 빅파마 M&A ≥$1B in scope (현재 없음).",
        "Top-5 SD ΔR3→R4 ≥ 0.15 (R3 SD 0.136 → R4 변동 시 발동).",
        "Halozyme vs Merck IPR 결과 공시.",
        "사용자 신규 키워드 추가.",
    ],
}


def build_consolidated_xlsx(date: str, out_path: Path):
    out_path.parent.mkdir(parents=True, exist_ok=True)
    history = read_csv_rows(ROOT / "data" / "candidates_history.csv")
    current = read_csv_rows(ROOT / "data" / "candidates_current.csv")

    wb = Workbook()

    # ---- Sheet 1: 통합 요약 ----
    ws = wb.active
    ws.title = "1.통합요약"
    ws["A1"] = "Consolidated Digest — Round 1–3 통합 (2026-05-21)"
    ws["A1"].font = Font(name="맑은 고딕", bold=True, size=16, color="1F4E78")
    ws.row_dimensions[1].height = 28
    ws["A2"] = "run_id 궤적: 20260521-A → 20260521-B → 20260521-C   |   focus: broad_scan → deferred_and_boost → quantitative_validation_and_ip_fto"
    ws["A2"].font = Font(name="맑은 고딕", italic=True, size=10, color="595959")

    ws["A4"] = "▣ 3-Round Executive Summary"
    ws["A4"].font = SUBHEAD_FONT
    ws.merge_cells("A5:F11")
    ws["A5"] = CONSOLIDATED_META["exec_summary"]
    ws["A5"].alignment = WRAP
    ws["A5"].font = BODY_FONT

    ws["A13"] = "▣ 최종 Top 3 + 신뢰도 등급"
    ws["A13"].font = SUBHEAD_FONT
    headers = ["순위", "id", "아이템", "R3 가중합", "신뢰도", "한 줄"]
    for i, h in enumerate(headers, start=1):
        ws.cell(row=14, column=i, value=h)
    style_header_row(ws, 14, len(headers))
    for r, (rank, cid, name, sc, tier, why) in enumerate(CONSOLIDATED_META["top3"], start=15):
        ws.cell(row=r, column=1, value=rank)
        ws.cell(row=r, column=2, value=cid)
        ws.cell(row=r, column=3, value=name)
        ws.cell(row=r, column=4, value=sc)
        ws.cell(row=r, column=5, value=tier)
        ws.cell(row=r, column=6, value=why)
        apply_body_style(ws, r, 6, fill=SHORTLIST_FILL)
        ws.row_dimensions[r].height = 48
    set_col_widths(ws, [10, 12, 30, 12, 10, 60])

    # ---- Sheet 2: 점수 궤적 ----
    ws2 = wb.create_sheet("2.점수궤적")
    cols = ["id", "아이템", "R1", "R2", "R3", "누적 Δ", "R1 SL", "R2 SL", "R3 SL", "횟수", "등급"]
    for i, h in enumerate(cols, start=1):
        ws2.cell(row=1, column=i, value=h)
    style_header_row(ws2, 1, len(cols))
    sh = CONSOLIDATED_META["shortlist_history"]
    sm = CONSOLIDATED_META["shortlist_membership"]
    names = CONSOLIDATED_META["names"]
    # order by R3 weighted desc (R1-only ★ to bottom)
    ordering = sorted(sh.keys(), key=lambda i: (-(sh[i].get(3, 0) or 0), -(sh[i].get(1, 0) or 0)))
    for r, cid in enumerate(ordering, start=2):
        s = sh[cid]
        mem = sm.get(cid, (False, False, False))
        count = sum(mem)
        tier = "★★★" if count == 3 else "★★" if count == 2 else "★"
        r1 = s.get(1)
        r2 = s.get(2)
        r3 = s.get(3)
        base = r1 if r1 is not None else r2
        delta = (r3 - base) if (r3 is not None and base is not None) else None
        ws2.cell(row=r, column=1, value=cid)
        ws2.cell(row=r, column=2, value=names.get(cid, cid))
        ws2.cell(row=r, column=3, value=f"{r1:.2f}" if r1 is not None else "—")
        ws2.cell(row=r, column=4, value=f"{r2:.2f}" if r2 is not None else "—")
        ws2.cell(row=r, column=5, value=f"{r3:.2f}" if r3 is not None else "—")
        ws2.cell(row=r, column=6, value=(f"{delta:+.2f}" if delta is not None else "—"))
        ws2.cell(row=r, column=7, value="✓" if mem[0] else "")
        ws2.cell(row=r, column=8, value="✓" if mem[1] else "")
        ws2.cell(row=r, column=9, value="✓" if mem[2] else "")
        ws2.cell(row=r, column=10, value=count)
        ws2.cell(row=r, column=11, value=tier)
        apply_body_style(ws2, r, len(cols), fill=(SHORTLIST_FILL if count >= 2 else None))
        for c in (3, 4, 5, 6, 7, 8, 9, 10, 11):
            ws2.cell(row=r, column=c).alignment = CENTER
        if count == 3:
            ws2.cell(row=r, column=11).font = Font(name="맑은 고딕", bold=True, size=11, color="C00000")
        ws2.row_dimensions[r].height = 30
    set_col_widths(ws2, [10, 38, 8, 8, 8, 10, 8, 8, 8, 7, 9])
    ws2.freeze_panes = "C2"

    # ---- Sheet 3: Short-list 변동 ----
    ws3 = wb.create_sheet("3.SL변동")
    ws3["A1"] = "▣ Short-list 멤버십 in/out 매트릭스"
    ws3["A1"].font = SUBHEAD_FONT
    cols = ["id", "아이템", "R1", "R2", "R3", "전이 패턴"]
    for i, h in enumerate(cols, start=1):
        ws3.cell(row=2, column=i, value=h)
    style_header_row(ws3, 2, len(cols))
    pattern_label = {
        (True, True, True): "유지 (R1→R3 안정)",
        (True, False, False): "OUT (R2에서 제외)",
        (False, True, True): "IN at R2 (유지)",
        (False, False, True): "IN at R3",
        (True, True, False): "OUT at R3",
        (False, True, False): "IN at R2, OUT at R3",
    }
    for r, cid in enumerate(ordering, start=3):
        mem = sm.get(cid, (False, False, False))
        ws3.cell(row=r, column=1, value=cid)
        ws3.cell(row=r, column=2, value=names.get(cid, cid))
        ws3.cell(row=r, column=3, value="✓" if mem[0] else "—")
        ws3.cell(row=r, column=4, value="✓" if mem[1] else "—")
        ws3.cell(row=r, column=5, value="✓" if mem[2] else "—")
        ws3.cell(row=r, column=6, value=pattern_label.get(mem, "기타"))
        apply_body_style(ws3, r, len(cols))
        for c in (3, 4, 5):
            ws3.cell(row=r, column=c).alignment = CENTER
        ws3.row_dimensions[r].height = 26
    set_col_widths(ws3, [10, 38, 6, 6, 6, 32])

    # ---- Sheet 4: Cumulative scoring (R3 23개) ----
    ws4 = wb.create_sheet("4.Cumulative스코어")
    cols = ["rank", "id", "아이템", "분류", "biz1", "biz2", "lifecycle",
            "M", "cM", "F", "cF", "R", "cR", "W", "cW", "IP", "cIP", "T", "cT", "가중합", "SL"]
    for i, h in enumerate(cols, start=1):
        ws4.cell(row=1, column=i, value=h)
    style_header_row(ws4, 1, len(cols))
    sorted_cur = sorted(current, key=lambda r: int(r["rank"]))
    axes = [("market", "confidence_market"), ("feasibility", "confidence_feasibility"),
            ("regulatory", "confidence_regulatory"), ("whitespace", "confidence_whitespace"),
            ("ip", "confidence_ip"), ("time", "confidence_time")]
    for r, row in enumerate(sorted_cur, start=2):
        ws4.cell(row=r, column=1, value=int(row["rank"]))
        ws4.cell(row=r, column=2, value=row["id"])
        ws4.cell(row=r, column=3, value=row["item_name"])
        ws4.cell(row=r, column=4, value=row["inclusion_bucket"])
        ws4.cell(row=r, column=5, value=row.get("business_model_primary", ""))
        ws4.cell(row=r, column=6, value=row.get("business_model_secondary", ""))
        ws4.cell(row=r, column=7, value=row.get("lifecycle", ""))
        col = 8
        for key, conf_key in axes:
            s = int(row[key])
            cell = ws4.cell(row=r, column=col, value=s)
            cell.alignment = CENTER
            cell.font = Font(name="맑은 고딕", size=10, bold=True)
            cell.fill = SCORE_FILLS[s]
            cell.border = BORDER
            col += 1
            conf = row.get(conf_key, "")
            cc = ws4.cell(row=r, column=col, value=conf)
            cc.alignment = CENTER
            cc.font = Font(name="맑은 고딕", size=9, bold=True)
            if conf in CONFIDENCE_FILLS:
                cc.fill = CONFIDENCE_FILLS[conf]
            cc.border = BORDER
            col += 1
        cell = ws4.cell(row=r, column=col, value=float(row["weighted_score"]))
        cell.alignment = CENTER
        cell.font = Font(name="맑은 고딕", size=10, bold=True)
        cell.number_format = "0.00"
        cell.border = BORDER
        col += 1
        cell = ws4.cell(row=r, column=col, value="✓" if row["shortlist"] == "1" else "")
        cell.alignment = CENTER
        cell.font = Font(name="맑은 고딕", size=12, bold=True, color="C00000")
        cell.border = BORDER
        for cc in (1, 2, 3, 4, 5, 6, 7):
            cell = ws4.cell(row=r, column=cc)
            cell.font = BODY_FONT
            cell.alignment = WRAP
            cell.border = BORDER
            if row["shortlist"] == "1" and (cell.fill.fgColor.rgb in (None, "00000000")):
                cell.fill = SHORTLIST_FILL
        ws4.row_dimensions[r].height = 36
    set_col_widths(ws4, [6, 10, 36, 18, 7, 7, 22, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 8, 7])
    ws4.freeze_panes = "C2"

    # ---- Sheet 5: 사업화 형태별 추천 ----
    ws5 = wb.create_sheet("5.사업화형태별추천")
    ws5["A1"] = "▣ 즉시 착수 (≤1년 ROI, K primary)"
    ws5["A1"].font = SUBHEAD_FONT
    headers = ["우선", "id", "아이템", "등급", "R3 점수", "biz", "한 줄"]
    cur_row = 2
    for section_title, key in [("즉시 착수 (≤1년 ROI, K primary)", "immediate"),
                                ("중기 검증 (1~2년 ROI, L primary)", "mid_term"),
                                ("장기 R&D (2~5년 ROI)", "long_term")]:
        ws5.cell(row=cur_row, column=1, value=f"▣ {section_title}").font = SUBHEAD_FONT
        ws5.cell(row=cur_row, column=1).fill = SUBHEAD_FILL
        ws5.merge_cells(start_row=cur_row, start_column=1, end_row=cur_row, end_column=7)
        cur_row += 1
        for i, h in enumerate(headers, start=1):
            ws5.cell(row=cur_row, column=i, value=h)
        style_header_row(ws5, cur_row, len(headers))
        cur_row += 1
        for entry in CONSOLIDATED_META["recommendations"][key]:
            pri, cid, name, tier, sc, bm, line = entry
            ws5.cell(row=cur_row, column=1, value=pri)
            ws5.cell(row=cur_row, column=2, value=cid)
            ws5.cell(row=cur_row, column=3, value=name)
            ws5.cell(row=cur_row, column=4, value=tier)
            ws5.cell(row=cur_row, column=5, value=sc)
            ws5.cell(row=cur_row, column=6, value=bm)
            ws5.cell(row=cur_row, column=7, value=line)
            apply_body_style(ws5, cur_row, len(headers), fill=SHORTLIST_FILL)
            ws5.row_dimensions[cur_row].height = 48
            cur_row += 1
        cur_row += 1
    set_col_widths(ws5, [6, 10, 36, 12, 10, 8, 72])

    # ---- Sheet 6: confidence 분포 ----
    ws6 = wb.create_sheet("6.confidence분포")
    ws6["A1"] = "▣ 6축 confidence H/M/L 카운트 (R3 종료, 23개 후보 × 6축 = 138 셀)"
    ws6["A1"].font = SUBHEAD_FONT
    headers = ["축", "H", "M", "L", "H 비율"]
    for i, h in enumerate(headers, start=1):
        ws6.cell(row=2, column=i, value=h)
    style_header_row(ws6, 2, len(headers))
    counts = defaultdict(lambda: {"H": 0, "M": 0, "L": 0})
    for row in current:
        for axis_label, conf_key in [("M (market)", "confidence_market"),
                                      ("F (feasibility)", "confidence_feasibility"),
                                      ("R (regulatory)", "confidence_regulatory"),
                                      ("W (whitespace)", "confidence_whitespace"),
                                      ("IP", "confidence_ip"),
                                      ("T (time)", "confidence_time")]:
            v = row.get(conf_key, "").strip()
            if v in ("H", "M", "L"):
                counts[axis_label][v] += 1
    total_h = total_m = total_l = 0
    for r, axis_label in enumerate(["M (market)", "F (feasibility)", "R (regulatory)",
                                     "W (whitespace)", "IP", "T (time)"], start=3):
        h, m, l = counts[axis_label]["H"], counts[axis_label]["M"], counts[axis_label]["L"]
        total_h += h; total_m += m; total_l += l
        ws6.cell(row=r, column=1, value=axis_label)
        ws6.cell(row=r, column=2, value=h)
        ws6.cell(row=r, column=3, value=m)
        ws6.cell(row=r, column=4, value=l)
        denom = h + m + l
        ws6.cell(row=r, column=5, value=(f"{h/denom*100:.1f}%" if denom else "—"))
        apply_body_style(ws6, r, len(headers))
        for c in (2, 3, 4, 5):
            ws6.cell(row=r, column=c).alignment = CENTER
        ws6.cell(row=r, column=2).fill = CONFIDENCE_FILLS["H"]
        ws6.cell(row=r, column=3).fill = CONFIDENCE_FILLS["M"]
        ws6.cell(row=r, column=4).fill = CONFIDENCE_FILLS["L"]
    total_row = 9
    ws6.cell(row=total_row, column=1, value="합계").font = Font(name="맑은 고딕", bold=True, size=11)
    ws6.cell(row=total_row, column=2, value=total_h)
    ws6.cell(row=total_row, column=3, value=total_m)
    ws6.cell(row=total_row, column=4, value=total_l)
    total = total_h + total_m + total_l
    ws6.cell(row=total_row, column=5, value=(f"H {total_h/total*100:.1f}% / M {total_m/total*100:.1f}% / L {total_l/total*100:.1f}%" if total else "—"))
    apply_body_style(ws6, total_row, len(headers))
    set_col_widths(ws6, [22, 8, 8, 8, 32])

    # R2 vs R3 비교
    ws6.cell(row=12, column=1, value="▣ R2 vs R3 H 카운트 비교 (라운드별 H 비율)").font = SUBHEAD_FONT
    ws6.cell(row=13, column=1, value="라운드"); ws6.cell(row=13, column=2, value="H"); ws6.cell(row=13, column=3, value="M"); ws6.cell(row=13, column=4, value="L"); ws6.cell(row=13, column=5, value="H 비율")
    style_header_row(ws6, 13, 5)
    for i, (label, h, m, l) in enumerate([("R2", 42, 85, 11), ("R3", 51, 76, 11)], start=14):
        ws6.cell(row=i, column=1, value=label)
        ws6.cell(row=i, column=2, value=h)
        ws6.cell(row=i, column=3, value=m)
        ws6.cell(row=i, column=4, value=l)
        ws6.cell(row=i, column=5, value=f"{h/(h+m+l)*100:.1f}%")
        apply_body_style(ws6, i, 5)
        for c in (2, 3, 4, 5):
            ws6.cell(row=i, column=c).alignment = CENTER

    # ---- Sheet 7: Open questions / R4 triggers ----
    ws7 = wb.create_sheet("7.OpenQ·R4")
    ws7["A1"] = "▣ Open Questions (R3 미해결 / R4 1순위)"
    ws7["A1"].font = SUBHEAD_FONT
    for r, q in enumerate(CONSOLIDATED_META["open_questions"], start=2):
        ws7.cell(row=r, column=1, value=f"Q{r-1}")
        ws7.cell(row=r, column=2, value=q)
        apply_body_style(ws7, r, 2)
        ws7.row_dimensions[r].height = 36
    trig_start = 2 + len(CONSOLIDATED_META["open_questions"]) + 2
    ws7.cell(row=trig_start, column=1, value="▣ Quality-gate / R4 자동 발동 트리거 후보").font = SUBHEAD_FONT
    for i, t in enumerate(CONSOLIDATED_META["r4_triggers"], start=1):
        ws7.cell(row=trig_start + i, column=1, value="•")
        ws7.cell(row=trig_start + i, column=2, value=t)
        apply_body_style(ws7, trig_start + i, 2)
        ws7.cell(row=trig_start + i, column=1).alignment = CENTER
        ws7.row_dimensions[trig_start + i].height = 30
    set_col_widths(ws7, [10, 110])

    # ---- Sheet 8: 메타 ----
    ws8 = wb.create_sheet("8.메타")
    sd_trajectory = [
        ("R1", "4.20, 4.20, 4.10, 4.05, 3.95", "4.10", "0.095"),
        ("R2", "4.30, 4.20, 4.10, 4.10, 3.95", "4.13", "0.117"),
        ("R3", "4.30, 4.30, 4.25, 4.10, 3.95", "4.18", "0.136"),
    ]
    headers = ["라운드", "Top-5 가중합", "평균", "SD"]
    for i, h in enumerate(headers, start=1):
        ws8.cell(row=1, column=i, value=h)
    style_header_row(ws8, 1, len(headers))
    for r, row in enumerate(sd_trajectory, start=2):
        for c, v in enumerate(row, start=1):
            ws8.cell(row=r, column=c, value=v)
        apply_body_style(ws8, r, len(headers))
        for c in (3, 4):
            ws8.cell(row=r, column=c).alignment = CENTER

    base = len(sd_trajectory) + 3
    ws8.cell(row=base, column=1, value="항목").font = HEAD_FONT
    ws8.cell(row=base, column=1).fill = HEAD_FILL
    ws8.cell(row=base, column=2, value="값").font = HEAD_FONT
    ws8.cell(row=base, column=2).fill = HEAD_FILL
    meta_rows = [
        ("run_id 궤적", "20260521-A → 20260521-B → 20260521-C"),
        ("focus 궤적", "broad_scan → deferred_and_boost → quantitative_validation_and_ip_fto"),
        ("총 라운드", "3 (min_iterations=3 도달)"),
        ("누적 활성 후보", "23 (R1 14 → R2 23 → R3 23)"),
        ("누적 short-list (≥2회)", "7 (★★★ 5 + ★★ 2)"),
        ("총 signal events", "약 75 (R1 18 + R2 18 + R3 27 정량 + 7 IP/FTO + 5 RFI)"),
        ("총 web search", "약 249건 (R1 79 + R2 78 + R3 92)"),
        ("Quality-gate 발동", "0건 (R1·R2·R3 모두 미발동)"),
        ("ranking 수렴", "매우 강함 (R2→R3 short-list 멤버 100% 동일)"),
        ("confidence H 비율 (R3)", "37.0% (R2 30.4%에서 +6.6pp)"),
        ("가장 큰 점수 변동", "R2 item_006 −0.25 / R3 item_021 +0.15"),
        ("산출 파일",
         "R1: reports/digest_20260521.{xlsx,docx,md} / R2: iterations/iter_02/digest.{xlsx,docx,md} + reports/digest_round_02_20260521.{xlsx,docx} / R3: iterations/iter_03/digest.{xlsx,docx,md} + reports/digest_round_03_20260521.{xlsx,docx} / 통합: reports/consolidated_digest_20260521.{xlsx,docx}"),
        ("데이터", "data/candidates_current.csv (R3 미러 23행), data/candidates_history.csv (R1+R2+R3 60 데이터행)"),
    ]
    for r, (k, v) in enumerate(meta_rows, start=base + 1):
        ws8.cell(row=r, column=1, value=k).font = Font(name="맑은 고딕", bold=True, size=10)
        ws8.cell(row=r, column=2, value=v).font = BODY_FONT
        ws8.cell(row=r, column=1).alignment = WRAP
        ws8.cell(row=r, column=2).alignment = WRAP
        ws8.cell(row=r, column=1).border = BORDER
        ws8.cell(row=r, column=2).border = BORDER
        ws8.row_dimensions[r].height = 32
    set_col_widths(ws8, [22, 110])

    wb.save(out_path)


def build_consolidated_docx(date: str, out_path: Path):
    out_path.parent.mkdir(parents=True, exist_ok=True)
    history = read_csv_rows(ROOT / "data" / "candidates_history.csv")
    current = read_csv_rows(ROOT / "data" / "candidates_current.csv")

    doc = Document()
    for section in doc.sections:
        section.left_margin = Cm(2.0)
        section.right_margin = Cm(2.0)
        section.top_margin = Cm(2.0)
        section.bottom_margin = Cm(2.0)

    add_heading(doc, "Consolidated Digest — Round 1–3 통합 (2026-05-21)", level=0)
    add_para(doc,
             "run_id 궤적: 20260521-A → 20260521-B → 20260521-C   |   focus: broad_scan → deferred_and_boost → quantitative_validation_and_ip_fto",
             size=9.5, italic=True)

    # 1
    add_heading(doc, "1. 통합 요약")
    add_para(doc, CONSOLIDATED_META["exec_summary"])
    add_heading(doc, "최종 Top 3 + 신뢰도 등급", level=2)
    add_table(
        doc,
        headers=["순위", "id", "아이템", "R3 가중합", "신뢰도", "한 줄"],
        rows=[(r, cid, n, f"{s:.2f}", tier, w) for r, cid, n, s, tier, w in CONSOLIDATED_META["top3"]],
        col_widths_cm=[1.5, 1.6, 4.5, 1.6, 1.4, 6.4],
        row_bgs=["FFF2CC"] * len(CONSOLIDATED_META["top3"]),
    )

    # 2 점수 궤적
    add_heading(doc, "2. 점수 궤적 (★★★ + ★★ + R1 단독 ★)")
    sh = CONSOLIDATED_META["shortlist_history"]
    sm = CONSOLIDATED_META["shortlist_membership"]
    names = CONSOLIDATED_META["names"]
    ordering = sorted(sh.keys(), key=lambda i: (-(sh[i].get(3, 0) or 0), -(sh[i].get(1, 0) or 0)))
    rows = []
    bgs = []
    for cid in ordering:
        s = sh[cid]
        mem = sm.get(cid, (False, False, False))
        count = sum(mem)
        tier = "★★★" if count == 3 else "★★" if count == 2 else "★"
        r1 = s.get(1); r2 = s.get(2); r3 = s.get(3)
        base_v = r1 if r1 is not None else r2
        delta = (r3 - base_v) if (r3 is not None and base_v is not None) else None
        rows.append((
            cid, names.get(cid, cid),
            f"{r1:.2f}" if r1 is not None else "—",
            f"{r2:.2f}" if r2 is not None else "—",
            f"{r3:.2f}" if r3 is not None else "—",
            f"{delta:+.2f}" if delta is not None else "—",
            count, tier,
        ))
        bgs.append("FFF2CC" if count >= 2 else None)
    add_table(
        doc,
        headers=["id", "아이템", "R1", "R2", "R3", "Δ", "횟수", "등급"],
        rows=rows,
        col_widths_cm=[1.6, 6.8, 1.1, 1.1, 1.1, 1.1, 1.0, 1.2],
        row_bgs=bgs,
    )

    # 3 R1→R2→R3 short-list 변동
    add_heading(doc, "3. R1→R2→R3 Short-list in/out 매트릭스")
    pattern_label = {
        (True, True, True): "유지 (R1→R3 안정)",
        (True, False, False): "OUT at R2",
        (False, True, True): "IN at R2 (유지)",
        (False, False, True): "IN at R3",
        (True, True, False): "OUT at R3",
        (False, True, False): "IN at R2 / OUT at R3",
    }
    rows = []
    for cid in ordering:
        mem = sm.get(cid, (False, False, False))
        rows.append((
            cid, names.get(cid, cid),
            "✓" if mem[0] else "—",
            "✓" if mem[1] else "—",
            "✓" if mem[2] else "—",
            pattern_label.get(mem, "기타"),
        ))
    add_table(
        doc,
        headers=["id", "아이템", "R1", "R2", "R3", "전이 패턴"],
        rows=rows,
        col_widths_cm=[1.6, 7.0, 1.0, 1.0, 1.0, 5.4],
    )

    # 4 cumulative scoring
    add_heading(doc, "4. Cumulative Scoring (R3 23개)")
    sorted_cur = sorted(current, key=lambda r: int(r["rank"]))
    rows = []
    bgs = []
    for row in sorted_cur:
        rows.append((
            int(row["rank"]),
            row["id"],
            row["item_name"][:42] + ("…" if len(row["item_name"]) > 42 else ""),
            row.get("business_model_primary", "") + (f"/{row.get('business_model_secondary')}" if row.get("business_model_secondary") else ""),
            f"{row['market']}({row.get('confidence_market', '?')})",
            f"{row['feasibility']}({row.get('confidence_feasibility', '?')})",
            f"{row['regulatory']}({row.get('confidence_regulatory', '?')})",
            f"{row['whitespace']}({row.get('confidence_whitespace', '?')})",
            f"{row['ip']}({row.get('confidence_ip', '?')})",
            f"{row['time']}({row.get('confidence_time', '?')})",
            f"{float(row['weighted_score']):.2f}",
            "✓" if row["shortlist"] == "1" else "",
        ))
        bgs.append("FFF2CC" if row["shortlist"] == "1" else None)
    add_table(
        doc,
        headers=["rank", "id", "아이템", "biz", "M(c)", "F(c)", "R(c)", "W(c)", "IP(c)", "T(c)", "가중합", "SL"],
        rows=rows,
        col_widths_cm=[0.8, 1.3, 4.6, 1.2, 1.2, 1.2, 1.2, 1.2, 1.2, 1.2, 1.1, 0.8],
        row_bgs=bgs,
    )

    # 5 사업화 형태별 추천
    add_heading(doc, "5. 사업화 형태별 추천 (즉시 / 중기 / 장기)")
    for title, key in [("즉시 착수 (≤1년 ROI, K primary)", "immediate"),
                        ("중기 검증 (1~2년 ROI, L primary)", "mid_term"),
                        ("장기 R&D (2~5년 ROI)", "long_term")]:
        add_heading(doc, title, level=2)
        rows = [(pri, cid, name, tier, f"{sc:.2f}", bm, line)
                for pri, cid, name, tier, sc, bm, line in CONSOLIDATED_META["recommendations"][key]]
        add_table(
            doc,
            headers=["우선", "id", "아이템", "등급", "R3", "biz", "한 줄"],
            rows=rows,
            col_widths_cm=[1.0, 1.6, 4.5, 1.5, 1.0, 1.0, 6.4],
            row_bgs=["FFF2CC"] * len(rows),
        )

    # 6 confidence 분포
    add_heading(doc, "6. confidence 분포 (R3 종료)")
    counts = defaultdict(lambda: {"H": 0, "M": 0, "L": 0})
    for row in current:
        for axis_label, conf_key in [("M (market)", "confidence_market"),
                                      ("F (feasibility)", "confidence_feasibility"),
                                      ("R (regulatory)", "confidence_regulatory"),
                                      ("W (whitespace)", "confidence_whitespace"),
                                      ("IP", "confidence_ip"),
                                      ("T (time)", "confidence_time")]:
            v = row.get(conf_key, "").strip()
            if v in ("H", "M", "L"):
                counts[axis_label][v] += 1
    rows = []
    for axis_label in ["M (market)", "F (feasibility)", "R (regulatory)", "W (whitespace)", "IP", "T (time)"]:
        h = counts[axis_label]["H"]
        m = counts[axis_label]["M"]
        l = counts[axis_label]["L"]
        denom = h + m + l
        rows.append((axis_label, h, m, l, f"{h/denom*100:.1f}%" if denom else "—"))
    add_table(
        doc,
        headers=["축", "H", "M", "L", "H 비율"],
        rows=rows,
        col_widths_cm=[3.5, 2.0, 2.0, 2.0, 3.0],
    )
    add_para(doc,
             "R2(H 30.4%) → R3(H 37.0%) — IP 축 H가 1→5로 5배 증가, R3 IP/FTO focus의 직접 성과.",
             size=10, italic=True)

    # 7 open questions / R4 triggers
    add_heading(doc, "7. Open Questions / R4+ 트리거")
    add_heading(doc, "Open Questions (R3 미해결)", level=2)
    for q in CONSOLIDATED_META["open_questions"]:
        doc.add_paragraph(q, style="List Bullet")
    add_heading(doc, "Quality-gate / R4 자동 발동 트리거", level=2)
    for t in CONSOLIDATED_META["r4_triggers"]:
        doc.add_paragraph(t, style="List Bullet")

    # 8 메타
    add_heading(doc, "8. 메타")
    add_heading(doc, "Top-5 가중합 SD 궤적", level=2)
    add_table(
        doc,
        headers=["라운드", "Top-5 가중합", "평균", "SD"],
        rows=[
            ("R1", "4.20, 4.20, 4.10, 4.05, 3.95", "4.10", "0.095"),
            ("R2", "4.30, 4.20, 4.10, 4.10, 3.95", "4.13", "0.117"),
            ("R3", "4.30, 4.30, 4.25, 4.10, 3.95", "4.18", "0.136"),
        ],
        col_widths_cm=[2.0, 7.0, 3.0, 3.0],
    )
    add_table(
        doc,
        headers=["항목", "값"],
        rows=[
            ("run_id 궤적", "20260521-A → 20260521-B → 20260521-C"),
            ("focus 궤적", "broad_scan → deferred_and_boost → quantitative_validation_and_ip_fto"),
            ("총 라운드", "3 (min_iterations=3 도달)"),
            ("누적 활성 후보", "23 (R1 14 → R2 23 → R3 23)"),
            ("누적 short-list (≥2회)", "7 (★★★ 5 + ★★ 2)"),
            ("총 signal events", "약 75 (R1 18 + R2 18 + R3 27 정량 + 7 IP/FTO + 5 RFI)"),
            ("총 web search", "약 249건 (R1 79 + R2 78 + R3 92)"),
            ("Quality-gate 발동", "0건 (R1·R2·R3 모두 미발동)"),
            ("ranking 수렴", "매우 강함 (R2→R3 short-list 멤버 100% 동일)"),
            ("confidence H 비율 (R3)", "37.0% (R2 30.4%에서 +6.6pp)"),
            ("가장 큰 점수 변동", "R2 item_006 −0.25 / R3 item_021 +0.15"),
        ],
        col_widths_cm=[4.0, 13.0],
    )

    doc.save(out_path)


# ---------------------------------------------------------------------------
# Dispatch
# ---------------------------------------------------------------------------

def run_round(iter_n: int, date: str):
    if iter_n not in ROUND_META:
        raise SystemExit(f"Unknown iter {iter_n}; supported: {sorted(ROUND_META.keys())}")
    # Primary outputs
    if iter_n == 1:
        primary_xlsx = ROOT / "reports" / f"digest_{date}.xlsx"
        primary_docx = ROOT / "reports" / f"digest_{date}.docx"
        build_round_xlsx(iter_n, date, primary_xlsx)
        build_round_docx(iter_n, date, primary_docx)
        # also mirror to reports/digest_round_01_<date>.xlsx
        mirror_xlsx = ROOT / "reports" / f"digest_round_{iter_n:02d}_{date}.xlsx"
        mirror_docx = ROOT / "reports" / f"digest_round_{iter_n:02d}_{date}.docx"
        build_round_xlsx(iter_n, date, mirror_xlsx)
        build_round_docx(iter_n, date, mirror_docx)
        print(f"Wrote {primary_xlsx}")
        print(f"Wrote {primary_docx}")
        print(f"Wrote {mirror_xlsx}")
        print(f"Wrote {mirror_docx}")
    else:
        iter_xlsx = ROOT / f"iterations/iter_{iter_n:02d}/digest.xlsx"
        iter_docx = ROOT / f"iterations/iter_{iter_n:02d}/digest.docx"
        mirror_xlsx = ROOT / "reports" / f"digest_round_{iter_n:02d}_{date}.xlsx"
        mirror_docx = ROOT / "reports" / f"digest_round_{iter_n:02d}_{date}.docx"
        build_round_xlsx(iter_n, date, iter_xlsx)
        build_round_docx(iter_n, date, iter_docx)
        build_round_xlsx(iter_n, date, mirror_xlsx)
        build_round_docx(iter_n, date, mirror_docx)
        print(f"Wrote {iter_xlsx}")
        print(f"Wrote {iter_docx}")
        print(f"Wrote {mirror_xlsx}")
        print(f"Wrote {mirror_docx}")


def run_consolidated(date: str):
    out_xlsx = ROOT / "reports" / f"consolidated_digest_{date}.xlsx"
    out_docx = ROOT / "reports" / f"consolidated_digest_{date}.docx"
    build_consolidated_xlsx(date, out_xlsx)
    build_consolidated_docx(date, out_docx)
    print(f"Wrote {out_xlsx}")
    print(f"Wrote {out_docx}")


def main():
    parser = argparse.ArgumentParser(description="Export Phase D digests to xlsx + docx.")
    parser.add_argument("--mode", required=True, choices=["round", "consolidated"])
    parser.add_argument("--iter", type=int, default=None, help="Iteration number (1-3) for --mode round")
    parser.add_argument("--date", required=True, help="YYYYMMDD")
    args = parser.parse_args()

    if args.mode == "round":
        if args.iter is None:
            parser.error("--iter required for --mode round")
        run_round(args.iter, args.date)
    elif args.mode == "consolidated":
        run_consolidated(args.date)


if __name__ == "__main__":
    main()
