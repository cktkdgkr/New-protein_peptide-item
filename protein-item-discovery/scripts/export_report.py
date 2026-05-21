"""Export Phase A~D results into a single Excel workbook and a Word report."""
import csv
from pathlib import Path

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
OUT_XLSX = ROOT / "reports" / "digest_20260521.xlsx"
OUT_DOCX = ROOT / "reports" / "digest_20260521.docx"

# ---------------------------------------------------------------------------
# Data
# ---------------------------------------------------------------------------

EXEC_SUMMARY = (
    "이번 회차는 단백질·펩타이드 의약 모달리티(SC 항체, ADC, AOC, radioligand, mRNA, GLP-1 peptide)의 "
    "시장 신호 18개를 수집하고, 그로부터 사업화 후보 14개를 도출해 6축 정량 스코어링한 뒤 short-list "
    "7개를 확정했다. 핵심 발견: 빅파마 모달리티 트렌드는 모두 항체·핵산·펩타이드의 결합(conjugation)·"
    "합성(ligation)·후처리(modification) 효소 수요로 수렴하며, 임상 부담 없는 process enzyme "
    "화이트스페이스가 가장 크다."
)

TOP3 = [
    ("1 (tie)", "Engineered mTG (ADC site-specific conjugation)", 4.20,
     "ADC $13.5B + Lonza Visp 2배 확장 + Hzymes가 'enzyme cost'를 산업 통설로 지적 → cost-down 변이체 직접 수요."),
    ("1 (tie)", "Peptiligase / OaAEP1 C247A (green peptide ligation)", 4.20,
     "Bachem·PolyPeptide GLP-1 캐파 2배 + Vinnova green chem + OaAEP1 C247A 140× 효율 입증 (PMC11607802)."),
    ("3", "Engineered RNA ligase (AOC/ASO splint-ligation)", 4.10,
     "Novartis–Avidity $12B AOC 인수 + Codexis ECO Synthesis 빅파마 첫 수주 = 시장 형성기 + 백색공간 가장 큼."),
]

# 18 demand signals
SIGNALS = [
    # (#, 카테고리, 신호, 출처, 태그, 기반 효소)
    (1, "빅파마 모달리티 트렌드",
     "SC(피하주사) 전환이 종양·면역 빅파마 표준 — BMS Opdivo SC EU 승인, argenx VYVGART SC EU, Roche Ocrevus·Tecentriq SC 동시 출시; Halozyme 2025 매출 $1.4B(+38%), 로열티 +52%",
     "prnewswire (Halozyme/BMS, argenx)",
     "[빅파마][CDMO]",
     "recombinant human hyaluronidase PH20 (rHuPH20) 및 변이체"),
    (2, "빅파마 모달리티 트렌드",
     "ADC 시장 $13.5B, 승인 15품목; Datroway 폐암 확장 등 차세대 linker·payload·conjugation 폭증",
     "bioworld.com 727478",
     "[빅파마]",
     "mTG (EC 2.3.2.13), Sortase A (EC 3.4.22.70), FGE (EC 1.8.3.7)"),
    (3, "빅파마 모달리티 트렌드",
     "TPD 빅파마 표준 자산화 — Arvinas/Pfizer ARV-471 NDA, Novartis–Monte Rosa $5.7B, AbbVie–Neomorph $1.64B 등 molecular glue 딜 연속",
     "biospectrumasia, bio-itworld",
     "[빅파마][딜]",
     "E3 ligase recombinant cocktail, deubiquitinase, E1/E2 효소 (PROTAC screening 시약, [추정])"),
    (4, "빅파마 모달리티 트렌드",
     "Radioconjugate 빅파마 진입 가속 — Novartis–PeptiDream $2.7B, Lilly–Aktis $1.1B, AstraZeneca–Fusion $2.4B",
     "fiercepharma, biospace",
     "[빅파마][딜]",
     "peptide-chelator site-specific ligase (subtiligase, OaAEP1, sortase variant), peptide amidation 효소"),
    (5, "M&A·라이선싱 딜",
     "Novartis–Avidity $12B 인수(2025.10) — AOC 플랫폼 확보(del-zota/DMD, del-desiran/DM1, del-brax/FSHD)",
     "bioanalysis-zone.com",
     "[딜][빅파마]",
     "항체-올리고 site-specific bioconjugation 효소, RNA/splint ligase, IdeS/IdeZ"),
    (6, "M&A·라이선싱 딜",
     "Gilead–Tubulis $3.15B 인수(2026.Q2 클로징) — ADC 차세대 linker·payload 플랫폼",
     "gilead.com",
     "[딜]",
     "mTG, sortase, FGE, EndoS2 glycosynthase 변이체"),
    (7, "M&A·라이선싱 딜",
     "Halozyme–Takeda vedolizumab(Entyvio) ENHANZE 라이선스(2025.12), Merus·Skye Bio 추가 계약",
     "prnewswire",
     "[딜][CDMO]",
     "rHuPH20 (PH20 hyaluronidase)"),
    (8, "M&A·라이선싱 딜",
     "Merck KEYTRUDA QLEX(SC) FDA 승인(2025.9) — Alteogen ALT-B4; Halozyme이 Merck 상대 특허 침해 소송",
     "yahoo finance, fiercepharma",
     "[딜][빅파마][규제]",
     "차세대 human hyaluronidase 변이체 (ALT-B4, MDASE 등)"),
    (9, "CDMO·플랫폼 동향",
     "Lonza Visp ADC bioconjugation 2배 확장(2028 가동, 2×1,200L, 200명 신규); enzymatic은 'enzyme cost' 이슈로 평가",
     "fiercepharma, hzymesbiotech",
     "[CDMO][공급망]",
     "enzymatic site-specific conjugation kit (mTG, sortase, FGE)"),
    (10, "CDMO·플랫폼 동향",
     "Bachem(Vista 1톤/yr SPPS) + PolyPeptide(말뫼 €100M 2배 확장 + Vinnova green GLP-1 펀딩 + Peptiligase/EnzyTag)",
     "bachem.com, dcatvci.org",
     "[CDMO][공급망]",
     "peptiligase, subtiligase, OaAEP1 C247A, butelase-1 variant"),
    (11, "CDMO·플랫폼 동향",
     "Codexis ECO Synthesis ligase 빅파마 첫 수주(2025 Q1), Merck 비희석 자금 계약",
     "SEC 8-K",
     "[CDMO][딜]",
     "engineered RNA/DNA ligase variants (oligonucleotide synthesis)"),
    (12, "학계·preprint",
     "RFdiffusion2(2025) 천연 효소 수준 catalytic proficiency, RFdiffusion3 오픈소스화(2025.12)",
     "ipd.uw.edu, genengnews",
     "[학계]",
     "de novo 설계 효소 (reagent grade 단기, process enzyme 중기)"),
    (13, "학계·preprint",
     "Engineered T7 RNAP 변이체(low-dsRNA, co-transcriptional capping, Mol Ther 2026); mRNA 600+ 임상 / IVT 효소 시장 $1.8B→$3.9B(2034)",
     "PMC12932865, dataintelo",
     "[학계][공급망]",
     "engineered T7 RNAP, capping enzyme 변이체, polyA polymerase, RNase H/III"),
    (14, "학계·preprint",
     "Prime editor 오류율 60× 감소 vPE Cas9 변이체 (MIT 2025.9)",
     "news.mit.edu",
     "[학계]",
     "vPE Cas9 변이체, MMLV-RT 변이체 (research·ex-vivo CGT manufacturing)"),
    (15, "학계·preprint",
     "OaAEP1 C247A 변이체 — butelase 대비 발현 용이 + 촉매효율 140× 개선",
     "PMC11607802",
     "[학계]",
     "OaAEP1 / butelase-1 variant (효소적 peptide ligation·환상화 차세대 표준)"),
    (16, "스타트업·VC",
     "Biomatter €6.5M, NSF $32M(Arzeda non-natural cofactor 효소 포함), AI-driven protein engineering 자금 유입",
     "synbiobeta, nsf.gov",
     "[스타트업]",
     "AI 설계 효소 일반 (non-natural cofactor 사용 process enzyme)"),
    (17, "스타트업·VC",
     "Radiopharma 스타트업 — Actithera $75.5M(2025 최대 시리즈 A), Nuclidium $98M 시리즈 B",
     "labiotech.eu",
     "[스타트업]",
     "peptide-chelator site-specific conjugation 효소, GMP peptide ligase ([추정])"),
    (18, "인접산업·규제·공급망",
     "Halozyme vs Merck Keytruda SC 특허 침해 소송 — 라이선싱 협상 결렬; SC 비용효과 분석 논문 등장",
     "fiercepharma, pearceip.law",
     "[규제][공급망][딜]",
     "non-PH20 hyaluronidase, leech hyaluronidase, chondroitinase variant ([추정])"),
]
# CRISPR Dx, IdeS, PETase, glycan QC are in the candidate list too — represented in mapping table separately

