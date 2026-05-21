"""
Build the final Word (.docx) report for Peptiligase / OaAEP1 Deep Dive.

Includes embedded PNG figures (matplotlib + Pillow) at points where figure
explanation is judged advantageous (per CLAUDE.md rule R1).

Figures generated:
  fig1_market_projection.png   - Market size projection (TAM/SAM)
  fig2_barrier_radar.png       - Entry barrier radar (Peptiligase vs OaAEP1)
  fig3_whitespace_2x2.png      - White Space 2x2 (barrier x opportunity)
  fig4_tech_compare_radar.png  - Competing technologies radar
  fig5_patent_timeline.png     - Patent expiry timeline (Gantt)
  fig6_pmi_compare.png         - PMI comparison (SPPS vs enzymatic)
  fig7_valuechain.png          - Value chain diagram (Pillow)
"""

import os
import re
from docx import Document
from docx.shared import Pt, Cm, RGBColor, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_ALIGN_VERTICAL, WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib import font_manager
import numpy as np
from PIL import Image, ImageDraw, ImageFont


# --- Paths --------------------------------------------------------------------

BASE = "/home/user/New-protein_peptide-item/research/peptiligase_oaaep1"
FIG_DIR = os.path.join(BASE, "figures")
os.makedirs(FIG_DIR, exist_ok=True)
OUTPUT_PATH = os.path.join(BASE, "FINAL_REPORT.docx")

ITEM_NAME = "Peptiligase / OaAEP1 (Enzymatic Peptide Ligation)"
REPORT_DATE = "2026-05-21"
PURPOSE = "사업기획 / 신규 진입 검토"
SCOPE = "글로벌 (전 세계)"
COMPANY_CAP = "(미지정 — platform IP 없는 중견 biotech/CDMO/reagent player 가정)"

SECTION_FILES = [
    ("A", "기술 분석", "A_technology.md", "✅ 검증완료"),
    ("B", "시장 분석", "B_market.md", "⚠️ 부분검증"),
    ("C", "주요 Player 분석", "C_players.md", "✅ 검증완료"),
    ("D", "고객 분석", "D_customers.md", "✅ 검증완료"),
    ("E", "특허/IP 분석", "E_patents.md", "✅ 검증완료"),
    ("F", "리스크 및 규제 분석", "F_risk_regulatory.md", "✅ 검증완료"),
    ("G", "사업성 및 전략 시사점", "G_business.md", "⚠️ 부분검증"),
    ("H", "진입장벽 & White Space 분석 (Core Synthesis)", "H_entry_whitespace.md", "✅ 검증완료"),
]

# Korean font setup for matplotlib
plt.rcParams["font.family"] = "NanumGothic"
plt.rcParams["axes.unicode_minus"] = False
plt.rcParams["font.size"] = 10


# ==============================================================================
# Figure generation
# ==============================================================================

NAVY = "#1F3A6E"
ORANGE = "#E67E22"
TEAL = "#16A085"
RED = "#C0392B"
GRAY = "#7F8C8D"
LIGHT_BLUE = "#5DADE2"


def fig1_market_projection():
    """Stacked & line chart: TAM(therapeutic peptide), SAM(GLP-1), CDMO market."""
    fig, ax = plt.subplots(figsize=(8, 4.5), dpi=130)
    years = [2025, 2026, 2028, 2030, 2032, 2035]
    # Source: Precedence/Coherent/Mordor synthesis + Grand View GLP-1 + IMARC CDMO
    tam_peptide = [48, 53, 64, 71, 78, 87]      # USD B, therapeutic peptide TAM
    glp1 = [50, 66, 100, 140, 175, 200]          # USD B, GLP-1 RA SAM (corrected)
    cdmo = [2.65, 2.98, 3.6, 4.2, 4.6, 5.0]      # USD B, peptide CDMO
    enz_som = [0.10, 0.13, 0.18, 0.25, 0.32, 0.45]  # USD B, enzymatic SOM [추정]

    ax.plot(years, glp1, marker="o", color=ORANGE, linewidth=2.5, label="GLP-1 RA (SAM)")
    ax.plot(years, tam_peptide, marker="s", color=NAVY, linewidth=2.0, label="치료용 펩타이드 (TAM)")
    ax.plot(years, cdmo, marker="^", color=TEAL, linewidth=2.0, label="펩타이드 CDMO")
    ax.plot(years, enz_som, marker="d", color=RED, linewidth=2.0, label="효소 합성 sub-segment (SOM, [추정])")

    ax.set_xlabel("연도")
    ax.set_ylabel("시장 규모 (USD B)")
    ax.set_title("그림 1. 시장 규모 전망: TAM / SAM / SOM (2025-2035)", fontsize=11, fontweight="bold")
    ax.legend(loc="upper left", fontsize=9, framealpha=0.95)
    ax.grid(True, alpha=0.3, linestyle="--")
    ax.set_yscale("log")
    ax.set_ylim(0.05, 300)
    ax.set_xticks(years)
    plt.tight_layout()
    path = os.path.join(FIG_DIR, "fig1_market_projection.png")
    plt.savefig(path, dpi=130, bbox_inches="tight")
    plt.close()
    return path


