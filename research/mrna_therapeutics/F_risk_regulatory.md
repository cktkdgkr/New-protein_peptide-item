# [F] 리스크 및 규제 분석 — mRNA 기반 단백질 대체 치료제

조사 범위: in vivo 단백질 치환(protein replacement)·기능성 단백질 발현용 mRNA 치료제 (RNAi 및 백신 제외)
조사일: 2026-05-22

---

## F.1 규제 환경 (FDA/EMA/PMDA/NMPA/MFDS)

### F.1.1 미국 FDA — CBER vs CDER 관할권
- **mRNA 치료제는 원칙적으로 CBER(Center for Biologics Evaluation and Research) 산하 OTAT(Office of Tissues and Advanced Therapies, 현 OTP — Office of Therapeutic Products)에서 심사**한다. mRNA 자체가 유전자 산물로 분류되며, in vivo로 단백질을 발현하므로 **Human Gene Therapy** 정의 범주에 들어간다 (FDA 2024).
  - 단, **표적이 vaccine prophylaxis가 아닌 protein replacement / enzyme replacement인 경우**, CBER/CDER 공동 심사(joint review)가 발생할 수 있음 [추정] — FDA 2025 가이드라인에서는 CDER·CBER 공동 가이던스 발행 계획이 명시됨.
- **2024.01**: FDA 「Human Gene Therapy Products Incorporating Human Genome Editing」 final guidance 발행 — in vivo CRISPR/base editing/prime editing 포함.
- **2025**: CBER 가이던스 어젠다 14건 (Therapeutic Products), 2026 어젠다 19건 (6 new + 12 final + 1 reissued) 예고.
- **2026.04**: CBER 「Safety Assessment of Genome Editing in Human Gene Therapy Products Using Next-Generation Sequencing」 draft guidance — ex vivo·in vivo 모두 NGS 기반 off-target 평가 기준 제시.
- **2025.09**: 「Postapproval Methods To Capture Safety and Efficacy Data for Cell and Gene Therapy Products」 draft guidance — long-term follow-up(LTFU) 강화.
- **2025**: FDA "Plausible Mechanism Pathway" — bespoke/n-of-1 CRISPR·mRNA 치료제 신속 승인 경로 발표 (BioPharma Dive 2025).
- **mRNA 백신 특화 가이던스(2023, 「Considerations for the Quality, Safety and Efficacy」)**는 존재하지만 **치료용 mRNA(non-vaccine) 전용 FDA 가이던스는 2026.05 현재 미발표** [미확인 — Casgevy 등 gene therapy 가이던스에서 일부 차용].

### F.1.2 EMA — ATMP 분류 및 CAT 심사
- **mRNA 치료제는 ATMP(Advanced Therapy Medicinal Product) 중 Gene Therapy Medicinal Product(GTMP)로 분류 가능성이 높음** — EMA CAT(Committee for Advanced Therapies)가 case-by-case로 60일 내 의견 제시.
  - 단, **유전자 자체의 변경 없이 일시적 단백질 발현만 유도하는 mRNA**의 경우, CAT 선례에서 "유전자형 변경 없는 표현형 변경"으로 보아 GTMP가 아닌 일반 biologic으로 분류된 사례도 있음 (예: mRNA-electroporated dendritic cells → somatic cell therapy 분류) — 따라서 in vivo 단백질 치환 mRNA의 분류는 **개별 판단**.
- **2025.03**: EMA·HMA(Heads of Medicines Agencies) 공동 — 비규제 advanced therapies 리스크 경고문 발표.
- EU IVT mRNA 백신 품질 가이드라인(EMA draft) 존재 — 치료제 적용 시 borrow 가능.
- 승인 경로: PRIME(PRIority MEdicines) 지정 → 신속 과학적 자문 + accelerated assessment(150일).