# 14 candidates - extracted from 02_candidates.md
CANDIDATES = [
    # id, 아이템, 효소클래스, 분류, 핵심신호(요약), 사업화시나리오, 잠재경쟁자, scope판정
    ("item_001",
     "Next-gen recombinant hyaluronidase for SC conversion",
     "hyaluronidase (EC 3.2.1.35), GH56 fold 또는 PL8 lyase",
     "제형변경 조력",
     "SC 전환 표준화 + Halozyme–Merck IP 분쟁 우회 수요",
     "빅파마·biosimilar 대상 SC co-formulation 라이선스 (ENHANZE/ALT-B4의 제3 대안)",
     "Halozyme, Alteogen, Sanofi/Argobio [추정]",
     "경계 — 결합제형 트랙으로 한정"),
    ("item_002",
     "Engineered microbial transglutaminase (mTG) for ADC",
     "aminoacyltransferase (EC 2.3.2.13), Streptomyces mobaraensis",
     "생산공정용 효소",
     "ADC $13.5B + Lonza Visp 2배 + Hzymes가 enzyme cost 지적",
     "ADC CDMO·biotech 대상 GMP enzyme kit + Q-tag 설계 + DAR 보증 라이선스",
     "Innate EFAT2, Ajinomoto AJICAP, Hzymes, Zedira",
     "명백 포함"),
    ("item_003",
     "Engineered Sortase A variant (Ca-independent, high-kcat)",
     "transpeptidase (EC 3.4.22.70), S. aureus 패밀리",
     "생산공정용 효소",
     "ADC 차세대 + Tubulis $3.15B + radioligand·AOC 다목적",
     "ADC·AOC·radioligand CDMO + radiopharma startup에 효소 + tag 설계 패키지",
     "NBE-Therapeutics SMAC(Boehringer), academic spin-out",
     "명백 포함"),
    ("item_004",
     "Formylglycine-Generating Enzyme (FGE) — aldehyde-tag dual-payload ADC",
     "sulfatase-modifying (EC 1.8.3.7), Cu monooxygenase",
     "생산공정용 효소",
     "Dual-payload·branched linker ADC 차별화",
     "ADC 디벨로퍼·CDMO에 FGE + aldehyde-tag 항체 설계 패키지",
     "Catalent SMARTag, R&D Systems FGE",
     "명백 포함"),
    ("item_005",
     "EndoS2 glycosynthase mutant (Fc glycan remodeling)",
     "endo-β-N-acetylglucosaminidase (EC 3.2.1.96), GH18, S. pyogenes",
     "생산공정용 효소",
     "Fc glycoengineering + biosimilar QC + ADCC 강화",
     "항체·ADC CDMO + biosimilar 개발사에 cGMP enzyme + donor sugar 공급",
     "Genovis, Synaffix(Lonza), NEB",
     "명백 포함"),
    ("item_006",
     "Engineered T7 RNA polymerase (low-dsRNA, co-trans capping)",
     "DNA-directed RNA polymerase (EC 2.7.7.6)",
     "생산공정용 효소",
     "mRNA 600+ 임상 / IVT 효소 $1.8B→$3.9B(2034)",
     "Moderna·Pfizer·BioNTech·CureVac + IVT 효소 supply에 cGMP T7 enzyme 직접 판매·라이선스",
     "NEB Hi-T7, Aldevron, Trilink, Thermo, Promega",
     "명백 포함"),
    ("item_007",
     "Engineered RNA ligase (splint-ligation, oligo·AOC 합성)",
     "RNA ligase (EC 6.5.1.3), T4 Rnl2 / RtcB",
     "생산공정용 효소",
     "Novartis–Avidity $12B + Codexis ECO Synthesis 빅파마 첫 수주",
     "올리고 CDMO·RNA 치료제사에 cGMP enzyme + 공정 라이선스",
     "Codexis ECO, NEB SplintR, Moderna in-house [추정]",
     "명백 포함"),
    ("item_008",
     "Peptiligase / OaAEP1 C247A — green peptide ligation",
     "asparaginyl endopeptidase (EC 3.4.22.-), butelase-1 family",
     "펩타이드 제조",
     "Bachem·PolyPeptide GLP-1 캐파 2배 + green chem + OaAEP1 C247A 140× 효율",
     "Bachem·PolyPeptide·Lonza Peptides·CordenPharma에 cGMP enzyme + 공정 라이선스",
     "EnzyPep(Fresenius Kabi/EnzyTag), Sumitomo/Genovis",
     "명백 포함"),
    ("item_009",
     "Engineered Peptide Amidating Enzyme (PAM, bifunctional)",
     "PHM (EC 1.14.17.3) + PAL (EC 4.3.2.5), bifunctional",
     "펩타이드 제조",
     "GLP-1·calcitonin·oxytocin·radioligand peptide C-amide 필수",
     "GLP-1 biosimilar + peptide CDMO + radioligand 제조사에 cGMP PAM 공급 (cGMP supplier 부재)",
     "Unigene(특허 만료), Strongbridge, Akzo Diosynth [추정]",
     "명백 포함"),
    ("item_010",
     "Engineered IdeS/IdeZ variant (FabRICATOR class)",
     "cysteine protease (EC 3.4.22.-), S. pyogenes/S. equi",
     "진단·연구·산업 의약 인접",
     "mAb/ADC/biosimilar QC + AAV redosing enabling",
     "QC lab·CDMO·CRO·bioanalytical 공급사에 cGMP IdeS/IdeZ kit + LC-MS 워크플로",
     "Genovis FabRICATOR/Z, Promega SmartEnzymes, NEB",
     "경계 — imlifidase 치료제는 out-of-scope; QC·연구 시나리오만"),
    ("item_011",
     "Recombinant PNGase F + sialyl·galactosyltransferase set (glycan QC)",
     "PNGase F (EC 3.5.1.52) + ST6Gal1·ST3Gal3 (EC 2.4.99.x) + β1,4-GalT (EC 2.4.1.38)",
     "진단·연구·산업 의약 인접",
     "Biosimilar N-glycan QC + NEB cGMP glycosidase 확장",
     "Biosimilar·ADC·항체 CDMO·QC lab에 enzyme set + 워크플로 공급",
     "NEB Rapid PNGase F, Genovis GlycINATOR, Agilent",
     "명백 포함"),
    ("item_012",
     "Next-gen Cas12/Cas13 + RPA recombinase·SSB (POC molecular Dx)",
     "RNA-guided nuclease (EC 3.1.-.-) + Bst pol + UvsX + gp32",
     "진단·연구·산업 의약 인접",
     "SHERLOCK COVID EUA + DETECTR HPV CE 99.3%",
     "POC Dx 개발사·진단 OEM(Roche, Abbott, BD)에 enzyme kit + 라이선스",
     "NEB Cas12/Cas13/Bst, TwistDx RPA, Mammoth·Sherlock IP",
     "명백 포함"),
    ("item_013",
     "High-fidelity Prime Editor enzyme set (vPE Cas9 + MMLV-RT)",
     "Cas9 nickase (EC 3.1.-.-) + MMLV-RT (EC 2.7.7.49)",
     "진단·연구·산업 의약 인접",
     "MIT 2025 vPE 60× 정밀도 + ex-vivo CGT 제조 시약",
     "연구용 시약 공급사(IDT, Aldevron) + ex-vivo CGT CDMO에 enzyme + pegRNA 설계 서비스",
     "Prime Medicine 특허, IDT Alt-R Cas9, Aldevron SpyFi",
     "경계 — research·ex-vivo만; in-vivo 치료제는 out-of-scope"),
    ("item_014",
     "AI-designed (RFdiffusion2/3) custom enzymes (reagent-grade)",
     "de novo designed (자연 fold 아님)",
     "진단·연구·산업 의약 인접",
     "RFdiffusion2/3 천연 수준 활성 + Biomatter·Arzeda VC 자금",
     "Custom enzyme as a service — 제약·진단·CDMO 고객 맞춤 설계 + GMP 발현 패키지",
     "Codexis CodeEvolver, Biomatter, Arzeda, Cradle, Enzymit, Generate",
     "명백 포함 (reagent·process 한정)"),
]