def fig2_barrier_radar():
    """Radar chart: 7-axis entry barriers, Peptiligase vs OaAEP1."""
    axes_labels = ["기술 난이도", "특허 장벽", "표준/규제", "공급망", "인력/장비", "자본 요건", "시간 요건"]
    # Scale 1-5 (5 = highest barrier)
    peptiligase = [3, 5, 4, 4, 3, 4, 4]
    oaaep1 = [3, 4, 4, 3, 3, 3, 4]

    angles = np.linspace(0, 2*np.pi, len(axes_labels), endpoint=False).tolist()
    angles += angles[:1]
    peptiligase += peptiligase[:1]
    oaaep1 += oaaep1[:1]

    fig, ax = plt.subplots(figsize=(7, 6), subplot_kw=dict(polar=True), dpi=130)
    ax.plot(angles, peptiligase, color=NAVY, linewidth=2, label="Peptiligase (가중평균 4.0/5)")
    ax.fill(angles, peptiligase, color=NAVY, alpha=0.18)
    ax.plot(angles, oaaep1, color=ORANGE, linewidth=2, label="OaAEP1 (가중평균 3.7/5)")
    ax.fill(angles, oaaep1, color=ORANGE, alpha=0.18)
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(axes_labels, fontsize=10)
    ax.set_ylim(0, 5)
    ax.set_yticks([1, 2, 3, 4, 5])
    ax.set_yticklabels(["1\n낮음", "2", "3\n중", "4", "5\n높음"], fontsize=8)
    ax.set_title("그림 2. 진입장벽 7개 차원 평가 (Peptiligase vs OaAEP1)", fontsize=11, fontweight="bold", pad=20)
    ax.legend(loc="upper right", bbox_to_anchor=(1.3, 1.05), fontsize=9)
    ax.grid(True, alpha=0.4)
    plt.tight_layout()
    path = os.path.join(FIG_DIR, "fig2_barrier_radar.png")
    plt.savefig(path, dpi=130, bbox_inches="tight")
    plt.close()
    return path


def fig3_whitespace_2x2():
    """2x2 matrix: White Space candidates plotted by (barrier, opportunity)."""
    fig, ax = plt.subplots(figsize=(8.5, 6.5), dpi=130)
    # x = entry barrier (1-5, low to high), y = market opportunity (1-5, low to high)
    # bubble size = priority weight
    ws = [
        ("WS-1\nCα-ester GMP\nBuilding Block",     2.5, 3.8, 750, TEAL),
        ("WS-2\nOaAEP1 ADC/PDC\nReagent + CRO",    3.2, 4.0, 700, NAVY),
        ("WS-3\nGLP-1 Biosimilar\nEnzymatic CDMO", 4.3, 4.5, 850, ORANGE),
        ("WS-4\nMacrocyclic\nPeptide CDMO",        3.5, 3.5, 500, LIGHT_BLUE),
        ("WS-5\nML 신규 Ligase\n(Profluent 협업)",  4.5, 3.0, 400, GRAY),
    ]
    for label, x, y, s, c in ws:
        ax.scatter(x, y, s=s, color=c, alpha=0.65, edgecolors="black", linewidth=1.2, zorder=3)
        ax.annotate(label, (x, y), fontsize=9, ha="center", va="center", fontweight="bold", zorder=4)

    # Quadrant lines
    ax.axhline(3, color="black", linewidth=0.8, alpha=0.5)
    ax.axvline(3, color="black", linewidth=0.8, alpha=0.5)

    # Quadrant labels
    ax.text(1.5, 4.7, "Q1: 기회 크고 장벽 낮음\n(우선 진입)", fontsize=9,
            ha="center", color="green", fontweight="bold",
            bbox=dict(boxstyle="round,pad=0.3", fc="lightgreen", alpha=0.3))
    ax.text(4.5, 4.7, "Q2: 기회 크고 장벽 높음\n(전략적 진입)", fontsize=9,
            ha="center", color="darkblue", fontweight="bold",
            bbox=dict(boxstyle="round,pad=0.3", fc="lightblue", alpha=0.3))
    ax.text(1.5, 1.3, "Q3: 기회 작고 장벽 낮음\n(보조 진입)", fontsize=9,
            ha="center", color="darkorange", fontweight="bold",
            bbox=dict(boxstyle="round,pad=0.3", fc="moccasin", alpha=0.3))
    ax.text(4.5, 1.3, "Q4: 기회 작고 장벽 높음\n(비권장)", fontsize=9,
            ha="center", color="darkred", fontweight="bold",
            bbox=dict(boxstyle="round,pad=0.3", fc="mistyrose", alpha=0.3))

    ax.set_xlabel("진입장벽 (1=낮음, 5=높음)", fontsize=11)
    ax.set_ylabel("시장 기회 (1=작음, 5=큼)", fontsize=11)
    ax.set_xlim(0.5, 5.5)
    ax.set_ylim(0.5, 5.5)
    ax.set_xticks([1, 2, 3, 4, 5])
    ax.set_yticks([1, 2, 3, 4, 5])
    ax.set_title("그림 3. White Space 2×2 매트릭스 (진입장벽 × 시장 기회)", fontsize=11, fontweight="bold")
    ax.grid(True, alpha=0.3, linestyle="--")
    plt.tight_layout()
    path = os.path.join(FIG_DIR, "fig3_whitespace_2x2.png")
    plt.savefig(path, dpi=130, bbox_inches="tight")
    plt.close()
    return path