### F.1.3 PMDA 일본 — Sakigake / 재생의료등제품
- **Sakigake 지정**은 일본 우선 개발(first-in-world in Japan) 조건 필수 — FDA Breakthrough/EMA PRIME와 차별점. 2017년 첫 지정 이후 누적 운영.
- **재생의료등제품(Regenerative Medical Products)** 카테고리에 mRNA 치료제가 들어가며, **조건부 시한부 승인(Conditional Time-Limited Approval, 최대 7년)** 적용 가능 — 초기 임상에서 likely efficacy + confirmed safety 확인 시 시판 가능, 7년 내 본승인 재신청.
- **2025.12**: BlueRock bemdaneprocel(파킨슨 세포치료), Nanoscope MCO-010(optogenetic gene therapy) Sakigake 지정 — in vivo mRNA 적용 사례는 아직 제한적 [미확인 — 2026 시점 mRNA 치료제 Sakigake 지정 사례 없음 추정].

### F.1.4 NMPA 중국 — 신속 승인 경로
- **Priority Review**: 130 working days(~6개월) 목표. 2024년 110건 처리(+29% YoY).
- **30-Day Clinical Trial Review**(2025.10 directive) — 국가중점 R&D 품목·글로벌 동시개발 품목 대상 IND 신속 심사.
- 2024 first-in-class 48건 중 17건 Priority, 11건 Conditional, 13건 Breakthrough rolling 활용.
- mRNA 치료제 전용 가이던스는 NMPA CDE 차원에서 별도 발행 미확인 — 코로나 mRNA 백신(CCFDIE 2024 CMC 가이드라인) 가이드 차용 가정 [추정].

### F.1.5 MFDS 한국 — 첨단바이오의약품
- **첨단재생바이오법(2020 시행, 2025.02 개정)** — mRNA in vivo 치료제는 「인체세포등관리업」 적용 가능 + 첨단바이오의약품 분류.
- 2025년 바이오의약품 심사기간 406→295일, 2026 Q4에 240일로 단축 목표 (MFDS).
- 바이오 CDMO 특별법(2026년 말 시행 예정) — 국내 mRNA CDMO(에스티팜·삼성바이오·SK바이오사이언스) 글로벌 진출 지원 프레임.

---

## F.2 CMC 품질 관리 요건

