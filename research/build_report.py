"""
Build the final Word (.docx) report for EndoS2 Glycosynthase Mutant Deep Dive.

Reads 8 markdown research files + verification log, generates a professional
report with cover page, TOC, executive summary, full body sections,
and appendix.
"""

import re
import os
from datetime import datetime
from docx import Document
from docx.shared import Pt, Cm, RGBColor, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK
from docx.enum.table import WD_ALIGN_VERTICAL, WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn, nsmap
from docx.oxml import OxmlElement


RESEARCH_DIR = "/home/user/New-protein_peptide-item/research"
OUTPUT_PATH = os.path.join(RESEARCH_DIR, "FINAL_REPORT.docx")

ITEM_NAME = "EndoS2 Glycosynthase Mutant (Fc Glycan Remodeling)"
REPORT_DATE = "2026-05-21"
PURPOSE = "사업기획 / 신규 진입 검토"
SCOPE = "글로벌 (전 세계)"
COMPANY_CAP = "(미지정 — 일반화된 중견 biotech/CDMO/reagent player 가정)"

SECTION_FILES = [
    ("A", "기술 분석", "A_technology.md", "✅ 검증완료"),
    ("B", "시장 분석", "B_market.md", "⚠️ 부분검증"),
    ("C", "주요 Player 분석", "C_players.md", "✅ 검증완료"),
    ("D", "고객 분석", "D_customers.md", "✅ 검증완료"),
    ("E", "특허/IP 분석", "E_patents.md", "✅ 검증완료"),
    ("F", "리스크 및 규제 분석", "F_risk_regulatory.md", "✅ 검증완료"),
    ("G", "사업성 및 전략 시사점", "G_business.md", "✅ 검증완료"),
    ("H", "진입장벽 & White Space 분석 (Core Synthesis)", "H_entry_whitespace.md", "⚠️ 부분검증 (논리 OK)"),
]


# --- Markdown parsing helpers --------------------------------------------------

INLINE_BOLD = re.compile(r"\*\*(.+?)\*\*")
INLINE_ITALIC = re.compile(r"(?<!\*)\*([^*]+)\*(?!\*)")
INLINE_CODE = re.compile(r"`([^`]+)`")


def add_inline_runs(paragraph, text):
    """Add text to paragraph, handling **bold**, *italic*, `code`."""
    # Simple tokenizer: split on bold first, then italic/code per chunk.
    pos = 0
    pattern = re.compile(r"\*\*(.+?)\*\*|`([^`]+)`")
    for m in pattern.finditer(text):
        if m.start() > pos:
            _add_plain(paragraph, text[pos:m.start()])
        if m.group(1) is not None:
            run = paragraph.add_run(m.group(1))
            run.bold = True
        elif m.group(2) is not None:
            run = paragraph.add_run(m.group(2))
            run.font.name = "Consolas"
            run.font.size = Pt(9)
        pos = m.end()
    if pos < len(text):
        _add_plain(paragraph, text[pos:])


def _add_plain(paragraph, text):
    if text:
        paragraph.add_run(text)


def parse_table(lines, start_idx):
    """Parse a Markdown table starting at start_idx. Returns (rows, next_idx)."""
    rows = []
    i = start_idx
    while i < len(lines) and lines[i].strip().startswith("|"):
        line = lines[i].strip()
        # Skip separator row like |---|---|
        if re.match(r"^\|?\s*[-:|\s]+\|[-:|\s]+", line) and "---" in line:
            i += 1
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        rows.append(cells)
        i += 1
    return rows, i


def add_table_to_doc(doc, rows):
    if not rows:
        return
    n_cols = max(len(r) for r in rows)
    # Normalize row widths
    rows = [r + [""] * (n_cols - len(r)) for r in rows]
    table = doc.add_table(rows=len(rows), cols=n_cols)
    table.style = "Light Grid Accent 1"
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    for i, row in enumerate(rows):
        for j, cell_text in enumerate(row):
            cell = table.cell(i, j)
            cell.text = ""
            p = cell.paragraphs[0]
            add_inline_runs(p, cell_text)
            for run in p.runs:
                run.font.size = Pt(9)
                if i == 0:
                    run.bold = True
            cell.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
    # Small spacing after table
    doc.add_paragraph()


