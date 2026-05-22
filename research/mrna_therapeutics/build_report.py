"""
Build the final Word (.docx) report for mRNA Therapeutics (non-vaccine) Deep Dive.

Embedded PNG figures (matplotlib + Pillow) per CLAUDE.md R1.

Figures:
  fig1_market_projection.png       - Market size projection (TAM/SAM/SOM + comparators)
  fig2_tissue_tropism.png          - LNP IV biodistribution (간 vs 폐 vs CNS vs muscle)
  fig3_feasibility_matrix.png      - Disease segment feasibility (가능/경계/불가능)
  fig4_root_cause_heatmap.png      - 4-bucket root cause × application heatmap
  fig5_ma_timeline.png             - Big Pharma M&A wave 2025-2026 (timeline)
  fig6_ip_timeline.png             - Patent expiry timeline (UPenn/Arbutus/Acuitas)
  fig7_barrier_radar.png           - 7-dim entry barrier radar (mRNA vs Peptiligase vs EndoS2)
  fig8_whitespace_2x2.png          - White Space 2x2 matrix
  fig9_valuechain.png              - mRNA value chain diagram (Pillow)
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
import numpy as np
from PIL import Image, ImageDraw, ImageFont

BASE = "/home/user/New-protein_peptide-item/research/mrna_therapeutics"
FIG_DIR = os.path.join(BASE, "figures")
os.makedirs(FIG_DIR, exist_ok=True)
OUTPUT_PATH = os.path.join(BASE, "FINAL_REPORT.docx")

ITEM_NAME = "mRNA-기반 치료제 / 기능성 단백질 대체제 (비백신·비RNAi)"
REPORT_DATE = "2026-05-22"
PURPOSE = "사업기획 / 신규 진입 검토 + 가능 영역·불가능 원인 규명"
SCOPE = "글로벌 (전 세계)"
COMPANY_CAP = "(미지정 — platform IP 없는 중견 biotech/CDMO/reagent player 가정)"

SECTION_FILES = [
    ("A", "기술 분석", "A_technology.md", "✅ 검증완료"),
    ("B", "시장 분석", "B_market.md", "✅ 검증완료"),
    ("C", "주요 Player 분석", "C_players.md", "✅ 검증완료"),
    ("D", "고객 / 응용분야 분석 (핵심 매트릭스)", "D_customers_applications.md", "✅ 검증완료"),
    ("E", "특허/IP 분석", "E_patents.md", "⚠️ 부분검증"),
    ("F", "리스크 및 규제 분석", "F_risk_regulatory.md", "✅ 검증완료"),
    ("G", "사업성 및 전략 시사점", "G_business.md", "✅ 검증완료"),
    ("H", "진입장벽 & White Space (Core Synthesis)", "H_entry_whitespace.md", "✅ 검증완료"),
]

plt.rcParams["font.family"] = "NanumGothic"
plt.rcParams["axes.unicode_minus"] = False
plt.rcParams["font.size"] = 10

NAVY = "#1F3A6E"
ORANGE = "#E67E22"
TEAL = "#16A085"
RED = "#C0392B"
GREEN = "#27AE60"
GRAY = "#7F8C8D"
LIGHT_BLUE = "#5DADE2"
PURPLE = "#8E44AD"


# ==============================================================================
# Figures
# ==============================================================================

def fig1_market_projection():
    fig, ax = plt.subplots(figsize=(9, 5), dpi=130)
    years = [2025, 2026, 2028, 2030, 2032, 2035]
    # Non-vaccine mRNA therapeutics (Persistence, B§B.1.1)
    nonvax_mrna = [5.3, 6.6, 10.3, 14.5, 21.4, 32.5]  # USD B
    # In vivo gene editing (B§B.1.2)
    in_vivo_edit = [2.5, 3.2, 5.5, 9.5, 16.2, 37.8]
    # In vivo CAR-T (low base, 61% CAGR)
    in_vivo_cart = [0.6, 1.1, 3.0, 7.5, 18.0, 42.0]
    # Comparator: AAV gene therapy
    aav = [3.5, 5.0, 9.5, 16.5, 25.0, 60.0]
    # Comparator: ERT
    ert = [11.3, 12.3, 13.7, 15.0, 16.5, 18.5]

    ax.plot(years, nonvax_mrna, marker="o", color=NAVY, linewidth=2.5, label="mRNA 치료제 (비백신, 우리 타겟)")
    ax.plot(years, in_vivo_edit, marker="s", color=ORANGE, linewidth=2.0, label="In vivo gene editing")
    ax.plot(years, in_vivo_cart, marker="^", color=PURPLE, linewidth=2.0, label="In vivo CAR-T")
    ax.plot(years, aav, marker="d", color=TEAL, linewidth=2.0, label="AAV gene therapy (인접)", linestyle="--")
    ax.plot(years, ert, marker="v", color=GRAY, linewidth=2.0, label="ERT (성숙 비교)", linestyle="--")

    # Mark "0 approval" anchor
    ax.axhline(0.01, color="red", linewidth=1, alpha=0)
    ax.annotate("승인 0건 → 첫 승인 wave 2027-2030\n(lonvo-z BLA H2 2026)",
                xy=(2027, 8), xytext=(2027.5, 30),
                fontsize=9, ha="left", color=RED,
                arrowprops=dict(arrowstyle="->", color=RED, lw=1.5))

    ax.set_xlabel("연도")
    ax.set_ylabel("시장 규모 (USD B, 로그 스케일)")
    ax.set_title("그림 1. 시장 규모 전망: mRNA 치료제(비백신) vs 인접 modality (2025-2035)",
                 fontsize=11, fontweight="bold")
    ax.legend(loc="upper left", fontsize=9, framealpha=0.95)
    ax.grid(True, alpha=0.3, linestyle="--")
    ax.set_yscale("log")
    ax.set_ylim(0.4, 100)
    ax.set_xticks(years)
    plt.tight_layout()
    path = os.path.join(FIG_DIR, "fig1_market_projection.png")
    plt.savefig(path, dpi=130, bbox_inches="tight")
    plt.close()
    return path


def fig2_tissue_tropism():
    """LNP IV biodistribution showing % of dose by tissue."""
    fig, ax = plt.subplots(figsize=(9, 5), dpi=130)
    tissues = ["간 (Liver)", "비장 (Spleen)", "골수 (Bone marrow)", "폐 (Lung)",
               "심장 (Heart)", "근육 (Muscle)", "신장 (Kidney)", "CNS (Brain)"]
    pct_low = [70, 5, 1, 0.5, 0.3, 0.2, 0.5, 0.05]
    pct_high = [90, 15, 5, 2, 1.0, 1.0, 2.0, 0.1]
    colors_bars = [GREEN, TEAL, LIGHT_BLUE, ORANGE, RED, RED, RED, RED]

    x_pos = np.arange(len(tissues))
    width_bars = 0.6
    for x, low, high, c, t in zip(x_pos, pct_low, pct_high, colors_bars, tissues):
        ax.bar(x, high, width_bars, color=c, alpha=0.85, edgecolor="black", linewidth=0.8)
        ax.bar(x, low, width_bars, color=c, alpha=1.0, edgecolor="black", linewidth=0.8)
        ax.text(x, high + 1.5, f"{low}-{high}%", ha="center", fontsize=8.5, fontweight="bold")

    ax.set_xticks(x_pos)
    ax.set_xticklabels(tissues, rotation=20, ha="right", fontsize=9)
    ax.set_ylabel("표준 LNP IV 투여 시 dose 분포 (%)")
    ax.set_yscale("log")
    ax.set_ylim(0.01, 200)
    ax.set_title("그림 2. LNP IV 투여 시 조직별 생체분포 — 간 우점 (70-90%) 본질적 한계",
                 fontsize=11, fontweight="bold")

    # Add feasibility annotations
    ax.text(0, 130, "✓ 가능", ha="center", fontsize=10, color=GREEN, fontweight="bold")
    ax.text(2, 130, "✓ 가능", ha="center", fontsize=10, color=TEAL, fontweight="bold")
    ax.text(3, 130, "✗ 어려움", ha="center", fontsize=10, color=ORANGE, fontweight="bold")
    ax.text(5.5, 130, "✗ 본질적 불가능", ha="center", fontsize=10, color=RED, fontweight="bold")

    ax.grid(True, alpha=0.3, axis="y", which="both")
    plt.tight_layout()
    path = os.path.join(FIG_DIR, "fig2_tissue_tropism.png")
    plt.savefig(path, dpi=130, bbox_inches="tight")
    plt.close()
    return path


def fig3_feasibility_matrix():
    """Disease segment feasibility — 2D scatter: clinical evidence × technical feasibility."""
    fig, ax = plt.subplots(figsize=(11, 7), dpi=130)

    # (segment, technical_feasibility 1-5, clinical_evidence 1-5, category)
    segments = [
        ("HAE\n(lonvo-z)",                4.8, 5.0, "feasible", 800),
        ("ATTR amyloidosis\n(nex-z)",     4.5, 4.5, "feasible", 700),
        ("HoFH PCSK9\n(VERVE-102)",       4.3, 4.0, "feasible", 600),
        ("AATD\n(BEAM-302)",              4.3, 3.5, "feasible", 500),
        ("OTC deficiency\n(ARCT-810)",    4.0, 3.5, "feasible", 500),
        ("PA\n(mRNA-3927)",               3.8, 3.5, "feasible", 450),
        ("MMA\n(mRNA-3705)",              3.8, 3.0, "feasible", 400),
        ("Hemophilia A/B",                3.5, 2.0, "borderline", 350),
        ("In vivo CAR-T 자가면역",         3.2, 2.5, "feasible", 500),
        ("PKU",                           3.5, 2.0, "borderline", 300),
        ("Sickle Cell Disease (in vivo)", 2.5, 1.5, "borderline", 300),
        ("Cardiac VEGF\n(AZD8601)",       1.5, 1.0, "infeasible", 600),
        ("CFTR / CF\n(VX-522 종료)",       1.0, 1.0, "infeasible", 700),
        ("DMD / muscle",                  0.8, 0.5, "infeasible", 500),
        ("CNS rare neurometabolic",       0.5, 0.5, "infeasible", 600),
        ("ADPKD / kidney",                0.8, 0.5, "infeasible", 400),
    ]
    color_map = {"feasible": GREEN, "borderline": ORANGE, "infeasible": RED}
    label_map = {"feasible": "가능 (Phase 2-3+ evidence)", "borderline": "경계 (early/uncertain)", "infeasible": "불가능 (실패 또는 본질 차단)"}
    seen = set()
    for name, tf, ce, cat, s in segments:
        c = color_map[cat]
        lbl = label_map[cat] if cat not in seen else None
        seen.add(cat)
        ax.scatter(tf, ce, s=s, color=c, alpha=0.55, edgecolors="black", linewidth=1.0, zorder=3, label=lbl)
        ax.annotate(name, (tf, ce), fontsize=8, ha="center", va="center", fontweight="bold", zorder=4)

    ax.axhline(2.5, color="black", linewidth=0.8, alpha=0.5)
    ax.axvline(2.5, color="black", linewidth=0.8, alpha=0.5)
    ax.set_xlim(0, 5.5)
    ax.set_ylim(0, 5.5)
    ax.set_xlabel("기술 feasibility (LNP tropism + delivery)", fontsize=11)
    ax.set_ylabel("임상 evidence 수준 (Phase 단계)", fontsize=11)
    ax.set_xticks([1, 2, 3, 4, 5])
    ax.set_yticks([1, 2, 3, 4, 5])
    ax.set_yticklabels(["전임상", "Phase 1", "Phase 2", "Phase 3", "BLA/승인"])
    ax.set_title("그림 3. 질환 세그먼트 feasibility 매트릭스 — 사용자 핵심 질문 직접 답변",
                 fontsize=12, fontweight="bold")
    ax.legend(loc="upper left", fontsize=10, framealpha=0.95)
    ax.grid(True, alpha=0.3, linestyle="--")
    plt.tight_layout()
    path = os.path.join(FIG_DIR, "fig3_feasibility_matrix.png")
    plt.savefig(path, dpi=130, bbox_inches="tight")
    plt.close()
    return path


def fig4_root_cause_heatmap():
    """4-bucket root cause × application heatmap (불가능 영역 정확한 원인)."""
    applications = [
        "CFTR / 폐", "Cardiac VEGF", "CNS 신경대사", "DMD / 근육",
        "ADPKD / 신장", "Hemophilia (vs AAV)", "Hepatic ERT 영역",
        "in vivo gene editing 간", "in vivo CAR-T"
    ]
    buckets = ["Delivery\n(조직 tropism)", "Duration\n(발현/재투여)", "Cost\n(vs AAV/ERT)", "Safety\n(면역원성)"]
    # 0=문제없음, 1=경미, 2=중대, 3=치명적 / 본질차단
    data = np.array([
        [3, 1, 2, 2],  # CFTR
        [3, 2, 1, 1],  # Cardiac
        [3, 2, 1, 1],  # CNS
        [3, 2, 1, 1],  # DMD
        [3, 2, 1, 1],  # Kidney
        [1, 3, 3, 1],  # Hemophilia (vs AAV one-shot economics)
        [1, 2, 2, 2],  # Hepatic ERT
        [0, 0, 0, 2],  # In vivo gene editing 간 (one-shot, but off-target safety)
        [1, 0, 1, 1],  # In vivo CAR-T
    ])

    fig, ax = plt.subplots(figsize=(8.5, 6), dpi=130)
    cmap = plt.get_cmap("RdYlGn_r")
    im = ax.imshow(data, cmap=cmap, vmin=0, vmax=3, aspect="auto")

    ax.set_xticks(np.arange(len(buckets)))
    ax.set_xticklabels(buckets, fontsize=10)
    ax.set_yticks(np.arange(len(applications)))
    ax.set_yticklabels(applications, fontsize=10)
    labels = {0: "없음", 1: "경미", 2: "중대", 3: "본질 차단"}
    for i in range(data.shape[0]):
        for j in range(data.shape[1]):
            ax.text(j, i, labels[data[i, j]], ha="center", va="center",
                    color="white" if data[i, j] >= 2 else "black", fontsize=9, fontweight="bold")
    ax.set_title("그림 4. 불가능 영역 정확한 원인 — 4-bucket × 응용분야 매트릭스",
                 fontsize=11, fontweight="bold")
    cbar = plt.colorbar(im, ax=ax, ticks=[0, 1, 2, 3])
    cbar.ax.set_yticklabels(["없음", "경미", "중대", "본질차단"])
    plt.tight_layout()
    path = os.path.join(FIG_DIR, "fig4_root_cause_heatmap.png")
    plt.savefig(path, dpi=130, bbox_inches="tight")
    plt.close()
    return path


def fig5_ma_timeline():
    """Big Pharma M&A wave 2025-2026 timeline."""
    deals = [
        ("2025-01", "BioNTech ← CureVac\n$1.25B + $740M 합의", PURPLE),
        ("2025-04", "Verve VERVE-102\nLDL-C -53% (Ph1b)", GRAY),
        ("2025-06", "Lilly ← Verve\n$1.3B 인수", ORANGE),
        ("2025-07", "Alnylam-Moderna 합의\n(LNP, no payment)", LIGHT_BLUE),
        ("2025-08", "AbbVie ← Capstan\n$2.1B (in vivo CAR-T)", NAVY),
        ("2025-08", "HHS BARDA mRNA\n$500M 22건 종료", RED),
        ("2025-10", "BMS ← Orbital\n$1.5B (in vivo CAR-T)", NAVY),
        ("2025-10", "Intellia nex-z FDA hold\n(Grade 4 LFT)", RED),
        ("2026-02", "Lilly ← Orna/SAIL\n$2.4B (circRNA)", NAVY),
        ("2026-03", "Moderna-Arbutus\n$2.25B 합의", LIGHT_BLUE),
        ("2026-03", "Intellia nex-z\nFDA hold 해제", GREEN),
        ("2026-04", "★ lonvo-z Phase 3\n양성 — 첫 in vivo edit", GREEN),
    ]
    fig, ax = plt.subplots(figsize=(13, 5.5), dpi=130)
    y_positions = []
    for i, (date, label, color) in enumerate(deals):
        x = i
        y = 1 if i % 2 == 0 else -1
        y_positions.append(y)
        ax.scatter(x, 0, s=200, color=color, edgecolor="black", linewidth=1.2, zorder=3)
        ax.plot([x, x], [0, y * 0.5], color=color, linewidth=1.5, zorder=2)
        ax.text(x, y * 0.9, label, ha="center", va="center" if y > 0 else "center",
                fontsize=8.5, fontweight="bold",
                bbox=dict(boxstyle="round,pad=0.3", fc="white", ec=color, lw=1.2))
        ax.text(x, -0.15 if y > 0 else 0.15, date, ha="center",
                va="top" if y > 0 else "bottom", fontsize=8, color=color, fontweight="bold")

    ax.axhline(0, color="black", linewidth=2, zorder=1)
    ax.set_xlim(-0.7, len(deals) - 0.3)
    ax.set_ylim(-1.5, 1.5)
    ax.set_yticks([])
    ax.set_xticks([])
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_visible(False)
    ax.spines["bottom"].set_visible(False)
    ax.set_title("그림 5. 2025-2026 mRNA 치료제 핵심 이벤트 타임라인 (M&A · 임상 · 규제 · IP)",
                 fontsize=11, fontweight="bold", pad=15)
    plt.tight_layout()
    path = os.path.join(FIG_DIR, "fig5_ma_timeline.png")
    plt.savefig(path, dpi=130, bbox_inches="tight")
    plt.close()
    return path


def fig6_ip_timeline():
    """Key mRNA / LNP patent expiry timeline."""
    patents = [
        ("UPenn Karikó-Weissman\nUS 8,278,036 (modified nucleoside)", 2006, 2025, "공중영역 진입 ★ (PTA 시 ~2027)", PURPLE),
        ("UPenn Karikó-Weissman\nUS 8,748,089", 2008, 2028, "EU 잔존 (Moderna EP'949)", PURPLE),
        ("Arbutus/Genevant\nLNP onpattro family", 2008, 2028, "감염병만 \$2.25B 합의 후 라이선스", ORANGE),
        ("Arbutus/Genevant\n추가 LNP family", 2010, 2033, "비감염병 신규 진입자 차단", ORANGE),
        ("Acuitas ALC-0315\n(Pfizer/BioNTech)", 2017, 2037, "신규 진입자 in-license 필요", LIGHT_BLUE),
        ("Moderna SM-102\n자체 lipid", 2016, 2036, "자체 사용, 외부 라이선스 제한", NAVY),
        ("Alnylam cationic lipid\nUS 11,246,933", 2009, 2029, "Pfizer 1심 비침해 (2025-07-30)", RED),
        ("Karikó-Weissman 신규 변형\n(saRNA, circRNA — 회피 경로)", 2018, 2038, "IP 회피 옵션 (Arcturus/Orna)", GREEN),
    ]
    fig, ax = plt.subplots(figsize=(11.5, 6), dpi=130)
    y_pos = np.arange(len(patents))[::-1]
    for y, (name, start, end, note, color) in zip(y_pos, patents):
        ax.barh(y, end - start, left=start, color=color, alpha=0.8, edgecolor="black", linewidth=0.6)
        ax.text(end + 0.3, y, f"{end}", va="center", fontsize=8.5, fontweight="bold", color=color)
        ax.text(start - 0.3, y, note, va="center", ha="right", fontsize=7.5, color="#444")

    ax.set_yticks(y_pos)
    ax.set_yticklabels([p[0] for p in patents], fontsize=8.5)
    ax.set_xlabel("연도 (우선일 → 만료 추정)")
    ax.set_xlim(1995, 2045)
    ax.axvline(2026, color="red", linewidth=1.8, linestyle="--", alpha=0.7, label="현재 (2026-05)")
    ax.axvline(2028, color="green", linewidth=1.3, linestyle=":", alpha=0.7, label="Arbutus core 만료")
    ax.axvline(2033, color="purple", linewidth=1.3, linestyle=":", alpha=0.7, label="Arbutus thicket 해소")
    ax.set_title("그림 6. mRNA / LNP 핵심 특허 만료 Timeline — UPenn 진입 골든타임 + Arbutus 2028-2033",
                 fontsize=10.5, fontweight="bold")
    ax.legend(loc="lower right", fontsize=9)
    ax.grid(True, alpha=0.3, axis="x")
    plt.tight_layout()
    path = os.path.join(FIG_DIR, "fig6_ip_timeline.png")
    plt.savefig(path, dpi=130, bbox_inches="tight")
    plt.close()
    return path


def fig7_barrier_radar_3way():
    """Compare entry barriers: mRNA vs Peptiligase vs EndoS2 (3-platform series)."""
    axes_labels = ["기술 난이도", "특허 장벽", "표준/규제", "공급망", "인력/장비", "자본 요건", "시간 요건"]
    # From H sections
    mrna_v       = [4.5, 5.0, 4.0, 4.0, 4.0, 4.5, 4.0]   # 평균 4.07
    peptiligase_v= [3,   5,   4,   4,   3,   4,   4]      # 평균 4.0
    endos2_v     = [3,   5,   4,   4,   3,   3,   3]      # 평균 3.6 (EndoS2 was 上)

    angles = np.linspace(0, 2*np.pi, len(axes_labels), endpoint=False).tolist()
    angles += angles[:1]
    mrna_v += mrna_v[:1]
    peptiligase_v += peptiligase_v[:1]
    endos2_v += endos2_v[:1]

    fig, ax = plt.subplots(figsize=(8, 7), subplot_kw=dict(polar=True), dpi=130)
    ax.plot(angles, mrna_v, color=NAVY, linewidth=2.5, label="mRNA 치료제 (평균 4.07/5) ★ 최고")
    ax.fill(angles, mrna_v, color=NAVY, alpha=0.18)
    ax.plot(angles, peptiligase_v, color=ORANGE, linewidth=2, label="Peptiligase (평균 4.0/5)")
    ax.fill(angles, peptiligase_v, color=ORANGE, alpha=0.12)
    ax.plot(angles, endos2_v, color=TEAL, linewidth=2, label="EndoS2 (평균 3.6/5)")
    ax.fill(angles, endos2_v, color=TEAL, alpha=0.12)

    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(axes_labels, fontsize=10)
    ax.set_ylim(0, 5)
    ax.set_yticks([1, 2, 3, 4, 5])
    ax.set_yticklabels(["1", "2", "3", "4", "5"], fontsize=8)
    ax.set_title("그림 7. 진입장벽 7개 차원 — 3개 분석 비교 (mRNA = 가장 어려운 진입)",
                 fontsize=11, fontweight="bold", pad=20)
    ax.legend(loc="upper right", bbox_to_anchor=(1.35, 1.05), fontsize=9)
    ax.grid(True, alpha=0.4)
    plt.tight_layout()
    path = os.path.join(FIG_DIR, "fig7_barrier_radar.png")
    plt.savefig(path, dpi=130, bbox_inches="tight")
    plt.close()
    return path


def fig8_whitespace_2x2():
    fig, ax = plt.subplots(figsize=(9, 7), dpi=130)
    ws = [
        ("WS-1\nGene editing payload\nCDMO ★ 1순위",         3.5, 4.5, 850, NAVY),
        ("WS-2\nNon-PEG / tLNP IP\n라이선싱",                  4.0, 4.0, 700, ORANGE),
        ("WS-3\nT cell tLNP\n(in vivo CAR-T)",                 4.3, 4.5, 650, PURPLE),
        ("WS-4\nUltra-rare hepatic\nin-license",               3.5, 3.0, 500, TEAL),
        ("WS-5\ncircRNA + 한국 LNP\n(post-COVID 회복)",        3.8, 2.8, 450, LIGHT_BLUE),
        ("Drug Product\n자체 신약 ✗ 비권장",                    4.8, 4.2, 600, RED),
    ]
    for label, x, y, s, c in ws:
        ax.scatter(x, y, s=s, color=c, alpha=0.65, edgecolors="black", linewidth=1.2, zorder=3)
        ax.annotate(label, (x, y), fontsize=9, ha="center", va="center", fontweight="bold", zorder=4)

    ax.axhline(3, color="black", linewidth=0.8, alpha=0.5)
    ax.axvline(3, color="black", linewidth=0.8, alpha=0.5)
    ax.text(1.5, 4.7, "Q1: 기회 크고 장벽 낮음\n(우선 진입)", fontsize=9, ha="center", color="green", fontweight="bold",
            bbox=dict(boxstyle="round,pad=0.3", fc="lightgreen", alpha=0.3))
    ax.text(4.5, 4.7, "Q2: 기회 크고 장벽 높음\n(전략적 진입)", fontsize=9, ha="center", color="darkblue", fontweight="bold",
            bbox=dict(boxstyle="round,pad=0.3", fc="lightblue", alpha=0.3))
    ax.text(1.5, 1.3, "Q3: 기회 작고 장벽 낮음\n(보조 진입)", fontsize=9, ha="center", color="darkorange", fontweight="bold",
            bbox=dict(boxstyle="round,pad=0.3", fc="moccasin", alpha=0.3))
    ax.text(4.5, 1.3, "Q4: 기회 작고 장벽 높음\n(비권장)", fontsize=9, ha="center", color="darkred", fontweight="bold",
            bbox=dict(boxstyle="round,pad=0.3", fc="mistyrose", alpha=0.3))

    ax.set_xlabel("진입장벽 (1=낮음, 5=높음)", fontsize=11)
    ax.set_ylabel("시장 기회 (1=작음, 5=큼)", fontsize=11)
    ax.set_xlim(0.5, 5.5)
    ax.set_ylim(0.5, 5.5)
    ax.set_title("그림 8. White Space 2×2 매트릭스 — mRNA 치료제 신규 진입 후보", fontsize=11, fontweight="bold")
    ax.grid(True, alpha=0.3, linestyle="--")
    plt.tight_layout()
    path = os.path.join(FIG_DIR, "fig8_whitespace_2x2.png")
    plt.savefig(path, dpi=130, bbox_inches="tight")
    plt.close()
    return path


def fig9_valuechain():
    """mRNA value chain (Pillow)."""
    W, H = 1400, 540
    img = Image.new("RGB", (W, H), "white")
    draw = ImageDraw.Draw(img)
    try:
        font = ImageFont.truetype("/usr/share/fonts/truetype/nanum/NanumGothicBold.ttf", 18)
        font_small = ImageFont.truetype("/usr/share/fonts/truetype/nanum/NanumGothic.ttf", 13)
        font_title = ImageFont.truetype("/usr/share/fonts/truetype/nanum/NanumGothicBold.ttf", 22)
    except Exception:
        font = ImageFont.load_default()
        font_small = ImageFont.load_default()
        font_title = ImageFont.load_default()

    draw.text((W//2 - 260, 15), "그림 9. mRNA 치료제 밸류체인", fill=NAVY, font=font_title)

    boxes = [
        (40, 90, 220, 150, "#D6EAF8", "① mRNA 설계 / IP",
         ["• UPenn (Karikó-Weissman)", "• Moderna / BioNTech", "• circRNA: Orna→Lilly", "• saRNA: Arcturus"]),
        (300, 90, 220, 150, "#A9CCE3", "② IVT 효소 / Cap",
         ["• T7 RNAP (NEB/Aldevron)", "• TriLink CleanCap", "• Aldevron (Danaher)", "• ST Pharm"]),
        (560, 90, 220, 150, "#5DADE2", "③ LNP / Lipid",
         ["• Acuitas (ALC-0315)", "• Arbutus/Genevant", "• CordenPharma / Evonik", "• Croda / Avanti"]),
        (820, 90, 240, 150, "#2E86C1", "④ Fill/Finish / CDMO",
         ["• Catalent/Moderna", "• Aldevron", "• Lonza (Visp)", "• ST Pharm (KR)"]),
        (1100, 90, 260, 150, "#1A5276", "⑤ Drug Product / 임상",
         ["• Moderna (rare disease)", "• Intellia (in vivo edit)", "• Verve (Lilly)", "• Capstan (AbbVie)"]),
    ]
    for (x, y, w, h, color, title, lines) in boxes:
        draw.rectangle([x, y, x+w, y+h], fill=color, outline="black", width=2)
        text_color = "white" if color in ("#2E86C1", "#1A5276") else "black"
        draw.text((x+10, y+8), title, fill=text_color, font=font)
        for i, line in enumerate(lines):
            draw.text((x+12, y+38+i*22), line, fill=text_color, font=font_small)

    # Arrows
    arrow_y = 165
    for x_end in [285, 545, 805, 1085]:
        draw.line([(x_end - 25, arrow_y), (x_end - 5, arrow_y)], fill="black", width=3)
        draw.polygon([(x_end - 5, arrow_y - 7), (x_end - 5, arrow_y + 7), (x_end + 5, arrow_y)], fill="black")

    # Entry points
    draw.text((40, 285), "권장 진입 지점:", fill=RED, font=font)
    enter_points = [
        ("EP1: ② IVT/Cap + ④ Fill/Finish CDMO (Gene editing payload 특화, 5y $100-200M) ★ 1순위", 320),
        ("EP2: ③ LNP / Lipid (Non-PEG·tLNP IP 라이선싱, 5y $50-100M)", 350),
        ("EP3: ⑤ Drug Product (Asia rights in-licensing 1-2개 자산, 5y $50-150M, 조건부)", 380),
        ("비권장: ⑤ 자체 신약 풀스택 (5y $500M-1.5B, 임상 검증 lonvo-z 1건뿐, post-COVID 자금 환경 최악)", 410),
    ]
    for txt, y in enter_points:
        color = NAVY if "비권장" not in txt else GRAY
        draw.text((60, y), txt, fill=color, font=font_small)

    # Value pool
    draw.text((40, 460), "값풀(value pool) 추정:", fill="black", font=font)
    legend = [
        ("① mRNA 설계: IP 라이선스 + Moderna/BioNTech 통합", 0),
        ("② IVT/Cap: $200-400M", 380),
        ("③ LNP: $300-600M", 640),
        ("④ CDMO: $500M-1B (post-COVID 과잉)", 850),
    ]
    for txt, x in legend:
        draw.text((50 + x, 495), txt, fill="black", font=font_small)

    path = os.path.join(FIG_DIR, "fig9_valuechain.png")
    img.save(path)
    return path


# ==============================================================================
# Markdown -> docx helpers
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


def insert_figure(doc, path, caption, width_inches=6.4):
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
    run.font.size = Pt(15)
    run.font.bold = True

    doc.add_paragraph()
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run("— 가능 치료 영역 + 불가능 영역의 정확한 원인 규명 —")
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
        "본 보고서는 사용자의 핵심 질문 — **\"mRNA 기반 치료제 / 기능성 단백질 대체제(RNAi·백신 제외)가 "
        "어떤 영역에서 작동하는가? 불가능하다면 그 정확한 원인은 무엇인가?\"** — 에 대한 종합 답변이다. "
        "조사 일자 2026-05-22 기준으로 [A]~[G] 7개 리서치 에이전트 + [H] 종합 분석 + 독립 검증 에이전트가 작업하였다. "
        "8개 섹션 중 7개 ✅ 검증완료, 1개 ⚠️ 부분검증(UPenn 만료일 PTA 정정 권고), 0개 ❌ 검증실패로 **신뢰도 4.5/5 '고신뢰'** 등급."
    ))

    insert_figure(doc, fig_paths["fig1"],
                  "그림 1. 시장 규모 전망 — 비백신 mRNA 치료제 USD 5.3B(2025)→21.4B(2032), CAGR ~20%. "
                  "단 2026-05 기준 승인 0건. 출처: Persistence·Grand View·Mordor·IMARC 합성.")

    doc.add_heading("핵심 질문에 대한 직접 답변", level=2)

    p = doc.add_paragraph()
    run = p.add_run("작동 영역 (모두 \"간 표적\"으로 수렴)")
    run.bold = True
    run.font.size = Pt(11)
    run.font.color.rgb = RGBColor(GREEN[1:3] and 0x27, 0x7E and 0xAE, 0x60)

    feasible = [
        "**HAE in vivo CRISPR (Intellia lonvo-z)** — 2026-04-27 **Phase 3 HAELO 양성** (4중 1차 출처 검증). 발작 -87%. BLA H2 2026, US launch H1 2027. **세계 최초 in vivo gene editing 임상 검증.**",
        "**ATTR amyloidosis (Intellia nex-z)** — Phase 3 MAGNITUDE/MAGNITUDE-2 진행. 2025-10 Grade 4 LFT FDA hold → 2026-01·03 해제. Vutrisiran/Tafamidis 대비 단회투여 차별화.",
        "**Hepatic urea cycle / organic acidemia** — Arcturus ARCT-810 OTC Phase 2 RUF 29→43.7%, Moderna mRNA-3927(PA)·mRNA-3705(MMA) pivotal 단계. ERT 부재 영역 first-in-class.",
        "**HoFH PCSK9 base editing (Verve VERVE-102)** — Lilly $1.3B 인수(2025-06). LDL-C 평균 -53%, max -69%.",
        "**In vivo CAR-T 자가면역** — Capstan(AbbVie $2.1B 2025-08), MagicRNA SLE NEJM 2026 Phase 1 양성. 비간 응용 첫 검증.",
    ]
    for f in feasible:
        p = doc.add_paragraph(style="List Bullet")
        add_inline_runs(p, f)

    p = doc.add_paragraph()
    run = p.add_run("불가능 영역 — 4-bucket 정확한 원인")
    run.bold = True
    run.font.size = Pt(11)
    run.font.color.rgb = RGBColor(0xC0, 0x39, 0x2B)

    infeasible = [
        "**CFTR / Cystic fibrosis** — Translate Bio MRT5005 2021 efficacy 실패, Vertex VX-522 2025-05 폐 염증 tolerability 이슈로 종료. **본질 원인: LNP 폐 IV uptake <2% + 점액·inflammation 본질 차단 + Trikafta 90% cover로 unmet need 축소**.",
        "**Cardiac VEGF (AZD8601)** — AZ 2022 drop, Moderna 2023 drop. **본질 원인: CABG 동시 직접 주사 투여경로 비현실 + Phase 2a exploratory만 trend**.",
        "**CNS / Muscle / Kidney (rare neurometabolic, DMD, ADPKD)** — 임상 단계 mRNA 프로그램 전무. **본질 원인: LNP의 BBB(<0.1%)·근육·신장 tropism 실질적 부재 — AAV가 reference modality 점유**.",
        "**Hemophilia A/B (vs AAV)** — 기술 가능하나 **AAV one-shot 경제(Hemgenix $3.5M, Roctavian $2.9M) 대비 mRNA 평생 재투여 비용·면역원성 불리**.",
    ]
    for f in infeasible:
        p = doc.add_paragraph(style="List Bullet")
        add_inline_runs(p, f)

    insert_figure(doc, fig_paths["fig3"],
                  "그림 2. 질환 세그먼트 feasibility 매트릭스 (기술 feasibility × 임상 evidence). "
                  "녹색=가능 (Phase 2-3+), 주황=경계, 빨강=본질 불가능 또는 실패.")

    doc.add_heading("기타 핵심 결론", level=2)
    bullets = [
        "**진입장벽**: 7차원 평균 **4.07/5 (3개 분석 시리즈 중 가장 높음)**. LNP IP 5/5, 자본 4.5/5, 기술 4.5/5. UPenn Karikó-Weissman 본체 2025-08(PTA 시 2027 추정) 만료, Arbutus core 2028, thicket 해소 ~2033.",
        "**시장**: 비백신 mRNA 치료제 USD 5.3B(2025) → 21.4B(2032) CAGR ~20%. **승인 0건**. 첫 승인 wave 2027-2030 (lonvo-z 1순위).",
        "**Player**: Big Pharma 본격 진입 — Lilly-Verve $1.3B, AbbVie-Capstan $2.1B, Lilly-Orna $2.4B(circRNA), BioNTech-CureVac 합병. Moderna 시총 -94%, 인력 -10%. Gritstone 파산(2024-10).",
        "**IP**: UPenn 본체 만료 골든타임 + Arbutus 2026-03 $2.25B 합의(감염병만, 비감염병 진입자 여전히 차단). 신규 FTO 4.0-4.5/5.",
        "**규제·리스크**: 치료용 mRNA-specific FDA guidance 부재. HHS BARDA mRNA $500M 22건 종료(2025-08). Critical risk: anti-PEG/LNP ABC, null-mutation ADA, Cas9 off-target.",
        "**Top 3 권장 진입 지점 (Phased)**: **EP1 In vivo gene editing payload CDMO ($100-200M, 1순위)** → **EP2 Non-PEG/tLNP IP 라이선싱 ($50-100M)** → **EP3 Asia rights in-licensing 1-2개 자산 ($50-150M, 조건부)**. **자체 신약 풀스택 (S4, $500M-1.5B)은 비권장**.",
        "**EndoS2/Peptiligase 시리즈 대비**: mRNA = **가장 보수적 권고**. 승인약 0건, IP 압박 최대, post-COVID 자금 최악. Big Pharma도 R&D 축소 중 — 신규 진입자는 신약 회피하고 도구·시약·CDMO 위치가 합리적.",
    ]
    for b in bullets:
        p = doc.add_paragraph(style="List Bullet")
        add_inline_runs(p, b)

    doc.add_heading("최종 권고 한 줄", level=2)
    p = doc.add_paragraph()
    add_inline_runs(p, (
        "**간 표적에서만 작동(lonvo-z 첫 검증), 폐·CNS·근육·신장은 2030까지 본질 불가능**. "
        "신규 진입자에게는 **EP1 in vivo gene editing payload CDMO**가 최적 — "
        "EndoS2·Peptiligase 시리즈 통틀어 가장 신중한 진입 권고."
    ))

    doc.add_page_break()


def section_intro(doc, code, title, grade):
    doc.add_heading(f"[{code}] {title}", level=1)
    p = doc.add_paragraph()
    run = p.add_run(f"검증 등급: {grade}")
    run.bold = True
    run.font.size = Pt(11)
    run.font.color.rgb = RGBColor(0x2E, 0x7D, 0x32) if "✅" in grade else RGBColor(0xE6, 0x7E, 0x22)


def appendix(doc, fig_paths):
    doc.add_page_break()
    doc.add_heading("부록 A. 출처 목록 (Sources)", level=1)
    p = doc.add_paragraph()
    add_inline_runs(p, (
        "본문 내 (Source: URL, 발행일) 형식으로 인용된 모든 출처는 8개 마크다운 산출물에 포함되어 있다. 주요 1차 출처군:"
    ))
    primary_sources = [
        "**학술/특허**: Karikó-Weissman (UPenn, US 8,278,036 / US 8,748,089), Anderson (MIT LNP), Langer (Moderna). Google Patents 검증.",
        "**기업 IR**: Moderna, BioNTech, CureVac, Intellia, Verve, Capstan, Arcturus, Vertex, Translate Bio/Sanofi, AstraZeneca, Eli Lilly, AbbVie, BMS, Orna/SAIL, Beam, Tessera, Strand.",
        "**임상 1차**: ClinicalTrials.gov (NCT NTLA-2001, NTLA-2002, ARCT-810, mRNA-3927, mRNA-3705, VERVE-102), NEJM 2026 (MagicRNA SLE).",
        "**시장조사**: Persistence Market Research, Grand View, Mordor, Roots Analysis, IMARC, BCC, EvaluatePharma, GlobalData.",
        "**규제**: FDA Genome Editing guidance (2024-01), FDA NGS off-target draft (2026-04), EMA CAT, BIOSECURE Act FY26 NDAA (2025-12), HHS BARDA termination announcement (2025-08).",
        "**법률/IP 분석**: USPTO, Google Patents, Justia Federal Circuit, IPKat, Goodwin/Sidley/Foley analyses of Moderna v Arbutus / Alnylam suits.",
    ]
    for s in primary_sources:
        p = doc.add_paragraph(style="List Bullet")
        add_inline_runs(p, s)

    doc.add_heading("부록 B. 검증 로그 요약", level=1)
    rows = [
        ["섹션", "검증 등급", "검증 요지"],
        ["[A] 기술", "✅ 검증완료", "LNP 간 70-90% 정량, VERVE-102 LDL-C -53%~-69%, Intellia nex-z FDA hold 2025-10→해제 2026-03 — 4중 출처 일치"],
        ["[B] 시장", "✅ 검증완료", "비백신 mRNA USD 5.3B(2025)→21.4B(2032), 승인 0건, M&A wave $6.6B/7개월 — 독립 출처 일치"],
        ["[C] Player", "✅ 검증완료", "Lilly-Verve $1.3B, AbbVie-Capstan $2.1B, BioNTech-CureVac+$740M, Gritstone 파산, Sanofi mRNA 폐기 — 모두 1차 출처 확인"],
        ["[D] 응용분야", "✅ 검증완료", "lonvo-z Phase 3 2026-04-27 양성 (4중 출처 확인 ★), VX-522 종료, MRT5005 실패, AZD8601 drop — 핵심 binary claims 모두 검증"],
        ["[E] 특허/IP", "⚠️ 부분검증", "Moderna-Arbutus $2.25B(2026-03), Alnylam 1심 패배, CureVac-BioNTech 합병+$740M 모두 확인. UPenn US 8,278,036 만료 PTA 적용 시 2027-05-24 추정 — 정정 권고."],
        ["[F] 리스크/규제", "✅ 검증완료", "BIOSECURE 2025-12 서명, HHS BARDA mRNA $500M 22건 종료 2025-08, FDA Genome Editing guidance 2024-01, NGS off-target 2026-04 — 정확"],
        ["[G] 사업성", "✅ 검증완료", "Moderna 2025 매출 $1.9B(-42%) R&D -31%, post-COVID 시총 -94%, CDMO overcapacity — 다수 출처 일치"],
        ["[H] 진입장벽", "✅ 검증완료", "인용 facts 검증완료. EP1 gene editing payload CDMO 권고 논리 비약 없음. 4-bucket root cause 분석 본질 차단 vs 공학 과제 구분 명확."],
    ]
    add_table_to_doc(doc, rows)

    doc.add_heading("부록 C. 사용 시 유의사항", level=1)
    cautions = [
        "**Binary claim 검증**: 2026-05 기준 FDA/EMA 승인 mRNA 비백신 치료제 **0건** — 다중 출처 반증 0건. lonvo-z BLA(H2 2026) 결과가 modality validation의 1차 이벤트.",
        "**UPenn 특허 만료 보정**: US 8,278,036 명목 2025-08-23 만료지만 PTA(Patent Term Adjustment) 적용 시 ~2027-05-24까지 연장 가능. SPC/PTE 별도 확인 필수. 골든타임 큰 흐름은 유효하나 정확 일자는 IP 변호사 검토 필요.",
        "**Big Pharma 자본 흐름의 양면성**: 7개월 $6.6B M&A wave는 모달리티 확신 신호이지만, 동시에 Moderna R&D -31%·Sanofi mRNA 독감 폐기·Gritstone 파산은 platform 단독 사업 모델의 한계 신호. 신규 진입자는 어느 신호에 베팅하는지 명확해야 함.",
        "**시점 민감성**: 6개월 단위 재평가 권장. 핵심 이벤트 — lonvo-z BLA 제출(H2 2026), Moderna mRNA-3927 PA pivotal readout(2026), Verve VERVE-102 Phase 2(2026-2027), Beam BEAM-302 AATD pivotal, BIOSECURE 2032 deadline, Arbutus 만료 2028.",
        "**자사 capability에 따른 진입 모드 조정**: 본 보고서는 'platform IP 없는 중견 player' 가정. 자사가 (a) LNP / lipid chemistry capability, (b) GMP IVT 설비, (c) Big Pharma BD 채널 어떤 조합인지에 따라 EP1/EP2/EP3 우선순위 재평가 필수.",
        "**EndoS2 · Peptiligase 시리즈와의 비교**: 본 분석은 3개 보고서 중 가장 보수적. EndoS2는 platform 검증된 시장 진입 권고(Asia 통합), Peptiligase는 building block anchor 권고, mRNA는 신약 회피 + CDMO 권고. 자사 capability 적합성에 따라 시리즈 간 우선순위 검토 가능.",
    ]
    for c in cautions:
        p = doc.add_paragraph(style="List Bullet")
        add_inline_runs(p, c)


# ==============================================================================
# Main build
# ==============================================================================

def main():
    print("Generating figures...")
    fig_paths = {
        "fig1": fig1_market_projection(),
        "fig2": fig2_tissue_tropism(),
        "fig3": fig3_feasibility_matrix(),
        "fig4": fig4_root_cause_heatmap(),
        "fig5": fig5_ma_timeline(),
        "fig6": fig6_ip_timeline(),
        "fig7": fig7_barrier_radar_3way(),
        "fig8": fig8_whitespace_2x2(),
        "fig9": fig9_valuechain(),
    }
    for k, p in fig_paths.items():
        print(f"  {k}: {os.path.basename(p)} ({os.path.getsize(p)/1024:.1f} KB)")

    print("Building Word document...")
    doc = Document()
    set_styles(doc)
    cover_page(doc)

    doc.add_heading("목차 (Table of Contents)", level=1)
    add_table_of_contents(doc)
    p = doc.add_paragraph()
    run = p.add_run("※ MS Word에서 목차를 마우스 오른쪽 → '필드 업데이트' 또는 F9로 자동 생성.")
    run.italic = True
    run.font.size = Pt(9)
    run.font.color.rgb = RGBColor(0x80, 0x80, 0x80)
    doc.add_page_break()

    executive_summary(doc, fig_paths)

    # Use fire_once to prevent multiple matches on sub-headings
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
            "A.1.2 LNP": fire_once("fig2", lambda d: insert_figure(
                d, fig_paths["fig2"],
                "그림 2. LNP IV 투여 시 조직별 생체분포 — 표준 LNP는 70-90% 간으로, 폐 <2%·CNS <0.1%. "
                "이 분포가 mRNA 치료제 가능 영역과 불가능 영역을 결정짓는 본질적 한계."
            )),
            "A.3 기술적 난제": fire_once("fig4", lambda d: insert_figure(
                d, fig_paths["fig4"],
                "그림 4. 불가능 영역의 정확한 원인 — 4-bucket × 응용분야 매트릭스. "
                "CFTR·Cardiac·CNS·Muscle·Kidney는 Delivery에서 본질 차단 (빨강), "
                "in vivo gene editing 간은 Safety만 중대 관리 대상."
            )),
        },
        "B": {},
        "C": {
            "C.7 최근 M&A": fire_once("fig5", lambda d: insert_figure(
                d, fig_paths["fig5"],
                "그림 5. 2025-2026 mRNA 치료제 핵심 이벤트 타임라인 — Big Pharma M&A wave $6.6B/7개월, "
                "lonvo-z Phase 3 양성, FDA hold·해제, HHS BARDA 종료, IP 합의 모두 종합."
            )),
        },
        "D": {
            "D.1 질환 세그먼트": fire_once("fig3", lambda d: insert_figure(
                d, fig_paths["fig3"],
                "그림 3. 질환 세그먼트 feasibility 매트릭스 (★ 사용자 핵심 질문 답변). "
                "녹색=가능, 주황=경계, 빨강=본질 불가능."
            )),
        },
        "E": {
            "E.8 만료": fire_once("fig6", lambda d: insert_figure(
                d, fig_paths["fig6"],
                "그림 6. mRNA / LNP 핵심 특허 만료 Timeline — UPenn 본체 2025-08(PTA 시 2027) 만료 골든타임. "
                "Arbutus core 2028, thicket 해소 ~2033."
            )),
        },
        "F": {},
        "G": {
            "G.7 전략적": fire_once("fig9", lambda d: insert_figure(
                d, fig_paths["fig9"],
                "그림 9. mRNA 치료제 밸류체인 — 5단계 (mRNA 설계 → IVT·Cap → LNP → CDMO → Drug Product). "
                "권장 진입 지점 EP1-EP3 시각화."
            )),
        },
        "H": {
            "H.2 진입장벽": fire_once("fig7", lambda d: insert_figure(
                d, fig_paths["fig7"],
                "그림 7. 진입장벽 7개 차원 — 3개 보고서 시리즈 비교 (mRNA 4.07/5 = 최고 / Peptiligase 4.0 / EndoS2 3.6). "
                "mRNA는 모든 차원에서 동등 이상의 진입장벽."
            )),
            "H.4 종합 결론": fire_once("fig8", lambda d: insert_figure(
                d, fig_paths["fig8"],
                "그림 8. White Space 2×2 매트릭스 — WS-1 Gene editing payload CDMO가 Q1-Q2 경계 최우선. "
                "자체 신약 풀스택은 Q2 우측 비권장."
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

    appendix(doc, fig_paths)
    add_page_number(doc)
    doc.save(OUTPUT_PATH)
    size_kb = os.path.getsize(OUTPUT_PATH) / 1024
    print(f"\n✅ Word report saved: {OUTPUT_PATH} ({size_kb:.1f} KB)")


if __name__ == "__main__":
    main()