### F.2.1 mRNA Drug Substance (IVT mRNA) Critical Quality Attributes
| 항목 | 기준/방법 | 비고 |
|---|---|---|
| Identity | DNA template sequence, RNA sequence (Sanger/NGS), PCR | FDA 권장 |
| Capping efficiency (5'cap m7GpppN) | >95% (LC-MS) | CleanCap M6/AG, vaccinia capping enzyme |
| Poly-A tail length | 100~150 nt 균일성 (LC-MS, gel) | 짧을수록 안정성·번역 효율 ↓ |
| 5'/3' truncation | <10% (capillary gel electrophoresis) | RNA integrity |
| dsRNA contamination | **<0.1 ng/μg** (immuno dot blot, J2 antibody) | 핵심 — innate immune trigger |
| Residual dsDNA template | <10 pg/dose (qPCR) | WHO 가이드 |
| Residual T7 RNAP | <ppm 수준 (ELISA) | 면역원성 위험 |
| Residual NTPs / cap analog | HPLC | impurity profile |
| Endotoxin | <0.5 EU/mL (LAL) | |
| Sterility | USP <71> | |

- TriLink **CleanScribe RNA Polymerase**(2024 출시, with Alphazyme)는 dsRNA 부산물을 wild-type T7 대비 **최대 85% 저감** → CMC 부담 완화.

### F.2.2 LNP Drug Product CQA
| 항목 | 일반 사양 | 비고 |
|---|---|---|
| Particle size | 60~100 nm (DLS, NTA, cryo-EM) | 70~80 nm 최적 |
| PDI | <0.2 | 균일성 |
| Encapsulation efficiency (EE%) | **>85%** (RiboGreen) | 함량 정확도 |
| Zeta potential | -10~+10 mV | 안정성 |
| Ionizable lipid pKa | 6.2~6.8 | endosomal escape |
| Ionizable lipid 불순물 | impurity profile + 산화·가수분해 산물 모니터링 | SM-102, ALC-0315 등 |
| 저장 안정성 | -20°C(상업), -80°C(임상초기), 동결건조(R&D) | 보관 cold chain critical |

### F.2.3 주요 CMC 챌린지
- **Comparability**: 스케일업·공정변경 시 CQA가 미세하게 변동 → FDA는 quality data → nonclinical → clinical 순차 비교성 시험 요구. mRNA는 표준 접근법 수정 필요 — gene therapy/vaccine 가이드 borrow.
- **Plasmid template QC**: 선형화·정제·잔여 enzyme/host cell protein.
- **GMP 스케일**: gram→kg 단위 IVT 시 dsRNA 저감 공정(modified nucleotide, lower temp, post-IVT cellulose chromatography) 핵심.
- **Lyophilization**: 동결건조 안정성 연구는 R&D 단계 — 상업 제품은 동결액제(-20/-80°C) 위주.

---

## F.3 정책·보조금 동향

### F.3.1 미국
- **BARDA mRNA platform 정책 반전 (2025.08)**: HHS(케네디 장관 체제)가 22개 BARDA mRNA 프로젝트 종결, 약 **$500M 규모 GHIC mRNA equity 투자 중단**. Moderna·Pfizer·CSL Seqirus 계약 해지. **단, Arcturus(조류독감 mRNA)·Amplitude(trans-amplifying RNA) 진행 중 계약은 완료 허용**. 이 정책 변화에 항의해 ARPA-H 최고위 인사 사임 (BioSpace).
- **ARPA-H FY2025 예산** $1.5B 수준 [미확인 — 정확 분배 미공개]. mRNA 직접 라인은 축소 추세.
- **시사점**: 미국 연방 mRNA 백신 자금은 위축, **치료용 mRNA(non-vaccine)는 여전히 OTAT 심사 진행 중**이며 민간(VC, Big Pharma) 자금에 의존도 ↑.

### F.3.2 유럽
- **IPCEI Med4Cure (2024.05 승인)**: 6개국 13사 14 프로젝트, 공공 €1B + 민간 €5.9B 매칭.
- **IPCEI Tech4Cure (2025.07 승인)**: 5개국 10사 10 프로젝트, 공공 €403M.
- **BioTechEU initiative (2026-27)**: EC + EIB Group → €10B 동원.
- **Sanofi**: 2020년 이후 mRNA에 €3.5B 투자, 프랑스 end-to-end mRNA Center of Excellence 구축 (€1B+).

### F.3.3 중국
- "Made in China 2025" 생물의약 우선순위 + NMPA 신속 심사 + 지방정부 보조금.
- mRNA CDMO 캐파 급증(StemiRNA, Abogen 등) — 단, BIOSECURE 영향으로 미국향 수주 제약.

### F.3.4 한국
- **KDDF**(범부처 신약개발사업단) 신규 mRNA 과제 다수, 산업부 백신·치료제 mRNA 클러스터(인천 송도) 조성.
- **MFDS 첨단바이오의약품 패스트트랙** + 「국가전략기술 세액공제」(15~30%) mRNA 포함.

### F.3.5 BIOSECURE Act 영향
- 2024년 말 NDAA 끼워넣기로 통과(2025), 1260H 리스트 기반 — BGI, MGI 명시. **WuXi AppTec은 차기 1260H 업데이트에 추가 예상**.
- 연방기관·보조금 수령자는 1260H 기업 장비·서비스 사용 금지. 기존 계약 **~5~8년 wind-down 유예**.
- **mRNA CDMO 영향**: 미국 자금이 들어간 mRNA 치료제 개발사는 WuXi ATU(advanced therapies unit), GenScript ProBio, Abogen 등 중국 mRNA 서비스 의존 불가 → CordenPharma, Aldevron(Danaher), Recipharm, Catalent, 에스티팜 등으로 재편.

### F.3.6 IRA Medicare Price Negotiation
- **Orphan drug 예외 확대 (2025 reconciliation law)**: 단일 희귀병이 아닌 복수 희귀병 지정 약물도 협상 제외. 비희귀 적응증 추가 시 협상 카운터 지연 — 즉 **희귀병 mRNA 치료제(예: PKU, MMA, OTC 결핍 등)는 IRA 협상에서 일정 기간 보호**.
- **시사점**: protein replacement mRNA 치료제 다수가 ultra-rare 적응증 → IRA 가격 협상 노출 위험 낮음 (단, 적응증 확장 시 risk 재발생).
- Cell and Gene Therapy Access Model — sickle cell pilot, 향후 mRNA gene editing(예: VERVE) 확장 가능.

---

## F.4 지정학적 리스크 (lipid, enzyme 공급망)

### F.4.1 이온화 지질(Ionizable Lipid) 공급
- **CordenPharma (스위스/룩셈부르크)**: SM-102, ALC-0315 GMP 공급 주력. 2024.05 Certest와 차세대 ionizable lipid 포트폴리오 협업, 2025년 LNP Starter Kits 출시.
- **Croda / Avanti Polar Lipids (영국/미국)**: 2025.03 Avanti Research가 Certest와 ionizable lipid 협업 확대.
- **Evonik (독일)**: 2025.01 한국 에스티팜과 RNA·핵산 치료제 서비스 협업.
- **Merck KGaA**, **NOF Corp(일본)** — PEG-lipid·헬퍼 지질.
- **리스크**: 4~5개 GMP-grade ionizable lipid 공급자에 집중 → 단일점 실패 시 글로벌 mRNA 파이프라인 지연. 특허 분쟁(Alnylam·Arbutus·Moderna·Pfizer 진행 중) 시 공급 중단 가능 [추정].

### F.4.2 효소 및 reagent
- **TriLink BioTechnologies (미국, Maravai LifeSciences)**: CleanCap M6/AG/AU 캡 analog GMP 공급, T7 RNAP, CleanScribe RNAP (with Alphazyme, dsRNA 85% 저감).
- **Aldevron (미국 ND, Danaher 산하)**: pDNA·mRNA CDMO. 2025.02 TriLink와 non-exclusive CleanCap 라이선스·공급 계약.
- **NEB (New England Biolabs)**, **Thermo Fisher**, **Lucigen** — IVT 효소 보조 공급.
- **리스크**: 캡 analog(CleanCap)·고순도 T7 RNAP가 미국 기업 과점. WTO/수출통제 변동 시 한·중·유럽 영향. 중국향 BIOSECURE 역(逆) 효과 — 중국이 자체 IVT 효소(Vazyme 등) 내재화 가속.

### F.4.3 Plasmid DNA 템플릿
- Aldevron, Cobra Biologics, VGXI 등 — GMP pDNA 수요 폭증, 리드타임 12~18개월.

---

## F.5 ESG 리스크

### F.5.1 콜드체인 탄소발자국
- COVID-19 mRNA 백신 dose당 GHG: **0.01~0.2 kg CO2e** (독일 연구). **운송이 총 footprint의 최대 99% 차지** — 항공·도로·라스트마일 합산이 ultra-low freezer + 드라이아이스 + 포장 합계 대비 약 19배.
- 치료용 mRNA는 백신보다 dose 수는 적지만 dose당 RNA량·LNP 함량이 크고 -80°C/-20°C 유통 필수 → **환자당 footprint는 백신보다 클 가능성** [추정].
- 향후 **동결건조 제형**(R&D 단계, Arcturus·CureVac 발표) 상용화 시 콜드체인 부담 대폭 완화 가능.

### F.5.2 제조 공정 폐기물
- LNP 제조 시 에탄올/시트르산 완충액 사용 — 마이크로플루이딕 mixing 후 다이아필트레이션. 유기용매 폐액 처리 및 lipid 합성 단계 부산물(특히 ionizable lipid 합성 4~6 단계).
- pDNA 발효 후 cell lysate·CsCl·detergent 폐기물.

### F.5.3 ESG 종합
- 환자 단위 footprint는 저분자보다 높지만, **희귀질환 small population × 평생 1회/저빈도 투여**(특히 in vivo gene editing) 가정 시 환자 단위 평생 footprint는 만성 ERT(주 1~2회 평생 IV)보다 작을 수 있음 [추정] — Life cycle assessment 필요.

---

## F.6 안전성 리스크 (★ 핵심: re-dosing immunogenicity)

### F.6.1 Anti-PEG / Anti-LNP 항체 — re-dosing 핵심 리스크
- mRNA-LNP는 PEG-lipid(통상 1.5 mol%) 포함 → **반복투여 시 anti-PEG IgM/IgG 유도, accelerated blood clearance(ABC) 현상으로 재투여 효능 ↓**.
- 동물(rat) 모델: 초회 LNP 투여 후 재투여 시 **anti-PEG IgM·IgG isotype switch 및 immune memory** 입증, blood clearance 가속화 (PMC10622525, 2023).
- 인간 임상(SARS-CoV-2 mRNA 백신): vaccine-induced anti-PEG 항체 상승 → **2차 접종 시 systemic reactogenicity와 상관**. 단, neutralizing Ab 생성에는 영향 없음 (medRxiv 2022).
- **시사점**: **단백질 치환용 mRNA 치료제는 평생 반복투여(주~월 단위)가 필요**한 경우가 다수 → anti-PEG/anti-LNP는 **최대 사업화 장벽**.
  - 대안 1: **모든 정맥 전 steroid premedication** (patisiran 사례 — IV 80분 + 스테로이드 전처치).
  - 대안 2: **Non-PEG lipid coating** (phosphorylcholine PCB lipid, polysarcosine).
  - 대안 3: **LNP-free 전달체** (polymer, virus-like particle, conjugate).
  - 대안 4: **단회 또는 저빈도** in vivo gene editing(VERVE 등)으로 reposition.

### F.6.2 Patisiran(GalNAc 아닌 LNP-siRNA) 임상 데이터 — RNAi지만 LNP 참고
- 3주 1회 만성 투여 (0.3 mg/kg) — **ADA 발생률 낮고 PK/효능 영향 없음**.
- 단, 매 dose 마다 **80분 IV + steroid premedication 필수** (LNP infusion reaction 방지).
- **2년 OLE 데이터에서 안전·내약성 유지** → LNP 반복투여가 임상적으로 불가능하지는 않으나 부담↑.
- mRNA-LNP(치료용)는 patisiran보다 더 빈번한 dose 가능성 → premedication burden 증가.

### F.6.3 Innate immune 활성화
- TLR3/7/8, RIG-I, MDA5, PKR → IFN-α/β·TNF·IL-6.
- **수정 뉴클레오시드(N1-methylpseudouridine, m1Ψ)** 사용 시 PKR·OAS·RIG-I 활성 ↓, dsRNA 잔류량 동시 관리 필수.
- 그래도 LNP 자체가 TLR4·NLRP3 인플라마좀 활성 가능 → infusion reaction 잔존.

### F.6.4 Anti-drug antibody (ADA) — 발현 단백질에 대한 면역
- 환자가 표적 단백질을 deficient(null/missense)한 경우, mRNA로 외인성 형태 단백질 발현 시 **항원으로 인식 → ADA 생성**, ERT 사례와 동일 메커니즘 (e.g., Pompe rhGAA, Fabry α-Gal A).
- mRNA의 경우 단백질 농도 변동성·intracellular 발현이라 ADA 영향이 다를 수 있음 [추정] — 임상 데이터 미성숙.

### F.6.5 LNP 생체분포 (biodistribution)
- IV 투여 LNP는 **ApoE 매개로 간 hepatocyte 우선 흡수** — 의도하지 않은 간·비장 축적, **간독성 신호** (ALT/AST 상승) 보고. SM-102 LNP는 hepatic metabolism으로 non-hepatic target 약화.
- 비표적 조직(spleen, BM) 축적 시 장기 면역영향 [미확인].
- **차세대 표적 LNP** (SORT lipid, antibody-LNP conjugate, GalNAc-LNP) 개발로 간외 표적화 시도 (Capstan, Sail Biomedicines 등).

### F.6.6 Genome editing off-target (mRNA Cas9/base editor 전달)
- mRNA 자체는 비통합 (transient) — insertional mutagenesis risk 없음.
- 그러나 Cas9·base editor mRNA로 in vivo gene editing 시 **유전체 off-target 편집**이 핵심 risk → FDA 2024 가이던스 + 2026 NGS 가이던스가 정량 평가 의무화. p53 활성, chromosomal rearrangement, large deletion 모니터링.
- VERVE-101(PCSK9 base editing) — Phase 1b 일부 환자 grade 4 transaminase 상승 보고(2023~24) → 재설계 (LDLR 표적 변경, lipid 변경) [미확인 정확 timeline].

### F.6.7 Myocarditis / 자가면역 신호
- COVID-19 mRNA 백신 myocarditis: 이스라엘 10.4M 접종 중 148건, 주로 16~30세 남성. 기전: spike protein 매개 + IFN-γ 매개 심근 단백질 분해 (Stanford 2025).
- **치료용 mRNA(non-vaccine)는 일반적으로 IM 투여가 아닌 IV·LNP 표적 → 심근 노출 경로 다름** → myocarditis signal 직접 전이는 낮을 가능성. 단, 누적 LNP 노출량·반복투여·spleen·심외막 분포 시 fully ruled out 불가 [추정].
- **AZD8601 (VEGF-A mRNA, 심근 직접 epicardial 주사, CABG 환자)**: EPICCURE Phase 2 (n=11, AZ8601 7명, placebo 4명) — **primary endpoint(safety/tolerability) 충족**, LVEF·NT-proBNP 개선 trend. **VEGF off-target/angioma 신호 보고 없음**. 단, AstraZeneca는 2022년 파이프라인 제거 (사업적 결정).

### F.6.8 비교성(Comparability) 리스크
- 스케일업 시 dsRNA 함량·LNP 입자 크기·EE% 미세 변동 → 면역원성/PK 변화 가능성. FDA는 quality + nonclinical bridging study 요구. 임상 후기 단계 공정 변경은 추가 임상 시험 트리거 위험.

---

## F.7 종합 리스크 매트릭스

| # | 리스크 카테고리 | 발생 가능성 | 영향도 | 종합 | 주요 완화책 |
|---|---|---|---|---|---|
| R1 | **Anti-PEG / Anti-LNP 항체 → re-dosing 효능 저하** | 高 | 高 | **★★★ Critical** | non-PEG lipid, polysarcosine, premedication, dose interval ↑, gene editing 1회성 전환 |
| R2 | **발현 단백질 ADA (특히 null mutation 환자)** | 中~高 | 高 | ★★★ Critical | tolerance induction, immunosuppression, 환자 stratification(missense 우선) |
| R3 | **LNP 간·비장 축적, hepatotoxicity** | 中 | 中~高 | ★★ High | targeting LNP (SORT, antibody-conjugate), dose limit, LFT 모니터링 |
| R4 | **Innate immune (IFN, infusion reaction)** | 中 | 中 | ★★ High | m1Ψ, dsRNA QC <0.1 ng/μg, slow IV + steroid premed |
| R5 | **Genome editing off-target (Cas9/BE mRNA)** | 中 | 高 | ★★★ Critical (gene editing 한정) | NGS off-target, base editor 정밀화, FDA 2024/26 guidance 준수 |
| R6 | **이온화 지질·캡 analog 공급 집중** | 中 | 高 | ★★ High | 다중 공급자 qualification, in-house lipid 합성, BIOSECURE 우회 |
| R7 | **BIOSECURE — 중국 CDMO 단절** | 高 (입법 진행) | 中 | ★★ High | 미국·유럽·한국·일본 CDMO 이중 source |
| R8 | **콜드체인 -80°C 의존 → 유통·ESG** | 高 | 中 | ★★ High | 동결건조 R&D 가속, -20°C 안정성 데이터 확보 |
| R9 | **CMC comparability (스케일업·공정 변경)** | 高 | 中 | ★★ High | 조기 platform CMC 확립, 분석법 사전 검증, bridging 임상 예산 |
| R10 | **규제 가이던스 부재(치료용 mRNA 전용)** | 中 | 中 | ★★ High | FDA pre-IND·INTERACT·Type B meeting 적극 활용, EMA scientific advice |
| R11 | **BARDA/HHS mRNA 자금 축소 (2025)** | 高 (사실 발생) | 中 (치료제는 vaccine 대비 영향 낮음) | ★ Medium | 민간 VC·Big Pharma 파트너십, ARPA-H 비-mRNA 라인 활용 |
| R12 | **IRA Medicare 가격 협상** | 低 (orphan 보호) | 中 | ★ Medium | 단일 orphan indication 유지, 적응증 확장 시점 전략 |
| R13 | **Myocarditis / 자가면역 carryover signal** | 低 | 高 | ★ Medium | 적응증별 심혈관 모니터링, AZD8601 사례 reference |
| R14 | **지정학 — 미·중·EU 수출통제** | 中 | 中 | ★ Medium | 지역별 GMP 거점 확보 |
| R15 | **특허 분쟁 (LNP, cap, modified base)** | 高 | 高 | ★★★ Critical | freedom-to-operate 분석, cross-license, 회피 설계 |

평가 척도: ★★★ Critical (즉시 mitigation 필수) / ★★ High / ★ Medium

**가장 중요한 인사이트**: 단백질 치환용 mRNA의 사업 성패는 **R1(anti-PEG/LNP) + R2(발현 단백질 ADA)** 의 두 면역원성 리스크 해결 여부에 달려 있다. 둘 다 해결 어려운 적응증은 **단회·저빈도 in vivo gene editing(R5 관리 하)** 으로 modality 전환이 합리적이다.

---

## 핵심 출처 목록

1. FDA — [Cellular & Gene Therapy Guidances 포털](https://www.fda.gov/vaccines-blood-biologics/biologics-guidances/cellular-gene-therapy-guidances)
2. FDA — [Human Gene Therapy Products Incorporating Human Genome Editing (2024.01 final)](https://www.fda.gov/vaccines-blood-biologics/biologics-guidances/cellular-gene-therapy-guidances)
3. FDA — [Safety Assessment of Genome Editing Using NGS (2026.04 draft)](https://www.fda.gov/news-events/press-announcements/fda-issues-draft-guidance-genome-editing-safety-standards-advance-gene-therapy-development)
4. AABB — [FDA 2026 CBER Guidance Agenda](https://www.aabb.org/news-resources/news/article/2026/01/12/regulatory-update--fda-releases-2026-cber-guidance-agenda)
5. BioPharma Dive — [FDA bespoke n-of-1 CRISPR pathway](https://www.biopharmadive.com/news/fda-plausible-mechanism-pathway-n-of-1-crispr/805235/)
6. EMA — [ATMP Overview](https://www.ema.europa.eu/en/human-regulatory-overview/advanced-therapy-medicinal-products-overview)
7. EMA — [Advanced Therapy Classification (revised guidance public consultation)](https://www.ema.europa.eu/en/news/european-medicines-agency-releases-revised-guidance-advanced-therapy-classification-public-consultation)
8. EMA — [CAT Quarterly Highlights May 2025](https://www.ema.europa.eu/en/documents/committee-report/cat-quarterly-highlights-approved-atmps-may-2025_en.pdf)
9. EMA — [Draft Guideline on Quality Aspects of mRNA Vaccines](https://www.ema.europa.eu/en/documents/scientific-guideline/draft-guideline-quality-aspects-mrna-vaccines_en.pdf)
10. PMDA — [Regenerative Medical Products](https://www.pmda.go.jp/english/review-services/reviews/0003.html)
11. PMDA — [Regulatory Update of Regenerative Medicine in Japan](https://www.pmda.go.jp/files/000269742.pdf)
12. NMPA — [Optimizing Innovative Drug Clinical Trial Review 2025 No.86](https://english.nmpa.gov.cn/2025-10/14/c_1132769.htm)
13. KoreaBiomed — [MFDS Bio-CDMO regulatory regime](https://www.koreabiomed.com/news/articleView.html?idxno=30171)
14. Seoul Economic Daily — [Korea biotech approval 240 days](https://en.sedaily.com/technology/2026/01/02/korea-drug-agency-cuts-biotech-approval-to-240-days-aims)
15. HHS — [Winds Down mRNA Vaccine Development Under BARDA (2025.08)](https://www.hhs.gov/press-room/hhs-winds-down-mrna-development-under-barda.html)
16. BioSpace — [ARPA-H Official Departs Over BARDA mRNA Cuts](https://www.biospace.com/policy/top-arpa-h-official-departs-in-protest-of-barda-mrna-cuts)
17. Foley Hoag — [Congress Passes BIOSECURE Act 2025](https://foleyhoag.com/news-and-insights/publications/alerts-and-updates/2025/december/congress-passes-biosecure-act-here-s-what-you-need-to-know/)
18. Fierce Pharma — [BIOSECURE in NDAA China biopharma constraints 2026](https://www.fiercepharma.com/pharma/biosecure-legislation-makes-way-key-us-defense-bill-teeing-potential-china-biopharma)
19. KFF — [IRA orphan drug exclusion 2025 reconciliation](https://www.kff.org/medicare/people-with-medicare-will-face-higher-costs-for-some-orphan-drugs-due-to-changes-in-the-new-tax-and-budget-law/)
20. European Commission — [Approved IPCEIs Health (Med4Cure, Tech4Cure)](https://competition-policy.ec.europa.eu/state-aid/ipcei/approved-ipceis/health_en)
21. EIB — [€10B BioTechEU initiative](https://www.eib.org/en/press/news/european-commission-and-eib-group-announce-new-initiative-to-mobilise-eur10-billion-investment-for-europe-s-biotech-sector)
22. EU Perspectives — [Sanofi European mRNA chain](https://euperspectives.eu/2026/01/sanofi-mrna-centre-of-excellence/)
23. CordenPharma — [LNP Starter Kits 2025](https://cordenpharma.com/articles/cordenpharma-launches-lnp-starter-kits-to-mitigate-loss-of-high-value-payloads-during-the-gene-editing-journey-to-market/)
24. Avanti Research / Croda — [Certest collaboration 2025.03](https://www.avantiresearch.com/en-gb/news/press-releases/croda-avanti-research-certest)
25. TriLink — [CleanCap Aldevron supply agreement 2025.02](https://www.trilinkbiotech.com/press-releases/trilink-biotechnologies-and-aldevron-enter-into-non-exclusive-license-and-supply-agreement-for-cleancap-mrna-capping-technology)
26. TriLink + Alphazyme — [CleanScribe RNA Polymerase 2024.09](https://www.businesswire.com/news/home/20240924933319/en/TriLink-BioTechnologies-Alphazyme-Collaborate-to-Launch-New-CleanScribe-RNA-Polymerase)
27. npj Vaccines — [Anti-PEG immune responses, LNP rats 2023](https://www.nature.com/articles/s41541-023-00766-z)
28. medRxiv — [Anti-PEG antibodies boosted by SARS-CoV-2 mRNA LNP vaccine 2022](https://www.medrxiv.org/content/10.1101/2022.01.08.22268953.full.pdf)
29. Molecular Pharmaceutics — [Anti-PEG Ab effect on mRNA-LNP immune response](https://pubs.acs.org/doi/10.1021/acs.molpharmaceut.4c00628)
30. Biopharma PEG — [Next-gen mRNA-LNPs to reduce anti-PEG](https://www.biochempeg.com/article/453.html)
31. Alnylam — [Patisiran ALN-TTR02 OLE protocol](https://www.alnylam.com/OLE-Study-Protocol-Amendment.pdf)
32. PMC — [Pharmacokinetics of Patisiran](https://pmc.ncbi.nlm.nih.gov/articles/PMC7187331/)
33. Cell Molecular Therapy — [Why do LNPs target the liver? 2025](https://www.cell.com/molecular-therapy-family/advances/fulltext/S2329-0501(25)00031-2)
34. Stanford Medicine — [mRNA COVID vaccine myocarditis mechanism 2025.12](https://med.stanford.edu/news/all-news/2025/12/myocarditis-vaccine-covid.html)
35. AstraZeneca — [AZD8601 EPICCURE Phase 2 results](https://www.astrazeneca.com/media-centre/press-releases/2021/azd8601-epiccure-phase-ii-trial-demonstrated-safety-and-tolerability-in-patients-with-heart-failure.html)
36. MDPI Environment — [Ecological Footprint of COVID-19 mRNA Vaccines (Germany)](https://www.mdpi.com/1660-4601/18/14/7425)
37. Advancing RNA — [Comparability Considerations For mRNA Product Development](https://www.advancingrna.com/doc/comparability-considerations-for-mrna-product-development-0001)
38. Advancing RNA — [Strategies To Address FDA CMC Trends For mRNA Therapies](https://www.advancingrna.com/doc/strategies-to-address-fda-cmc-trends-for-mrna-therapies-0001)
39. Parexel — [RNA-based therapies "borrowed" FDA CMC guidance](https://www.parexel.com/insights/blog/rna-based-therapies-aligning-cmc-strategies-with-borrowed-fda-regulatory-guidance)
40. CCFDIE — [China CMC Guideline COVID-19 mRNA Vaccines (current version)](https://www.ccfdie.org/en/gzdt/webinfo/2024/12/1732613149983055.htm)