def render_markdown_to_doc(doc, md_text, base_heading_level=2):
    """
    Render a markdown subsection into the doc.
    base_heading_level=2 means top-level `#` becomes Heading 2 etc.
    Skips the very first H1 (which is the section title) since we add our own.
    """
    lines = md_text.split("\n")
    i = 0
    skipped_first_h1 = False
    while i < len(lines):
        line = lines[i].rstrip()
        # Tables
        if line.startswith("|") and i + 1 < len(lines) and "---" in lines[i+1]:
            rows, i = parse_table(lines, i)
            add_table_to_doc(doc, rows)
            continue
        # Headings
        h_match = re.match(r"^(#{1,6})\s+(.*)$", line)
        if h_match:
            level = len(h_match.group(1))
            heading_text = h_match.group(2).strip()
            if level == 1 and not skipped_first_h1:
                skipped_first_h1 = True
                i += 1
                continue
            actual_level = min(max(base_heading_level + level - 2, 1), 9)
            p = doc.add_heading(level=actual_level)
            add_inline_runs(p, heading_text)
            i += 1
            continue
        # Blockquote / metadata
        if line.startswith(">"):
            p = doc.add_paragraph(style="Intense Quote")
            add_inline_runs(p, line.lstrip("> ").strip())
            i += 1
            continue
        # Horizontal rule
        if line.strip() in ("---", "***"):
            doc.add_paragraph()
            i += 1
            continue
        # Bullet list
        m = re.match(r"^(\s*)[-*]\s+(.*)$", line)
        if m:
            indent_spaces = len(m.group(1))
            text = m.group(2)
            level = min(indent_spaces // 2, 4)
            style = "List Bullet" if level == 0 else f"List Bullet {min(level+1,3)}"
            try:
                p = doc.add_paragraph(style=style)
            except KeyError:
                p = doc.add_paragraph(style="List Bullet")
            add_inline_runs(p, text)
            i += 1
            continue
        # Numbered list
        m = re.match(r"^(\s*)\d+\.\s+(.*)$", line)
        if m:
            text = m.group(2)
            try:
                p = doc.add_paragraph(style="List Number")
            except KeyError:
                p = doc.add_paragraph()
            add_inline_runs(p, text)
            i += 1
            continue
        # Blank line
        if not line.strip():
            i += 1
            continue
        # Regular paragraph (collect consecutive non-empty lines that aren't markers)
        para_lines = [line]
        j = i + 1
        while j < len(lines):
            nxt = lines[j].rstrip()
            if (not nxt.strip()
                or nxt.startswith("|")
                or re.match(r"^#{1,6}\s", nxt)
                or re.match(r"^\s*[-*]\s", nxt)
                or re.match(r"^\s*\d+\.\s", nxt)
                or nxt.startswith(">")
                or nxt.strip() in ("---", "***")):
                break
            para_lines.append(nxt)
            j += 1
        p = doc.add_paragraph()
        add_inline_runs(p, " ".join(para_lines))
        i = j


# --- TOC helper ---------------------------------------------------------------

def add_table_of_contents(doc):
    """Insert a Word TOC field. User must press F9 in Word to populate."""
    paragraph = doc.add_paragraph()
    run = paragraph.add_run()
    fldChar1 = OxmlElement("w:fldChar")
    fldChar1.set(qn("w:fldCharType"), "begin")

    instrText = OxmlElement("w:instrText")
    instrText.set(qn("xml:space"), "preserve")
    instrText.text = 'TOC \\o "1-3" \\h \\z \\u'

    fldChar2 = OxmlElement("w:fldChar")
    fldChar2.set(qn("w:fldCharType"), "separate")

    fldChar3 = OxmlElement("w:t")
    fldChar3.text = "목차를 업데이트하려면 Word에서 F9를 누르세요."

    fldChar4 = OxmlElement("w:fldChar")
    fldChar4.set(qn("w:fldCharType"), "end")

    run._r.append(fldChar1)
    run._r.append(instrText)
    run._r.append(fldChar2)
    r2 = paragraph.add_run()
    r2._r.append(fldChar3)
    r3 = paragraph.add_run()
    r3._r.append(fldChar4)


# --- Document setup -----------------------------------------------------------

def set_styles(doc):
    styles = doc.styles
    normal = styles["Normal"]
    normal.font.name = "맑은 고딕"
    normal._element.rPr.rFonts.set(qn("w:eastAsia"), "맑은 고딕")
    normal.font.size = Pt(10)

    for hname, size in [("Heading 1", 18), ("Heading 2", 14), ("Heading 3", 12), ("Heading 4", 11)]:
        try:
            s = styles[hname]
            s.font.name = "맑은 고딕"
            s._element.rPr.rFonts.set(qn("w:eastAsia"), "맑은 고딕")
            s.font.size = Pt(size)
            s.font.color.rgb = RGBColor(0x1F, 0x3A, 0x6E)
            s.font.bold = True
        except KeyError:
            pass


def add_page_number(doc):
    section = doc.sections[0]
    footer = section.footer
    p = footer.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run()
    fldChar1 = OxmlElement("w:fldChar")
    fldChar1.set(qn("w:fldCharType"), "begin")
    instrText = OxmlElement("w:instrText")
    instrText.set(qn("xml:space"), "preserve")
    instrText.text = "PAGE"
    fldChar2 = OxmlElement("w:fldChar")
    fldChar2.set(qn("w:fldCharType"), "end")
    run._r.append(fldChar1)
    run._r.append(instrText)
    run._r.append(fldChar2)


def cover_page(doc):
    section = doc.sections[0]
    section.top_margin = Cm(2.5)
    section.bottom_margin = Cm(2.5)
    section.left_margin = Cm(2.5)
    section.right_margin = Cm(2.5)

    # Spacer
    for _ in range(4):
        doc.add_paragraph()

    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run("신규 아이템 Deep Dive 조사 보고서")
    run.font.size = Pt(20)
    run.font.bold = True
    run.font.color.rgb = RGBColor(0x1F, 0x3A, 0x6E)

    doc.add_paragraph()
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run(ITEM_NAME)
    run.font.size = Pt(16)
    run.font.bold = True

    doc.add_paragraph()
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run("— IgG Fc N-Glycan 부위특이적 리모델링 효소 플랫폼 종합 분석 —")
    run.font.size = Pt(11)
    run.italic = True

    for _ in range(6):
        doc.add_paragraph()

    # Metadata table on cover
    table = doc.add_table(rows=4, cols=2)
    table.style = "Light List Accent 1"
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    meta = [
        ("조사 일자", REPORT_DATE),
        ("조사 목적", PURPOSE),
        ("조사 범위", SCOPE),
        ("자사 역량 가정", COMPANY_CAP),
    ]
    for i, (k, v) in enumerate(meta):
        c1 = table.cell(i, 0)
        c2 = table.cell(i, 1)
        c1.text = k
        c2.text = v
        for cell in (c1, c2):
            for run in cell.paragraphs[0].runs:
                run.font.size = Pt(11)
        for run in c1.paragraphs[0].runs:
            run.bold = True

    for _ in range(5):
        doc.add_paragraph()

    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run("Orchestrated by Multi-Agent Research Workflow")
    run.font.size = Pt(9)
    run.italic = True
    run.font.color.rgb = RGBColor(0x80, 0x80, 0x80)

    doc.add_page_break()


def executive_summary(doc):
    doc.add_heading("Executive Summary", level=1)

    p = doc.add_paragraph()
    add_inline_runs(p, (
        "본 보고서는 신규 아이템 **EndoS2 Glycosynthase Mutant (Fc Glycan Remodeling)** 에 대한 "
        "기술·시장·Player·고객·특허·규제·사업성·진입장벽 8개 영역의 종합 Deep Dive 분석 결과이다. "
        "조사 일자 2026-05-21 기준으로 [A]~[G] 7개 리서치 에이전트와 [H] 종합 분석 에이전트, "
        "독립 검증 에이전트가 순차적·병렬적으로 작업하였으며, 8개 섹션 중 6개 ✅ 검증완료, "
        "2개 ⚠️ 부분검증, 0개 ❌ 검증실패로 **전체 신뢰도 '고신뢰'** 등급이다."
    ))

    doc.add_heading("핵심 결론", level=2)

    bullets = [
        ("**기술 성숙도**: EndoS2 glycosynthase mutant(D184M/D184Q)는 Wang lab(2016, *JBC*) 보고된 "
         "검증된 화학효소 기반 site-specific 항체 Fc 리모델링 기술로 TRL 7-8 수준이며, "
         "ADC 임상(Phase 1-3) 자산 다수에 적용 중이다."),
        ("**시장 규모**: ADC 치료제 시장 USD 13.5B@2025 → 32-57B@2035, "
         "ADC linker·conjugation 기술 USD 1.25B@2025 → 4.4B@2035, "
         "그중 chemoenzymatic sub-segment CAGR 12.5%+ (Roots Analysis, ⚠️ 단일 출처). "
         "현재는 도입기 후반 ~ 성장기 진입 (transition) 단계."),
        ("**경쟁 구도**: Synaffix(Lonza 2023 인수, €160M, 누적 deal $10B+ biobucks, 8개 임상)이 platform 시장 압도. "
         "Genovis AB가 reagent enzyme 시장 ~70% [추정] 점유. UMd Wang lab의 WO2017/124084·US 11,008,601 (D184M/Q claim, "
         "만료 ~2037)이 사실상 원천 IP."),
        ("**진입장벽 종합 등급: 상(高)**. 7개 차원 중 특허·표준/인증·공급망이 모두 '상', 기술·인력·자본·시간이 '중'. "
         "FTO 위험 4.0/5.0 — UMd/GlycoT in-license가 사실상 유일 합리 진입 경로."),
        ("**Top White Space — Asia-Centric 통합 platform**: 한국 송도 ADC 클러스터·LigaChem·중국 Innovent·인도 CDMO와 "
         "결합한 Asia 본거지 EndoS2 enzyme + 비독점 라이선스 패키지. APAC ADC CAGR 29.22%(Mordor)·BIOSECURE Act·"
         "EU Biotech Act 3중 모멘텀."),
        ("**권장 진입 지점**: (1) **Asia-centric GMP EndoS2 enzyme + 비독점 라이선스 hybrid (적극 권장)** — "
         "5년 누적 USD 40-70M 투자, Year 5+ ARR USD 15-30M 목표. "
         "(2) **GMP donor specialist (조건부 권장)** — carbohydrate chemistry talent 보유 시. "
         "(3) **Full-stack CDMO/단독 platform licensor/자체 ADC 신약 — 비권장**."),
        ("**핵심 리스크**: ① BIOSECURE Act bifurcated supply 부담, ② 잔류 EndoS2 면역원성(인간 사전 항체 존재), "
         "③ ICH Q5E 바이오시밀러 동등성 평가 불확실성, ④ 2026.05 기준 FDA 승인 chemoenzymatic ADC 0건."),
    ]
    for b in bullets:
        p = doc.add_paragraph(style="List Bullet")
        add_inline_runs(p, b)

    doc.add_heading("최종 권고 한 줄", level=2)
    p = doc.add_paragraph()
    add_inline_runs(p, (
        "**Asia-centric GMP EndoS2 enzyme + 비독점 라이선스 hybrid 모델이 risk-adjusted 최우선 진입 지점**이며, "
        "carbohydrate chemistry talent 보유 시 GMP donor specialist가 second 옵션. "
        "그 외 진입 모드는 IP/CAPEX 부담 대비 ROI 정당화 어렵다."
    ))

    doc.add_page_break()


def section_intro(doc, code, title, grade):
    h = doc.add_heading(f"[{code}] {title}", level=1)
    p = doc.add_paragraph()
    run = p.add_run(f"검증 등급: {grade}")
    run.bold = True
    run.font.size = Pt(11)
    run.font.color.rgb = RGBColor(0x2E, 0x7D, 0x32) if "✅" in grade else RGBColor(0xE6, 0x7E, 0x22)


def appendix_sources_and_verification(doc):
    doc.add_page_break()
    doc.add_heading("부록 A. 출처 목록 (Sources)", level=1)
    p = doc.add_paragraph()
    add_inline_runs(p, (
        "각 섹션 본문 내에서 (Source: URL, 발행일) 형식으로 인용된 모든 출처는 "
        "원본 마크다운 산출물(`research/A_technology.md` 외 7개)에 포함되어 있다. "
        "주요 1차 출처군은 다음과 같다:"
    ))
    primary_sources = [
        "**학술/특허**: Lai-Xi Wang Lab (Univ. of Maryland) — *JBC* 2016, *JACS* 시리즈; WO2017/124084 / US 11,008,601 (Google Patents, USPTO)",
        "**기업 IR/보도자료**: Lonza, Synaffix, Genovis AB, Hansa Biopharma, ADC Therapeutics, Mersana, Sidewinder Therapeutics, Daiichi Sankyo, Amgen, Boehringer Ingelheim",
        "**시장조사**: Roots Analysis, Mordor Intelligence, Grand View Research, Towards Healthcare, Precedence Research, InsightAce",
        "**규제 가이던스**: ICH Q6B/Q5E/M7, USP <1132>, FDA BLA database, BIOSECURE Act (FY2026 NDAA Section 851), EU Biotech Act 제안서 (2025-12-16)",
        "**법률/IP 분석**: Goodwin Law, Sidley Austin, Arnold & Porter, IPKat, CAFC Opinions (Seagen v. Daiichi Sankyo 2025-12-02)",
    ]
    for s in primary_sources:
        p = doc.add_paragraph(style="List Bullet")
        add_inline_runs(p, s)

    doc.add_heading("부록 B. 검증 로그 요약 (Verification Log)", level=1)

    p = doc.add_paragraph()
    add_inline_runs(p, (
        "독립 검증 에이전트가 각 섹션의 핵심 사실 주장 3-5건을 새로운 WebSearch 쿼리로 교차 확인한 결과이다. "
        "상세 로그는 `research/VERIFICATION.md` 참조."
    ))

    rows = [
        ["섹션", "검증 등급", "검증 요지"],
        ["[A] 기술", "✅ 검증완료", "D184M 특성, US11008601B2 청구항, WO2017/124084 우선일 2016-01-15 — ResearchGate·Google Patents·USPTO 독립 확인"],
        ["[B] 시장", "⚠️ 부분검증", "ADC 시장 규모 USD 13.5B@2025 / 32.66B@2035 다수 출처 일치. CAGR은 4.8-28.88% 광범위 분산. Chemoenzymatic 12.5% CAGR은 Roots Analysis 단일 출처."],
        ["[C] Player", "✅ 검증완료", "Lonza-Synaffix €160M, Amgen $2B, BI $1.3B, Genmab $1.8B, Genovis 2026-03 라이선스 $20M/program — 다수 독립 확인"],
        ["[D] 고객", "✅ 검증완료", "ADCT-601 / XMT-1660(ORR 22-31%) / Sidewinder bispecific(2026-01) / 0 FDA 승인 chemoenzymatic ADC — 모두 일치"],
        ["[E] 특허/IP", "✅ 검증완료", "US11008601B2·WO2017124084 우선일/청구, GlycoT-Daiichi 2020-09 sublicense, Seagen v Daiichi CAFC 2025-12-02 무효 — 1차 문서 확인"],
        ["[F] 리스크/규제", "✅ 검증완료", "BIOSECURE 2025-12-18 서명·WuXi 제외·1260H, EU Biotech Act 2025-12-16, Hansa PDUFA 2026-12-19 — 모두 정확"],
        ["[G] 사업성", "✅ 검증완료", "Taiho-Araris $1.14B(2025-03), Genovis SEK 128.9M, Lonza-Synaffix €160M, Sidewinder Series B $137M(2026-04) — 모두 일치"],
        ["[H] 진입장벽", "⚠️ 부분검증 (논리 OK)", "인용 facts 6/7 검증완료. WS-2 > WS-1 우선순위 추론에 명시적 비약 없음. 'Chemoenzymatic SAM $150-250M@2025'는 [B] 추정 상속."],
    ]
    add_table_to_doc(doc, rows)

    doc.add_heading("부록 C. 사용 시 유의사항", level=1)
    cautions = [
        "**시점 민감성**: 6개월 단위 재평가 권장. 특히 BIOSECURE 1260H 리스트 업데이트(WuXi 추가 가능성), Hansa imlifidase PDUFA(2026-12-19) 결과에 따른 EndoS-family 면역원성 데이터 후속 갱신 필요.",
        "**시장 CAGR 광범위 분산**: ADC 시장 4.8-28.88%. 의사결정 시 낮은/중간/높은 CAGR 시나리오 모두 분석 권장.",
        "**임상 데이터 미성숙**: 2026-05 기준 chemoenzymatic ADC FDA 승인 0건. 첫 승인(2027-2028 예상) 결과에 따라 시장 매력도 ±30% 변동 가능.",
        "**자사 capability에 따른 진입 모드 조정**: 본 보고서 [G][H]는 일반화된 player 가정. 실제 자사 carbohydrate chemistry 인력, GMP 시설, 지역 footprint에 따라 진입 우선순위 재평가 필수.",
        "**IP 회피 옵션의 시간차**: WO2017/124084 만료 ~2037, WO2013/120066 만료 ~2032-2033. 2030년대 중반까지는 in-license가 사실상 유일 경로.",
    ]
    for c in cautions:
        p = doc.add_paragraph(style="List Bullet")
        add_inline_runs(p, c)


# --- Main ---------------------------------------------------------------------

def main():
    doc = Document()
    set_styles(doc)

    cover_page(doc)

    # TOC
    doc.add_heading("목차 (Table of Contents)", level=1)
    add_table_of_contents(doc)
    p = doc.add_paragraph()
    run = p.add_run("※ MS Word에서 목차를 마우스 오른쪽 → '필드 업데이트' 또는 F9 키로 자동 생성하세요.")
    run.italic = True
    run.font.size = Pt(9)
    run.font.color.rgb = RGBColor(0x80, 0x80, 0x80)
    doc.add_page_break()

    executive_summary(doc)

    # Body sections
    for code, title, fname, grade in SECTION_FILES:
        section_intro(doc, code, title, grade)
        path = os.path.join(RESEARCH_DIR, fname)
        with open(path, "r", encoding="utf-8") as f:
            md = f.read()
        render_markdown_to_doc(doc, md, base_heading_level=2)
        doc.add_page_break()

    # Appendix
    appendix_sources_and_verification(doc)

    add_page_number(doc)

    doc.save(OUTPUT_PATH)
    size_kb = os.path.getsize(OUTPUT_PATH) / 1024
    print(f"✅ Word report saved: {OUTPUT_PATH} ({size_kb:.1f} KB)")


if __name__ == "__main__":
    main()