def fig4_tech_compare_radar():
    """Multi-tech competitive radar: 6 ligation tech across 5 axes."""
    axes_labels = ["기질 범위", "수율/속도", "스케일성", "GMP 선례", "IP 자유도"]
    techs = {
        "Peptiligase":  [4, 5, 5, 3, 1],
        "OaAEP1":       [3, 4, 3, 1, 2],
        "Sortase A":    [3, 3, 3, 3, 3],
        "Butelase-1":   [3, 5, 2, 1, 2],
        "Subtiligase":  [4, 3, 3, 1, 5],
        "SPPS (기준)":   [5, 3, 5, 5, 5],
    }
    colors = [NAVY, ORANGE, TEAL, RED, "#9B59B6", GRAY]

    angles = np.linspace(0, 2*np.pi, len(axes_labels), endpoint=False).tolist()
    angles += angles[:1]

    fig, ax = plt.subplots(figsize=(8, 7), subplot_kw=dict(polar=True), dpi=130)
    for (name, vals), c in zip(techs.items(), colors):
        v = vals + vals[:1]
        ax.plot(angles, v, color=c, linewidth=1.8, label=name)
        ax.fill(angles, v, color=c, alpha=0.07)

    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(axes_labels, fontsize=10)
    ax.set_ylim(0, 5)
    ax.set_yticks([1, 2, 3, 4, 5])
    ax.set_yticklabels(["1", "2", "3", "4", "5"], fontsize=8)
    ax.set_title("그림 4. 경쟁 기술 다축 비교 (5점 척도)", fontsize=11, fontweight="bold", pad=20)
    ax.legend(loc="upper right", bbox_to_anchor=(1.35, 1.05), fontsize=9)
    ax.grid(True, alpha=0.4)
    plt.tight_layout()
    path = os.path.join(FIG_DIR, "fig4_tech_compare_radar.png")
    plt.savefig(path, dpi=130, bbox_inches="tight")
    plt.close()
    return path


def fig5_patent_timeline():
    """Gantt-style horizontal bar: key patent expiries."""
    patents = [
        ("Subtiligase (Genentech)", 1991, 2011, "Public Domain", "#27AE60"),
        ("OaAEP1 WT (UQ Craik)", 2014, 2034, "UQ", "#2E86C1"),
        ("Peptiligase 분자 청구\nWO2016/056913 (Fresenius Kabi)", 2014, 2035, "Fresenius Kabi iPSUM", NAVY),
        ("Peptiligase 공정\nWO2017/007324", 2015, 2036, "Fresenius Kabi iPSUM", NAVY),
        ("Butelase-1 WO2017/058114 (NTU Tam)", 2016, 2036, "NTU", "#9B59B6"),
        ("OaAEP1 C247A US 11,795,488 (UQ)", 2017, 2038, "UQ Craik", ORANGE),
        ("Peptiligase S2/S2' EP3404036", 2018, 2038, "Fresenius Kabi iPSUM", NAVY),
        ("Sortase ADC (Boehringer/SMAC)", 2013, 2033, "Boehringer", RED),
    ]
    fig, ax = plt.subplots(figsize=(10, 5.5), dpi=130)
    y_pos = np.arange(len(patents))[::-1]
    for y, (name, start, end, holder, color) in zip(y_pos, patents):
        ax.barh(y, end - start, left=start, color=color, alpha=0.75, edgecolor="black", linewidth=0.6)
        ax.text(end + 0.3, y, str(end), va="center", fontsize=8, fontweight="bold", color=color)

    ax.set_yticks(y_pos)
    ax.set_yticklabels([p[0] for p in patents], fontsize=8.5)
    ax.set_xlabel("연도 (우선일 → 만료 추정)")
    ax.set_xlim(1990, 2045)
    ax.axvline(2026, color="red", linewidth=1.8, linestyle="--", alpha=0.7, label="현재 (2026-05)")
    ax.axvline(2034, color="green", linewidth=1.3, linestyle=":", alpha=0.7, label="Peptiligase 분자 만료 (2034)")
    ax.axvline(2038, color="purple", linewidth=1.3, linestyle=":", alpha=0.7, label="Thicket 해소 (~2038)")
    ax.set_title("그림 5. 핵심 특허 만료 Timeline", fontsize=11, fontweight="bold")
    ax.legend(loc="lower right", fontsize=9)
    ax.grid(True, alpha=0.3, axis="x")
    plt.tight_layout()
    path = os.path.join(FIG_DIR, "fig5_patent_timeline.png")
    plt.savefig(path, dpi=130, bbox_inches="tight")
    plt.close()
    return path


