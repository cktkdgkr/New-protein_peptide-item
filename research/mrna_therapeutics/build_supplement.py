"""
Build supplementary report: One-Shot mRNA Concept + Moderna Approach.
Applies R1 (figures) + R2 (beginner-friendly) rules.
"""
import os, re
from docx import Document
from docx.shared import Pt, Cm, RGBColor, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_ALIGN_VERTICAL, WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image, ImageDraw, ImageFont

BASE = "/home/user/New-protein_peptide-item/research/mrna_therapeutics"
FIG_DIR = os.path.join(BASE, "figures")
os.makedirs(FIG_DIR, exist_ok=True)
OUTPUT = os.path.join(BASE, "SUPPLEMENT_oneshot_moderna.docx")

plt.rcParams["font.family"] = "NanumGothic"
plt.rcParams["axes.unicode_minus"] = False
plt.rcParams["font.size"] = 10

NAVY="#1F3A6E"; ORANGE="#E67E22"; TEAL="#16A085"; RED="#C0392B"; GREEN="#27AE60"
GRAY="#7F8C8D"; PURPLE="#8E44AD"; LIGHT_BLUE="#5DADE2"

# ── Figures ──────────────────────────────────────────────────────────────────

def fig1_oneshot_landscape():
    """10 strategies: scientific plausibility vs current evidence."""
    fig, ax = plt.subplots(figsize=(11, 7.5), dpi=130)
    strategies = [
        ("In vivo\nGene Editing\n(Cas9/Intellia)",         4.8, 4.8, 900, GREEN,  "Game-Changer"),
        ("Base Editing\n(Verve PCSK9)",                     4.8, 4.5, 850, GREEN,  "Game-Changer"),
        ("후성유전 편집\n(Epigenetic\nHit-and-Run)",          4.5, 2.5, 650, TEAL,   "Game-Changer"),
        ("In vivo CAR-T\n(Capstan/Orbital)",                4.5, 3.0, 750, NAVY,   "Game-Changer"),
        ("면역관용 유도\n(역백신 개념)",                        3.8, 2.0, 500, PURPLE, "유망"),
        ("mRNA 항체\n(장반감기 단백질)",                       3.5, 3.0, 550, ORANGE, "유망"),
        ("자가증폭 mRNA\n(saRNA, 빈도↓)",                    3.5, 3.5, 500, LIGHT_BLUE, "유망"),
        ("원형 RNA\n(circRNA, 발현↑)",                       3.5, 2.5, 450, LIGHT_BLUE, "유망"),
        ("훈련면역\n(Trained Immunity)",                      2.5, 1.5, 350, GRAY,   "추측"),
        ("장내세균 편집\n(비현실적)",                            1.0, 0.5, 250, RED,    "비현실적"),
    ]
    seen_cat = set()
    for name, plaus, evid, s, c, cat in strategies:
        lbl = cat if cat not in seen_cat else None
        seen_cat.add(cat)
        ax.scatter(plaus, evid, s=s, color=c, alpha=0.6, edgecolors="black", linewidth=1.2, zorder=3, label=lbl)
        ax.annotate(name, (plaus, evid), fontsize=9, ha="center", va="center", fontweight="bold", zorder=4)

    ax.axhline(2.5, color="black", linewidth=0.7, alpha=0.4)
    ax.axvline(3.0, color="black", linewidth=0.7, alpha=0.4)
    ax.set_xlim(0, 5.5); ax.set_ylim(0, 5.5)
    ax.set_xlabel("과학적 타당성 (1=낮음, 5=높음)", fontsize=11)
    ax.set_ylabel("현재 임상 근거 수준 (1=없음, 5=Phase 3+)", fontsize=11)
    ax.set_title("그림 1. 'One-Shot' mRNA 치료 전략 10가지 — 타당성 × 근거 매트릭스",
                 fontsize=12, fontweight="bold")
    ax.legend(loc="lower right", fontsize=10, framealpha=0.95)
    ax.grid(True, alpha=0.3, linestyle="--")
    plt.tight_layout()
    p = os.path.join(FIG_DIR, "sup_fig1_oneshot_landscape.png")
    plt.savefig(p, dpi=130, bbox_inches="tight"); plt.close()
    return p