# Scoring rows from data/candidates.csv
SCORING = []
with open(ROOT / "data" / "candidates.csv", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        SCORING.append(row)

# Short-list 1-pagers (top 7)
SHORTLIST = [
    {
        "rank": "1 (tie)",
        "id": "item_002",
        "name": "Engineered microbial transglutaminase (mTG) for ADC site-specific conjugation",
        "definition": "Streptomyces mTG 변이체로 항체 LLQG-tag glutamine과 amine payload를 isopeptide 결합 → 균일 DAR2/4 ADC 효소적 제조.",
        "biz": "ADC CDMO (Lonza Visp, Samsung Bio, WuXi XDC, AGC, Catalent) 및 ADC biotech 대상 GMP enzyme kit + Q-tag 설계 가이드 + DAR 보증 라이선스. [추정] enzyme $5~15k/g, upfront $1~5M + 로열티 0.5~2%.",
        "score": {"M":5,"F":4,"R":5,"W":3,"IP":3,"T":4}, "weighted": 4.20,
        "risk": "Hzymes·Ajinomoto·Zedira의 cluster 특허 회피 필요; CDMO의 chemical→enzymatic 전환 가정 의존.",
        "next": "Lonza/Samsung Bio/WuXi XDC에 enzymatic conjugation 채택 의향 RFI; mTG cluster 특허 freedom-to-operate 분석.",
    },
    {
        "rank": "1 (tie)",
        "id": "item_008",
        "name": "Peptiligase / OaAEP1 C247A — green enzymatic peptide ligation",
        "definition": "Asparaginyl endopeptidase (butelase-1 family) variant — SPPS fragment 2~3개를 효소 ligation해 GLP-1·인슐린·radioligand peptide(32~40mer)를 저용매·고수율로 제조.",
        "biz": "Bachem, PolyPeptide, Lonza Peptides, CordenPharma, Sumitomo, GLP-1 biosimilar 개발사 대상 cGMP enzyme + 공정 라이선스 (EnzyTag/EnzyPep 대안). [추정] enzyme $2~10k/g, upfront $2~10M + kg당 로열티.",
        "score": {"M":5,"F":4,"R":5,"W":3,"IP":4,"T":3}, "weighted": 4.20,
        "risk": "EnzyPep peptiligase IP 청구항 회피 필요; cGMP 라이선스 셋업 3~4년.",
        "next": "OaAEP1 C247A vs EnzyPep peptiligase IP 비교; PolyPeptide/Bachem 파트너십 RFI.",
    },
    {
        "rank": "3",
        "id": "item_007",
        "name": "Engineered RNA ligase (splint-ligation, AOC/ASO 합성)",
        "definition": "T4 RNA ligase 2 (Rnl2) 또는 RtcB variant로 splint DNA 가이드 하에 oligo fragment를 결합 → 긴 siRNA/AOC를 fragment ligation으로 저비용 합성.",
        "biz": "올리고 CDMO(Nitto Avecia, GenScript, Bachem oligo, Cytiva)·RNA 치료제 개발사에 cGMP enzyme + ECO Synthesis 스타일 워크플로 라이선스. [추정] enzyme $3~12k/g, upfront $1~5M + g당 로열티.",
        "score": {"M":4,"F":4,"R":5,"W":4,"IP":4,"T":3}, "weighted": 4.10,
        "risk": "Codexis ECO 핵심 청구항 범위; AOC enzymatic 채택률 [추정] 의존.",
        "next": "Codexis ECO Synthesis 특허 청구항 분석; Novartis Avidity 인수 후 oligo CDMO RFI.",
    },
    {
        "rank": "4",
        "id": "item_006",
        "name": "Engineered T7 RNAP variant (low-dsRNA, co-trans capping)",
        "definition": "thumb·finger 변이로 abortive·dsRNA 부산물을 줄이고 co-transcriptional cap1 효율을 높인 directed-evolution T7 RNAP.",
        "biz": "600+ mRNA 임상 보유 Moderna, Pfizer, BioNTech, CureVac + IVT 효소 supply (Aldevron, Trilink, Maravai, Thermo, NEB)에 cGMP enzyme 직접 판매 또는 라이선스. [추정] enzyme $5~30k/g, 시장 $1.8B→$3.9B (2034).",
        "score": {"M":5,"F":4,"R":5,"W":2,"IP":3,"T":4}, "weighted": 4.05,
        "risk": "NEB/Aldevron/Trilink/Thermo/Promega 시장 매우 혼잡; academic 특허 다수.",
        "next": "T7 RNAP 차세대 변이체 IP 매핑; mRNA 빅파마 cGMP enzyme spec RFI.",
    },
    {
        "rank": "5 (tie)",
        "id": "item_003",
        "name": "Engineered Sortase A variant (Ca-independent, high-kcat)",
        "definition": "eSrtA 7M/2A-9 등 directed-evolution variant — Ca²⁺ 없이 LPETG motif와 oligoglycine을 isopeptide 결합 → ADC/AOC/radioligand peptide conjugation.",
        "biz": "ADC·AOC·radioligand CDMO + Actithera·Nuclidium 등 radiopharma 스타트업에 enzyme + tag 설계 컨설팅 패키지 (NBE SMAC 대안). [추정] enzyme $3~10k/g, upfront $0.5~3M + 로열티.",
        "score": {"M":4,"F":4,"R":5,"W":3,"IP":3,"T":4}, "weighted": 3.95,
        "risk": "eSrtA 7M academic IP 풍부 — 차세대 evolution 필수; NBE/Boehringer SMAC 경쟁.",
        "next": "차세대 Sortase IP whitespace 분석; radiopharma 스타트업 RFI.",
    },
    {
        "rank": "5 (tie)",
        "id": "item_005",
        "name": "EndoS2 glycosynthase mutant (Fc glycan remodel)",
        "definition": "S. pyogenes EndoS2 D184M 등 transglycosylation-enhanced glycosynthase — 항체 N297 glycan trim → 균일 G2/G2S2/afucosylated G2 결합 (ADCC 강화, biosimilar 균질화).",
        "biz": "항체·ADC CDMO + Fc engineering biotech + biosimilar 개발사(Celltrion, Sandoz)에 cGMP enzyme + oxazoline donor 패키지 (GlycoConnect 대안). [추정] enzyme $5~15k/g + donor $2~10k/g + upfront $1~3M.",
        "score": {"M":4,"F":4,"R":5,"W":3,"IP":3,"T":4}, "weighted": 3.95,
        "risk": "Genovis·Synaffix·NEB 시장 점유; donor sugar 공급망 구축 필요.",
        "next": "EndoS2 변이체 IP 매핑; biosimilar 개발사(Celltrion 등) glycoform 균질화 수요 RFI.",
    },
    {
        "rank": "7",
        "id": "item_009",
        "name": "Engineered Peptide Amidating Enzyme (PAM, bifunctional)",
        "definition": "PHM (Cu monooxygenase) + PAL (lyase) bifunctional 재조합 효소 — peptide-Gly의 C-terminal glycine을 α-amide로 전환 (GLP-1·calcitonin·oxytocin·radioligand peptide 활성 필수 modification).",
        "biz": "GLP-1 biosimilar + peptide CDMO + radioligand peptide 제조사에 cGMP recombinant PAM 직접 공급. cGMP supplier 사실상 부재 — 화이트스페이스 가장 깨끗. [추정] enzyme $10~50k/g, upfront $1~5M.",
        "score": {"M":4,"F":2,"R":5,"W":5,"IP":4,"T":2}, "weighted": 3.75,
        "risk": "Cu·ascorbate 진핵 발현·capex 큼; cGMP 셋업 4~5년.",
        "next": "Unigene/BELLUS PAM 특허 만료 상태 확인; GMP 발현(P. pastoris/CHO) capex 추정.",
    },
]

NEXT_ROUND = {
    "search_areas": [
        "TPD E3 ligase / E1 / E2 / deubiquitinase 시약 시장 — PROTAC screening 효소 시장 규모·CRO 채택 신호 보강.",
        "Radioligand peptide-chelator 효소적 conjugation — GMP enzymatic 채택 가능성을 PeptiDream·Aktis·Fusion 공정 발표에서 추적.",
        "mRNA 보조 효소 — capping enzyme(vaccinia/faustovirus), polyA polymerase, RNase H/III 정제용 변이체의 cGMP 시장 신호.",
        "non-PH20 hyaluronidase — leech-derived, chondroitinase 변이체, 세균 hyaluronate lyase의 SC 확산 잠재력 검증.",
        "PETase·MHETase·cutinase의 의약품 PET 포장재 ESG 적용 — direct 의약 인접성 추가 검증.",
    ],
    "verifications": [
        "mTG/Sortase/EndoS2의 GMP CDMO RFI (Lonza, Samsung Bio, WuXi XDC) — 실제 enzymatic conjugation 채택 의향.",
        "OaAEP1 C247A vs EnzyPep peptiligase IP claim 비교, freedom-to-operate.",
        "Codexis ECO Synthesis 핵심 특허 청구항 범위 분석.",
        "Unigene·BELLUS PAM 특허 만료 상태 + GMP 발현 capex 추정.",
    ],
    "deep_dives": [
        "item_004 FGE (rank 8) — dual-payload ADC 상용화 신호 강해지면 우선 격상.",
        "item_001 hyaluronidase (rank 12) — Halozyme–Merck IP 분쟁 결과·non-PH20 IP-우회 가능성 보강 후 재검토.",
        "item_014 AI-designed enzyme (rank 13) — RFdiffusion3 오픈소스화 후 customer case 6~12개월 누적 후 재검토.",
        "신규: TPD-related E3 ligase recombinant cocktail / deubiquitinase 시약 (Phase B 보류 → Phase A 재스캔 후 후보화).",
        "신규: PETase / MHETase 의약품 포장재 ESG 시나리오 (Phase B 보류).",
    ],
}

RISKS = [
    ("데이터 부족", "[추정] 태그 다수 — T7 RNAP 시장 $3.9B(2034) 단일 출처, hyaluronidase non-PH20 효능, AOC enzymatic 채택률, GMP peptide ligase·PAM 수요 추정 근거 약함."),
    ("경계 사례", "item_001 hyaluronidase (결합제형 트랙), item_010 IdeS (imlifidase 치료제 존재; QC·연구만), item_013 prime editor (in-vivo 치료제 분리; research·ex-vivo만)."),
    ("가정 의존", "mTG/Sortase/EndoS2 변이체 시장 채택은 ADC CDMO의 enzymatic conjugation 전환 가속 가정 필요 (현재 chemical 우세); 가격 가정 GMP enzyme $5~30k/g 다수 [추정]."),
    ("IP 분쟁 시그널", "Halozyme vs Merck (Keytruda SC), Codexis ECO 핵심 청구항, NBE/Boehringer SMAC, EnzyPep peptiligase — 모두 freedom-to-operate 분석 선행 필요."),
    ("누락 가능성", "Phase A 18개 신호 중 TPD E3 ligase 시약·PETase는 Phase B에서 제외 — 다음 회차 재검토 권장."),
]

# ---------------------------------------------------------------------------
# Excel
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


def build_excel():
    wb = Workbook()
    # ----- Sheet 1: 요약 -----
    ws = wb.active
    ws.title = "1.요약"
    ws["A1"] = "Protein/Peptide Item Discovery — Digest 2026-05-21"
    ws["A1"].font = Font(name="맑은 고딕", bold=True, size=16, color="1F4E78")
    ws.row_dimensions[1].height = 28
    ws["A2"] = "run_id: 20260521-A   |   scope SSOT: therapeutic API 자체 제외, 공정·제형·진단·연구·산업 효소 포함"
    ws["A2"].font = Font(name="맑은 고딕", italic=True, size=10, color="595959")
    ws["A4"] = "▣ Executive Summary"
    ws["A4"].font = SUBHEAD_FONT
    ws.merge_cells("A5:F8")
    ws["A5"] = EXEC_SUMMARY
    ws["A5"].alignment = WRAP
    ws["A5"].font = BODY_FONT

    ws["A10"] = "▣ Top 3 Short-list"
    ws["A10"].font = SUBHEAD_FONT
    headers = ["순위", "아이템", "가중합", "한 줄 추천 사유"]
    for i, h in enumerate(headers, start=1):
        ws.cell(row=11, column=i, value=h)
    style_header_row(ws, 11, len(headers))
    for r, (rank, name, ws_score, why) in enumerate(TOP3, start=12):
        ws.cell(row=r, column=1, value=rank)
        ws.cell(row=r, column=2, value=name)
        ws.cell(row=r, column=3, value=ws_score)
        ws.cell(row=r, column=4, value=why)
        apply_body_style(ws, r, 4, fill=SHORTLIST_FILL)
        ws.row_dimensions[r].height = 48

    ws["A17"] = "▣ 6축 평균 (전체 14개)"
    ws["A17"].font = SUBHEAD_FONT
    axis_headers = ["축", "평균", "패턴"]
    for i, h in enumerate(axis_headers, start=1):
        ws.cell(row=18, column=i, value=h)
    style_header_row(ws, 18, len(axis_headers))
    axis_rows = [
        ("M (market)", 3.79, "시장 신호 전반적으로 강함 (Phase A 18개 신호 효과)"),
        ("F (feasibility)", 3.43, "미생물·E. coli 효소는 4점대, 진핵 발현(PAM·AI) 2점대 양극화"),
        ("R (regulatory)", 4.50, "SSOT(임상 API 제외) 효과로 평균 매우 높음 — process enzyme 5점 다수"),
        ("W (whitespace)", 3.00, "가장 약한 축 — 대부분 분야에 강한 기존 supplier 존재"),
        ("IP (defensibility)", 3.21, "academic IP·기존 cluster 특허 회피가 공통 숙제"),
        ("T (time-to-revenue)", 3.21, "kit 2~3년 vs cGMP 라이선스 4~5년 양극화"),
    ]
    for r, row_data in enumerate(axis_rows, start=19):
        for c, v in enumerate(row_data, start=1):
            ws.cell(row=r, column=c, value=v)
        apply_body_style(ws, r, 3)

    set_col_widths(ws, [12, 42, 10, 60, 5, 5])

    # ----- Sheet 2: 시장신호 18개 -----
    ws2 = wb.create_sheet("2.시장신호18")
    cols = ["#", "카테고리", "demand signal", "출처", "태그", "기반 효소·단백질"]
    for i, h in enumerate(cols, start=1):
        ws2.cell(row=1, column=i, value=h)
    style_header_row(ws2, 1, len(cols))
    for r, row in enumerate(SIGNALS, start=2):
        for c, v in enumerate(row, start=1):
            ws2.cell(row=r, column=c, value=v)
        apply_body_style(ws2, r, len(cols))
        ws2.row_dimensions[r].height = 60
    set_col_widths(ws2, [5, 18, 65, 28, 18, 45])
    ws2.freeze_panes = "A2"

    # ----- Sheet 3: 후보 long-list 14개 -----
    ws3 = wb.create_sheet("3.후보14개")
    cols = ["id", "아이템", "효소 클래스", "포함기준 분류", "핵심 신호", "사업화 시나리오", "잠재 경쟁자", "scope 판정"]
    for i, h in enumerate(cols, start=1):
        ws3.cell(row=1, column=i, value=h)
    style_header_row(ws3, 1, len(cols))
    shortlist_ids = {row["id"] for row in SCORING if row["shortlist"] == "1"}
    for r, row in enumerate(CANDIDATES, start=2):
        for c, v in enumerate(row, start=1):
            ws3.cell(row=r, column=c, value=v)
        fill = SHORTLIST_FILL if row[0] in shortlist_ids else None
        apply_body_style(ws3, r, len(cols), fill=fill)
        ws3.row_dimensions[r].height = 70
    set_col_widths(ws3, [10, 36, 32, 18, 38, 50, 32, 32])
    ws3.freeze_panes = "A2"

    # ----- Sheet 4: 스코어링 -----
    ws4 = wb.create_sheet("4.스코어링")
    cols = ["id", "아이템", "분류", "M (0.25)", "F (0.20)", "R (0.20)", "W (0.15)", "IP (0.10)", "T (0.10)",
            "가중합", "rank", "short-list"]
    for i, h in enumerate(cols, start=1):
        ws4.cell(row=1, column=i, value=h)
    style_header_row(ws4, 1, len(cols))
    sorted_rows = sorted(SCORING, key=lambda r: int(r["rank"]))
    for r, row in enumerate(sorted_rows, start=2):
        ws4.cell(row=r, column=1, value=row["id"])
        ws4.cell(row=r, column=2, value=row["item_name"])
        ws4.cell(row=r, column=3, value=row["inclusion_bucket"])
        for c, k in enumerate(["market","feasibility","regulatory","whitespace","ip","time"], start=4):
            s = int(row[k])
            cell = ws4.cell(row=r, column=c, value=s)
            cell.alignment = CENTER
            cell.font = Font(name="맑은 고딕", size=10, bold=True)
            cell.fill = SCORE_FILLS[s]
            cell.border = BORDER
        cell = ws4.cell(row=r, column=10, value=float(row["weighted_score"]))
        cell.alignment = CENTER
        cell.font = Font(name="맑은 고딕", size=10, bold=True)
        cell.border = BORDER
        cell.number_format = "0.00"
        cell = ws4.cell(row=r, column=11, value=int(row["rank"]))
        cell.alignment = CENTER
        cell.font = BODY_FONT
        cell.border = BORDER
        cell = ws4.cell(row=r, column=12, value="✓" if row["shortlist"] == "1" else "")
        cell.alignment = CENTER
        cell.font = Font(name="맑은 고딕", size=12, bold=True, color="C00000")
        cell.border = BORDER
        ws4.cell(row=r, column=1).font = BODY_FONT
        ws4.cell(row=r, column=2).font = BODY_FONT
        ws4.cell(row=r, column=3).font = BODY_FONT
        ws4.cell(row=r, column=1).alignment = WRAP
        ws4.cell(row=r, column=2).alignment = WRAP
        ws4.cell(row=r, column=3).alignment = WRAP
        ws4.cell(row=r, column=1).border = BORDER
        ws4.cell(row=r, column=2).border = BORDER
        ws4.cell(row=r, column=3).border = BORDER
        if row["shortlist"] == "1":
            for cc in (1,2,3,10,11,12):
                cell = ws4.cell(row=r, column=cc)
                if cell.fill.fgColor.rgb in (None, "00000000"):
                    cell.fill = SHORTLIST_FILL
        ws4.row_dimensions[r].height = 38
    set_col_widths(ws4, [10, 50, 22, 9, 9, 9, 9, 9, 9, 9, 7, 10])
    ws4.freeze_panes = "C2"
    # 가중치·산식 메모
    note_row = len(sorted_rows) + 4
    ws4.cell(row=note_row, column=1, value="가중치 / 산식 / 색상").font = SUBHEAD_FONT
    notes = [
        "가중치: Market 0.25 / Feasibility 0.20 / Regulatory 0.20 / Whitespace 0.15 / IP 0.10 / Time 0.10",
        "weighted_score = Σ(score_i × weight_i), 5점 만점",
        "Short-list: 가중합 상위 5위 + 6·7위가 5위와 0.20 이내 → 7개 선정",
        "셀 색: 5 (진녹) → 4 (연녹) → 3 (노랑) → 2 (주황) → 1 (빨강)",
    ]
    for i, n in enumerate(notes, start=1):
        ws4.cell(row=note_row + i, column=1, value=n).font = BODY_FONT
        ws4.merge_cells(start_row=note_row + i, start_column=1, end_row=note_row + i, end_column=12)

    # ----- Sheet 5: Short-list 상세 7개 -----
    ws5 = wb.create_sheet("5.ShortList상세")
    cols = ["rank", "id", "아이템", "정의", "사업화 시나리오", "M", "F", "R", "W", "IP", "T",
            "가중합", "위험·미지수", "다음 액션"]
    for i, h in enumerate(cols, start=1):
        ws5.cell(row=1, column=i, value=h)
    style_header_row(ws5, 1, len(cols))
    for r, item in enumerate(SHORTLIST, start=2):
        ws5.cell(row=r, column=1, value=item["rank"])
        ws5.cell(row=r, column=2, value=item["id"])
        ws5.cell(row=r, column=3, value=item["name"])
        ws5.cell(row=r, column=4, value=item["definition"])
        ws5.cell(row=r, column=5, value=item["biz"])
        for c, k in enumerate(["M","F","R","W","IP","T"], start=6):
            s = item["score"][k]
            cell = ws5.cell(row=r, column=c, value=s)
            cell.alignment = CENTER
            cell.font = Font(name="맑은 고딕", size=10, bold=True)
            cell.fill = SCORE_FILLS[s]
            cell.border = BORDER
        cell = ws5.cell(row=r, column=12, value=item["weighted"])
        cell.alignment = CENTER
        cell.font = Font(name="맑은 고딕", size=10, bold=True)
        cell.number_format = "0.00"
        cell.border = BORDER
        ws5.cell(row=r, column=13, value=item["risk"])
        ws5.cell(row=r, column=14, value=item["next"])
        for c in (1,2,3,4,5,13,14):
            cell = ws5.cell(row=r, column=c)
            cell.font = BODY_FONT
            cell.alignment = WRAP
            cell.border = BORDER
            cell.fill = SHORTLIST_FILL
        ws5.row_dimensions[r].height = 120
    set_col_widths(ws5, [10, 10, 36, 50, 60, 5, 5, 5, 5, 5, 5, 8, 38, 38])
    ws5.freeze_panes = "C2"

    # ----- Sheet 6: 위험 + 다음 회차 -----
    ws6 = wb.create_sheet("6.위험·다음회차")
    ws6["A1"] = "▣ 5. 위험·미지수"
    ws6["A1"].font = SUBHEAD_FONT
    for i, h in enumerate(["영역", "내용"], start=1):
        ws6.cell(row=2, column=i, value=h)
    style_header_row(ws6, 2, 2)
    for r, (area, content) in enumerate(RISKS, start=3):
        ws6.cell(row=r, column=1, value=area)
        ws6.cell(row=r, column=2, value=content)
        apply_body_style(ws6, r, 2)
        ws6.row_dimensions[r].height = 60

    next_start = len(RISKS) + 5
    ws6.cell(row=next_start, column=1, value="▣ 6. 다음 회차 제안").font = SUBHEAD_FONT
    sec_rows = [("보강 검색 영역", NEXT_ROUND["search_areas"]),
                ("추가 검증 항목", NEXT_ROUND["verifications"]),
                ("다음 deep-dive 후보", NEXT_ROUND["deep_dives"])]
    r = next_start + 1
    for label, items in sec_rows:
        ws6.cell(row=r, column=1, value=label).font = Font(name="맑은 고딕", bold=True, size=11, color="1F4E78")
        ws6.cell(row=r, column=1).fill = SUBHEAD_FILL
        ws6.cell(row=r, column=1).alignment = CENTER
        ws6.cell(row=r, column=1).border = BORDER
        ws6.cell(row=r, column=2).fill = SUBHEAD_FILL
        ws6.cell(row=r, column=2).border = BORDER
        ws6.merge_cells(start_row=r, start_column=2, end_row=r, end_column=2)
        r += 1
        for it in items:
            ws6.cell(row=r, column=1, value="•")
            ws6.cell(row=r, column=2, value=it)
            apply_body_style(ws6, r, 2)
            ws6.cell(row=r, column=1).alignment = CENTER
            ws6.row_dimensions[r].height = 36
            r += 1
        r += 1

    set_col_widths(ws6, [22, 110])

    # ----- Sheet 7: 메타 -----
    ws7 = wb.create_sheet("7.메타")
    meta_rows = [
        ("run_id", "20260521-A"),
        ("실행일", "2026-05-21 (UTC)"),
        ("Phase A 완료", "2026-05-21 05:08 UTC — 18 demand signal (우선 11 / 확장 7)"),
        ("Phase B 완료", "2026-05-21 05:42 UTC — 14 candidates (공정 6/제형 1/진단·연구 5/펩타이드 2)"),
        ("Phase C 완료", "2026-05-21 06:15 UTC — 6축 스코어링, short-list 7 (top5 + 0.2 이내 6·7위)"),
        ("Phase D 완료", "2026-05-21 — Executive digest 작성"),
        ("재시도", "없음 (A→B→C→D 1회 통과)"),
        ("주요 한계",
         "(1) 시장 사이즈 수치 다수 [추정]. (2) TPD E3 ligase·PETase는 Phase B에서 제외(다음 회차). "
         "(3) 경계 사례 3건은 한정 시나리오로만 포함. (4) freedom-to-operate IP 분석은 후속 deep-dive."),
        ("입력 파일",
         "pipeline/01_landscape_scan.md, pipeline/02_candidates.md, pipeline/03_scored.md, "
         "data/candidates.csv, candidates/item_{002,003,005,006,007,008,009}_*.md, state/run_state.json"),
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
        ws7.row_dimensions[r].height = 32
    set_col_widths(ws7, [18, 100])

    wb.save(OUT_XLSX)


# ---------------------------------------------------------------------------
# Word
# ---------------------------------------------------------------------------

def set_cell_bg(cell, hex_color):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement("w:shd")
    shd.set(qn("w:val"), "clear")
    shd.set(qn("w:color"), "auto")
    shd.set(qn("w:fill"), hex_color)
    tcPr.append(shd)


def add_table(doc, headers, rows, col_widths_cm=None, header_bg="1F4E78", header_color=RGBColor(0xFF,0xFF,0xFF), row_bgs=None):
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
    return "█" * score + "░" * (5 - score) + f" {score}/5"


def build_word():
    doc = Document()

    # Page margins
    for section in doc.sections:
        section.left_margin = Cm(2.0)
        section.right_margin = Cm(2.0)
        section.top_margin = Cm(2.0)
        section.bottom_margin = Cm(2.0)

    # Title
    add_heading(doc, "Protein / Peptide Item Discovery — Digest 2026-05-21", level=0)
    add_para(doc, "run_id: 20260521-A   |   scope SSOT: therapeutic API 자체 제외, 공정·제형·진단·연구·산업 효소 포함",
             size=9.5, italic=True)

    # 1. Executive Summary
    add_heading(doc, "1. 한 페이지 요약 (Executive Summary)")
    add_para(doc, EXEC_SUMMARY)

    add_heading(doc, "Top 3 Short-list", level=2)
    add_table(
        doc,
        headers=["순위", "아이템", "가중합", "한 줄 추천 사유"],
        rows=[(r, n, f"{s:.2f}", w) for r, n, s, w in TOP3],
        col_widths_cm=[1.6, 6.0, 1.4, 8.0],
        row_bgs=["FFF2CC"] * len(TOP3),
    )

    # 2. Market signals
    add_heading(doc, "2. 핵심 시장 신호 (Landscape Top 5)")
    top5 = [
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
    add_table(
        doc,
        headers=["#", "신호", "출처", "함의"],
        rows=top5,
        col_widths_cm=[0.8, 7.5, 2.8, 5.9],
    )
    add_para(doc,
             "보조 신호: TPD 빅파마 자산화, radioligand 빅파마 진입, RFdiffusion2/3 de novo 효소, "
             "vPE prime editor 60× 정밀도, SHERLOCK/DETECTR 임상 진입.",
             size=9, italic=True)

    # 3. Candidate Long-list
    add_heading(doc, "3. 후보 Long-list (14개)")
    rows = []
    bgs = []
    sl_ids = {row["id"] for row in SCORING if row["shortlist"] == "1"}
    for cid, name, eclass, bucket, signal, _biz, _comp, _scope in CANDIDATES:
        rows.append((cid, name, bucket, signal))
        bgs.append("FFF2CC" if cid in sl_ids else None)
    add_table(
        doc,
        headers=["id", "아이템", "분류", "핵심 신호"],
        rows=rows,
        col_widths_cm=[1.6, 6.5, 2.6, 6.3],
        row_bgs=bgs,
    )
    add_para(doc, "노란색 행 = short-list 7개", size=9, italic=True)

    # 4. Scoring summary
    add_heading(doc, "4. 6축 스코어링 결과")
    add_para(doc, "가중치: M 0.25 / F 0.20 / R 0.20 / W 0.15 / IP 0.10 / T 0.10. 가중합 5점 만점.",
             size=10, italic=True)
    sorted_sc = sorted(SCORING, key=lambda r: int(r["rank"]))
    score_rows = []
    score_bgs = []
    for row in sorted_sc:
        score_rows.append((
            row["rank"],
            row["id"],
            row["item_name"][:40] + ("…" if len(row["item_name"]) > 40 else ""),
            row["market"], row["feasibility"], row["regulatory"],
            row["whitespace"], row["ip"], row["time"],
            f"{float(row['weighted_score']):.2f}",
            "✓" if row["shortlist"] == "1" else "",
        ))
        score_bgs.append("FFF2CC" if row["shortlist"] == "1" else None)
    add_table(
        doc,
        headers=["rank", "id", "아이템", "M", "F", "R", "W", "IP", "T", "가중합", "SL"],
        rows=score_rows,
        col_widths_cm=[1.0, 1.5, 6.3, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 1.3, 0.9],
        row_bgs=score_bgs,
    )

    # 6축 평균
    add_heading(doc, "6축 평균 / 강·약점", level=2)
    add_table(
        doc,
        headers=["축", "평균", "패턴"],
        rows=[
            ("M (market)", "3.79", "시장 신호 전반적으로 강함 (Phase A 18개 신호 효과)"),
            ("F (feasibility)", "3.43", "미생물·E. coli 효소 4점대, 진핵 발현(PAM·AI) 2점대 양극화"),
            ("R (regulatory)", "4.50", "SSOT 효과로 평균 매우 높음 — process enzyme 5점 다수"),
            ("W (whitespace)", "3.00", "가장 약한 축 — NEB·Genovis·Halozyme 등 기존 supplier 존재"),
            ("IP (defensibility)", "3.21", "academic IP·기존 cluster 특허 회피가 공통 숙제"),
            ("T (time-to-revenue)", "3.21", "kit 2~3년 vs cGMP 라이선스 4~5년 양극화"),
        ],
        col_widths_cm=[3.5, 1.7, 11.8],
    )

    # 5. Short-list details
    add_heading(doc, "5. Short-list 상세 (7개)")
    for item in SHORTLIST:
        add_heading(doc, f"#{item['rank']} {item['id']} — {item['name']}", level=2)
        add_para(doc, f"정의: {item['definition']}")
        add_para(doc, f"사업화: {item['biz']}")
        bar_lines = "  ".join(f"{k} {score_bar(item['score'][k])}" for k in ["M","F","R","W","IP","T"])
        p = doc.add_paragraph()
        run = p.add_run(bar_lines + f"   →   가중합 {item['weighted']:.2f}")
        run.font.name = "Consolas"
        run.font.size = Pt(9)
        add_para(doc, f"위험: {item['risk']}", size=10)
        add_para(doc, f"다음 액션: {item['next']}", size=10)

    # 6. Risks
    add_heading(doc, "6. 위험·미지수")
    add_table(
        doc,
        headers=["영역", "내용"],
        rows=RISKS,
        col_widths_cm=[3.2, 13.8],
    )

    # 7. Next round
    add_heading(doc, "7. 다음 회차 제안")
    add_heading(doc, "보강 검색 영역", level=2)
    for it in NEXT_ROUND["search_areas"]:
        doc.add_paragraph(it, style="List Bullet")
    add_heading(doc, "추가 검증 항목", level=2)
    for it in NEXT_ROUND["verifications"]:
        doc.add_paragraph(it, style="List Bullet")
    add_heading(doc, "다음 deep-dive 후보", level=2)
    for it in NEXT_ROUND["deep_dives"]:
        doc.add_paragraph(it, style="List Bullet")

    # 8. Meta
    add_heading(doc, "8. 메타")
    meta_rows = [
        ("run_id", "20260521-A"),
        ("실행일", "2026-05-21 (UTC)"),
        ("Phase A 완료", "05:08 UTC — 18 demand signal (우선 11 / 확장 7)"),
        ("Phase B 완료", "05:42 UTC — 14 candidates (공정 6/제형 1/진단·연구 5/펩타이드 2)"),
        ("Phase C 완료", "06:15 UTC — 6축 스코어링, short-list 7"),
        ("Phase D 완료", "Executive digest 작성"),
        ("재시도", "없음 (1회 통과)"),
        ("주요 한계",
         "(1) 시장 사이즈 수치 다수 [추정]. (2) TPD E3 ligase·PETase는 Phase B에서 제외. "
         "(3) 경계 사례 3건은 한정 시나리오로만 포함. (4) freedom-to-operate IP 분석은 후속 deep-dive."),
    ]
    add_table(doc, headers=["항목", "값"], rows=meta_rows, col_widths_cm=[3.2, 13.8])

    doc.save(OUT_DOCX)


if __name__ == "__main__":
    build_excel()
    build_word()
    print(f"Wrote {OUT_XLSX}")
    print(f"Wrote {OUT_DOCX}")