def fig6_pmi_compare():
    """Horizontal bar comparing PMI: SPPS vs enzymatic vs hybrid."""
    methods = ["SPPS (보수)", "SPPS (long peptide)", "Hybrid 화학효소", "Peptiligase\n(chemoenzymatic)", "OaAEP1\n(cyclization)"]
    pmi_low = [3000, 8000, 500, 100, 80]
    pmi_high = [5000, 15000, 1500, 500, 300]

    y_pos = np.arange(len(methods))[::-1]
    fig, ax = plt.subplots(figsize=(9, 4.5), dpi=130)
    colors_bar = [RED, "#922B21", ORANGE, TEAL, NAVY]
    for y, low, high, c, m in zip(y_pos, pmi_low, pmi_high, colors_bar, methods):
        ax.barh(y, high - low, left=low, color=c, alpha=0.75, edgecolor="black", linewidth=0.7)
        ax.text(high + 200, y, f"{low:,}–{high:,}", va="center", fontsize=8.5, fontweight="bold", color=c)

    ax.set_yticks(y_pos)
    ax.set_yticklabels(methods, fontsize=10)
    ax.set_xlabel("PMI (Process Mass Intensity, kg input per kg product)")
    ax.set_xscale("log")
    ax.set_xlim(50, 30000)
    ax.set_title("그림 6. PMI 비교: SPPS vs 효소 ligation (낮을수록 친환경)", fontsize=11, fontweight="bold")
    ax.grid(True, alpha=0.3, axis="x", which="both")
    plt.tight_layout()
    path = os.path.join(FIG_DIR, "fig6_pmi_compare.png")
    plt.savefig(path, dpi=130, bbox_inches="tight")
    plt.close()
    return path


