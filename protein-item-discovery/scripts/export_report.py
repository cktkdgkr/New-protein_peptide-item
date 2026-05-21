"""Export the final consolidated digest into Excel (.xlsx) + Word (.docx).

CLI usage:
    python scripts/export_report.py --mode consolidated --date 20260521
    python scripts/export_report.py                       # auto-infers date

Notes:
    - `--mode round` is **deprecated and removed**. The harness no longer
      produces per-round xlsx/docx. Per-round digests stay as markdown
      working artifacts only. The single user-facing deliverable is the
      consolidated digest (xlsx + docx, exactly 2 files).
    - The consolidated builder produces 10 Excel sheets and 10 Word
      sections (plus a docx appendix that inlines R3 short-list 1-pagers).

Sources of truth:
    - Score / confidence / business_model / lifecycle / shortlist:
      `data/candidates_history.csv` (per-iter rows) and
      `data/candidates_current.csv` (R3 mirror).
    - Narrative blocks (signals, risks, methodology, selection rationale):
      hardcoded constants below reflecting the markdown digests as of
      2026-05-21.
    - R3 1-pager cards (docx appendix): `candidates/item_*.md` plus
      `iterations/iter_02/candidates/item_*.md`.
"""
from __future__ import annotations

import argparse
import csv
import re
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


# ---------------------------------------------------------------------------
# Narrative constants (carry over R1/R2/R3 content from the markdown digests)
# ---------------------------------------------------------------------------

# ----- Methodology (Sheet 1) -----

METHODOLOGY = {
    "ssot": (
        "포함/제외 기준은 `scope/inclusion.md` · `scope/exclusion.md`의 단일 진실원천(SSOT)을 따른다. "
        "핵심 원칙: 임상시험을 거쳐야 하는 therapeutic API 그 자체는 제외. 단 생산공정용·제형변경 조력 효소는 "
        "최종 제품이 약이어도 그 효소 자체는 임상 신약이 아니므로 포함."
    ),
    "axes": [
        ("M", "Market", 0.25, "TAM·CAGR·고객수·매출 검증성. 5=시장 명확하고 정량 출처 ≥3건."),
        ("F", "Feasibility", 0.20, "발현·공정·재현성·CMC 성숙도. 5=cGMP 생산 사례·DMF 존재."),
        ("R", "Regulatory / Reg-friction", 0.20, "임상 부담 거리. 5=process enzyme (no IND), 1=therapeutic API."),
        ("W", "Whitespace", 0.15, "경쟁자 부재·차별화 여지. 5=공급사 사실상 부재, 1=상위 5사 commodity."),
        ("IP", "IP / FTO", 0.10, "특허 자유도·carve-out 가능성. 5=청구항 명확 회피·자체 출원, 1=다중 IPR."),
        ("T", "Time-to-revenue", 0.10, "라이선스·매출까지 거리. 5=≤12개월, 1=≥5년."),
    ],
    "formula": "weighted_score = Σ(score_i × weight_i)  — 5점 만점.",
    "shortlist_rule": (
        "가중합 상위 ≥ ~3.90 또는 R(N)에서 white-space·IP·biz-model 측면 정성 우위가 명확한 후보를 short-list로 "
        "분류. R2부터는 confidence H/M/L 태그가 short-list 안정성에 가중치를 주는 보조 신호로 사용된다."
    ),
    "confidence": [
        ("H (High)", "정량 출처 ≥2건, 1차 근거(공시·라이선스 계약·peer-review)로 확정."),
        ("M (Medium)", "출처 1건 or 2차 인용. 합리적 추정 가능하나 출처 보강 필요."),
        ("L (Low)", "[추정] / 단일 secondary 출처. R(N+1)에서 우선 검증 대상."),
    ],
    "tier": [
        ("★★★", "3라운드 short-list 모두 유지 (R1·R2·R3 일관 멤버)."),
        ("★★", "2회 short-list (R2 또는 R3에서 진입한 후 유지)."),
        ("★", "1회만 short-list (R1 only, R2 이후 OUT). 등급 외(권장 보류)."),
    ],
    "business_model": [
        ("L (License-out)", "지식재산·노하우 라이선스 — 변이체·공정·tag-design."),
        ("K (Kit / Reagent)", "GMP/RUO 효소 자체를 catalog·DMF 형태로 판매."),
        ("C (CDMO / Service)", "위탁생산·위탁공정 (Lonza/Samsung Bio/WuXi XDC 등 인접)."),
        ("S (Supplier integration)", "공급망 통합 (raw material, carrier protein)."),
        ("H (Hybrid)", "L + K 또는 L + C 패키지 라이선스."),
    ],
}

# ----- R1 narrative (Sheet 2) -----