def fig2_concept_diagram():
    """Pillow: vaccine vs chronic vs one-shot therapeutic concept comparison."""
    W, H = 1350, 650
    img = Image.new("RGB", (W, H), "white")
    draw = ImageDraw.Draw(img)
    try:
        fb = ImageFont.truetype("/usr/share/fonts/truetype/nanum/NanumGothicBold.ttf", 20)
        fs = ImageFont.truetype("/usr/share/fonts/truetype/nanum/NanumGothic.ttf", 15)
        ft = ImageFont.truetype("/usr/share/fonts/truetype/nanum/NanumGothicBold.ttf", 24)
    except:
        fb = fs = ft = ImageFont.load_default()

    draw.text((W//2-320, 10), "그림 2. 백신 원리를 치료제에 적용하는 발상의 전환", fill=NAVY, font=ft)

    # Row 1: vaccine
    draw.rectangle([40, 70, 410, 200], fill="#D5F5E3", outline="black", width=2)
    draw.text((50, 75), "A. mRNA 백신 (현재 작동 중)", fill=GREEN, font=fb)
    draw.text((50, 105), "mRNA 주사 → 세포가 '스파이크' 만듦", fill="black", font=fs)
    draw.text((50, 130), "→ 면역계가 기억 → 수개월~수년 보호", fill="black", font=fs)
    draw.text((50, 158), "핵심: 한 번의 레시피로 면역 '기억' 생성", fill=GREEN, font=fs)

    draw.line([(425, 135), (455, 135)], fill="black", width=3)
    draw.polygon([(455, 128), (455, 142), (465, 135)], fill="black")

    # Row 1: insight
    draw.rectangle([470, 70, 900, 200], fill="#FEF9E7", outline=ORANGE, width=2)
    draw.text((480, 75), "핵심 통찰", fill=ORANGE, font=fb)
    draw.text((480, 105), "mRNA 자체는 며칠이면 사라지지만,", fill="black", font=fs)
    draw.text((480, 130), "그것이 '촉발한 결과'는 오래 지속!", fill=ORANGE, font=fs)
    draw.text((480, 158), "비유: 성냥(mRNA)은 타 없어져도", fill="black", font=fs)
    draw.text((518, 178), "불(치료 효과)은 계속 탄다", fill=ORANGE, font=fs)

    draw.line([(915, 135), (945, 135)], fill="black", width=3)
    draw.polygon([(945, 128), (945, 142), (955, 135)], fill="black")

    # Row 1: question
    draw.rectangle([960, 70, 1320, 200], fill="#FDEDEC", outline=RED, width=2)
    draw.text((970, 75), "사용자 질문", fill=RED, font=fb)
    draw.text((970, 108), "이걸 '치료제'에도", fill="black", font=fs)
    draw.text((970, 133), "적용할 수 없을까?", fill=RED, font=fb)
    draw.text((970, 168), "→ 아래 3가지가 답!", fill="black", font=fs)

    # Row 2: Three solutions
    solutions = [
        (40, 240, 400, 420, "#D6EAF8", "Game-Changer #1", "유전자 편집 (Base Editing)",
         ["mRNA가 '가위 효소'를 만듦", "→ DNA를 영구 수정", "→ mRNA 사라져도 DNA는 영구", "예: Verve PCSK9 → LDL -62%", "★ 단 1회 주사로 영구 효과"]),
        (470, 240, 830, 420, "#E8DAEF", "Game-Changer #2", "In vivo CAR-T",
         ["mRNA가 T세포를 '슈퍼전사'로", "→ 슈퍼전사가 질병세포 제거", "→ 질병세포 없어지면 끝!", "예: Capstan → 자가면역 치료", "★ mRNA 소멸 뒤에도 질병 해결"]),
        (900, 240, 1320, 420, "#FDEBD0", "Game-Changer #3", "후성유전 편집 (Epigenetic)",
         ["mRNA가 '스위치 끄기' 도구 만듦", "→ 문제 유전자의 스위치 OFF", "→ DNA 자르지 않아 안전", "예: PCSK9 1년간 침묵 (마우스)", "★ 가역적이면서 장기 지속"]),
    ]
    for (x1, y1, x2, y2, color, tag, title, lines) in solutions:
        draw.rectangle([x1, y1, x2, y2], fill=color, outline="black", width=2)
        draw.text((x1+10, y1+8), tag, fill=NAVY, font=fb)
        draw.text((x1+10, y1+35), title, fill="black", font=fb)
        for i, l in enumerate(lines):
            draw.text((x1+15, y1+65+i*28), l, fill="black", font=fs)

    # Bottom row: vs chronic
    draw.rectangle([40, 450, 1320, 560], fill="#F2F3F4", outline=GRAY, width=2)
    draw.text((50, 458), "참고 — 기존 mRNA 치료제의 한계 (만성 재투여 방식)", fill=GRAY, font=fb)
    draw.text((50, 490), "mRNA 주사 → 단백질 3~7일 → 사라짐 → 2주마다 반복 → 평생 → anti-PEG 면역 → 효능↓ → 비용↑↑", fill=GRAY, font=fs)
    draw.text((50, 520), "→ 위 3가지 'One-Shot' 전략이 이 한계를 근본적으로 우회!", fill=RED, font=fb)

    # Bottom note
    draw.text((40, 580), "출처: Intellia lonvo-z Phase 3 (2026-04-27), Verve VERVE-102 Phase 1b (2026-05), Nature 2024 epigenetic, Capstan CPTX2309 Phase 1 (2025-H2)",
              fill="#888", font=ImageFont.truetype("/usr/share/fonts/truetype/nanum/NanumGothic.ttf", 12))

    p = os.path.join(FIG_DIR, "sup_fig2_concept_diagram.png")
    img.save(p)
    return p


def fig3_moderna_pipeline():
    """Moderna pipeline status horizontal Gantt."""
    fig, ax = plt.subplots(figsize=(11, 5), dpi=130)
    programs = [
        ("mRNA-3927 (PA)\n프로피온산혈증", 2019, 2028, "Pivotal\nreadout 2026", GREEN, "★ 가장 진행"),
        ("mRNA-3705 (MMA)\n메틸말론산혈증", 2022, 2029, "FDA START\n등록 시작 2026", TEAL, "2세대"),
        ("mRNA-3704 (MMA)\n1세대, 중단", 2018, 2023, "중단\n(3705로 대체)", GRAY, "중단"),
        ("mRNA-6231 (IL-2)\n면역조절", 2021, 2024, "Phase 1 후\n소식 없음 [미확인]", ORANGE, "보류"),
        ("mRNA-1944 (항체)\n치쿤구니아 mAb", 2019, 2022, "Phase 1 완료\n추가 진행 미정", ORANGE, "보류"),
        ("AZD8601 (VEGF-A)\n심장 재생 (with AZ)", 2017, 2023, "AZ 2022 drop\nModerna 2023 drop", RED, "중단"),
    ]
    y_pos = np.arange(len(programs))[::-1]
    for y, (name, start, end, note, color, status) in zip(y_pos, programs):
        ax.barh(y, end - start, left=start, color=color, alpha=0.8, edgecolor="black", linewidth=0.7)
        ax.text(end + 0.2, y, note, va="center", fontsize=8.5, color=color, fontweight="bold")

    ax.set_yticks(y_pos)
    ax.set_yticklabels([p[0] for p in programs], fontsize=9)
    ax.set_xlim(2016, 2031)
    ax.axvline(2026.4, color="red", linewidth=1.8, linestyle="--", alpha=0.7, label="현재 (2026-05)")
    ax.axvline(2028, color="green", linewidth=1.3, linestyle=":", alpha=0.7, label="Moderna 첫 승인 목표 (2028)")
    ax.set_xlabel("연도")
    ax.set_title("그림 3. Moderna 비백신 mRNA 치료제 파이프라인 현황 (2026-05)",
                 fontsize=11, fontweight="bold")
    ax.legend(loc="lower right", fontsize=9)
    ax.grid(True, alpha=0.3, axis="x")
    plt.tight_layout()
    p = os.path.join(FIG_DIR, "sup_fig3_moderna_pipeline.png")
    plt.savefig(p, dpi=130, bbox_inches="tight"); plt.close()
    return p


def fig4_limitation_solution():
    """Heatmap: 4 limitations × which One-Shot strategy solves them."""
    strategies = ["In vivo\nGene Editing", "Base\nEditing", "후성유전\n편집", "In vivo\nCAR-T",
                  "면역관용\n(역백신)", "mRNA 항체\n(장반감기)", "saRNA\n(빈도↓)", "circRNA\n(발현↑)"]
    limitations = ["간 외 전달\n(Delivery)", "발현 기간\n(Duration)", "재투여 면역\n(ABC)", "비용\n(Cost)"]
    # 0=해결안됨, 1=부분해결, 2=해결
    data = np.array([
        [0, 2, 2, 2],  # Gene edit
        [0, 2, 2, 2],  # Base edit
        [0, 2, 2, 2],  # Epigenetic
        [2, 2, 2, 1],  # CAR-T (solves delivery via T cell targeting!)
        [0, 2, 2, 1],  # Tolerance
        [0, 1, 1, 1],  # mRNA antibody
        [0, 1, 1, 1],  # saRNA
        [0, 1, 1, 1],  # circRNA
    ])
    fig, ax = plt.subplots(figsize=(9, 5.5), dpi=130)
    cmap = plt.cm.RdYlGn
    im = ax.imshow(data, cmap=cmap, vmin=0, vmax=2, aspect="auto")
    ax.set_xticks(np.arange(len(limitations)))
    ax.set_xticklabels(limitations, fontsize=10)
    ax.set_yticks(np.arange(len(strategies)))
    ax.set_yticklabels(strategies, fontsize=10)
    lbl = {0: "미해결", 1: "부분", 2: "해결"}
    for i in range(data.shape[0]):
        for j in range(data.shape[1]):
            ax.text(j, i, lbl[data[i,j]], ha="center", va="center",
                    color="white" if data[i,j]==0 else "black", fontsize=9, fontweight="bold")
    ax.set_title("그림 4. 'One-Shot' 전략이 mRNA 치료제 4대 한계를 얼마나 해결하는가",
                 fontsize=11, fontweight="bold")
    cbar = plt.colorbar(im, ax=ax, ticks=[0,1,2])
    cbar.ax.set_yticklabels(["미해결", "부분 해결", "해결"])
    plt.tight_layout()
    p = os.path.join(FIG_DIR, "sup_fig4_limitation_solution.png")
    plt.savefig(p, dpi=130, bbox_inches="tight"); plt.close()
    return p


# ── Docx helpers ─────────────────────────────────────────────────────────────

def add_inline_runs(paragraph, text):
    pos = 0
    pattern = re.compile(r"\*\*(.+?)\*\*|`([^`]+)`")
    for m in pattern.finditer(text):
        if m.start() > pos: paragraph.add_run(text[pos:m.start()])
        if m.group(1): r=paragraph.add_run(m.group(1)); r.bold=True
        elif m.group(2): r=paragraph.add_run(m.group(2)); r.font.name="Consolas"; r.font.size=Pt(9)
        pos = m.end()
    if pos < len(text): paragraph.add_run(text[pos:])

def parse_table(lines, si):
    rows=[]; i=si
    while i<len(lines) and lines[i].strip().startswith("|"):
        line=lines[i].strip()
        if re.match(r"^\|?\s*[-:|\s]+\|[-:|\s]+",line) and "---" in line: i+=1; continue
        rows.append([c.strip() for c in line.strip("|").split("|")]); i+=1
    return rows, i

def add_table_to_doc(doc, rows):
    if not rows: return
    nc=max(len(r) for r in rows); rows=[r+[""]*(nc-len(r)) for r in rows]
    t=doc.add_table(rows=len(rows),cols=nc); t.style="Light Grid Accent 1"; t.alignment=WD_TABLE_ALIGNMENT.CENTER
    for i,row in enumerate(rows):
        for j,ct in enumerate(row):
            c=t.cell(i,j); c.text=""; p=c.paragraphs[0]; add_inline_runs(p,ct)
            for r in p.runs: r.font.size=Pt(9);
            if i==0:
                for r in p.runs: r.bold=True
            c.vertical_alignment=WD_ALIGN_VERTICAL.CENTER
    doc.add_paragraph()

def render_md(doc, md, base=2, hooks=None):
    hooks=hooks or {}; lines=md.split("\n"); i=0; skip1=False
    while i<len(lines):
        line=lines[i].rstrip()
        if line.startswith("|") and i+1<len(lines) and "---" in lines[i+1]:
            rows,i=parse_table(lines,i); add_table_to_doc(doc,rows); continue
        hm=re.match(r"^(#{1,6})\s+(.*)$",line)
        if hm:
            lv=len(hm.group(1)); ht=hm.group(2).strip()
            if lv==1 and not skip1: skip1=True; i+=1; continue
            al=min(max(base+lv-2,1),9); p=doc.add_heading(level=al); add_inline_runs(p,ht)
            for mk,hk in hooks.items():
                if mk in ht: hk(doc)
            i+=1; continue
        if line.startswith(">"): p=doc.add_paragraph(style="Intense Quote"); add_inline_runs(p,line.lstrip("> ").strip()); i+=1; continue
        if line.strip() in ("---","***"): doc.add_paragraph(); i+=1; continue
        m=re.match(r"^(\s*)[-*]\s+(.*)$",line)
        if m:
            try: p=doc.add_paragraph(style="List Bullet")
            except: p=doc.add_paragraph()
            add_inline_runs(p,m.group(2)); i+=1; continue
        m=re.match(r"^(\s*)\d+\.\s+(.*)$",line)
        if m:
            try: p=doc.add_paragraph(style="List Number")
            except: p=doc.add_paragraph()
            add_inline_runs(p,m.group(2)); i+=1; continue
        if not line.strip(): i+=1; continue
        pl=[line]; j=i+1
        while j<len(lines):
            nx=lines[j].rstrip()
            if not nx.strip() or nx.startswith("|") or re.match(r"^#{1,6}\s",nx) or re.match(r"^\s*[-*]\s",nx) or re.match(r"^\s*\d+\.\s",nx) or nx.startswith(">") or nx.strip() in ("---","***"): break
            pl.append(nx); j+=1
        p=doc.add_paragraph(); add_inline_runs(p," ".join(pl)); i=j

def insert_fig(doc, path, caption, w=6.4):
    p=doc.add_paragraph(); p.alignment=WD_ALIGN_PARAGRAPH.CENTER
    r=p.add_run(); r.add_picture(path, width=Inches(w))
    c=doc.add_paragraph(); c.alignment=WD_ALIGN_PARAGRAPH.CENTER
    cr=c.add_run(caption); cr.italic=True; cr.font.size=Pt(9); cr.font.color.rgb=RGBColor(0x55,0x55,0x55)

def set_styles(doc):
    n=doc.styles["Normal"]; n.font.name="맑은 고딕"
    n._element.rPr.rFonts.set(qn("w:eastAsia"),"맑은 고딕"); n.font.size=Pt(10)
    for h,sz in [("Heading 1",18),("Heading 2",14),("Heading 3",12),("Heading 4",11)]:
        try:
            s=doc.styles[h]; s.font.name="맑은 고딕"; s._element.rPr.rFonts.set(qn("w:eastAsia"),"맑은 고딕")
            s.font.size=Pt(sz); s.font.color.rgb=RGBColor(0x1F,0x3A,0x6E); s.font.bold=True
        except: pass

def add_page_number(doc):
    f=doc.sections[0].footer; p=f.paragraphs[0]; p.alignment=WD_ALIGN_PARAGRAPH.CENTER
    r=p.add_run()
    fc1=OxmlElement("w:fldChar"); fc1.set(qn("w:fldCharType"),"begin")
    it=OxmlElement("w:instrText"); it.set(qn("xml:space"),"preserve"); it.text="PAGE"
    fc2=OxmlElement("w:fldChar"); fc2.set(qn("w:fldCharType"),"end")
    r._r.append(fc1); r._r.append(it); r._r.append(fc2)

# ── Main ─────────────────────────────────────────────────────────────────────

def main():
    print("Generating figures...")
    fps = {
        "fig1": fig1_oneshot_landscape(),
        "fig2": fig2_concept_diagram(),
        "fig3": fig3_moderna_pipeline(),
        "fig4": fig4_limitation_solution(),
    }
    for k,p in fps.items(): print(f"  {k}: {os.path.basename(p)} ({os.path.getsize(p)/1024:.1f} KB)")

    print("Building Word document...")
    doc = Document(); set_styles(doc)
    sec = doc.sections[0]
    sec.top_margin=Cm(2.5); sec.bottom_margin=Cm(2.5); sec.left_margin=Cm(2.5); sec.right_margin=Cm(2.5)

    # ── Cover ──
    for _ in range(3): doc.add_paragraph()
    p=doc.add_paragraph(); p.alignment=WD_ALIGN_PARAGRAPH.CENTER
    r=p.add_run("보충 분석 보고서"); r.font.size=Pt(20); r.font.bold=True; r.font.color.rgb=RGBColor(0x1F,0x3A,0x6E)
    doc.add_paragraph()
    p=doc.add_paragraph(); p.alignment=WD_ALIGN_PARAGRAPH.CENTER
    r=p.add_run("mRNA 치료제의 한계를 극복하는\n'One-Shot' 전략 + Moderna 접근법 분석"); r.font.size=Pt(15); r.font.bold=True
    doc.add_paragraph()
    p=doc.add_paragraph(); p.alignment=WD_ALIGN_PARAGRAPH.CENTER
    r=p.add_run("— 백신의 '한 번이면 충분한' 원리를 치료제에 적용할 수 있는가? —"); r.font.size=Pt(11); r.italic=True
    for _ in range(4): doc.add_paragraph()
    t=doc.add_table(rows=3,cols=2); t.style="Light List Accent 1"; t.alignment=WD_TABLE_ALIGNMENT.CENTER
    for i,(k,v) in enumerate([("조사 일자","2026-05-22"),("본 보고서 성격","mRNA 치료제 Deep Dive의 보충 분석 (추측 포함)"),("작성 규칙","R1(그림 적극 활용) + R2(초보자 친화적 작성) 적용")]):
        t.cell(i,0).text=k; t.cell(i,1).text=v
        for c in (t.cell(i,0),t.cell(i,1)):
            for r in c.paragraphs[0].runs: r.font.size=Pt(11)
        for r in t.cell(i,0).paragraphs[0].runs: r.bold=True
    doc.add_page_break()

    # ── Executive Summary ──
    doc.add_heading("핵심 요약 — 초보자를 위한 설명", level=1)
    p=doc.add_paragraph()
    add_inline_runs(p, (
        "**쉽게 말하면**, mRNA 치료제의 가장 큰 문제는 '효과가 며칠밖에 안 가서 평생 맞아야 한다'는 점입니다. "
        "그런데 mRNA 백신은 같은 mRNA인데도 한 번 맞으면 수개월~수년 동안 면역이 유지되죠. "
        "왜냐면, 백신은 mRNA가 만든 단백질로 면역계에 '기억'을 심어주고, 그 기억이 mRNA 없이도 계속 남기 때문입니다."
    ))
    p=doc.add_paragraph()
    add_inline_runs(p, (
        "**이 보고서의 핵심 질문**: 이 원리를 치료제에도 적용할 수 없을까? "
        "즉, mRNA가 며칠 만에 사라지더라도, 그것이 '촉발한 결과'가 오래 지속되는 치료법은 없을까?"
    ))
    p=doc.add_paragraph()
    add_inline_runs(p, (
        "**답**: 있습니다. 이미 임상에서 검증되고 있는 3가지 'Game-Changer' 전략이 존재합니다. "
        "비유하자면, mRNA는 '성냥'이고 치료 효과는 '불'입니다. "
        "성냥(mRNA)은 타 없어져도 불(치료)은 계속 타는 방법을 찾은 것입니다."
    ))

    insert_fig(doc, fps["fig2"],
               "그림 1. 백신 원리를 치료제에 적용하는 '발상의 전환' — 성냥(mRNA)은 사라져도 불(치료 효과)은 계속 타는 3가지 전략.")

    bullets = [
        "**Game-Changer #1 — 유전자 편집 (Base Editing)**: mRNA가 세포 안에서 '유전자 편집 가위'를 잠깐 만들고, 이 가위가 DNA를 영구 수정합니다. mRNA는 사라져도 DNA 변화는 영구적! Verve사의 PCSK9 편집은 단 1회 주사로 나쁜 콜레스테롤(LDL)을 62% 영구 감소시켰습니다.",
        "**Game-Changer #2 — In vivo CAR-T**: mRNA가 환자의 면역세포(T세포)를 일시적으로 '슈퍼전사'로 변신시킵니다. 이 슈퍼전사가 질병을 일으키는 세포를 모두 파괴합니다. mRNA는 사라져도 질병 세포가 이미 제거되었으므로 효과 영구 지속!",
        "**Game-Changer #3 — 후성유전 편집**: DNA를 자르지 않고, 문제 유전자의 '스위치'만 끕니다. Nature 2024 논문에서 마우스 실험 시 PCSK9 유전자를 1년간 침묵시키는 데 성공했습니다. DNA를 자르지 않으므로 안전하면서도 장기 지속!",
        "**Moderna의 현재 접근**: Moderna는 위의 'One-Shot' 전략을 사용하지 않고, 전통적인 '반복 투여' 방식을 고수 중입니다. 대표 프로그램 mRNA-3927(프로피온산혈증)은 2~3주마다 정맥 주사를 맞아야 합니다. 2028년 첫 승인을 목표로 하고 있습니다.",
    ]
    for b in bullets:
        p=doc.add_paragraph(style="List Bullet"); add_inline_runs(p, b)

    doc.add_page_break()

    # ── Part 1: One-Shot Analysis ──
    doc.add_heading("Part 1. 'One-Shot' mRNA 치료 전략 분석", level=1)
    p=doc.add_paragraph()
    add_inline_runs(p, "**이 섹션을 한 줄로 요약하면**: mRNA가 며칠 만에 사라져도 치료 효과가 오래 지속되는 10가지 전략을 분석합니다.")

    insert_fig(doc, fps["fig1"],
               "그림 2. 10가지 'One-Shot' 전략 — 과학적 타당성 × 현재 임상 근거 수준. "
               "우측 상단(녹색) = 이미 임상에서 검증 중인 Game-Changer.")

    # Load md and render
    with open(os.path.join(BASE, "ANALYSIS_oneshot_concept.md"), "r") as f:
        md1 = f.read()

    fired = set()
    def fo(k, fn):
        def _w(d):
            if k in fired: return
            fired.add(k)
            fn(d)
        return _w

    hooks1 = {
        "Part 3": fo("fig4", lambda d: insert_fig(
            d, fps["fig4"],
            "그림 3. 각 'One-Shot' 전략이 mRNA 치료제 4대 한계를 얼마나 해결하는가. "
            "유전자 편집·Base 편집·후성유전 편집은 Duration·ABC·Cost 3개 한계를 동시 해결 (녹색)."
        )),
    }
    render_md(doc, md1, base=2, hooks=hooks1)
    doc.add_page_break()

    # ── Part 2: Moderna ──
    doc.add_heading("Part 2. Moderna mRNA 치료제 개발 방식 심층 분석", level=1)
    p=doc.add_paragraph()
    add_inline_runs(p, "**이 섹션을 한 줄로 요약하면**: Moderna는 'One-Shot'이 아닌 '만성 재투여' 방식으로 희귀 대사질환을 타겟하고 있으며, 2028년 첫 승인을 목표로 합니다.")

    insert_fig(doc, fps["fig3"],
               "그림 4. Moderna 비백신 mRNA 치료제 파이프라인 현황. "
               "mRNA-3927(PA)만 pivotal 단계, 나머지는 보류 또는 중단.")

    with open(os.path.join(BASE, "ANALYSIS_moderna_approach.md"), "r") as f:
        md2 = f.read()
    render_md(doc, md2, base=2)

    add_page_number(doc)
    doc.save(OUTPUT)
    print(f"\n✅ Supplement report saved: {OUTPUT} ({os.path.getsize(OUTPUT)/1024:.1f} KB)")

if __name__ == "__main__":
    main()