def fig7_valuechain():
    """Value chain block diagram (Pillow)."""
    W, H = 1400, 520
    img = Image.new("RGB", (W, H), "white")
    draw = ImageDraw.Draw(img)
    try:
        font = ImageFont.truetype("/usr/share/fonts/truetype/nanum/NanumGothicBold.ttf", 18)
        font_small = ImageFont.truetype("/usr/share/fonts/truetype/nanum/NanumGothic.ttf", 14)
        font_title = ImageFont.truetype("/usr/share/fonts/truetype/nanum/NanumGothicBold.ttf", 22)
    except Exception:
        font = ImageFont.load_default()
        font_small = ImageFont.load_default()
        font_title = ImageFont.load_default()

    draw.text((W//2 - 250, 15), "그림 7. Peptide ligase 밸류체인", fill=NAVY, font=font_title)

    # Boxes (x, y, w, h, color, title, lines[])
    boxes = [
        (40, 90, 220, 130, "#D6EAF8", "① 효소 R&D / IP",
         ["• UQ (Craik)", "• NTU (Tam)", "• DSM → EnzyPep", "• Profluent/Cradle (ML)"]),
        (300, 90, 220, 130, "#A9CCE3", "② 효소 생산",
         ["• Fresenius Kabi iPSUM", "• Singzyme", "• Bachem (자체)", "• Asahi Kasei (CMO)"]),
        (560, 90, 220, 130, "#5DADE2", "③ Cα-ester 빌딩블록",
         ["• Sieber/Rink/Ramage", "• PEPperPRINT", "• Iris Biotech", "• Bachem"]),
        (820, 90, 220, 130, "#2E86C1", "④ Peptide API/GMP",
         ["• Bachem CHF 695M", "• PolyPeptide €389M", "• CordenPharma €900M", "• SK pharmteco"]),
        (1080, 90, 280, 130, "#1A5276", "⑤ Drug Product / 상용",
         ["• Novo Nordisk (Sema)", "• Eli Lilly (Tirze)", "• Pfizer / AZ / Roche", "• GLP-1 biosimilar (2026~)"]),
    ]
    for (x, y, w, h, color, title, lines) in boxes:
        draw.rectangle([x, y, x+w, y+h], fill=color, outline="black", width=2)
        text_color = "white" if color in ("#2E86C1", "#1A5276") else "black"
        draw.text((x+10, y+8), title, fill=text_color, font=font)
        for i, line in enumerate(lines):
            draw.text((x+12, y+38+i*18), line, fill=text_color, font=font_small)

    # Arrows between boxes
    arrow_y = 155
    for x_end in [285, 545, 805, 1065]:
        draw.line([(x_end - 25, arrow_y), (x_end - 5, arrow_y)], fill="black", width=3)
        draw.polygon([(x_end - 5, arrow_y - 7), (x_end - 5, arrow_y + 7), (x_end + 5, arrow_y)], fill="black")

    # Bottom annotation: where to enter
    draw.text((40, 270), "권장 진입 지점:", fill=RED, font=font)
    enter_points = [
        ("EP1: ③ Cα-ester GMP Building Block (anchor, 5y $30-50M)", 305),
        ("EP2: ① 효소 R&D (OaAEP1 reagent + ADC/PDC CRO, 5y $40-80M)", 335),
        ("EP3: ④ Peptide API/GMP (Asia GLP-1 biosimilar JV, 5y $400-900M, Phase 2)", 365),
        ("비권장: ⑤ 자체 Drug Product (5y $500M-1.5B, 트랙레코드 0건 가정 R/R 비대칭)", 395),
    ]
    for txt, y in enter_points:
        draw.text((60, y), txt, fill=NAVY if "비권장" not in txt else GRAY, font=font_small)

    # Value pool legend
    draw.text((40, 440), "값풀(value pool) 추정:", fill="black", font=font)
    legend = [
        ("① 효소 R&D:  $50-200M global", 0),
        ("② 효소 생산:  $100-300M", 280),
        ("③ Cα-ester:  $150-400M", 560),
        ("④ Peptide CDMO:  $2.98B (2026)", 820),
        ("⑤ Drug Product:  GLP-1 $50B+ TAM", 1080),
    ]
    for txt, x in legend:
        draw.text((50 + x, 475), txt, fill="black", font=font_small)

    path = os.path.join(FIG_DIR, "fig7_valuechain.png")
    img.save(path)
    return path


# ==============================================================================
# Markdown -> docx conversion helpers (reused & adapted)
# ==============================================================================

def add_inline_runs(paragraph, text):
    pos = 0
    pattern = re.compile(r"\*\*(.+?)\*\*|`([^`]+)`")
    for m in pattern.finditer(text):
        if m.start() > pos:
            paragraph.add_run(text[pos:m.start()])
        if m.group(1) is not None:
            run = paragraph.add_run(m.group(1))
            run.bold = True
        elif m.group(2) is not None:
            run = paragraph.add_run(m.group(2))
            run.font.name = "Consolas"
            run.font.size = Pt(9)
        pos = m.end()
    if pos < len(text):
        paragraph.add_run(text[pos:])


def parse_table(lines, start_idx):
    rows = []
    i = start_idx
    while i < len(lines) and lines[i].strip().startswith("|"):
        line = lines[i].strip()
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
    doc.add_paragraph()


def render_markdown_to_doc(doc, md_text, base_heading_level=2, figure_hooks=None):
    """
    Render markdown into doc. figure_hooks = dict of {section_marker: callable(doc)}
    triggered when a heading containing the marker substring is encountered.
    """
    figure_hooks = figure_hooks or {}
    lines = md_text.split("\n")
    i = 0
    skipped_first_h1 = False
    while i < len(lines):
        line = lines[i].rstrip()
        if line.startswith("|") and i + 1 < len(lines) and "---" in lines[i+1]:
            rows, i = parse_table(lines, i)
            add_table_to_doc(doc, rows)
            continue
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
            # Figure hook
            for marker, hook in figure_hooks.items():
                if marker in heading_text:
                    hook(doc)
            i += 1
            continue
        if line.startswith(">"):
            p = doc.add_paragraph(style="Intense Quote")
            add_inline_runs(p, line.lstrip("> ").strip())
            i += 1
            continue
        if line.strip() in ("---", "***"):
            doc.add_paragraph()
            i += 1
            continue
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
        if not line.strip():
            i += 1
            continue
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


# ==============================================================================
# Figure insertion helper
# ==============================================================================

def insert_figure(doc, path, caption, width_inches=6.3):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run()
    run.add_picture(path, width=Inches(width_inches))
    cap = doc.add_paragraph()
    cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
    crun = cap.add_run(caption)
    crun.italic = True
    crun.font.size = Pt(9)
    crun.font.color.rgb = RGBColor(0x55, 0x55, 0x55)


# ==============================================================================
# Document scaffolding
# ==============================================================================

def add_table_of_contents(doc):
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
    run = p.add_run("— 엔지니어드 Subtilisin 변이체 / 식물 Asparaginyl Endopeptidase 효소 펩타이드 라이게이션 플랫폼 비교 분석 —")
    run.font.size = Pt(11)
    run.italic = True

    for _ in range(6):
        doc.add_paragraph()

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


def executive_summary(doc, fig_paths):
    doc.add_heading("Executive Summary", level=1)

    p = doc.add_paragraph()
    add_inline_runs(p, (
        "본 보고서는 신규 아이템 **Peptiligase / OaAEP1 (효소 펩타이드 라이게이션 플랫폼)** 에 대한 "
        "기술·시장·Player·고객·특허·규제·사업성·진입장벽 8개 영역의 Deep Dive 분석 결과이다. "
        "조사 일자 2026-05-21 기준으로 [A]~[G] 7개 리서치 에이전트와 [H] 종합 분석 에이전트, "
        "독립 검증 에이전트가 작업하였다. 8개 섹션 중 6개 ✅ 검증완료, 2개 ⚠️ 부분검증, 0개 ❌ 검증실패로 "
        "**전체 신뢰도 '고신뢰'** 등급이며, 핵심 binary claim 1건(효소 ligation 사용 FDA/EMA 승인 의약품 2026-05 기준 **0건**)도 다중 독립 출처로 교차 확인되었다."
    ))

    # Insert market figure right after intro
    insert_figure(doc, fig_paths["fig1"],
                  "그림 1. 시장 규모 전망 (로그 스케일, USD B). 출처: Precedence/Coherent/Mordor/Grand View 합성, 2025-2026 발행.")

    doc.add_heading("핵심 결론", level=2)

    bullets = [
        ("**기술 성숙도**: Peptiligase(엔지니어링된 subtilisin BPN' Δ75-83+S221C+P225A, EnzyPep/Fresenius Kabi iPSUM)는 "
         "**TRL 6-7** — exenatide·thymosin-α1·aviptadil 화학효소 합성 입증, semaglutide/liraglutide 특허 경로 보유. "
         "OaAEP1-C247A(*Oldenlandia affinis*, ~160× WT 활성)는 **TRL 3-5** — cyclization·ADC linker 응용 위주, GMP API 사례 없음."),
        ("**시장**: 치료용 펩타이드 TAM USD 50-56B@2026 → 81-87B@2035. **GLP-1 SAM** Semaglutide $28B + Tirzepatide $36.5B (2025, 합산 ~$70B)로 단일 modality 사상 최대. "
         "펩타이드 CDMO USD 2.98B@2026 (CAGR 11-12%). **효소 합성 sub-segment SOM USD 100-200M [추정]** (cell-free/enzymatic CAGR 8.40%, Mordor)."),
        ("**경쟁 구도**: Fresenius Kabi iPSUM이 EnzyPep을 흡수(2018-19)하여 Peptiligase IP를 사실상 단일 보유. "
         "Singzyme(NTU spin-off, Amgen Golden Ticket 2025-08)가 OaAEP1 상업화 선두. "
         "SPPS 빅3 — Bachem(CHF 695M, EBITDA 30.9%), PolyPeptide(EUR 389M), CordenPharma(€1B+ CAPEX)가 GLP-1 capa 경쟁의 주역. "
         "Novo Holdings의 Catalent 인수 $16.5B(2024-12)가 2024년 최대 peptide CDMO M&A."),
        ("**진입장벽 종합 등급**: Peptiligase **4.0/5 (高)**, OaAEP1 **3.7/5 (高)**. "
         "FTO HIGH — Fresenius Kabi iPSUM(WO2016/056913 만료 ~2035, WO2017/007324 ~2036, EP3404036 ~2038) + "
         "UQ Craik(US 11,795,488 OaAEP1 C247A ~2038) + NTU Tam(butelase WO2017/058114 ~2036) 다자 라이선스 + stacked royalty 필요. "
         "핵심 변곡점 2034(Peptiligase 분자 만료) — thicket 해소 ~2038."),
        ("**결정적 차이 vs EndoS2 분석**: 2026-05 기준 효소 ligation으로 핵심 합성 단계에 사용된 FDA/EMA 승인 의약품 **0건**. "
         "EndoS2 분석 대비 시장 검증 신호가 한 단계 더 약하므로 권고도 한 단계 더 보수적으로 조정."),
        ("**ESG 차별성**: SPPS PMI 3,000–15,000 vs 효소 합성 100–500 — **10~30배 개선**. "
         "EU Green Deal·CSRD Scope 3 압박, IRA Round 2 (Ozempic -71%, 2027 발효)와 결합 시 효소 공정의 경제·환경 ROI 명확."),
        ("**Top 3 권장 진입 지점 (Phased)**: "
         "**EP1: Cα-ester GMP Building Block Supplier (적극 권장, Phase 1 anchor)** — 5년 누적 $30-50M, GP 50-65%, TTM 2-3년. "
         "**EP2: OaAEP1 Reagent + ADC/PDC Bioconjugation CRO (조건부 권장)** — 5년 누적 $40-80M, Genovis-style EBITDA 28%. "
         "**EP3: Asia GLP-1 Biosimilar Enzymatic CDMO JV (Phase 2 조건부)** — 5년 누적 $400-900M, EP1·EP2 검증 + 2034 IP 만료 가시화 후 확장. "
         "**자체 신약(S4, $500M-1.5B, TTM 7-10년)은 비권장**."),
    ]
    for b in bullets:
        p = doc.add_paragraph(style="List Bullet")
        add_inline_runs(p, b)

    doc.add_heading("최종 권고 한 줄", level=2)
    p = doc.add_paragraph()
    add_inline_runs(p, (
        "**EndoS2 분석의 'Asia fast-second' 결론을 한 단계 더 보수화** — "
        "Cα-ester GMP Building Block(EP1)을 anchor로, OaAEP1 ADC/PDC reagent + CRO(EP2)를 paired 진입, "
        "GLP-1 biosimilar enzymatic CDMO(EP3)는 검증 후 Phase 2 확장이 최적의 risk-adjusted 진입 경로."
    ))

    doc.add_page_break()


def section_intro(doc, code, title, grade):
    doc.add_heading(f"[{code}] {title}", level=1)
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
        "각 섹션 본문 내 (Source: URL, 발행일) 형식으로 인용된 모든 출처는 "
        "원본 마크다운 산출물에 포함되어 있다. 주요 1차 출처군:"
    ))
    primary_sources = [
        "**학술/특허**: Wang/Wells (UCSF subtiligase), Quaedflieg/Nuijens (DSM/EnzyPep Peptiligase), Craik (UQ OaAEP1), Tam (NTU butelase); Google Patents WO2016/056913, US 10,138,268, US 11,795,488, WO2017/058114",
        "**기업 IR/보도자료**: Fresenius Kabi, EnzyPep, Singzyme, Bachem AG, PolyPeptide Group, CordenPharma, SK pharmteco, Novo Holdings, Catalent",
        "**시장조사**: Precedence Research, Coherent Market Insights, Mordor Intelligence, Grand View Research, Towards Healthcare, IMARC",
        "**규제 가이던스**: FDA Synthetic Peptide Guidance (2021), EMA Synthetic Peptide Guideline (2026-06-01 effective), ICH Q5E/Q11/M7, USP <1132>, BIOSECURE Act (FY2026 NDAA), IRA Round 2",
        "**기술 문헌**: Toplak/Nuijens 2016 Adv Synth Catal (Peptiligase), Yang/Liu 2017 JACS (OaAEP1 C247A), 2025 JACS (70× AEP), Angew Chem 2026 (Lilly NCL tirzepatide)",
    ]
    for s in primary_sources:
        p = doc.add_paragraph(style="List Bullet")
        add_inline_runs(p, s)

    doc.add_heading("부록 B. 검증 로그 요약 (Verification Log)", level=1)
    p = doc.add_paragraph()
    add_inline_runs(p, "독립 검증 에이전트가 각 섹션의 핵심 사실 주장을 새로운 WebSearch 쿼리로 교차 확인한 결과. 상세 로그는 `peptiligase_oaaep1/VERIFICATION.md` 참조.")
    rows = [
        ["섹션", "검증 등급", "검증 요지"],
        ["[A] 기술", "✅ 검증완료", "Peptiligase BPN' Δ75-83+S221C+P225A 청구항, OaAEP1 C247A ~160× WT 활성, JACS 2025 70× AEP — 1차 출처 일치"],
        ["[B] 시장", "⚠️ 부분검증", "Tirzepatide 2025 매출 실제 USD 36.5B (보고서 $20B → 정정 필요). GLP-1 합산 ~$70B로 상향. 펩타이드 CDMO USD 2.98B@2026 다수 출처 일치."],
        ["[C] Player", "✅ 검증완료", "Singzyme Amgen Golden Ticket 2025-08-21, Granules-Senn $22.3M 2025-04-10, Novo-Catalent $16.5B 2024-12-18, CordenPharma €900M — 1:1 일치"],
        ["[D] 고객", "✅ 검증완료", "Lilly NCL tirzepatide(Angew Chem 2026), 인도 semaglutide 만료 2026-03, Bicycle 화학 cyclization 모두 확인. Bachem CHF 1B 계약 일자 minor 정정 권고."],
        ["[E] 특허/IP", "✅ 검증완료", "WO2016/056913 우선일 2014-10-10, US 11,795,488 C247A (UQ Craik), WO2017/058114 (NTU Tam butelase) 모두 Google Patents 직접 확인"],
        ["[F] 리스크/규제", "✅ 검증완료", "EMA Synthetic Peptide Guideline 2026-06-01 발효, BIOSECURE 2025-12-18 NDAA 서명, subtilisin 1970s 작업자 50% 알레르기 다중 출처 확인"],
        ["[G] 사업성", "⚠️ 부분검증", "Bachem CHF 695M EBITDA 30.9%, PolyPeptide EUR 389M 일치. 단 [B][G] 시장 사이즈 USD 50-56B vs USD 140.9B 내부 불일치 — 출처 차이 [B] 권장 채택"],
        ["[H] 진입장벽", "✅ 검증완료", "인용 facts 검증완료, 'EP1 building block anchor + EP2 ADC reagent' 권고 논리에 명시적 비약 없음"],
    ]
    add_table_to_doc(doc, rows)

    doc.add_heading("부록 C. 사용 시 유의사항", level=1)
    cautions = [
        "**Binary claim 검증**: 2026-05 기준 효소 ligation 사용 FDA/EMA 승인 의약품 **0건** — 다중 출처 반증 0건. 본 보고서의 보수적 권고(EP1+EP2 anchor)는 이 사실에 강하게 의존하며, 첫 승인 사례 발생 시 (예: Fresenius Kabi 자체 GLP-1 biosimilar 승인) **즉시 권고 재평가** 필요.",
        "**시점 민감성**: 6개월 단위 재평가 권장. 2026-03 인도 semaglutide 특허 만료, 2026-06 EMA 펩타이드 가이드라인 발효, IRA Round 2 (2027-01 Ozempic 가격 -71%), 2034 Peptiligase 분자 청구 만료 — 각 이벤트가 시장 가치 재평가 트리거.",
        "**시장 규모 출처 차이**: [B] 보고서 USD 50-56B@2026 vs [G] 인용 USD 140.9B는 'therapeutic peptide' vs 'wider peptide drug market' 정의 차이. 의사결정 시 본 ExecSum의 [B] 기반 수치 (50-56B@2026)를 권장.",
        "**자사 capability에 따른 진입 모드 조정**: 본 보고서 [G][H]는 'platform IP 없는 중견 player' 가정. 자사가 (a) carbohydrate/peptide chemistry 인력, (b) GMP 시설, (c) 지역 footprint 어떤 조합인지에 따라 EP1/EP2/EP3 우선순위 재평가 필수.",
        "**IP timeline의 결정성**: 핵심 권고 시점은 2034(Peptiligase 분자 만료) 이전 vs 이후로 양분. 2026-2033 진입은 라이선스 부담을 받아들이거나 OaAEP1·butelase·신규 ligase 회피 경로 사용. 2034 이후는 SPPS+enzymatic 가격 경쟁 commodity 화 가속 — 본 보고서는 2026-2033 진입 시 한정 분석.",
    ]
    for c in cautions:
        p = doc.add_paragraph(style="List Bullet")
        add_inline_runs(p, c)