R1_NARRATIVE = {
    "summary": (
        "Round 1 (focus = broad_scan, run_id = 20260521-A)는 단백질·펩타이드 의약 모달리티(SC 항체, ADC, AOC, "
        "radioligand, mRNA, GLP-1 peptide)의 시장 신호 18개를 수집하고, 그로부터 사업화 후보 14개를 도출해 "
        "6축 정량 스코어링한 뒤 short-list 7개를 확정했다. 핵심 발견: 빅파마 모달리티 트렌드는 모두 항체·핵산·"
        "펩타이드의 결합(conjugation)·합성(ligation)·후처리(modification) 효소 수요로 수렴하며, 임상 부담 없는 "
        "process enzyme 화이트스페이스가 가장 크다."
    ),
    "signals_top5": [
        ("1",
         "Halozyme 2025 매출 $1.4B(+38%), 로열티 +52% — BMS Opdivo SC EU·argenx VYVGART SC EU·Roche Ocrevus/Tecentriq SC 동시 출시",
         "prnewswire",
         "SC 전환은 빅파마 표준 — hyaluronidase 단일 효소 시장 최대, IP 분쟁(Halozyme vs Merck) 발목."),
        ("2",
         "ADC $13.5B / 15품목 — Gilead-Tubulis $3.15B + Lonza Visp bioconjugation 2배 확장(200명 신규)",
         "bioworld, gilead.com, fiercepharma",
         "차세대 site-specific conjugation 효소(mTG, Sortase, FGE, EndoS2)가 차별화. CDMO 캐파가 효소 채택 견인."),
        ("3",
         "Novartis-Avidity $12B AOC 인수(2025.10) + Codexis ECO Synthesis 빅파마 첫 수주",
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
    ],
    "shortlist_ids": ["item_002", "item_008", "item_007", "item_006", "item_003", "item_005", "item_009"],
    "items_brief": {
        # id : (1-line def, key signal, weighted)
        "item_001": ("Next-gen recombinant hyaluronidase (non-PH20/PH20 variant) for SC conversion",
                     "Halozyme 분쟁·non-PH20 후보 부재 → 신규 진입 명분 있음.", 3.15),
        "item_002": ("Engineered microbial transglutaminase (mTG) for site-specific ADC conjugation",
                     "ADC $13.5B + Lonza Visp 2배 확장 + 'enzyme cost' 산업 통설.", 4.20),
        "item_003": ("Engineered Sortase A variant (Ca-independent, high-kcat) — ADC/AOC/radioligand conjugation",
                     "eSrtA 7M/2A-9 commodity 직전, dual-track 가능.", 3.95),
        "item_004": ("Formylglycine-Generating Enzyme (FGE) for aldehyde-tag dual-payload ADC",
                     "Lonza dpADC PoC, dual-payload 차세대 분명 but 점유율 미확정.", 3.65),
        "item_005": ("EndoS2 glycosynthase mutant (transglycosylation) for homogeneous Fc glycan",
                     "biosimilar 균질화 + GlycoConnect 대안 — Lonza Synaffix 신호.", 3.95),
        "item_006": ("Engineered T7 RNA polymerase variant (low-dsRNA, co-trans capping)",
                     "mRNA 임상 600+, IVT 효소 $1.8B→$3.9B but NEB/Aldevron 매우 혼잡.", 4.05),
        "item_007": ("Engineered RNA ligase (splint-ligation for AOC/ASO synthesis)",
                     "Novartis-Avidity $12B + Codexis ECO 빅파마 첫 수주.", 4.10),
        "item_008": ("Peptiligase / OaAEP1 C247A — green enzymatic peptide ligation",
                     "Bachem·PolyPeptide GLP-1 캐파 2배 + OaAEP1 140× 효율.", 4.20),
        "item_009": ("Engineered Peptide Amidating Enzyme (PAM, bifunctional)",
                     "GLP-1·calcitonin C-term amide 필수, cGMP supplier 부재.", 3.75),
        "item_010": ("Engineered IdeS/IdeZ variant (FabRICATOR class) for QC + ex-vivo research",
                     "imlifidase 치료제와 분리, QC/연구 grade만.", 3.25),
        "item_011": ("Recombinant PNGase F + sialyl/galactosyltransferase set (glycan QC/remodel)",
                     "Glycan QC 표준이나 Genovis·NEB commodity.", 3.25),
        "item_012": ("Next-gen Cas12/Cas13 + RPA recombinase/SSB set for POC molecular Dx",
                     "POC Dx 명확하나 진단 RA 부담.", 2.75),
        "item_013": ("High-fidelity Prime Editor (vPE Cas9 + engineered MMLV-RT)",
                     "in-vivo는 분리, research·ex-vivo만.", 3.35),
        "item_014": ("AI-designed (RFdiffusion2/3) custom enzyme — reagent-grade",
                     "기술 신규성 vs 채택률 [추정].", 3.10),
    },
}

# ----- R2 narrative (Sheet 3) -----

R2_NARRATIVE = {
    "summary": (
        "Round 2 (focus = deferred_and_boost, run_id = 20260521-B)는 R1에서 보류·[추정]이던 5개 영역을 표적 스캔해 "
        "fresh signal 18개를 추가하고, 부활 후보 1건(item_020 PETase)과 신규 후보 8건(item_015~019, 021~023)을 정식 "
        "카드화했다. 누적 활성 후보 23개. R1 14개에 business_model(L/K/C/S/H)·lifecycle 사후 부여 + 모든 6축 점수에 "
        "confidence H/M/L 태그를 적용했다."
    ),
    "boost_focus": [
        "TPD reagents (E3 ligase / E1 / E2 / DUB cocktail)",
        "PETase·cutinase 의약 PET 포장재 ESG",
        "non-PH20 hyaluronidase (leech / bacterial PL8)",
        "Radioligand enzymatic conjugation (sortase·OaAEP1 cGMP)",
        "mRNA aux 효소 (FCE fusion, PPase, dsRNase III)",
    ],
    "shortlist_in_out": [
        ("item_006 (T7 RNAP)", "OUT at R2", "CleanCap M6 압박, T7 RNAP M=5→4, weighted 4.05→3.80."),
        ("item_009 (PAM)", "OUT at R2", "weighted 3.75 unchanged but short-list cutoff 밖으로 밀려남."),
        ("item_017 (yeast PPase)", "IN at R2", "Hzymes DMF #036853 non-animal source 채택 확인."),
        ("item_021 (cGMP Sortase A·OaAEP1 radioligand)", "IN at R2", "AZ-Fusion $2.4B + Aktis Phase 0 직접 동력."),
    ],
    "signals_top5": [
        ("1",
         "ARV-471 (vepdegestrant) FDA 승인 (2026.5.1) — oral PROTAC 첫 신약",
         "Biochempeg PROTAC, Promega TPD",
         "PROTAC QC·screening enzyme 시장의 임상→시판 단계 본격 진입. item_018·019·023 직접 동력."),
        ("2",
         "EfHyl8 (E. faecalis PL8 hyaluronate lyase) — JAFC 2025",
         "JAFC2025 EfHyl8, ScienceDirect2025, Springer2024 HylP",
         "비PH20 fold·메커니즘 → Halozyme/Alteogen IP 우회 명분. item_015의 IP=4(H), W=4(H) 핵심 근거."),
        ("3",
         "FCE::T7RNAP fusion + 2'-O-MTase one-pot Cap-1 (NEB·Takara·KACTUS GMP) vs TriLink CleanCap M6",
         "TriLink2025 CleanCap, NEB M2081, KACTUS DMF038029",
         "enzymatic capping이 chemical analog와 cost race. item_006 강등·item_016 신설 직접 원인."),
        ("4",
         "AstraZeneca-Fusion $2.4B 2026 Q1 클로징 + Ac-225 supply 통합 + Aktis Phase 0 + PeptiDream 두번째 program",
         "AZ2024 Fusion, BioSpace2025 PeptiDream",
         "radiopharma 공정 throughput 압박 → cGMP enzymatic conjugation 채택. item_021 신규 진입 직접 동력."),
        ("5",
         "Carbios Wankai JV (50 kt/년) + 프랑스 €1,000/톤 sensitive-contact 보너스 (2025.9) + Epoch Biodesign $50M+",
         "Carbios2025 Wankai, TechCrunch2025 Epoch, Crystals2026 CtCut",
         "PETase·LCC variant의 의약 PET 포장재 ESG incentive. item_020 부활·신설 근거."),
    ],
    "new_revived_items": {
        # id : (1-line def, key signal, weighted, shortlist_bool)
        "item_015": ("EfHyl8 PL8 hyaluronate lyase (non-PH20 SC diffusion agent)",
                     "JAFC 2025 EfHyl8 — Halozyme PH20 우회 명분 학술 보고.", 3.40, False),
        "item_016": ("FCE::T7RNAP fusion / FCE + 2'-O-MTase one-pot Cap-1 system",
                     "NEB/Takara/KACTUS GMP — chemical CleanCap M6와 cost race.", 3.60, False),
        "item_017": ("Inorganic pyrophosphatase (IVT helper, non-animal GMP)",
                     "Hzymes DMF #036853 non-animal source 채택.", 3.90, True),
        "item_018": ("CRBN/VHL E3 ligase ternary complex assay reagent",
                     "ARV-471 FDA 승인 후 PROTAC QC 시약 시장 본격.", 3.20, False),
        "item_019": ("USP7/USP28/OTUB1 recombinant DUB cocktail (DUBTAC)",
                     "DUBTAC modality 확장 — Promega DUB-Glo가 catalog 기준.", 3.40, False),
        "item_020": ("Engineered LCC / cutinase + AI-designed PETase",
                     "Carbios Wankai 50kt JV + 프랑스 €1,000/t 보너스 (부활).", 3.10, False),
        "item_021": ("cGMP Sortase A / OaAEP1 C247A (radioligand peptide-chelator)",
                     "AZ-Fusion $2.4B + Aktis Phase 0 + PeptiDream 2nd program.", 4.10, True),
        "item_022": ("dsRNA-specific engineered nuclease (RNase III replacement IVT)",
                     "Maravai/Aldevron QC step, T7 RNAP 부산물 제거.", 3.65, False),
        "item_023": ("TPD reagent cocktail (E1+E2+E3+DUB recombinant cascade)",
                     "Promega TPD bundle 패키지 SKU 가능성.", 3.20, False),
    },
}

# ----- R3 narrative (Sheet 4) -----

R3_NARRATIVE = {
    "summary": (
        "Round 3 (focus = quantitative_validation_and_ip_fto, run_id = 20260521-C)는 R2 23개 후보 전체에 "
        "(a) 단가·시장·로열티 정량화, (b) IP/FTO 매핑(Halozyme MDASE vs PL8, Codexis ligase 청구항, mTG cluster, "
        "EnzyPep vs OaAEP1, NEB FCE, NBE SMAC), (c) CDMO RFI 공개 신호(Lonza·Samsung·WuXi·Aldevron·Bachem) "
        "3축을 집중 검증했다. 신규/병합/드롭 0, 23/23 카드 보강."
    ),
    "key_findings": [
        "Lonza Advanced Synthesis Synaffix 통합 (2026-02-19) — EndoS2 enzymatic glycan remodel + click이 빅 CDMO ADC GMP 라인 표준 step으로 진입한 공식 confirmation.",
        "Halozyme MDASE = PH20 (GH56, EC 3.2.1.35) vs EfHyl8 = PL8 (EC 4.2.2.1) — fold·메커니즘·EC 완전 다름 → item_015 IP carve-out 자명; Merck IPR 7건은 비PH20 진입장벽 추가 하락 잠재.",
        "EnzyPep peptiligase = subtilisin BPN' Y217 (S8 serine), OaAEP1 = C13 asparaginyl — US10883132B2가 OaAEP1을 직접 위협하지 않음 → item_008 carve-out 명확.",
        "Codexis-Merck $37.8M Supply Assurance (2025-10) + Q1 Roche dsDNA ligase $6.0M — item_007 빅파마 라이선싱 매출 정량 검증.",
        "Alteogen ALT-B4 = 2% net sales royalty 확정 (Keytruda SC) — 비PH20 후발주자의 협상 ceiling 정량.",
        "NBE SMAC WO2014140317A1 = ADC 한정 → item_021 radioligand white-space 확인, W 4→5.",
    ],
    "score_changes": [
        ("item_002", 4.20, 4.30, "+0.10", "IP 3→4 (M→H): Ajinomoto AJICAP은 enzyme-free (Lys248) → non-conflict; Araris RKAA carve-out."),
        ("item_021", 4.10, 4.25, "+0.15", "W 4→5: NBE SMAC = ADC 한정, radioligand white-space 확인."),
    ],
    "confidence_uplift": [
        ("item_002", "IP M→H"), ("item_005", "IP M→H"), ("item_007", "IP M→H"),
        ("item_008", "IP M→H, T M→H"), ("item_021", "W M→H"),
    ],
}

# ----- Final shortlist with selection rationale (Sheet 7) -----

FINAL_SHORTLIST = [
    {"rank": "1 (tie)", "id": "item_002", "name": "Engineered mTG (ADC site-specific)",
     "definition": "Streptomyces mTG 변이체로 항체 LLQG-tag / RKAA-tag glutamine과 amine payload를 isopeptide 결합 → 균일 DAR2/4 ADC.",
     "biz": "ADC CDMO(Lonza·Samsung·WuXi XDC)에 GMP mTG enzyme + Q-tag/RKAA-tag 설계 패키지. ADC $32.66B 2035.",
     "biz_model": "K / L",
     "score": {"M": 5, "F": 4, "R": 5, "W": 3, "IP": 4, "T": 4}, "weighted": 4.30,
     "risk": "Zedira/Hzymes commodity mTG와의 차별화 필요; US11786603 narrow-specificity 변이체 white-space 검증 필요.",
     "next": "Lonza Synaffix RFI; Araris RKAA-tag carve-out variant 후속 IP 매핑.",
     "rationale": "3라운드 연속 short-list 1·2위. Lonza+Samsung+Araris 자본 흐름 + AJICAP carve-out 명확 + R3 IP 3→4 상향 (M→H)."},
    {"rank": "1 (tie)", "id": "item_008", "name": "Peptiligase / OaAEP1 C247A",
     "definition": "OaAEP1 (C13 asparaginyl, cysteine) + Peptiligase (subtilisin BPN' Y217, S8 serine) — SPPS fragment 효소 ligation으로 GLP-1·radioligand peptide 제조.",
     "biz": "Bachem CEPS·PolyPeptide·EnzyTag·Sumitomo 대상 cGMP enzyme + 공정 라이선스. FDA Research-Grade Peptide 2026.1 enforce.",
     "biz_model": "L / K",
     "score": {"M": 5, "F": 4, "R": 5, "W": 3, "IP": 4, "T": 4}, "weighted": 4.30,
     "risk": "라이선스 ceiling 정량 부재(quote-only); cGMP 셋업 3~4년 유지.",
     "next": "Codexis-Merck Supply Assurance 모델 모방, Bachem CEPS RFI.",
     "rationale": "3라운드 연속 Top 1 또는 공동 1위. EnzyPep S8 vs OaAEP1 C13 fold carve-out 자명 + IP·T 모두 H 도달."},
    {"rank": "3", "id": "item_021", "name": "cGMP Sortase A / OaAEP1 (radioligand peptide-chelator)",
     "definition": "cGMP-grade Sortase A LPXTG + OaAEP1 C247A NGL로 DOTA/DOTAGA/NETA chelator를 peptide ligand에 site-specific 결합, ⁶⁴Cu/¹⁷⁷Lu/²²⁵Ac 라벨링.",
     "biz": "Radiopharma CDMO + Actithera·Nuclidium·PeptiDream·AZ-Fusion에 cGMP enzyme. NBE SMAC = ADC 한정 → radioligand white-space.",
     "biz_model": "K / L",
     "score": {"M": 4, "F": 4, "R": 5, "W": 5, "IP": 4, "T": 3}, "weighted": 4.25,
     "risk": "cGMP DMF 등록 3~4년 소요; USPTO 10556024 chelector-tag carve-out 추가 검증 필요.",
     "next": "AZ-Fusion / Aktis cGMP enzymatic conjugation RFI; chelator-tag 변이체 IP whitespace.",
     "rationale": "R2 신규 등장 → R3 +0.15 상승 (W 4→5). NBE SMAC carve-out + RLT $4.8B 2030 — radioligand white-space 가장 깨끗."},
    {"rank": "4", "id": "item_007", "name": "Engineered RNA ligase (splint, AOC/ASO)",
     "definition": "T4 Rnl2 / RtcB variant로 splint DNA 가이드 fragment ligation → 긴 siRNA·AOC 저비용 합성.",
     "biz": "올리고 CDMO·RNA 치료제 개발사에 cGMP enzyme + ECO Synthesis 워크플로 라이선스. Codexis-Merck $37.8M + Roche $6.0M 검증.",
     "biz_model": "L / K",
     "score": {"M": 4, "F": 4, "R": 5, "W": 4, "IP": 4, "T": 3}, "weighted": 4.10,
     "risk": "ECO Synthesis 진영 dominance; variant 청구항 carve-out 가능 but 정확 USPTO 번호 미확정.",
     "next": "Codexis ECO 패밀리 USPTO 검색; AOC enzymatic 채택률 R4 추적.",
     "rationale": "Novartis-Avidity $12B + Codexis 빅파마 첫 수주 → 시장 형성기 가장 명확. 3라운드 4위·5위 안정."},
    {"rank": "5 (tie)", "id": "item_003", "name": "Engineered Sortase A (Ca-independent)",
     "definition": "Caltech eSrtA 7M / 2A-9 directed-evolution variant — US10202593B2.",
     "biz": "ADC·AOC·radioligand CDMO + radiopharma 스타트업에 enzyme + tag 설계 dual track.",
     "biz_model": "L / K",
     "score": {"M": 4, "F": 4, "R": 5, "W": 3, "IP": 3, "T": 4}, "weighted": 3.95,
     "risk": "commodity화 추세 — Sortase A는 academic 풍부, 차세대 evolution 필수.",
     "next": "R4: commodity vs premium variant 단가 비교.",
     "rationale": "3라운드 일관 5위. ADC + radioligand fork 가능 → item_021과 dual track 시너지."},
    {"rank": "5 (tie)", "id": "item_005", "name": "EndoS2 glycosynthase mutant",
     "definition": "S. pyogenes EndoS2 D184M class — 항체 N297 glycan trim → 균일 G2 결합 (ADCC 강화, biosimilar 균질화).",
     "biz": "Lonza Synaffix 통합으로 ADC GMP 표준 step 진입. carve-out 변이체(D184M·EndoF/H) catalog 또는 Synaffix 라이선스 대안.",
     "biz_model": "K / L",
     "score": {"M": 4, "F": 4, "R": 5, "W": 3, "IP": 3, "T": 4}, "weighted": 3.95,
     "risk": "Genovis/Synaffix 시장 점유 — donor sugar 공급망 구축 필요.",
     "next": "R4: Lonza Synaffix L primary 격상 검토; biosimilar 개발사 RFI.",
     "rationale": "R3 Lonza Synaffix 통합 = ADC GMP 표준 step 공식화. 3라운드 일관 5위 + biosimilar trail."},
    {"rank": "7", "id": "item_017", "name": "Inorganic pyrophosphatase (IVT helper)",
     "definition": "Yeast PPase — T7 RNAP IVT의 PPi 피드백 억제 해제 → RNA yield +15-25%.",
     "biz": "Captive/Catalog OEM — Hzymes yeast PPase FDA DMF #036853 채택 확정. GMP-IVT $361.9M→$923M 정량.",
     "biz_model": "C",
     "score": {"M": 4, "F": 5, "R": 5, "W": 2, "IP": 2, "T": 4}, "weighted": 3.90,
     "risk": "Whitespace 약함(W=2); IP=2.",
     "next": "Hzymes 외 differentiator (catalytic 변이체) IP 매핑.",
     "rationale": "R2 신규 진입. F=5 GMP 성숙도 + R=5 + T=4 즉시성. 단 IP·whitespace 약점 명시."},
]

# ----- Recommendations grouped (Sheet 8) -----

RECOMMENDATIONS = {
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
}

# ----- Score history & shortlist membership (Sheet 6) -----

SHORTLIST_HISTORY = {
    "item_002": {1: 4.20, 2: 4.20, 3: 4.30},
    "item_003": {1: 3.95, 2: 3.95, 3: 3.95},
    "item_005": {1: 3.95, 2: 3.95, 3: 3.95},
    "item_006": {1: 4.05, 2: 3.80, 3: 3.80},
    "item_007": {1: 4.10, 2: 4.10, 3: 4.10},
    "item_008": {1: 4.20, 2: 4.30, 3: 4.30},
    "item_009": {1: 3.75, 2: 3.75, 3: 3.75},
    "item_017": {2: 3.90, 3: 3.90},
    "item_021": {2: 4.10, 3: 4.25},
}
SHORTLIST_MEMBERSHIP = {
    "item_002": (True, True, True),
    "item_003": (True, True, True),
    "item_005": (True, True, True),
    "item_006": (True, False, False),
    "item_007": (True, True, True),
    "item_008": (True, True, True),
    "item_009": (True, False, False),
    "item_017": (False, True, True),
    "item_021": (False, True, True),
}
SHORTLIST_NAMES = {
    "item_002": "Engineered mTG (ADC)",
    "item_003": "Engineered Sortase A (Ca-independent)",
    "item_005": "EndoS2 glycosynthase mutant",
    "item_006": "Engineered T7 RNAP (low-dsRNA, capping)",
    "item_007": "Engineered RNA ligase (splint)",
    "item_008": "Peptiligase / OaAEP1 C247A",
    "item_009": "Engineered Peptide Amidating Enzyme (PAM)",
    "item_017": "Inorganic pyrophosphatase (IVT helper)",
    "item_021": "cGMP Sortase A / OaAEP1 (radioligand)",
}

# ----- Sheet 0 / 9 metadata -----

TOP3 = [
    ("1 (tie)", "item_002", "Engineered mTG (ADC)", 4.30, "★★★",
     "3라운드 연속 short-list 1·2위. Lonza+Samsung+Araris 자본 흐름 + AJICAP carve-out 명확."),
    ("1 (tie)", "item_008", "Peptiligase / OaAEP1 C247A", 4.30, "★★★",
     "3라운드 연속 Top 1 또는 공동 1위. EnzyPep vs OaAEP1 fold carve-out 자명 + FDA Research-Grade Peptide."),
    ("3", "item_021", "cGMP Sortase A / OaAEP1 (radioligand)", 4.25, "★★",
     "R2 신규 등장 → R3에서 +0.15 상승. NBE SMAC carve-out + RLT $4.8B 2030."),
]

EXEC_SUMMARY = (
    "3라운드 동안 단백질·펩타이드 process/formulation/diagnostic 효소 시장에서 누적 활성 후보 23개"
    "(R1 14 → R2 +9 = 23 → R3 23 유지)를 발굴·평가하고 누적 short-list 7개(★★★ 5 + ★★ 2)를 확정했다. "
    "R3 short-list 7명 전원이 R2 멤버와 동일 — ranking 수렴 강함. "
    "공통 패러다임: 빅파마 modality 트렌드는 모두 결합(conjugation)·합성(ligation)·후처리(modification) 효소 "
    "수요로 수렴하며, 임상 부담 없는 process enzyme이 가장 큰 화이트스페이스를 보유한다. "
    "R3 결정적 결론: Lonza Synaffix 통합(2026-02-19) = enzymatic ADC conjugation 빅 CDMO 표준 채택 확정; "
    "EfHyl8 PL8 vs Halozyme PH20 IP 회피 자명; EnzyPep S8 vs OaAEP1 C13 carve-out 자명; "
    "NBE SMAC = ADC 한정, radioligand white-space 확인."
)

OPEN_QUESTIONS = [
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
]
R4_TRIGGERS = [
    "신규 빅파마 M&A ≥$1B in scope (현재 없음).",
    "Top-5 SD ΔR3→R4 ≥ 0.15 (R3 SD 0.136 → R4 변동 시 발동).",
    "Halozyme vs Merck IPR 결과 공시.",
    "사용자 신규 키워드 추가.",
]


# ---------------------------------------------------------------------------
# 1-pager card loader (for docx appendix)
# ---------------------------------------------------------------------------

R3_CARD_PATHS = {
    "item_002": ROOT / "candidates/item_002_engineered_mtg_adc.md",
    "item_003": ROOT / "candidates/item_003_engineered_sortase_a.md",
    "item_005": ROOT / "candidates/item_005_endos2_glycosynthase.md",
    "item_007": ROOT / "candidates/item_007_engineered_rna_ligase.md",
    "item_008": ROOT / "candidates/item_008_oaaep1_peptide_ligase.md",
    "item_017": ROOT / "iterations/iter_02/candidates/item_017_inorganic_pyrophosphatase.md",
    "item_021": ROOT / "iterations/iter_02/candidates/item_021_cgmp_sortase_oaaep1_radioligand.md",
}


def load_card_text(path: Path) -> str:
    if not path.exists():
        return f"[1-pager 파일 없음: {path.relative_to(ROOT)}]"
    return path.read_text(encoding="utf-8")


# ---------------------------------------------------------------------------
# Consolidated XLSX
# ---------------------------------------------------------------------------

def build_consolidated_xlsx(date: str, out_path: Path):
    out_path.parent.mkdir(parents=True, exist_ok=True)
    current = read_csv_rows(ROOT / "data" / "candidates_current.csv")
    history = read_csv_rows(ROOT / "data" / "candidates_history.csv")

    wb = Workbook()

    # =========================================================================
    # Sheet 0 — 표지·요약
    # =========================================================================
    ws = wb.active
    ws.title = "0.표지요약"
    ws["A1"] = "Consolidated Digest — Round 1–3 통합"
    ws["A1"].font = Font(name="맑은 고딕", bold=True, size=18, color="1F4E78")
    ws.row_dimensions[1].height = 32
    ws["A2"] = f"작성일: 2026-05-21   |   대상 일자: {date[:4]}-{date[4:6]}-{date[6:]}"
    ws["A2"].font = Font(name="맑은 고딕", italic=True, size=10, color="595959")
    ws["A3"] = "run_id 궤적: 20260521-A (R1 broad_scan) → 20260521-B (R2 deferred_and_boost) → 20260521-C (R3 quantitative_validation_and_ip_fto)"
    ws["A3"].font = Font(name="맑은 고딕", italic=True, size=10, color="595959")

    ws["A5"] = "▣ 한 페이지 Executive Summary"
    ws["A5"].font = SUBHEAD_FONT
    ws.merge_cells("A6:F12")
    ws["A6"] = EXEC_SUMMARY
    ws["A6"].alignment = WRAP
    ws["A6"].font = BODY_FONT

    ws["A14"] = "▣ 최종 추천 Top 3 (★ 등급)"
    ws["A14"].font = SUBHEAD_FONT
    headers = ["순위", "id", "아이템", "R3 가중합", "신뢰도", "한 줄 사유"]
    for i, h in enumerate(headers, start=1):
        ws.cell(row=15, column=i, value=h)
    style_header_row(ws, 15, len(headers))
    for r, (rank, cid, name, sc, tier, why) in enumerate(TOP3, start=16):
        ws.cell(row=r, column=1, value=rank)
        ws.cell(row=r, column=2, value=cid)
        ws.cell(row=r, column=3, value=name)
        ws.cell(row=r, column=4, value=sc)
        ws.cell(row=r, column=5, value=tier)
        ws.cell(row=r, column=6, value=why)
        apply_body_style(ws, r, 6, fill=SHORTLIST_FILL)
        ws.row_dimensions[r].height = 50
    set_col_widths(ws, [10, 12, 32, 12, 10, 60])

    ws.cell(row=21, column=1, value="▣ 본 보고서 구성 (10개 섹션)").font = SUBHEAD_FONT
    toc = [
        "0. 표지·요약 — 현재 시트.",
        "1. 선정 방법론 — SSOT / 6축 가중치 / weighted_score 산식 / short-list·★ 등급 / business_model 분류.",
        "2. R1 탐색 결과 — R1 시장 신호·후보 14개 (short-list 7 하이라이트).",
        "3. R2 탐색 결과 — boost focus 5 + 신규/부활 9 + short-list in/out.",
        "4. R3 탐색 결과 — 정량·IP·RFI 핵심 발견 + R2→R3 점수 변동.",
        "5. Cumulative 후보 23개 풀 — 활성 후보 전체 표.",
        "6. 점수 궤적 (R1→R2→R3) — 라운드별 점수 + sparkline + confidence M→H 상향.",
        "7. Final Short-list 7개 상세 — 정의·6축·위험·선정 사유.",
        "8. 사업화 형태별 추천 — 즉시(≤1년) / 중기(1~2년) / 장기(2~5년).",
        "9. Open Questions / R4+ Triggers / 메타.",
    ]
    for i, line in enumerate(toc, start=22):
        ws.cell(row=i, column=1, value=line).font = BODY_FONT
        ws.cell(row=i, column=1).alignment = WRAP
        ws.merge_cells(start_row=i, start_column=1, end_row=i, end_column=6)
        ws.row_dimensions[i].height = 20

    # =========================================================================
    # Sheet 1 — 선정 방법론
    # =========================================================================
    ws1 = wb.create_sheet("1.선정방법론")
    ws1["A1"] = "▣ 평가 프레임워크 (SSOT)"
    ws1["A1"].font = SUBHEAD_FONT
    ws1.merge_cells("A2:E4")
    ws1["A2"] = METHODOLOGY["ssot"]
    ws1["A2"].alignment = WRAP
    ws1["A2"].font = BODY_FONT
    ws1["A2"].border = BORDER

    ws1["A6"] = "▣ 6축 가중치 / weighted_score 산식"
    ws1["A6"].font = SUBHEAD_FONT
    headers = ["축", "이름", "가중치", "정의 / 평가 기준"]
    for i, h in enumerate(headers, start=1):
        ws1.cell(row=7, column=i, value=h)
    style_header_row(ws1, 7, len(headers))
    for r, (code, name, weight, definition) in enumerate(METHODOLOGY["axes"], start=8):
        ws1.cell(row=r, column=1, value=code)
        ws1.cell(row=r, column=2, value=name)
        ws1.cell(row=r, column=3, value=f"{weight:.2f}")
        ws1.cell(row=r, column=4, value=definition)
        apply_body_style(ws1, r, len(headers))
        ws1.cell(row=r, column=1).alignment = CENTER
        ws1.cell(row=r, column=3).alignment = CENTER
        ws1.row_dimensions[r].height = 32
    ws1.cell(row=14, column=1, value=METHODOLOGY["formula"]).font = Font(name="맑은 고딕", bold=True, size=10)
    ws1.merge_cells("A14:D14")

    ws1["A16"] = "▣ Short-list 규칙"
    ws1["A16"].font = SUBHEAD_FONT
    ws1.merge_cells("A17:E18")
    ws1["A17"] = METHODOLOGY["shortlist_rule"]
    ws1["A17"].alignment = WRAP
    ws1["A17"].font = BODY_FONT

    ws1["A20"] = "▣ Confidence H/M/L (R2부터 도입)"
    ws1["A20"].font = SUBHEAD_FONT
    headers = ["등급", "정의"]
    for i, h in enumerate(headers, start=1):
        ws1.cell(row=21, column=i, value=h)
    style_header_row(ws1, 21, len(headers))
    for r, (tier, defn) in enumerate(METHODOLOGY["confidence"], start=22):
        ws1.cell(row=r, column=1, value=tier)
        ws1.cell(row=r, column=2, value=defn)
        apply_body_style(ws1, r, len(headers))
        ws1.row_dimensions[r].height = 28
        if tier.startswith("H"):
            ws1.cell(row=r, column=1).fill = CONFIDENCE_FILLS["H"]
        elif tier.startswith("M"):
            ws1.cell(row=r, column=1).fill = CONFIDENCE_FILLS["M"]
        elif tier.startswith("L"):
            ws1.cell(row=r, column=1).fill = CONFIDENCE_FILLS["L"]

    ws1["A26"] = "▣ ★★★ / ★★ / ★ 등급 규칙"
    ws1["A26"].font = SUBHEAD_FONT
    for i, h in enumerate(["등급", "정의"], start=1):
        ws1.cell(row=27, column=i, value=h)
    style_header_row(ws1, 27, 2)
    for r, (tier, defn) in enumerate(METHODOLOGY["tier"], start=28):
        ws1.cell(row=r, column=1, value=tier)
        ws1.cell(row=r, column=2, value=defn)
        apply_body_style(ws1, r, 2)
        ws1.cell(row=r, column=1).font = Font(name="맑은 고딕", bold=True, size=11, color="C00000")
        ws1.row_dimensions[r].height = 26

    ws1["A32"] = "▣ Business model 분류 (L / K / C / S / H)"
    ws1["A32"].font = SUBHEAD_FONT
    for i, h in enumerate(["코드", "설명"], start=1):
        ws1.cell(row=33, column=i, value=h)
    style_header_row(ws1, 33, 2)
    for r, (code, defn) in enumerate(METHODOLOGY["business_model"], start=34):
        ws1.cell(row=r, column=1, value=code)
        ws1.cell(row=r, column=2, value=defn)
        apply_body_style(ws1, r, 2)
        ws1.row_dimensions[r].height = 26

    set_col_widths(ws1, [22, 22, 12, 70, 30])

    # =========================================================================
    # Sheet 2 — R1 탐색 결과
    # =========================================================================
    ws2 = wb.create_sheet("2.R1탐색결과")
    ws2["A1"] = "Round 1 — broad_scan (run_id 20260521-A)"
    ws2["A1"].font = Font(name="맑은 고딕", bold=True, size=14, color="1F4E78")
    ws2.row_dimensions[1].height = 24
    ws2["A2"] = "▣ R1 시장 신호 요약 (Top 5 of 18)"
    ws2["A2"].font = SUBHEAD_FONT
    ws2.merge_cells("A3:F5")
    ws2["A3"] = R1_NARRATIVE["summary"]
    ws2["A3"].alignment = WRAP
    ws2["A3"].font = BODY_FONT

    headers = ["#", "신호", "출처", "함의"]
    for i, h in enumerate(headers, start=1):
        ws2.cell(row=7, column=i, value=h)
    style_header_row(ws2, 7, len(headers))
    for r, row in enumerate(R1_NARRATIVE["signals_top5"], start=8):
        for c, v in enumerate(row, start=1):
            ws2.cell(row=r, column=c, value=v)
        apply_body_style(ws2, r, len(headers))
        ws2.row_dimensions[r].height = 56

    sl_ids = set(R1_NARRATIVE["shortlist_ids"])
    base = 14
    ws2.cell(row=base, column=1, value="▣ R1 후보 14개 전체 (short-list 7개는 음영)").font = SUBHEAD_FONT
    headers = ["id", "아이템 (1줄 정의)", "핵심 신호", "R1 가중합", "Short-list"]
    for i, h in enumerate(headers, start=1):
        ws2.cell(row=base + 1, column=i, value=h)
    style_header_row(ws2, base + 1, len(headers))
    for r, (cid, (defn, signal, weighted)) in enumerate(sorted(R1_NARRATIVE["items_brief"].items()), start=base + 2):
        in_sl = cid in sl_ids
        ws2.cell(row=r, column=1, value=cid)
        ws2.cell(row=r, column=2, value=defn)
        ws2.cell(row=r, column=3, value=signal)
        ws2.cell(row=r, column=4, value=f"{weighted:.2f}")
        ws2.cell(row=r, column=5, value="✓" if in_sl else "")
        apply_body_style(ws2, r, len(headers), fill=(SHORTLIST_FILL if in_sl else None))
        ws2.cell(row=r, column=4).alignment = CENTER
        ws2.cell(row=r, column=5).alignment = CENTER
        if in_sl:
            ws2.cell(row=r, column=5).font = Font(name="맑은 고딕", bold=True, color="C00000", size=11)
        ws2.row_dimensions[r].height = 40
    set_col_widths(ws2, [10, 55, 50, 10, 12])
    ws2.column_dimensions["B"].width = 55

    # =========================================================================
    # Sheet 3 — R2 탐색 결과
    # =========================================================================
    ws3 = wb.create_sheet("3.R2탐색결과")
    ws3["A1"] = "Round 2 — deferred_and_boost (run_id 20260521-B)"
    ws3["A1"].font = Font(name="맑은 고딕", bold=True, size=14, color="1F4E78")
    ws3.row_dimensions[1].height = 24
    ws3.merge_cells("A2:E5")
    ws3["A2"] = R2_NARRATIVE["summary"]
    ws3["A2"].alignment = WRAP
    ws3["A2"].font = BODY_FONT

    ws3["A7"] = "▣ R2 Boost Focus (5개 영역)"
    ws3["A7"].font = SUBHEAD_FONT
    for r, focus in enumerate(R2_NARRATIVE["boost_focus"], start=8):
        ws3.cell(row=r, column=1, value=f"{r-7}.")
        ws3.cell(row=r, column=2, value=focus)
        apply_body_style(ws3, r, 2)
        ws3.cell(row=r, column=1).alignment = CENTER
        ws3.row_dimensions[r].height = 22

    ws3["A14"] = "▣ R2 시장 신호 (Top 5)"
    ws3["A14"].font = SUBHEAD_FONT
    headers = ["#", "신호", "출처", "함의"]
    for i, h in enumerate(headers, start=1):
        ws3.cell(row=15, column=i, value=h)
    style_header_row(ws3, 15, len(headers))
    for r, row in enumerate(R2_NARRATIVE["signals_top5"], start=16):
        for c, v in enumerate(row, start=1):
            ws3.cell(row=r, column=c, value=v)
        apply_body_style(ws3, r, len(headers))
        ws3.row_dimensions[r].height = 60

    base = 22
    ws3.cell(row=base, column=1, value="▣ R2 신규·부활 후보 9개").font = SUBHEAD_FONT
    headers = ["id", "1줄 정의", "핵심 신호 (R2)", "R2 가중합", "Short-list"]
    for i, h in enumerate(headers, start=1):
        ws3.cell(row=base + 1, column=i, value=h)
    style_header_row(ws3, base + 1, len(headers))
    for r, (cid, (defn, signal, weighted, sl)) in enumerate(sorted(R2_NARRATIVE["new_revived_items"].items()), start=base + 2):
        ws3.cell(row=r, column=1, value=cid)
        ws3.cell(row=r, column=2, value=defn)
        ws3.cell(row=r, column=3, value=signal)
        ws3.cell(row=r, column=4, value=f"{weighted:.2f}")
        ws3.cell(row=r, column=5, value="✓" if sl else "")
        apply_body_style(ws3, r, len(headers), fill=(SHORTLIST_FILL if sl else None))
        ws3.cell(row=r, column=4).alignment = CENTER
        ws3.cell(row=r, column=5).alignment = CENTER
        if sl:
            ws3.cell(row=r, column=5).font = Font(name="맑은 고딕", bold=True, color="C00000", size=11)
        ws3.row_dimensions[r].height = 40

    in_out_base = base + 2 + len(R2_NARRATIVE["new_revived_items"]) + 2
    ws3.cell(row=in_out_base, column=1, value="▣ R1→R2 Short-list 변동 (item_006·009 OUT, item_017·021 IN)").font = SUBHEAD_FONT
    headers = ["후보", "변동", "사유"]
    for i, h in enumerate(headers, start=1):
        ws3.cell(row=in_out_base + 1, column=i, value=h)
    style_header_row(ws3, in_out_base + 1, len(headers))
    for r, (who, change, why) in enumerate(R2_NARRATIVE["shortlist_in_out"], start=in_out_base + 2):
        ws3.cell(row=r, column=1, value=who)
        ws3.cell(row=r, column=2, value=change)
        ws3.cell(row=r, column=3, value=why)
        apply_body_style(ws3, r, len(headers))
        ws3.row_dimensions[r].height = 32
    set_col_widths(ws3, [22, 55, 55, 12, 12])

    # =========================================================================
    # Sheet 4 — R3 탐색 결과
    # =========================================================================
    ws4 = wb.create_sheet("4.R3탐색결과")
    ws4["A1"] = "Round 3 — quantitative_validation_and_ip_fto (run_id 20260521-C)"
    ws4["A1"].font = Font(name="맑은 고딕", bold=True, size=14, color="1F4E78")
    ws4.row_dimensions[1].height = 24
    ws4.merge_cells("A2:E5")
    ws4["A2"] = R3_NARRATIVE["summary"]
    ws4["A2"].alignment = WRAP
    ws4["A2"].font = BODY_FONT

    ws4["A7"] = "▣ R3 핵심 발견 (정량 / IP / RFI)"
    ws4["A7"].font = SUBHEAD_FONT
    for r, finding in enumerate(R3_NARRATIVE["key_findings"], start=8):
        ws4.cell(row=r, column=1, value=f"{r-7}.")
        ws4.cell(row=r, column=2, value=finding)
        apply_body_style(ws4, r, 2)
        ws4.cell(row=r, column=1).alignment = CENTER
        ws4.row_dimensions[r].height = 44

    base = 16
    ws4.cell(row=base, column=1, value="▣ R2 → R3 점수 변동 (raw 가중합 변동은 단 2건)").font = SUBHEAD_FONT
    headers = ["id", "R2 가중합", "R3 가중합", "Δ", "사유"]
    for i, h in enumerate(headers, start=1):
        ws4.cell(row=base + 1, column=i, value=h)
    style_header_row(ws4, base + 1, len(headers))
    for r, (cid, r2sc, r3sc, delta, reason) in enumerate(R3_NARRATIVE["score_changes"], start=base + 2):
        ws4.cell(row=r, column=1, value=cid)
        ws4.cell(row=r, column=2, value=f"{r2sc:.2f}")
        ws4.cell(row=r, column=3, value=f"{r3sc:.2f}")
        ws4.cell(row=r, column=4, value=delta)
        ws4.cell(row=r, column=5, value=reason)
        apply_body_style(ws4, r, len(headers), fill=SHORTLIST_FILL)
        for c in (2, 3, 4):
            ws4.cell(row=r, column=c).alignment = CENTER
        ws4.cell(row=r, column=4).font = Font(name="맑은 고딕", bold=True, color="006100", size=10)
        ws4.row_dimensions[r].height = 40

    base2 = base + 2 + len(R3_NARRATIVE["score_changes"]) + 2
    ws4.cell(row=base2, column=1, value="▣ R2→R3 confidence M→H 상향 (7건 / 5개 후보 모두 short-list)").font = SUBHEAD_FONT
    headers = ["id", "상향 축"]
    for i, h in enumerate(headers, start=1):
        ws4.cell(row=base2 + 1, column=i, value=h)
    style_header_row(ws4, base2 + 1, len(headers))
    for r, (cid, axis) in enumerate(R3_NARRATIVE["confidence_uplift"], start=base2 + 2):
        ws4.cell(row=r, column=1, value=cid)
        ws4.cell(row=r, column=2, value=axis)
        apply_body_style(ws4, r, len(headers))
        ws4.cell(row=r, column=2).fill = CONFIDENCE_FILLS["H"]
        ws4.row_dimensions[r].height = 24
    set_col_widths(ws4, [12, 14, 14, 8, 70, 14])

    # =========================================================================
    # Sheet 5 — Cumulative 후보 23개 풀
    # =========================================================================
    ws5 = wb.create_sheet("5.Cumulative23개")
    cols = ["rank", "id", "아이템", "class (EC)", "분류", "biz1", "biz2", "lifecycle",
            "R1", "R2", "R3", "★ 등급", "SL"]
    for i, h in enumerate(cols, start=1):
        ws5.cell(row=1, column=i, value=h)
    style_header_row(ws5, 1, len(cols))
    sorted_cur = sorted(current, key=lambda r: int(r["rank"]))
    # build per-iter weighted_score lookup
    score_by_id = defaultdict(dict)  # id -> {iter: weighted}
    for row in history:
        try:
            it = int(row["iter"])
            sc = float(row["weighted_score"])
            score_by_id[row["id"]][it] = sc
        except (ValueError, KeyError):
            continue
    for r, row in enumerate(sorted_cur, start=2):
        cid = row["id"]
        ws5.cell(row=r, column=1, value=int(row["rank"]))
        ws5.cell(row=r, column=2, value=cid)
        ws5.cell(row=r, column=3, value=row["item_name"])
        ws5.cell(row=r, column=4, value=row.get("class", ""))
        ws5.cell(row=r, column=5, value=row.get("inclusion_bucket", ""))
        ws5.cell(row=r, column=6, value=row.get("business_model_primary", ""))
        ws5.cell(row=r, column=7, value=row.get("business_model_secondary", ""))
        ws5.cell(row=r, column=8, value=row.get("lifecycle", ""))
        scores = score_by_id.get(cid, {})
        for c, it in zip((9, 10, 11), (1, 2, 3)):
            v = scores.get(it)
            ws5.cell(row=r, column=c, value=(f"{v:.2f}" if v is not None else "—"))
        # tier
        mem = SHORTLIST_MEMBERSHIP.get(cid)
        if mem is not None:
            count = sum(mem)
            tier = "★★★" if count == 3 else "★★" if count == 2 else "★"
        else:
            tier = "—"
        ws5.cell(row=r, column=12, value=tier)
        ws5.cell(row=r, column=13, value="✓" if row.get("shortlist") == "1" else "")
        sl_fill = SHORTLIST_FILL if row.get("shortlist") == "1" else None
        apply_body_style(ws5, r, len(cols), fill=sl_fill)
        for c in (1, 9, 10, 11, 12, 13):
            ws5.cell(row=r, column=c).alignment = CENTER
        if tier == "★★★":
            ws5.cell(row=r, column=12).font = Font(name="맑은 고딕", bold=True, color="C00000", size=11)
        elif tier == "★★":
            ws5.cell(row=r, column=12).font = Font(name="맑은 고딕", bold=True, color="C65911", size=10)
        ws5.row_dimensions[r].height = 36
    set_col_widths(ws5, [6, 10, 38, 24, 18, 6, 6, 22, 8, 8, 8, 9, 6])
    ws5.freeze_panes = "C2"

    # =========================================================================
    # Sheet 6 — 점수 궤적 (R1→R2→R3)
    # =========================================================================
    ws6 = wb.create_sheet("6.점수궤적")
    cols = ["id", "아이템", "R1", "R2", "R3", "누적 Δ", "sparkline", "R1 SL", "R2 SL", "R3 SL", "횟수", "★"]
    for i, h in enumerate(cols, start=1):
        ws6.cell(row=1, column=i, value=h)
    style_header_row(ws6, 1, len(cols))
    ordering = sorted(SHORTLIST_HISTORY.keys(),
                       key=lambda i: (-(SHORTLIST_HISTORY[i].get(3, 0) or 0),
                                      -(SHORTLIST_HISTORY[i].get(1, 0) or 0)))
    for r, cid in enumerate(ordering, start=2):
        s = SHORTLIST_HISTORY[cid]
        mem = SHORTLIST_MEMBERSHIP.get(cid, (False, False, False))
        count = sum(mem)
        tier = "★★★" if count == 3 else "★★" if count == 2 else "★"
        r1 = s.get(1); r2 = s.get(2); r3 = s.get(3)
        base_v = r1 if r1 is not None else r2
        delta = (r3 - base_v) if (r3 is not None and base_v is not None) else None
        # text sparkline
        vals = [v for v in (r1, r2, r3) if v is not None]
        sparkline = ""
        if vals:
            lo, hi = min(vals), max(vals)
            blocks = "▁▂▃▄▅▆▇█"
            def bar(v):
                if v is None: return " "
                if hi == lo: return blocks[4]
                idx = round((v - lo) / (hi - lo) * (len(blocks) - 1))
                return blocks[idx]
            sparkline = "".join(bar(v) for v in (r1, r2, r3))

        ws6.cell(row=r, column=1, value=cid)
        ws6.cell(row=r, column=2, value=SHORTLIST_NAMES.get(cid, cid))
        ws6.cell(row=r, column=3, value=f"{r1:.2f}" if r1 is not None else "—")
        ws6.cell(row=r, column=4, value=f"{r2:.2f}" if r2 is not None else "—")
        ws6.cell(row=r, column=5, value=f"{r3:.2f}" if r3 is not None else "—")
        ws6.cell(row=r, column=6, value=(f"{delta:+.2f}" if delta is not None else "—"))
        ws6.cell(row=r, column=7, value=sparkline)
        ws6.cell(row=r, column=8, value="✓" if mem[0] else "")
        ws6.cell(row=r, column=9, value="✓" if mem[1] else "")
        ws6.cell(row=r, column=10, value="✓" if mem[2] else "")
        ws6.cell(row=r, column=11, value=count)
        ws6.cell(row=r, column=12, value=tier)
        apply_body_style(ws6, r, len(cols), fill=(SHORTLIST_FILL if count >= 2 else None))
        for c in range(3, 13):
            ws6.cell(row=r, column=c).alignment = CENTER
        if count == 3:
            ws6.cell(row=r, column=12).font = Font(name="맑은 고딕", bold=True, color="C00000", size=11)
        elif count == 2:
            ws6.cell(row=r, column=12).font = Font(name="맑은 고딕", bold=True, color="C65911", size=10)
        if delta is not None:
            color = "C00000" if delta < 0 else ("006100" if delta > 0 else "595959")
            ws6.cell(row=r, column=6).font = Font(name="맑은 고딕", bold=True, color=color, size=10)
        ws6.row_dimensions[r].height = 28
    set_col_widths(ws6, [10, 38, 7, 7, 7, 9, 10, 6, 6, 6, 7, 8])
    ws6.freeze_panes = "C2"

    # confidence uplift summary
    cu_base = len(ordering) + 4
    ws6.cell(row=cu_base, column=1, value="▣ R2→R3 confidence M→H 상향 (7건 / 5개 후보)").font = SUBHEAD_FONT
    headers = ["id", "상향 축"]
    for i, h in enumerate(headers, start=1):
        ws6.cell(row=cu_base + 1, column=i, value=h)
    style_header_row(ws6, cu_base + 1, len(headers))
    for r, (cid, axis) in enumerate(R3_NARRATIVE["confidence_uplift"], start=cu_base + 2):
        ws6.cell(row=r, column=1, value=cid)
        ws6.cell(row=r, column=2, value=axis)
        apply_body_style(ws6, r, len(headers))
        ws6.cell(row=r, column=2).fill = CONFIDENCE_FILLS["H"]
        ws6.row_dimensions[r].height = 22

    # =========================================================================
    # Sheet 7 — Final Short-list 7개 상세
    # =========================================================================
    ws7 = wb.create_sheet("7.FinalShortList")
    cols = ["rank", "id", "아이템", "biz_model", "정의", "사업화 시나리오",
            "M", "F", "R", "W", "IP", "T", "가중합", "위험·미지수", "다음 액션", "선정 사유"]
    for i, h in enumerate(cols, start=1):
        ws7.cell(row=1, column=i, value=h)
    style_header_row(ws7, 1, len(cols))
    for r, item in enumerate(FINAL_SHORTLIST, start=2):
        ws7.cell(row=r, column=1, value=item["rank"])
        ws7.cell(row=r, column=2, value=item["id"])
        ws7.cell(row=r, column=3, value=item["name"])
        ws7.cell(row=r, column=4, value=item["biz_model"])
        ws7.cell(row=r, column=5, value=item["definition"])
        ws7.cell(row=r, column=6, value=item["biz"])
        for c, k in enumerate(["M", "F", "R", "W", "IP", "T"], start=7):
            s = item["score"][k]
            cell = ws7.cell(row=r, column=c, value=s)
            cell.alignment = CENTER
            cell.font = Font(name="맑은 고딕", size=10, bold=True)
            cell.fill = SCORE_FILLS[s]
            cell.border = BORDER
        cell = ws7.cell(row=r, column=13, value=item["weighted"])
        cell.alignment = CENTER
        cell.font = Font(name="맑은 고딕", size=10, bold=True)
        cell.number_format = "0.00"
        cell.border = BORDER
        ws7.cell(row=r, column=14, value=item["risk"])
        ws7.cell(row=r, column=15, value=item["next"])
        ws7.cell(row=r, column=16, value=item["rationale"])
        for c in (1, 2, 3, 4, 5, 6, 14, 15, 16):
            cell = ws7.cell(row=r, column=c)
            cell.font = BODY_FONT
            cell.alignment = WRAP
            cell.border = BORDER
            cell.fill = SHORTLIST_FILL
        ws7.row_dimensions[r].height = 140
    set_col_widths(ws7, [10, 10, 30, 10, 42, 44, 5, 5, 5, 5, 5, 5, 8, 34, 34, 40])
    ws7.freeze_panes = "C2"

    # =========================================================================
    # Sheet 8 — 사업화 형태별 추천
    # =========================================================================
    ws8 = wb.create_sheet("8.사업화형태별추천")
    ws8["A1"] = "▣ 사업화 형태별 추천 (즉시 / 중기 / 장기)"
    ws8["A1"].font = Font(name="맑은 고딕", bold=True, size=14, color="1F4E78")
    headers = ["우선", "id", "아이템", "등급", "R3 점수", "biz", "한 줄"]
    cur_row = 3
    for section_title, key in [("즉시 착수 (≤1년 ROI, K primary)", "immediate"),
                                ("중기 검증 (1~2년 ROI, L primary)", "mid_term"),
                                ("장기 R&D (2~5년 ROI)", "long_term")]:
        ws8.cell(row=cur_row, column=1, value=f"▣ {section_title}").font = SUBHEAD_FONT
        ws8.cell(row=cur_row, column=1).fill = SUBHEAD_FILL
        ws8.merge_cells(start_row=cur_row, start_column=1, end_row=cur_row, end_column=7)
        cur_row += 1
        for i, h in enumerate(headers, start=1):
            ws8.cell(row=cur_row, column=i, value=h)
        style_header_row(ws8, cur_row, len(headers))
        cur_row += 1
        for entry in RECOMMENDATIONS[key]:
            pri, cid, name, tier, sc, bm, line = entry
            ws8.cell(row=cur_row, column=1, value=pri)
            ws8.cell(row=cur_row, column=2, value=cid)
            ws8.cell(row=cur_row, column=3, value=name)
            ws8.cell(row=cur_row, column=4, value=tier)
            ws8.cell(row=cur_row, column=5, value=sc)
            ws8.cell(row=cur_row, column=6, value=bm)
            ws8.cell(row=cur_row, column=7, value=line)
            apply_body_style(ws8, cur_row, len(headers), fill=SHORTLIST_FILL)
            for c in (1, 4, 5, 6):
                ws8.cell(row=cur_row, column=c).alignment = CENTER
            ws8.row_dimensions[cur_row].height = 48
            cur_row += 1
        cur_row += 1
    set_col_widths(ws8, [6, 10, 36, 14, 10, 8, 72])

    # =========================================================================
    # Sheet 9 — Open Questions / R4+ Triggers / 메타
    # =========================================================================
    ws9 = wb.create_sheet("9.OpenQR4메타")
    ws9["A1"] = "▣ Open Questions (R3 미해결 / R4 1순위)"
    ws9["A1"].font = SUBHEAD_FONT
    for r, q in enumerate(OPEN_QUESTIONS, start=2):
        ws9.cell(row=r, column=1, value=f"Q{r-1}")
        ws9.cell(row=r, column=2, value=q)
        apply_body_style(ws9, r, 2)
        ws9.cell(row=r, column=1).alignment = CENTER
        ws9.row_dimensions[r].height = 32

    trig_start = 2 + len(OPEN_QUESTIONS) + 2
    ws9.cell(row=trig_start, column=1, value="▣ Quality-gate / R4 자동 발동 트리거 후보").font = SUBHEAD_FONT
    for i, t in enumerate(R4_TRIGGERS, start=1):
        ws9.cell(row=trig_start + i, column=1, value="•")
        ws9.cell(row=trig_start + i, column=2, value=t)
        apply_body_style(ws9, trig_start + i, 2)
        ws9.cell(row=trig_start + i, column=1).alignment = CENTER
        ws9.row_dimensions[trig_start + i].height = 24

    meta_start = trig_start + len(R4_TRIGGERS) + 3
    ws9.cell(row=meta_start, column=1, value="▣ 3-Round 통계 (Top-5 가중합 SD 궤적)").font = SUBHEAD_FONT
    headers = ["라운드", "Top-5 가중합", "평균", "SD"]
    for i, h in enumerate(headers, start=1):
        ws9.cell(row=meta_start + 1, column=i, value=h)
    style_header_row(ws9, meta_start + 1, len(headers))
    sd_rows = [
        ("R1", "4.20, 4.20, 4.10, 4.05, 3.95", "4.10", "0.095"),
        ("R2", "4.30, 4.20, 4.10, 4.10, 3.95", "4.13", "0.117"),
        ("R3", "4.30, 4.30, 4.25, 4.10, 3.95", "4.18", "0.136"),
    ]
    for r, row in enumerate(sd_rows, start=meta_start + 2):
        for c, v in enumerate(row, start=1):
            ws9.cell(row=r, column=c, value=v)
        apply_body_style(ws9, r, len(headers))
        for c in (3, 4):
            ws9.cell(row=r, column=c).alignment = CENTER

    meta2_start = meta_start + 2 + len(sd_rows) + 2
    ws9.cell(row=meta2_start, column=1, value="항목").font = HEAD_FONT
    ws9.cell(row=meta2_start, column=1).fill = HEAD_FILL
    ws9.cell(row=meta2_start, column=2, value="값").font = HEAD_FONT
    ws9.cell(row=meta2_start, column=2).fill = HEAD_FILL
    meta_rows = [
        ("run_id 궤적", "20260521-A → 20260521-B → 20260521-C"),
        ("focus 궤적", "broad_scan → deferred_and_boost → quantitative_validation_and_ip_fto"),
        ("총 라운드", "3 (min_iterations=3 도달)"),
        ("누적 활성 후보", "23 (R1 14 → R2 23 → R3 23)"),
        ("누적 short-list (≥1회)", "9 (★★★ 5 + ★★ 2 + ★ 2)"),
        ("Final short-list (≥2회)", "7 (★★★ 5 + ★★ 2)"),
        ("총 signal events", "약 75 (R1 18 + R2 18 + R3 27 정량 + 7 IP/FTO + 5 RFI)"),
        ("총 web search", "약 249건 (R1 79 + R2 78 + R3 92)"),
        ("Quality-gate 발동", "0건 (R1·R2·R3 모두 미발동)"),
        ("ranking 수렴", "매우 강함 (R2→R3 short-list 멤버 100% 동일)"),
        ("confidence H 비율 (R3)", "37.0% (R2 30.4%에서 +6.6pp)"),
        ("가장 큰 점수 변동", "R2 item_006 −0.25 / R3 item_021 +0.15"),
        ("한계",
         "(1) cGMP enzyme 단가 quote-only 다수; (2) WebFetch 403 차단 4건 → secondary 출처 교차로 보완; "
         "(3) FTO opinion 변호사 검토 필요(item_002·008·021); (4) EfHyl8 정량 미확보."),
        ("입력 파일 (md)",
         "R1: reports/digest_20260521.md / R2: iterations/iter_02/digest.md + reports/digest_round_02_20260521.md / "
         "R3: iterations/iter_03/digest.md + reports/digest_round_03_20260521.md / consolidated draft: reports/consolidated_digest_20260521.md"),
        ("입력 파일 (data)",
         "data/candidates_history.csv (R1+R2+R3 60 데이터행), data/candidates_current.csv (R3 미러 23행), "
         "data/candidates.csv (R1 원본 14행), iterations/iter_02/data/candidates.csv, iterations/iter_03/data/candidates.csv"),
        ("최종 사용자 산출물",
         "reports/consolidated_digest_20260521.xlsx (10 시트), reports/consolidated_digest_20260521.docx (10 섹션 + 부록)"),
    ]
    for r, (k, v) in enumerate(meta_rows, start=meta2_start + 1):
        ws9.cell(row=r, column=1, value=k).font = Font(name="맑은 고딕", bold=True, size=10)
        ws9.cell(row=r, column=2, value=v).font = BODY_FONT
        ws9.cell(row=r, column=1).alignment = WRAP
        ws9.cell(row=r, column=2).alignment = WRAP
        ws9.cell(row=r, column=1).border = BORDER
        ws9.cell(row=r, column=2).border = BORDER
        ws9.row_dimensions[r].height = 36
    set_col_widths(ws9, [22, 110, 10, 10])

    wb.save(out_path)


# ---------------------------------------------------------------------------
# Consolidated DOCX
# ---------------------------------------------------------------------------

def build_consolidated_docx(date: str, out_path: Path):
    out_path.parent.mkdir(parents=True, exist_ok=True)
    current = read_csv_rows(ROOT / "data" / "candidates_current.csv")
    history = read_csv_rows(ROOT / "data" / "candidates_history.csv")

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

    # ----- 0. 표지·요약 -----
    add_heading(doc, "0. 표지·요약")
    add_para(doc, EXEC_SUMMARY)
    add_heading(doc, "최종 추천 Top 3 (★ 등급)", level=2)
    add_table(
        doc,
        headers=["순위", "id", "아이템", "R3 가중합", "신뢰도", "한 줄"],
        rows=[(r, cid, n, f"{s:.2f}", tier, w) for r, cid, n, s, tier, w in TOP3],
        col_widths_cm=[1.5, 1.6, 4.5, 1.6, 1.4, 6.4],
        row_bgs=["FFF2CC"] * len(TOP3),
    )
    add_heading(doc, "본 보고서 구성 (10개 섹션)", level=2)
    for line in [
        "0. 표지·요약 | 1. 선정 방법론 | 2. R1 탐색 결과 | 3. R2 탐색 결과 | 4. R3 탐색 결과",
        "5. Cumulative 후보 23개 풀 | 6. 점수 궤적 (R1→R2→R3) | 7. Final Short-list 7개 상세",
        "8. 사업화 형태별 추천 | 9. Open Questions / R4+ Triggers / 메타 | 부록. R3 short-list 1-pager 7건",
    ]:
        add_para(doc, line, size=10)

    # ----- 1. 선정 방법론 -----
    add_heading(doc, "1. 선정 방법론")
    add_para(doc, METHODOLOGY["ssot"])
    add_heading(doc, "6축 가중치 & weighted_score 산식", level=2)
    add_table(
        doc,
        headers=["축", "이름", "가중치", "정의 / 평가 기준"],
        rows=[(c, n, f"{w:.2f}", d) for c, n, w, d in METHODOLOGY["axes"]],
        col_widths_cm=[1.2, 3.2, 1.8, 10.8],
    )
    add_para(doc, METHODOLOGY["formula"], bold=True)
    add_heading(doc, "Short-list 규칙", level=2)
    add_para(doc, METHODOLOGY["shortlist_rule"])
    add_heading(doc, "Confidence H/M/L 정의", level=2)
    add_table(doc, headers=["등급", "정의"], rows=METHODOLOGY["confidence"],
              col_widths_cm=[3.0, 14.0])
    add_heading(doc, "★★★ / ★★ / ★ 등급 규칙", level=2)
    add_table(doc, headers=["등급", "정의"], rows=METHODOLOGY["tier"],
              col_widths_cm=[3.0, 14.0])
    add_heading(doc, "Business model 분류 (L / K / C / S / H)", level=2)
    add_table(doc, headers=["코드", "설명"], rows=METHODOLOGY["business_model"],
              col_widths_cm=[4.0, 13.0])

    # ----- 2. R1 -----
    add_heading(doc, "2. R1 탐색 결과 (broad_scan)")
    add_para(doc, R1_NARRATIVE["summary"])
    add_heading(doc, "R1 시장 신호 Top 5", level=2)
    add_table(
        doc,
        headers=["#", "신호", "출처", "함의"],
        rows=R1_NARRATIVE["signals_top5"],
        col_widths_cm=[0.8, 7.5, 2.8, 5.9],
    )
    add_heading(doc, "R1 후보 14개 (short-list 7개 음영)", level=2)
    sl_ids = set(R1_NARRATIVE["shortlist_ids"])
    rows = []
    bgs = []
    for cid, (defn, signal, weighted) in sorted(R1_NARRATIVE["items_brief"].items()):
        in_sl = cid in sl_ids
        rows.append((cid, defn, signal, f"{weighted:.2f}", "✓" if in_sl else ""))
        bgs.append("FFF2CC" if in_sl else None)
    add_table(
        doc,
        headers=["id", "1줄 정의", "핵심 신호", "R1", "SL"],
        rows=rows,
        col_widths_cm=[1.6, 6.2, 6.4, 1.2, 1.0],
        row_bgs=bgs,
    )

    # ----- 3. R2 -----
    add_heading(doc, "3. R2 탐색 결과 (deferred_and_boost)")
    add_para(doc, R2_NARRATIVE["summary"])
    add_heading(doc, "R2 Boost Focus (5개 영역)", level=2)
    for f in R2_NARRATIVE["boost_focus"]:
        doc.add_paragraph(f, style="List Bullet")
    add_heading(doc, "R2 시장 신호 Top 5", level=2)
    add_table(
        doc,
        headers=["#", "신호", "출처", "함의"],
        rows=R2_NARRATIVE["signals_top5"],
        col_widths_cm=[0.8, 7.5, 2.8, 5.9],
    )
    add_heading(doc, "R2 신규·부활 후보 9개", level=2)
    rows = []
    bgs = []
    for cid, (defn, signal, weighted, sl) in sorted(R2_NARRATIVE["new_revived_items"].items()):
        rows.append((cid, defn, signal, f"{weighted:.2f}", "✓" if sl else ""))
        bgs.append("FFF2CC" if sl else None)
    add_table(
        doc,
        headers=["id", "1줄 정의", "핵심 신호 (R2)", "R2", "SL"],
        rows=rows,
        col_widths_cm=[1.6, 6.2, 6.4, 1.2, 1.0],
        row_bgs=bgs,
    )
    add_heading(doc, "R1 → R2 Short-list 변동", level=2)
    add_table(
        doc,
        headers=["후보", "변동", "사유"],
        rows=R2_NARRATIVE["shortlist_in_out"],
        col_widths_cm=[5.0, 3.0, 9.0],
    )

    # ----- 4. R3 -----
    add_heading(doc, "4. R3 탐색 결과 (quantitative_validation_and_ip_fto)")
    add_para(doc, R3_NARRATIVE["summary"])
    add_heading(doc, "R3 핵심 발견 (정량 / IP / RFI)", level=2)
    for f in R3_NARRATIVE["key_findings"]:
        doc.add_paragraph(f, style="List Bullet")
    add_heading(doc, "R2 → R3 점수 변동 (raw 가중합 변동은 단 2건)", level=2)
    add_table(
        doc,
        headers=["id", "R2", "R3", "Δ", "사유"],
        rows=[(cid, f"{r2:.2f}", f"{r3:.2f}", d, why) for cid, r2, r3, d, why in R3_NARRATIVE["score_changes"]],
        col_widths_cm=[1.6, 1.4, 1.4, 1.4, 11.2],
        row_bgs=["FFF2CC"] * len(R3_NARRATIVE["score_changes"]),
    )
    add_heading(doc, "Confidence M → H 상향 (7건 / 5개 후보)", level=2)
    add_table(
        doc,
        headers=["id", "상향 축"],
        rows=R3_NARRATIVE["confidence_uplift"],
        col_widths_cm=[2.0, 15.0],
    )

    # ----- 5. Cumulative 23개 -----
    add_heading(doc, "5. Cumulative 후보 23개 풀")
    sorted_cur = sorted(current, key=lambda r: int(r["rank"]))
    score_by_id = defaultdict(dict)
    for row in history:
        try:
            it = int(row["iter"])
            sc = float(row["weighted_score"])
            score_by_id[row["id"]][it] = sc
        except (ValueError, KeyError):
            continue
    rows = []
    bgs = []
    for row in sorted_cur:
        cid = row["id"]
        s = score_by_id.get(cid, {})
        mem = SHORTLIST_MEMBERSHIP.get(cid)
        tier = ("★★★" if mem and sum(mem) == 3 else
                "★★" if mem and sum(mem) == 2 else
                "★" if mem and sum(mem) == 1 else "—")
        rows.append((
            int(row["rank"]),
            cid,
            row["item_name"][:46] + ("…" if len(row["item_name"]) > 46 else ""),
            (row.get("business_model_primary", "") +
             (f"/{row.get('business_model_secondary')}" if row.get("business_model_secondary") else "")),
            row.get("lifecycle", "").replace("_", " ")[:16],
            f"{s.get(1):.2f}" if s.get(1) is not None else "—",
            f"{s.get(2):.2f}" if s.get(2) is not None else "—",
            f"{s.get(3):.2f}" if s.get(3) is not None else "—",
            tier,
            "✓" if row.get("shortlist") == "1" else "",
        ))
        bgs.append("FFF2CC" if row.get("shortlist") == "1" else None)
    add_table(
        doc,
        headers=["rank", "id", "아이템", "biz", "lifecycle", "R1", "R2", "R3", "★", "SL"],
        rows=rows,
        col_widths_cm=[0.9, 1.4, 4.6, 1.4, 2.2, 1.0, 1.0, 1.0, 1.0, 0.8],
        row_bgs=bgs,
    )

    # ----- 6. 점수 궤적 -----
    add_heading(doc, "6. 점수 궤적 (R1→R2→R3)")
    ordering = sorted(SHORTLIST_HISTORY.keys(),
                       key=lambda i: (-(SHORTLIST_HISTORY[i].get(3, 0) or 0),
                                      -(SHORTLIST_HISTORY[i].get(1, 0) or 0)))
    rows = []
    bgs = []
    for cid in ordering:
        s = SHORTLIST_HISTORY[cid]
        mem = SHORTLIST_MEMBERSHIP.get(cid, (False, False, False))
        count = sum(mem)
        tier = "★★★" if count == 3 else "★★" if count == 2 else "★"
        r1 = s.get(1); r2 = s.get(2); r3 = s.get(3)
        base_v = r1 if r1 is not None else r2
        delta = (r3 - base_v) if (r3 is not None and base_v is not None) else None
        vals = [v for v in (r1, r2, r3) if v is not None]
        sparkline = ""
        if vals:
            lo, hi = min(vals), max(vals)
            blocks = "▁▂▃▄▅▆▇█"
            def bar(v):
                if v is None: return " "
                if hi == lo: return blocks[4]
                idx = round((v - lo) / (hi - lo) * (len(blocks) - 1))
                return blocks[idx]
            sparkline = "".join(bar(v) for v in (r1, r2, r3))
        rows.append((
            cid, SHORTLIST_NAMES.get(cid, cid),
            f"{r1:.2f}" if r1 is not None else "—",
            f"{r2:.2f}" if r2 is not None else "—",
            f"{r3:.2f}" if r3 is not None else "—",
            f"{delta:+.2f}" if delta is not None else "—",
            sparkline, count, tier,
        ))
        bgs.append("FFF2CC" if count >= 2 else None)
    add_table(
        doc,
        headers=["id", "아이템", "R1", "R2", "R3", "Δ", "sparkline", "횟수", "★"],
        rows=rows,
        col_widths_cm=[1.6, 5.8, 1.1, 1.1, 1.1, 1.1, 1.6, 1.0, 1.2],
        row_bgs=bgs,
    )
    add_para(doc, "Confidence M→H 상향 7건 / 5개 후보(item_002·005·007·008·021 — 모두 short-list)는 R3 IP/FTO focus의 직접 성과.",
             size=10, italic=True)

    # ----- 7. Final Short-list 7개 상세 -----
    add_heading(doc, "7. Final Short-list 7개 상세")
    for item in FINAL_SHORTLIST:
        add_heading(doc, f"#{item['rank']} {item['id']} — {item['name']}  [{item['biz_model']}]", level=2)
        add_para(doc, f"정의: {item['definition']}")
        add_para(doc, f"사업화: {item['biz']}")
        bar_lines = "  ".join(f"{k} {score_bar(item['score'][k])}" for k in ["M", "F", "R", "W", "IP", "T"])
        p = doc.add_paragraph()
        run = p.add_run(bar_lines + f"   →   가중합 {item['weighted']:.2f}")
        run.font.name = "Consolas"
        run.font.size = Pt(9)
        add_para(doc, f"위험·미지수: {item['risk']}", size=10)
        add_para(doc, f"다음 액션: {item['next']}", size=10)
        add_para(doc, f"선정 사유: {item['rationale']}", size=10, bold=True)

    # ----- 8. 사업화 형태별 추천 -----
    add_heading(doc, "8. 사업화 형태별 추천")
    for title, key in [("즉시 착수 (≤1년 ROI, K primary)", "immediate"),
                        ("중기 검증 (1~2년 ROI, L primary)", "mid_term"),
                        ("장기 R&D (2~5년 ROI)", "long_term")]:
        add_heading(doc, title, level=2)
        rows = [(pri, cid, name, tier, f"{sc:.2f}", bm, line)
                for pri, cid, name, tier, sc, bm, line in RECOMMENDATIONS[key]]
        add_table(
            doc,
            headers=["우선", "id", "아이템", "등급", "R3", "biz", "한 줄"],
            rows=rows,
            col_widths_cm=[1.0, 1.6, 4.5, 1.5, 1.0, 1.0, 6.4],
            row_bgs=["FFF2CC"] * len(rows),
        )

    # ----- 9. Open Questions / R4+ / 메타 -----
    add_heading(doc, "9. Open Questions / R4+ Triggers / 메타")
    add_heading(doc, "Open Questions (R3 미해결)", level=2)
    for q in OPEN_QUESTIONS:
        doc.add_paragraph(q, style="List Bullet")
    add_heading(doc, "Quality-gate / R4 자동 발동 트리거", level=2)
    for t in R4_TRIGGERS:
        doc.add_paragraph(t, style="List Bullet")
    add_heading(doc, "3-Round 통계 (Top-5 SD 궤적)", level=2)
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
    add_heading(doc, "메타 (run_id / 입력 / 한계)", level=2)
    add_table(
        doc,
        headers=["항목", "값"],
        rows=[
            ("run_id 궤적", "20260521-A → 20260521-B → 20260521-C"),
            ("focus 궤적", "broad_scan → deferred_and_boost → quantitative_validation_and_ip_fto"),
            ("총 라운드", "3 (min_iterations=3 도달)"),
            ("누적 활성 후보", "23 (R1 14 → R2 23 → R3 23)"),
            ("Final short-list (≥2회)", "7 (★★★ 5 + ★★ 2)"),
            ("총 web search", "약 249건 (R1 79 + R2 78 + R3 92)"),
            ("Quality-gate 발동", "0건"),
            ("ranking 수렴", "매우 강함 (R2→R3 short-list 100% 동일)"),
            ("confidence H 비율 (R3)", "37.0% (R2 30.4%에서 +6.6pp)"),
            ("한계",
             "(1) cGMP enzyme 단가 quote-only 다수; (2) WebFetch 403 차단 4건; "
             "(3) FTO opinion 변호사 검토 필요(item_002·008·021); (4) EfHyl8 정량 미확보."),
            ("입력 파일 (md)",
             "R1 reports/digest_20260521.md / R2 iterations/iter_02/digest.md / R3 iterations/iter_03/digest.md / consolidated draft reports/consolidated_digest_20260521.md"),
            ("입력 파일 (data)",
             "data/candidates_history.csv, data/candidates_current.csv, data/candidates.csv, iterations/iter_{02,03}/data/candidates.csv"),
            ("최종 사용자 산출물",
             "reports/consolidated_digest_20260521.xlsx + .docx (총 2개 파일)"),
        ],
        col_widths_cm=[4.0, 13.0],
    )

    # ----- 부록: R3 short-list 1-pager 7건 -----
    doc.add_page_break()
    add_heading(doc, "부록. R3 Short-list 1-pager 7건 (전문 inline)", level=0)
    add_para(doc,
             "각 후보의 1-pager(markdown 카드)를 본문에 그대로 통합. 출처는 `candidates/item_*.md` 또는 `iterations/iter_02/candidates/item_*.md`.",
             size=9.5, italic=True)
    for cid in ["item_002", "item_008", "item_021", "item_007", "item_003", "item_005", "item_017"]:
        add_heading(doc, f"{cid}", level=1)
        path = R3_CARD_PATHS.get(cid)
        text = load_card_text(path) if path else "[경로 미지정]"
        # render line-by-line, treating headings shallow but keeping content readable
        for line in text.splitlines():
            stripped = line.rstrip()
            if not stripped:
                doc.add_paragraph()
                continue
            if stripped.startswith("# "):
                add_heading(doc, stripped[2:], level=1)
            elif stripped.startswith("## "):
                add_heading(doc, stripped[3:], level=2)
            elif stripped.startswith("### "):
                add_heading(doc, stripped[4:], level=3)
            elif stripped.startswith("- "):
                doc.add_paragraph(stripped[2:], style="List Bullet")
            else:
                add_para(doc, stripped, size=10)

    doc.save(out_path)


# ---------------------------------------------------------------------------
# Dispatch
# ---------------------------------------------------------------------------

def run_consolidated(date: str):
    out_xlsx = ROOT / "reports" / f"consolidated_digest_{date}.xlsx"
    out_docx = ROOT / "reports" / f"consolidated_digest_{date}.docx"
    build_consolidated_xlsx(date, out_xlsx)
    build_consolidated_docx(date, out_docx)
    print(f"Wrote {out_xlsx}")
    print(f"Wrote {out_docx}")


def infer_default_date() -> str:
    pat = re.compile(r"consolidated_digest_(\d{8})\.md$")
    candidates = []
    for p in (ROOT / "reports").glob("consolidated_digest_*.md"):
        m = pat.search(p.name)
        if m:
            candidates.append(m.group(1))
    if candidates:
        return sorted(candidates)[-1]
    return "20260521"


def main():
    parser = argparse.ArgumentParser(
        description="Export the final consolidated Phase D digest to xlsx + docx (the only user-facing deliverable).")
    parser.add_argument("--mode", default="consolidated",
                        choices=["consolidated", "round"],
                        help="Only 'consolidated' is supported. 'round' is deprecated.")
    parser.add_argument("--iter", type=int, default=None,
                        help="(deprecated, ignored)")
    parser.add_argument("--date", default=None,
                        help="YYYYMMDD; inferred from latest reports/consolidated_digest_*.md when omitted.")
    args = parser.parse_args()

    if args.mode == "round":
        print(
            "ERROR: --mode round is deprecated and no longer produces xlsx/docx.\n"
            "       Per-round digests are markdown-only working artifacts.\n"
            "       The only user-facing deliverable is the consolidated digest:\n"
            "         python scripts/export_report.py --mode consolidated --date YYYYMMDD",
            file=sys.stderr,
        )
        sys.exit(2)

    date = args.date or infer_default_date()
    run_consolidated(date)


if __name__ == "__main__":
    main()
