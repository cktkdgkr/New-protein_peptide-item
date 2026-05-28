"""
Build molecular mechanism report for 3 mRNA limitations.
R1 (figures with molecular cascade diagrams) + R2 (beginner-friendly).
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
OUTPUT = os.path.join(BASE, "MOLECULAR_report.docx")

plt.rcParams["font.family"] = "NanumGothic"
plt.rcParams["axes.unicode_minus"] = False
plt.rcParams["font.size"] = 10

NAVY="#1F3A6E"; ORANGE="#E67E22"; TEAL="#16A085"; RED="#C0392B"; GREEN="#27AE60"
GRAY="#7F8C8D"; PURPLE="#8E44AD"; LIGHT_BLUE="#5DADE2"; PINK="#EC7063"

def _fonts():
    try:
        fb = ImageFont.truetype("/usr/share/fonts/truetype/nanum/NanumGothicBold.ttf", 18)
        fs = ImageFont.truetype("/usr/share/fonts/truetype/nanum/NanumGothic.ttf", 14)
        ft = ImageFont.truetype("/usr/share/fonts/truetype/nanum/NanumGothicBold.ttf", 22)
        fxs = ImageFont.truetype("/usr/share/fonts/truetype/nanum/NanumGothic.ttf", 12)
        return fb, fs, ft, fxs
    except:
        d = ImageFont.load_default()
        return d, d, d, d


def fig1_hepatic_tropism():
    """Pillow: liver targeting molecular cascade."""
    W, H = 1400, 780
    img = Image.new("RGB", (W, H), "white")
    draw = ImageDraw.Draw(img)
    fb, fs, ft, fxs = _fonts()

    draw.text((W//2-450, 12), "그림 1. 간 표적 편향의 분자 메커니즘 — LNP가 왜 간으로만 가는가?", fill=NAVY, font=ft)

    # Step 1: LNP enters blood
    draw.ellipse([60, 80, 200, 220], fill="#FDEBD0", outline="black", width=2)
    draw.text((85, 100), "LNP", fill="black", font=fb)
    draw.text((75, 130), "(60-100 nm)", fill="black", font=fxs)
    draw.text((75, 150), "지질 + mRNA", fill="black", font=fxs)
    draw.text((75, 175), "PEG-lipid", fill=PURPLE, font=fxs)
    draw.text((75, 195), "(표면 코팅)", fill=PURPLE, font=fxs)

    # Arrow 1: PEG desorbs
    draw.line([(210, 150), (300, 150)], fill="black", width=3)
    draw.polygon([(300, 142), (300, 158), (315, 150)], fill="black")
    draw.text((215, 110), "혈장에서", fill=GRAY, font=fxs)
    draw.text((215, 125), "PEG 탈락", fill=GRAY, font=fxs)

    # Step 2: ApoE adsorbs
    draw.ellipse([330, 80, 470, 220], fill="#D6EAF8", outline="black", width=2)
    draw.text((340, 100), "LNP + ApoE", fill="black", font=fb)
    draw.text((345, 130), "(아포지단백 E,", fill="black", font=fxs)
    draw.text((345, 150), "혈장 단백질)", fill="black", font=fxs)
    draw.text((345, 175), "★ '간세포", fill=GREEN, font=fxs)
    draw.text((345, 195), "  출입증'", fill=GREEN, font=fxs)

    # Arrow 2
    draw.line([(480, 150), (570, 150)], fill="black", width=3)
    draw.polygon([(570, 142), (570, 158), (585, 150)], fill="black")
    draw.text((485, 110), "ApoE 표면의", fill=GRAY, font=fxs)
    draw.text((485, 125), "amphipathic helix", fill=GRAY, font=fxs)

    # Step 3: LDLR binding on hepatocyte
    draw.rectangle([600, 60, 850, 240], fill="#D5F5E3", outline="black", width=2)
    draw.text((615, 75), "간세포 표면", fill=GREEN, font=fb)
    draw.text((615, 105), "LDLR (저밀도지단백", fill="black", font=fxs)
    draw.text((615, 122), "수용체)", fill="black", font=fxs)
    draw.text((615, 145), "★ 세포당 10⁵개!", fill=RED, font=fb)
    draw.text((615, 175), "ApoE의 LDLR-binding", fill="black", font=fxs)
    draw.text((615, 192), "도메인 인식 → 결합", fill="black", font=fxs)
    draw.text((615, 215), "Akinc 2010: ApoE KO", fill=GRAY, font=fxs)
    draw.text((615, 230), "→ 활성 95% 손실", fill=GRAY, font=fxs)

    # Arrow 3
    draw.line([(860, 150), (950, 150)], fill="black", width=3)
    draw.polygon([(950, 142), (950, 158), (965, 150)], fill="black")
    draw.text((865, 125), "Clathrin", fill=GRAY, font=fxs)
    draw.text((865, 140), "endocytosis", fill=GRAY, font=fxs)

    # Step 4: Inside hepatocyte
    draw.rectangle([980, 60, 1340, 240], fill="#FADBD8", outline="black", width=2)
    draw.text((995, 75), "간세포 내부 흡수", fill=RED, font=fb)
    draw.text((995, 105), "→ Endosome 진입", fill="black", font=fxs)
    draw.text((995, 130), "→ pH 5.5에서 ionizable", fill="black", font=fxs)
    draw.text((1010, 147), "  lipid 양전하화", fill="black", font=fxs)
    draw.text((995, 170), "→ 막 융합 → mRNA 방출", fill="black", font=fxs)
    draw.text((995, 195), "★ 단, escape 1-2%만!", fill=RED, font=fb)
    draw.text((995, 215), "98%는 라이소좀 분해", fill=GRAY, font=fxs)

    # ────────────────────────────────────────────────────────
    # Bottom: Why other organs fail
    draw.text((40, 280), "왜 다른 장기에는 못 가는가? — '진화적 방벽' 때문", fill=NAVY, font=ft)

    organs = [
        (40,  330, "폐 (Lung)",     PINK,
         ["혈관 내피가 빈틈없이 단단함", "(continuous endothelium)", "Tight junction 단백질로 차단",
          "기관지 점액·기침 반사도 방어", "→ LNP IV의 <2%만 도달"]),
        (370, 330, "뇌 (Brain)",    PINK,
         ["BBB(혈뇌장벽) 존재", "claudin-5, occludin, ZO-1으로", "초강력 tight junction", "P-당단백(Pgp)이 약물 펌프-아웃",
          "→ LNP IV의 <0.1%"]),
        (700, 330, "근육 (Muscle)", PINK,
         ["빈틈없는 내피 + 기저막",
          "성숙 근섬유는 endocytosis 능력 낮음",
          "혈관 밀도도 낮음 (휴식 시)",
          "→ LNP 거의 도달 못함",
          ""]),
        (1030,330, "신장 (Kidney)", PINK,
         ["사구체 슬릿 5-8 nm cut-off",
          "(nephrin/podocin)",
          "LNP 60-100 nm = 통과 불가",
          "세뇨관 측은 LDLR 없음",
          "→ 신장 표적 사실상 불가능"]),
    ]
    for (x, y, name, c, lines) in organs:
        draw.rectangle([x, y, x+320, y+220], fill="#FDEDEC", outline=c, width=2)
        draw.text((x+10, y+8), name, fill=c, font=fb)
        for i, l in enumerate(lines):
            draw.text((x+12, y+38+i*30), l, fill="black", font=fxs)

    # ────────────────────────────────────────────────────────
    # Bottom annotation
    draw.rectangle([40, 590, 1340, 750], fill="#FEF9E7", outline=ORANGE, width=2)
    draw.text((50, 600), "★ 결정적 차이: 간 sinusoid(동굴혈관)의 '비밀'", fill=ORANGE, font=fb)
    draw.text((50, 635), "  • 간만 유일하게 fenestration(구멍)이 100-150 nm 크기로 뚫려있음", fill="black", font=fs)
    draw.text((50, 660), "  • 다른 장기 혈관 = 빈틈없이 막혀있음 (continuous endothelium)", fill="black", font=fs)
    draw.text((50, 685), "  • LNP(60-100 nm) = 간 구멍은 통과 가능, 다른 장기는 통과 불가", fill="black", font=fs)
    draw.text((50, 715), "  → 즉, LNP가 '간을 선호'하는 게 아니라 '다른 장기는 진화적으로 차단'된 것!", fill=RED, font=fb)

    p = os.path.join(FIG_DIR, "mol_fig1_liver.png")
    img.save(p)
    return p


def fig2_mrna_degradation():
    """Pillow: mRNA degradation pathways."""
    W, H = 1400, 760
    img = Image.new("RGB", (W, H), "white")
    draw = ImageDraw.Draw(img)
    fb, fs, ft, fxs = _fonts()

    draw.text((W//2-380, 12), "그림 2. mRNA 분해 메커니즘 — 왜 며칠밖에 못 가는가?", fill=NAVY, font=ft)

    # Central mRNA representation
    # 5'cap - UTR - CDS - UTR - polyA
    y_mrna = 100
    # 5' cap
    draw.ellipse([100, y_mrna-25, 160, y_mrna+25], fill="#F4D03F", outline="black", width=2)
    draw.text((110, y_mrna-12), "5'cap", fill="black", font=fxs)
    draw.text((100, y_mrna+30), "m7G cap", fill=GRAY, font=fxs)
    # 5' UTR
    draw.rectangle([160, y_mrna-15, 280, y_mrna+15], fill="#AED6F1", outline="black", width=2)
    draw.text((180, y_mrna-7), "5'UTR", fill="black", font=fxs)
    # CDS
    draw.rectangle([280, y_mrna-15, 700, y_mrna+15], fill="#82E0AA", outline="black", width=2)
    draw.text((430, y_mrna-7), "CDS (단백질 코딩)", fill="black", font=fs)
    # 3' UTR
    draw.rectangle([700, y_mrna-15, 820, y_mrna+15], fill="#AED6F1", outline="black", width=2)
    draw.text((720, y_mrna-7), "3'UTR", fill="black", font=fxs)
    # PolyA tail
    draw.rectangle([820, y_mrna-15, 1000, y_mrna+15], fill="#F5B7B1", outline="black", width=2)
    draw.text((860, y_mrna-7), "AAAAAA... (poly-A)", fill="black", font=fxs)

    # Modified nucleoside annotation
    draw.text((430, y_mrna+30), "★ m1Ψ (N1-methylpseudouridine) 수식 → PKR/RIG-I 차단", fill=PURPLE, font=fxs)

    # ──── 3 Decay Pathways ────
    # Pathway 1: Decapping (top-left)
    draw.rectangle([40, 200, 470, 450], fill="#FADBD8", outline=RED, width=2)
    draw.text((50, 210), "분해경로 #1: 5' Decapping", fill=RED, font=fb)
    draw.text((50, 240), "1) DCP2 + DCP1 + EDC4 복합체가", fill="black", font=fs)
    draw.text((65, 262), "   m7G cap을 잘라냄", fill="black", font=fs)
    draw.text((65, 285), "   (비유: '모자(cap)'를 벗기는 '가위')", fill=GRAY, font=fxs)
    draw.text((50, 312), "2) 5'-PPP 노출 → XRN1이 인식", fill="black", font=fs)
    draw.text((50, 335), "3) XRN1이 5'→3' 방향으로 한 입씩", fill="black", font=fs)
    draw.text((65, 357), "   mRNA를 '먹어치움'", fill="black", font=fs)
    draw.text((65, 380), "   (비유: '먼지 청소기'가 빨아들임)", fill=GRAY, font=fxs)
    draw.text((50, 410), "★ circRNA가 회피하는 경로!", fill=GREEN, font=fb)
    draw.text((65, 432), "  (원형이라 5' 끝 자체가 없음)", fill=GREEN, font=fxs)

    # Pathway 2: Deadenylation (top-right)
    draw.rectangle([490, 200, 920, 450], fill="#FCF3CF", outline=ORANGE, width=2)
    draw.text((500, 210), "분해경로 #2: Deadenylation", fill=ORANGE, font=fb)
    draw.text((500, 240), "1) CCR4-NOT 복합체 (CNOT6/7 핵심)", fill="black", font=fs)
    draw.text((515, 262), "   poly-A tail을 한 개씩 잘라냄", fill="black", font=fs)
    draw.text((515, 285), "   (비유: '꼬리'를 짧게 자르는 '가위')", fill=GRAY, font=fxs)
    draw.text((500, 312), "2) PAN2/PAN3가 추가 단축", fill="black", font=fs)
    draw.text((500, 335), "3) Exosome 복합체 (DIS3/RRP44)가", fill="black", font=fs)
    draw.text((515, 357), "   3'→5' 방향으로 분해", fill="black", font=fs)
    draw.text((515, 380), "   (비유: '뒤에서부터 먹는 청소기')", fill=GRAY, font=fxs)
    draw.text((500, 410), "★ poly-A 길이 ↑ → 안정성 ↑", fill=NAVY, font=fb)
    draw.text((515, 432), "  (Moderna: 100-150 nt 최적화)", fill=NAVY, font=fxs)

    # Pathway 3: LNP escape failure
    draw.rectangle([940, 200, 1360, 450], fill="#D6DBDF", outline=PURPLE, width=2)
    draw.text((950, 210), "★ 진짜 병목: LNP escape", fill=PURPLE, font=fb)
    draw.text((950, 240), "LNP가 endosome에 들어가면:", fill="black", font=fs)
    draw.text((965, 262), "• pH 5.5 → ionizable lipid 양전하화", fill="black", font=fxs)
    draw.text((965, 285), "• 막 융합 시도", fill="black", font=fxs)
    draw.text((965, 308), "• mRNA를 세포질로 방출", fill="black", font=fxs)
    draw.text((950, 340), "★ 성공률 단 1-2%! (Sahay 2013)", fill=RED, font=fb)
    draw.text((965, 365), "  98-99%는 라이소좀 분해", fill=RED, font=fs)
    draw.text((950, 395), "→ 즉, 발현 단명의 '진짜 원인'은", fill=NAVY, font=fs)
    draw.text((965, 417), "  분해효소가 아니라 'escape 실패'", fill=NAVY, font=fs)
    draw.text((965, 435), "  (대부분 LNP가 도달조차 못함)", fill=GRAY, font=fxs)

    # Bottom: Time scale
    draw.rectangle([40, 480, 1360, 720], fill="#EAF2F8", outline=NAVY, width=2)
    draw.text((50, 490), "결과: 단백질 발현 시간 경과 (Moderna mRNA-3927 PK 모델 기준)", fill=NAVY, font=fb)
    # Bar chart-like
    times = [(0, "0h", "투여"), (12, "12h", "Endo escape"), (24, "24-48h", "★ 최고 발현"), (96, "4일차", "발현 절반"), (168, "7일차", "거의 0")]
    for i, (t, lbl, note) in enumerate(times):
        x = 80 + i*250
        color = RED if t >= 96 else GREEN if t == 24 else NAVY
        draw.ellipse([x-30, 555-30, x+30, 555+30], fill=color, outline="black", width=2)
        draw.text((x-15, 545), lbl, fill="white", font=fs)
        draw.text((x-50, 600), note, fill=color, font=fxs)
        if i < len(times)-1:
            draw.line([(x+30, 555), (x+220, 555)], fill="black", width=2)

    draw.text((50, 640), "★ 핵심: 단명의 근본 원인 3가지 = (1) DCP2/XRN1 + (2) CCR4-NOT/exosome + (3) endosomal escape 1-2%", fill=RED, font=fs)
    draw.text((50, 670), "→ 해결책: (1) circRNA로 5' 끝 제거 + (2) 안정 UTR 설계 + (3) endosomolytic peptide 추가 LNP", fill=GREEN, font=fs)
    draw.text((50, 695), "★ 진짜 game-changer = 분해를 막는 것이 아니라 '한 번 작동하면 영구 효과'를 내는 것 (gene editing 등)", fill=PURPLE, font=fs)

    p = os.path.join(FIG_DIR, "mol_fig2_degradation.png")
    img.save(p)
    return p


def fig3_abc_cascade():
    """Pillow: anti-PEG IgM ABC cascade."""
    W, H = 1400, 800
    img = Image.new("RGB", (W, H), "white")
    draw = ImageDraw.Draw(img)
    fb, fs, ft, fxs = _fonts()

    draw.text((W//2-410, 12), "그림 3. ABC(Accelerated Blood Clearance) 분자 캐스케이드", fill=NAVY, font=ft)

    # Top: 1st dose
    draw.rectangle([40, 70, 680, 380], fill="#D5F5E3", outline=GREEN, width=2)
    draw.text((50, 80), "1차 투여 — 정상 작동", fill=GREEN, font=ft)

    # Stage 1
    draw.rectangle([55, 115, 220, 230], fill="white", outline="black", width=1)
    draw.text((65, 122), "Stage 1", fill=NAVY, font=fb)
    draw.text((65, 148), "LNP가 혈류 진입", fill="black", font=fs)
    draw.text((65, 170), "표면에 PEG2000", fill="black", font=fxs)
    draw.text((65, 188), "(~45 ethylene oxide", fill="black", font=fxs)
    draw.text((65, 206), "  단위 반복)", fill="black", font=fxs)

    # Arrow
    draw.line([(225, 170), (250, 170)], fill="black", width=2)
    draw.polygon([(250, 165), (250, 175), (258, 170)], fill="black")

    # Stage 2
    draw.rectangle([263, 115, 470, 230], fill="white", outline="black", width=1)
    draw.text((273, 122), "Stage 2", fill=NAVY, font=fb)
    draw.text((273, 148), "비장 marginal zone", fill="black", font=fs)
    draw.text((273, 170), "B세포가 PEG 인식", fill="black", font=fs)
    draw.text((273, 192), "→ IgM BCR 가교", fill="black", font=fxs)
    draw.text((273, 210), "(T세포 도움 없이!)", fill="black", font=fxs)

    # Arrow
    draw.line([(475, 170), (500, 170)], fill="black", width=2)
    draw.polygon([(500, 165), (500, 175), (508, 170)], fill="black")

    # Stage 3
    draw.rectangle([513, 115, 670, 230], fill="white", outline="black", width=1)
    draw.text((523, 122), "Stage 3", fill=NAVY, font=fb)
    draw.text((523, 148), "Plasmablast 분화", fill="black", font=fs)
    draw.text((523, 170), "anti-PEG IgM 생산", fill="black", font=fs)
    draw.text((523, 192), "(5-7일 소요)", fill="black", font=fxs)
    draw.text((523, 210), "혈중 분비 시작", fill="black", font=fxs)

    # 1st dose outcome
    draw.text((55, 250), "1차 투여 결과:", fill=NAVY, font=fb)
    draw.text((55, 278), "• LNP 반감기: 수 시간 (정상)", fill="black", font=fs)
    draw.text((55, 302), "• mRNA가 간세포 도달 → 단백질 발현", fill="black", font=fs)
    draw.text((55, 326), "• 약효 정상 발현", fill=GREEN, font=fs)
    draw.text((55, 350), "★ 단, 면역계는 '기억' 이미 형성됨", fill=ORANGE, font=fs)

    # Bottom: 2nd dose
    draw.rectangle([720, 70, 1360, 380], fill="#FADBD8", outline=RED, width=2)
    draw.text((730, 80), "2차 투여 — ABC 발생 (효능 붕괴)", fill=RED, font=ft)

    # Cascade
    cascade = [
        (730, 120, "①", "anti-PEG IgM이\n새 LNP의 PEG에 결합\n(다가 결합, 고친화도)"),
        (730, 220, "②", "IgM 5량체 → C1q 결합\n→ C1r/s 활성화\n→ C4/C2 절단"),
        (1050, 120, "③", "C3 convertase 형성\n→ C3 → C3b 절단\n→ LNP 표면에 C3b 침착"),
        (1050, 220, "④", "Kupffer cell의 CR3 수용체\n(CD11b/CD18, Mac-1)가\nC3b 인식 → 즉시 포식"),
    ]
    for x, y, num, txt in cascade:
        draw.rectangle([x, y, x+300, y+80], fill="white", outline=RED, width=1)
        draw.text((x+10, y+5), num, fill=RED, font=fb)
        for i, line in enumerate(txt.split("\n")):
            draw.text((x+35, y+5+i*20), line, fill="black", font=fxs)

    draw.text((730, 320), "★ 결과: LNP 반감기 시간→분 단위 추락! 약효 거의 0", fill=RED, font=fb)
    draw.text((730, 355), "★ IgM은 IgG보다 보체 활성화 ~1000배 강력!", fill=RED, font=fs)

    # Bottom panel: stats and solutions
    draw.rectangle([40, 410, 1360, 770], fill="#FEF9E7", outline=ORANGE, width=2)
    draw.text((50, 420), "정량 데이터 + 해결책 매핑", fill=ORANGE, font=ft)

    # Stats
    draw.text((50, 460), "[검증된 정량 데이터]", fill=NAVY, font=fb)
    stats = [
        "• 일반 인구의 ~72%가 이미 anti-PEG 항체 보유 (화장품·식품의 PEG 노출, Yang 2016)",
        "• IgM 펜타머(5량체)는 IgG보다 보체 활성화 1000배 강력",
        "• 2차 투여 시 LNP 혈중 반감기: 수 시간 → 수 분 (>100배 감소)",
        "• 간세포 LDLR: 세포당 ~10⁵개, 그러나 ABC로 인해 LNP가 간에 도달 자체를 못함",
        "• Null-mutation 환자(예: OTC 완전 결손)는 발현된 단백질 자체도 'foreign'으로 인식 → ADA 생성",
    ]
    for i, s in enumerate(stats):
        draw.text((60, 490+i*22), s, fill="black", font=fs)

    # Solutions
    draw.text((50, 620), "[해결책 매핑]", fill=GREEN, font=fb)
    solutions = [
        "(1) PEG-free LNP: PEG 대신 polysarcosine (Pas) 또는 zwitterionic polymer로 대체",
        "(2) C5 보체 억제제 동시 투여 (eculizumab repurposing) — 단, 감염 위험 증가",
        "(3) 면역관용 LNP (Selecta ImmTOR, rapamycin 동봉) — '재투여 면역' 자체를 차단",
        "(4) Splenectomy 환자 데이터: 비장 없으면 anti-PEG 생성 ↓ (분자 메커니즘 직접 증명)",
        "(5) ★ 근본 해결: 1회만 투여하는 modality로 전환 (gene editing, Yamanaka, hydrogel depot)",
    ]
    for i, s in enumerate(solutions):
        color = NAVY if i < 4 else RED
        draw.text((60, 650+i*22), s, fill=color, font=fs)

    p = os.path.join(FIG_DIR, "mol_fig3_abc.png")
    img.save(p)
    return p


def fig4_solution_mapping():
    """Heatmap: each solution → which molecular mechanism does it target?"""
    solutions = [
        "SORT lipid\n(Cheng 2020)",
        "Antibody-LNP\n(Capstan)",
        "PEG-free LNP\n(polysarcosine)",
        "circRNA\n(Orna/Lilly)",
        "saRNA\n(Arcturus)",
        "Base editing\n(Verve)",
        "Yamanaka mRNA\n(Life Bio)",
        "Hydrogel depot",
        "DNA origami\n+ LNP",
        "C5 inhibitor\n동시투여",
        "Tolerogenic LNP\n(ImmTOR)",
        "★ 콤보\n(Hydrogel+Origami)",
    ]
    mechanisms = [
        "ApoE-LDLR\n경로 회피",
        "다른 조직\n표적 부여",
        "DCP2/XRN1\n분해 회피",
        "CCR4-NOT\n분해 회피",
        "Endosomal\nescape 개선",
        "Anti-PEG IgM\n회피",
        "보체 C3b\n침착 차단",
        "재투여\n자체 불필요",
    ]
    # 0=영향없음, 1=부분해결, 2=직접해결
    data = np.array([
        [2, 2, 0, 0, 0, 0, 0, 0],  # SORT
        [1, 2, 0, 0, 0, 0, 0, 0],  # Ab-LNP
        [0, 0, 0, 0, 0, 2, 2, 1],  # PEG-free
        [0, 0, 2, 1, 0, 0, 0, 0],  # circRNA
        [0, 0, 1, 1, 0, 0, 0, 0],  # saRNA
        [0, 0, 0, 0, 0, 0, 0, 2],  # Base editing (1회 영구)
        [0, 0, 0, 0, 0, 0, 0, 2],  # Yamanaka (1회 영구)
        [0, 0, 0, 0, 1, 1, 1, 1],  # Hydrogel (부분 ↓ 횟수)
        [0, 0, 2, 1, 1, 0, 0, 1],  # Origami
        [0, 0, 0, 0, 0, 0, 2, 0],  # C5 inhibitor
        [0, 0, 0, 0, 0, 2, 2, 1],  # Tolerogenic
        [0, 0, 2, 1, 1, 1, 1, 2],  # Combo
    ])
    fig, ax = plt.subplots(figsize=(12, 7), dpi=130)
    cmap = plt.cm.YlGn
    im = ax.imshow(data, cmap=cmap, vmin=0, vmax=2, aspect="auto")
    ax.set_xticks(np.arange(len(mechanisms)))
    ax.set_xticklabels(mechanisms, fontsize=9.5)
    ax.set_yticks(np.arange(len(solutions)))
    ax.set_yticklabels(solutions, fontsize=10)
    lbl = {0: "—", 1: "부분", 2: "직접"}
    for i in range(data.shape[0]):
        for j in range(data.shape[1]):
            ax.text(j, i, lbl[data[i,j]], ha="center", va="center",
                    color="white" if data[i,j]>=2 else "black", fontsize=9, fontweight="bold")
    ax.set_title("그림 4. 해결책 × 분자 메커니즘 매핑 — 어떤 솔루션이 어떤 메커니즘을 정확히 타격하는가",
                 fontsize=11, fontweight="bold")
    cbar = plt.colorbar(im, ax=ax, ticks=[0,1,2])
    cbar.ax.set_yticklabels(["미해결", "부분 해결", "직접 해결"])
    plt.tight_layout()
    p = os.path.join(FIG_DIR, "mol_fig4_mapping.png")
    plt.savefig(p, dpi=130, bbox_inches="tight"); plt.close()
    return p


# ── Docx helpers (shared) ───────────────────────────────────────────────────

def add_ir(p, t):
    pos=0; pat=re.compile(r"\*\*(.+?)\*\*|`([^`]+)`")
    for m in pat.finditer(t):
        if m.start()>pos: p.add_run(t[pos:m.start()])
        if m.group(1): r=p.add_run(m.group(1)); r.bold=True
        elif m.group(2): r=p.add_run(m.group(2)); r.font.name="Consolas"; r.font.size=Pt(9)
        pos=m.end()
    if pos<len(t): p.add_run(t[pos:])

def parse_tbl(lines, si):
    rows=[]; i=si
    while i<len(lines) and lines[i].strip().startswith("|"):
        ln=lines[i].strip()
        if re.match(r"^\|?\s*[-:|\s]+\|[-:|\s]+",ln) and "---" in ln: i+=1; continue
        rows.append([c.strip() for c in ln.strip("|").split("|")]); i+=1
    return rows, i

def add_tbl(doc, rows):
    if not rows: return
    nc=max(len(r) for r in rows); rows=[r+[""]*(nc-len(r)) for r in rows]
    t=doc.add_table(rows=len(rows),cols=nc); t.style="Light Grid Accent 1"; t.alignment=WD_TABLE_ALIGNMENT.CENTER
    for i,row in enumerate(rows):
        for j,ct in enumerate(row):
            c=t.cell(i,j); c.text=""; p=c.paragraphs[0]; add_ir(p,ct)
            for r in p.runs: r.font.size=Pt(9)
            if i==0:
                for r in p.runs: r.bold=True
            c.vertical_alignment=WD_ALIGN_VERTICAL.CENTER
    doc.add_paragraph()

def render_md(doc, md, base=2, hooks=None):
    hooks=hooks or {}; lines=md.split("\n"); i=0; sk=False
    while i<len(lines):
        ln=lines[i].rstrip()
        if ln.startswith("|") and i+1<len(lines) and "---" in lines[i+1]:
            rows,i=parse_tbl(lines,i); add_tbl(doc,rows); continue
        hm=re.match(r"^(#{1,6})\s+(.*)$",ln)
        if hm:
            lv=len(hm.group(1)); ht=hm.group(2).strip()
            if lv==1 and not sk: sk=True; i+=1; continue
            al=min(max(base+lv-2,1),9); p=doc.add_heading(level=al); add_ir(p,ht)
            for mk,hk in hooks.items():
                if mk in ht: hk(doc)
            i+=1; continue
        if ln.startswith(">"): p=doc.add_paragraph(style="Intense Quote"); add_ir(p,ln.lstrip("> ").strip()); i+=1; continue
        if ln.strip() in ("---","***"): doc.add_paragraph(); i+=1; continue
        m=re.match(r"^(\s*)[-*]\s+(.*)$",ln)
        if m:
            try: p=doc.add_paragraph(style="List Bullet")
            except: p=doc.add_paragraph()
            add_ir(p,m.group(2)); i+=1; continue
        m=re.match(r"^(\s*)\d+\.\s+(.*)$",ln)
        if m:
            try: p=doc.add_paragraph(style="List Number")
            except: p=doc.add_paragraph()
            add_ir(p,m.group(2)); i+=1; continue
        if not ln.strip(): i+=1; continue
        pl=[ln]; j=i+1
        while j<len(lines):
            nx=lines[j].rstrip()
            if not nx.strip() or nx.startswith("|") or re.match(r"^#{1,6}\s",nx) or re.match(r"^\s*[-*]\s",nx) or re.match(r"^\s*\d+\.\s",nx) or nx.startswith(">") or nx.strip() in ("---","***"): break
            pl.append(nx); j+=1
        p=doc.add_paragraph(); add_ir(p," ".join(pl)); i=j

def ins_fig(doc, path, cap, w=6.4):
    p=doc.add_paragraph(); p.alignment=WD_ALIGN_PARAGRAPH.CENTER
    r=p.add_run(); r.add_picture(path, width=Inches(w))
    c=doc.add_paragraph(); c.alignment=WD_ALIGN_PARAGRAPH.CENTER
    cr=c.add_run(cap); cr.italic=True; cr.font.size=Pt(9); cr.font.color.rgb=RGBColor(0x55,0x55,0x55)

def set_styles(doc):
    n=doc.styles["Normal"]; n.font.name="맑은 고딕"
    n._element.rPr.rFonts.set(qn("w:eastAsia"),"맑은 고딕"); n.font.size=Pt(10)
    for h,sz in [("Heading 1",18),("Heading 2",14),("Heading 3",12)]:
        try:
            s=doc.styles[h]; s.font.name="맑은 고딕"; s._element.rPr.rFonts.set(qn("w:eastAsia"),"맑은 고딕")
            s.font.size=Pt(sz); s.font.color.rgb=RGBColor(0x1F,0x3A,0x6E); s.font.bold=True
        except: pass

def add_pn(doc):
    f=doc.sections[0].footer; p=f.paragraphs[0]; p.alignment=WD_ALIGN_PARAGRAPH.CENTER
    r=p.add_run()
    fc1=OxmlElement("w:fldChar"); fc1.set(qn("w:fldCharType"),"begin")
    it=OxmlElement("w:instrText"); it.set(qn("xml:space"),"preserve"); it.text="PAGE"
    fc2=OxmlElement("w:fldChar"); fc2.set(qn("w:fldCharType"),"end")
    r._r.append(fc1); r._r.append(it); r._r.append(fc2)


def main():
    print("Generating figures...")
    fps = {
        "fig1": fig1_hepatic_tropism(),
        "fig2": fig2_mrna_degradation(),
        "fig3": fig3_abc_cascade(),
        "fig4": fig4_solution_mapping(),
    }
    for k,p in fps.items(): print(f"  {k}: {os.path.basename(p)} ({os.path.getsize(p)/1024:.1f} KB)")

    print("Building Word document...")
    doc = Document(); set_styles(doc)
    sec=doc.sections[0]; sec.top_margin=Cm(2.5); sec.bottom_margin=Cm(2.5); sec.left_margin=Cm(2.5); sec.right_margin=Cm(2.5)

    # Cover
    for _ in range(3): doc.add_paragraph()
    p=doc.add_paragraph(); p.alignment=WD_ALIGN_PARAGRAPH.CENTER
    r=p.add_run("분자 메커니즘 심층 분석 보고서"); r.font.size=Pt(20); r.font.bold=True; r.font.color.rgb=RGBColor(0x1F,0x3A,0x6E)
    doc.add_paragraph()
    p=doc.add_paragraph(); p.alignment=WD_ALIGN_PARAGRAPH.CENTER
    r=p.add_run("mRNA 치료제 3대 한계의\n정확한 분자 단위 메커니즘"); r.font.size=Pt(15); r.font.bold=True
    doc.add_paragraph()
    p=doc.add_paragraph(); p.alignment=WD_ALIGN_PARAGRAPH.CENTER
    r=p.add_run("— 왜 간에만 가는가? 왜 며칠밖에 못 가는가? 왜 재투여하면 안 듣는가? —"); r.font.size=Pt(11); r.italic=True
    for _ in range(4): doc.add_paragraph()
    t=doc.add_table(rows=3,cols=2); t.style="Light List Accent 1"; t.alignment=WD_TABLE_ALIGNMENT.CENTER
    for i,(k,v) in enumerate([("조사 일자","2026-05-22"),("본 보고서 성격","분자생물학·약물전달 분야 정밀 메커니즘 분석"),("작성 규칙","R1(분자 다이어그램 4종) + R2(초보자 친화) 적용")]):
        t.cell(i,0).text=k; t.cell(i,1).text=v
        for c in (t.cell(i,0),t.cell(i,1)):
            for r in c.paragraphs[0].runs: r.font.size=Pt(11)
        for r in t.cell(i,0).paragraphs[0].runs: r.bold=True
    doc.add_page_break()

    # Exec Summary
    doc.add_heading("핵심 요약 — 한 줄로 정리하면", level=1)
    p=doc.add_paragraph()
    add_ir(p, (
        "**쉽게 말하면**, mRNA 치료제의 3가지 한계는 각각 다음 분자 사건에서 비롯됩니다:"
    ))

    bullets = [
        "**한계 1 (간 표적 편향)**: LNP(지질나노입자)가 혈류에 들어가면 **ApoE**라는 단백질이 자동으로 표면에 달라붙고, 이 ApoE를 **간세포의 LDLR 수용체**가 마치 '출입증'처럼 인식해서 LNP를 끌어들입니다. 더 결정적으로, **간 혈관은 100-150 nm 크기의 구멍**이 뚫려있어 LNP(60-100 nm)가 통과 가능하지만, 다른 장기 혈관은 빈틈없이 막혀있습니다. 즉, **LNP가 간을 '선호'하는 게 아니라 다른 장기는 '진화적으로 차단'된 것**입니다.",

        "**한계 2 (발현 단명)**: mRNA는 3개의 분해효소가 동시에 공격합니다. (1) **DCP2**가 mRNA의 '모자(5' cap)'를 벗기고, **XRN1**이 5'→3' 방향으로 먹어치움. (2) **CCR4-NOT**이 mRNA의 '꼬리(poly-A)'를 짧게 자르고, **exosome 복합체**가 3'→5' 방향으로 분해. 더 결정적으로, LNP가 세포 안 endosome에서 mRNA를 세포질로 풀어주는 데 **단 1-2%만 성공**합니다. 즉, **분해효소보다 'endosomal escape 실패'가 진짜 병목**입니다.",

        "**한계 3 (재투여 면역, ABC)**: LNP의 PEG(폴리에틸렌글리콜) 표면 코팅을 비장의 **marginal zone B세포**가 인식해서 **anti-PEG IgM 항체**를 만듭니다 (T세포 도움 없이 5-7일 내). 2회째 투여 시 이 IgM이 새 LNP에 결합 → **보체 C1q → C3b가 LNP 표면에 침착** → 간의 **Kupffer 세포(CR3 수용체)**가 즉시 포식. 결과: **LNP 반감기 수 시간 → 수 분**으로 추락. **IgM은 IgG보다 보체 활성화가 1000배 강력**한 점이 ABC를 결정적으로 만듭니다.",
    ]
    for b in bullets:
        p=doc.add_paragraph(style="List Bullet"); add_ir(p, b)

    p=doc.add_paragraph()
    add_ir(p, "**가장 중요한 통찰**: 이 3가지 한계의 분자 메커니즘을 정확히 알면, 각 해결책이 어느 분자 단계를 정확히 타격하는지 분명해집니다.")

    doc.add_page_break()

    # Section 1: Liver
    doc.add_heading("Part 1. 간 표적 편향의 분자 메커니즘", level=1)
    p=doc.add_paragraph()
    add_ir(p, "**이 섹션을 한 줄로 요약하면**: LNP는 간을 '선호'하는 게 아니라, 다른 장기가 '진화적으로 차단'되어 있어서 어쩔 수 없이 간으로 가는 것입니다.")
    ins_fig(doc, fps["fig1"],
            "그림 1. 간 표적 편향의 분자 캐스케이드 — ApoE 흡착 → LDLR 인식 → endocytosis → endosomal escape. "
            "왜 폐·뇌·근육·신장이 안 되는지의 분자적 이유 포함.")
    doc.add_page_break()

    # Section 2: Duration
    doc.add_heading("Part 2. 발현 단명의 분자 메커니즘", level=1)
    p=doc.add_paragraph()
    add_ir(p, "**이 섹션을 한 줄로 요약하면**: mRNA는 3개 분해효소가 동시에 공격하지만, 진짜 병목은 LNP의 endosomal escape 1-2%입니다.")
    ins_fig(doc, fps["fig2"],
            "그림 2. mRNA 분해 메커니즘 — 5' decapping(DCP2-XRN1) + deadenylation(CCR4-NOT-exosome) + endosomal escape 1-2% 병목.")
    doc.add_page_break()

    # Section 3: ABC
    doc.add_heading("Part 3. 재투여 면역 (ABC) 분자 캐스케이드", level=1)
    p=doc.add_paragraph()
    add_ir(p, "**이 섹션을 한 줄로 요약하면**: anti-PEG IgM이 1차 투여 후 5-7일 내 생성되고, 2차 투여 시 보체 C3b가 LNP에 침착되어 Kupffer 세포가 즉시 포식하므로 LNP 반감기가 시간→분 단위로 추락합니다.")
    ins_fig(doc, fps["fig3"],
            "그림 3. ABC 분자 캐스케이드 — marginal zone B세포 → anti-PEG IgM → C1q → C3b → Kupffer cell CR3.")
    doc.add_page_break()

    # Section 4: Solution mapping
    doc.add_heading("Part 4. 분자 메커니즘 × 해결책 매핑", level=1)
    p=doc.add_paragraph()
    add_ir(p, "**이 섹션을 한 줄로 요약하면**: 각 해결책이 어느 분자 단계를 정확히 타격하는지 한 장의 매트릭스로 정리했습니다.")
    ins_fig(doc, fps["fig4"],
            "그림 4. 해결책 × 분자 메커니즘 매핑 — '직접 해결' = 진녹색, '부분 해결' = 옅은 녹색, '미해결' = 흰색. "
            "★콤보(Hydrogel+Origami)가 가장 많은 분자 단계를 동시에 해결.")
    doc.add_page_break()

    # Detail body
    doc.add_heading("Part 5. 분자 메커니즘 상세 본문", level=1)
    p=doc.add_paragraph()
    add_ir(p, "**이 섹션을 한 줄로 요약하면**: 위의 3가지 한계를 분자생물학 교과서 수준의 정확도로 풀어 설명합니다. 모든 효소·수용체·복합체의 정확한 이름과 정량 데이터를 포함합니다.")

    with open(os.path.join(BASE, "MOLECULAR_mechanisms.md"), "r") as f:
        md = f.read()
    render_md(doc, md, base=2)

    add_pn(doc)
    doc.save(OUTPUT)
    sz = os.path.getsize(OUTPUT)/1024
    print(f"\n✅ Molecular report saved: {OUTPUT} ({sz:.1f} KB)")

if __name__ == "__main__":
    main()