# ==============================================================================
# Main build
# ==============================================================================

def main():
    # 1) Generate all figures first
    print("Generating figures...")
    fig_paths = {
        "fig1": fig1_market_projection(),
        "fig2": fig2_barrier_radar(),
        "fig3": fig3_whitespace_2x2(),
        "fig4": fig4_tech_compare_radar(),
        "fig5": fig5_patent_timeline(),
        "fig6": fig6_pmi_compare(),
        "fig7": fig7_valuechain(),
    }
    for k, p in fig_paths.items():
        print(f"  {k}: {os.path.basename(p)} ({os.path.getsize(p)/1024:.1f} KB)")

    # 2) Build doc
    print("Building Word document...")
    doc = Document()
    set_styles(doc)
    cover_page(doc)

    # TOC
    doc.add_heading("목차 (Table of Contents)", level=1)
    add_table_of_contents(doc)
    p = doc.add_paragraph()
    run = p.add_run("※ MS Word에서 목차를 마우스 오른쪽 → '필드 업데이트' 또는 F9로 자동 생성.")
    run.italic = True
    run.font.size = Pt(9)
    run.font.color.rgb = RGBColor(0x80, 0x80, 0x80)
    doc.add_page_break()

    # Executive summary with fig1
    executive_summary(doc, fig_paths)

    # Section-specific figure hooks (triggered when matching section heading appears)
    # Use seen-set to fire each hook exactly once
    fired = set()

    def fire_once(key, fn):
        def _wrap(d):
            if key in fired:
                return
            fired.add(key)
            fn(d)
        return _wrap

    section_hooks = {
        "A": {
            "A.4 대체/경쟁 기술 비교": fire_once("fig4", lambda d: insert_figure(
                d, fig_paths["fig4"],
                "그림 2. 6개 라이게이션 기술 다축 비교 — Peptiligase는 수율·스케일성·기질범위 강점, IP 자유도 약점. SPPS가 GMP 선례·IP 자유도에서 여전히 우세."
            )),
        },
        "B": {},
        "C": {},
        "D": {},
        "E": {
            "E.7 회피설계": fire_once("fig5", lambda d: insert_figure(
                d, fig_paths["fig5"],
                "그림 3. 핵심 특허 만료 Timeline — Peptiligase 분자 청구는 2034 만료, OaAEP1 C247A는 2038. 2026-2033 진입자는 in-license, 2034+ commodity화 가속."
            )),
        },
        "F": {
            "F.5 ESG": fire_once("fig6", lambda d: insert_figure(
                d, fig_paths["fig6"],
                "그림 4. PMI 비교 (로그 스케일) — SPPS 3,000-15,000 vs 효소 합성 100-500. 10-30배 환경 부담 감소. 출처: Sheldon 2018, Roche/Bachem 2023 case studies."
            )),
        },
        "G": {
            "G.7 전략적": fire_once("fig7", lambda d: insert_figure(
                d, fig_paths["fig7"],
                "그림 5. Peptide ligase 밸류체인 — ① 효소 R&D, ② 효소 생산, ③ Cα-ester 빌딩블록, ④ Peptide API/GMP, ⑤ Drug Product. 권장 진입 지점 EP1-EP3 시각화."
            )),
        },
        "H": {
            "H.1 기술적 진입장벽": fire_once("fig2", lambda d: insert_figure(
                d, fig_paths["fig2"],
                "그림 6. 진입장벽 7개 차원 레이더 — Peptiligase(가중평균 4.0/5)와 OaAEP1(3.7/5) 비교. 특허·표준/규제·공급망이 공통 '높음' 영역."
            )),
            "H.3 종합 결론": fire_once("fig3", lambda d: insert_figure(
                d, fig_paths["fig3"],
                "그림 7. White Space 2×2 매트릭스 — WS-1 (Cα-ester 빌딩블록)이 Q1 최우선, WS-2 (OaAEP1 ADC/PDC)는 Q1-Q2 경계. WS-3 (GLP-1 biosimilar CDMO)는 Q2 전략적 진입 영역."
            )),
        },
    }

    for code, title, fname, grade in SECTION_FILES:
        section_intro(doc, code, title, grade)
        path = os.path.join(BASE, fname)
        with open(path, "r", encoding="utf-8") as f:
            md = f.read()
        render_markdown_to_doc(doc, md, base_heading_level=2,
                               figure_hooks=section_hooks.get(code, {}))
        doc.add_page_break()

    appendix_sources_and_verification(doc)
    add_page_number(doc)
    doc.save(OUTPUT_PATH)
    size_kb = os.path.getsize(OUTPUT_PATH) / 1024
    print(f"\n✅ Word report saved: {OUTPUT_PATH} ({size_kb:.1f} KB)")


if __name__ == "__main__":
    main()
