# Scoring Result — 2026-05-21

Phase B의 14개 후보를 6축 정량 평가한 결과 및 short-list.

## 산식 / 가중치

6축 (각 1~5점 정수, 5점이 가장 유리):
1. **Market pull (M)** — 수요 신호 강도·다수성·금액 규모
2. **Technical feasibility (F)** — 발현·정제·생산성·안정성·제조 난이도
3. **Regulatory lightness (R)** — 임상 불필요 정도 (process/excipient·연구시약 = 5)
4. **Competitive whitespace (W)** — 경쟁자 적을수록 5
5. **IP defensibility (IP)** — 신규성·특허 가능성·기존 IP 충돌 회피
6. **Time-to-revenue (T)** — 빠를수록 5 (1~2년=5, 5년+=1)

가중치: **M 0.25, F 0.20, R 0.20, W 0.15, IP 0.10, T 0.10**.
`weighted_score = 0.25·M + 0.20·F + 0.20·R + 0.15·W + 0.10·IP + 0.10·T` (5점 만점, 소수 2자리 반올림).

Short-list 규칙: 가중합 상위 5개 이상; 6위 이하 점수가 5위와 0.2 이내면 함께 포함 (최대 7개).

---

## 전체 스코어 표

| id | item_name | M | F | R | W | IP | T | weighted | rank | shortlist |
|---|---|---|---|---|---|---|---|---|---|---|
| item_002 | Engineered mTG for site-specific ADC conjugation | 5 | 4 | 5 | 3 | 3 | 4 | **4.20** | 1 | ✓ |
| item_008 | Peptiligase / OaAEP1 C247A — green peptide ligation | 5 | 4 | 5 | 3 | 4 | 3 | **4.20** | 1 | ✓ |
| item_007 | Engineered RNA ligase (splint-ligation, AOC/ASO) | 4 | 4 | 5 | 4 | 4 | 3 | **4.10** | 3 | ✓ |
| item_006 | Engineered T7 RNAP variant (low-dsRNA, capping) | 5 | 4 | 5 | 2 | 3 | 4 | **4.05** | 4 | ✓ |
| item_003 | Engineered Sortase A variant (Ca-indep, high-kcat) | 4 | 4 | 5 | 3 | 3 | 4 | **3.95** | 5 | ✓ |
| item_005 | EndoS2 glycosynthase mutant (Fc glycan remodel) | 4 | 4 | 5 | 3 | 3 | 4 | **3.95** | 5 | ✓ |
| item_009 | Engineered PAM (peptide C-amidation, GLP-1) | 4 | 2 | 5 | 5 | 4 | 2 | **3.75** | 7 | ✓ |
| item_004 | FGE for aldehyde-tag dual-payload ADC | 3 | 3 | 5 | 4 | 4 | 3 | **3.65** | 8 | |
| item_013 | High-fidelity Prime Editor (research/ex-vivo) | 3 | 3 | 4 | 4 | 3 | 3 | **3.35** | 9 | |
| item_010 | Engineered IdeS/IdeZ variant (QC + ex-vivo) | 3 | 4 | 4 | 2 | 2 | 4 | **3.25** | 10 | |
| item_011 | PNGase F + sialyl/galactosyl-Tase glycan QC set | 3 | 4 | 4 | 2 | 2 | 4 | **3.25** | 10 | |
| item_001 | Next-gen hyaluronidase (non-PH20/variant) for SC | 5 | 3 | 3 | 2 | 2 | 2 | **3.15** | 12 | |
| item_014 | AI-designed (RFdiffusion2/3) custom enzyme service | 3 | 2 | 4 | 3 | 5 | 2 | **3.10** | 13 | |
| item_012 | Next-gen Cas12/Cas13 + RPA set for POC Dx | 3 | 3 | 3 | 2 | 2 | 3 | **2.75** | 14 | |

(동점 시 id 순으로 표기. 검증: 가중합 = 0.25·M+0.20·F+0.20·R+0.15·W+0.10·IP+0.10·T)

---

## 각 후보 스코어 근거

### item_001 — Next-gen hyaluronidase (3.15, rank 12)
- **M=5**: SC 전환 신호가 Phase A에서 가장 강함(Halozyme 매출 $1.4B +38%, Merck/AZ/Alteogen·BMS·argenx·Roche). 단일 효소로 수요 가장 큼.
- **F=3**: GH56 fold large glycoprotein, CHO/HEK 발현 필요 — 발현·면역원성·당사슬 균질성 난이도 큼.
- **R=3**: Co-formulation 트랙이라 단독 신약 아니지만 PK/면역원성 임상 부담 있음.
- **W=2**: Halozyme·Alteogen 양강 + Sanofi/Argobio EnhanzeR `[추정]`; 신규 진입자 한계.
- **IP=2**: Halozyme-Merck 현재 소송 진행, 강한 PH20 특허포트, IP 회피 설계 난도 큼.
- **T=2**: SC co-formulation 검증·라이선싱·co-mfg setup까지 4~5년+ 예상.

### item_002 — Engineered mTG (4.20, rank 1, ✓)
- **M=5**: ADC $13.5B + Lonza Visp 2× 확장 + Hzymes가 "enzyme cost issue" 명시 = cost-down 변이체 직접 수요.
- **F=4**: Streptomyces 유래 세균 효소, E. coli·Streptomyces 발현 잘 확립.
- **R=5**: 순수 process enzyme, 정제단계 제거.
- **W=3**: Ajinomoto AJICAP, Innate Pharma EFAT2, Hzymes, Zedira — 다수이나 specificity·면역원성 차별화 여지.
- **IP=3**: 변이체 신규성 가능, 기존 cluster 특허 회피 필요.
- **T=4**: 효소 kit 상품화는 2~3년 가능, 빅 라이선스는 3~4년.

### item_003 — Engineered Sortase A (3.95, rank 5, ✓)
- **M=4**: ADC/AOC/radioligand 모두 적용 가능하지만 mTG 대비 산업 채택 모멘텀이 약간 약함.
- **F=4**: S. aureus 유래 작은 단백질, E. coli 발현 매우 용이.
- **R=5**: Process enzyme.
- **W=3**: NBE-Therapeutics SMAC (Boehringer 자회사), academic spin-out 다수.
- **IP=3**: eSrtA 변이체 academic IP가 풍부, 신규 변이체 가능하지만 회피 설계 필요.
- **T=4**: 빠른 상품화 가능.

### item_004 — FGE (3.65, rank 8)
- **M=3**: 차세대 dual-payload ADC 차별화 신호는 있으나 대형 딜은 Catalent SMARTag로 집중 — 일반 수요는 mTG·Sortase보다 작음.
- **F=3**: Cu-dependent monooxygenase, anaerobic in vitro reaction 까다로움, FGE-항체 co-expression 또는 site-specific oxidation 공정 노하우 필요.
- **R=5**: Process.
- **W=4**: Catalent (Redwood SMARTag) 사실상 단독.
- **IP=4**: Anaerobic·고활성 variant 신규성 확보 가능.
- **T=3**: 3~4년.

### item_005 — EndoS2 glycosynthase (3.95, rank 5, ✓)
- **M=4**: ADCC 강화 + biosimilar QC 동시 수요. NEB cGMP 라인 확장이 모멘텀.
- **F=4**: GH18 Streptococcus 유래, E. coli 발현 가능, glycosynthase mutant (D184M 등) 활성 입증.
- **R=5**: Process.
- **W=3**: Genovis GlycINATOR/GlyCLICK, Synaffix GlycoConnect(Lonza), NEB Remove-iT 등.
- **IP=3**: Mutant·donor sugar 특허 가능.
- **T=4**: Kit·CDMO 라이선스 2~3년.

### item_006 — Engineered T7 RNAP (4.05, rank 4, ✓)
- **M=5**: 600+ mRNA 임상 + T7 시장 $1.8B → $3.9B (2034) — 단일 효소 시장으로 가장 크다.
- **F=4**: Single-subunit RNAP, E. coli 발현 잘 확립.
- **R=5**: Process.
- **W=2**: NEB Hi-T7, Aldevron, Trilink, Thermo, Promega 등 다수 시판 — 진입 비좁음.
- **IP=3**: Low-dsRNA 변이체 신규성 가능하나 academic·기업 특허 다수 존재.
- **T=4**: cGMP kit 2~3년.

### item_007 — Engineered RNA ligase (4.10, rank 3, ✓)
- **M=4**: Novartis–Avidity $12B AOC + Codexis ECO ligase 빅파마 첫 수주 = 신생 시장.
- **F=4**: T4 Rnl2/RtcB E. coli 발현 가능, 변이체 directed evolution 잘 작동.
- **R=5**: Process.
- **W=4**: Codexis가 선두지만 ECO Synthesis 시장이 막 형성 — 백색공간 여전히 큼.
- **IP=4**: Splint-ligation 효소 신규성 확보 가능, Codexis IP는 균주·공정 중심으로 우회 여지.
- **T=3**: Codexis와 경쟁하며 라이선스 확보까지 3~4년.

### item_008 — Peptiligase / OaAEP1 C247A (4.20, rank 1, ✓)
- **M=5**: Bachem $1톤/yr SPPS, PolyPeptide €100M 확장, Vinnova green GLP-1 펀딩 — GLP-1 시대 효소 합성 직접 수요.
- **F=4**: OaAEP1 C247A는 발현 용이성 입증(140× 개선 paper, PMC11607802); butelase-1 발현 난점 해결.
- **R=5**: Process.
- **W=3**: EnzyPep (peptiligase, Fresenius Kabi/EnzyTag), Sumitomo/Genovis, academic spin-out.
- **IP=4**: C247A 변이체·후속 evolution 신규 특허 여지.
- **T=3**: Bachem·PolyPeptide 채택 검증·cGMP 라이선스 3~4년.

### item_009 — Engineered PAM (3.75, rank 7, ✓)
- **M=4**: GLP-1·calcitonin·oxytocin·radioligand peptide C-amide는 활성에 필수 → 수요 명확하나 시장 사이즈는 ligation보다 좁음.
- **F=2**: Bifunctional PHM+PAL, Cu·ascorbate 의존 monooxygenase, 진핵 발현(CHO/HEK) 또는 가공 필요 — 매우 까다로움.
- **R=5**: Process.
- **W=5**: cGMP grade PAM supplier 사실상 부재 (Unigene 만료 후 plateau) — 가장 깨끗한 화이트스페이스.
- **IP=4**: Engineered variant 신규성 충분.
- **T=2**: 발현·정제·cGMP 확립까지 4~5년 예상.

### item_010 — IdeS/IdeZ (QC + ex-vivo) (3.25, rank 10)
- **M=3**: QC niche 수요는 안정적이나 시장 규모 작음. AAV redosing 시나리오는 본 후보 범위 밖.
- **F=4**: Streptococcus 유래, E. coli 발현 잘 됨.
- **R=4**: Research/QC reagent 트랙(IVD 등 별도 인허가 일부).
- **W=2**: Genovis FabRICATOR/Z 사실상 표준, Promega·NEB도 시판.
- **IP=2**: Genovis IP 강함, subtype-broad variant 신규성 제한.
- **T=4**: Kit 시판 2~3년.

### item_011 — PNGase F + glycan transferase set (3.25, rank 10)
- **M=3**: 안정적이지만 commodity화된 시장.
- **F=4**: 모두 잘 알려진 효소, E. coli 발현.
- **R=4**: Research/QC.
- **W=2**: NEB Rapid PNGase F, Genovis GlycINATOR, Agilent, Promega — 매우 혼잡.
- **IP=2**: 기존 특허 만료/회피 어려움.
- **T=4**: 빠른 상품화 가능.

### item_012 — Cas12/Cas13 + RPA Dx set (2.75, rank 14)
- **M=3**: SHERLOCK·DETECTR 임상 진입은 있으나 IVD 시장 자체가 진입장벽·매출화 더딤.
- **F=3**: 다수 효소 조합 + 안정성 이슈, freeze-dried 제형 난이도.
- **R=3**: IVD 신규 인허가 필요.
- **W=2**: Mammoth, Sherlock Biosciences, NEB, TwistDx — 혼잡 + 강한 IP.
- **IP=2**: Broad/Mammoth/Sherlock 핵심 특허 다수, 회피 난이도 큼.
- **T=3**: IVD 인허가 3~4년.

### item_013 — Prime Editor (research/ex-vivo) (3.35, rank 9)
- **M=3**: 연구·CGT manufacturing reagent 수요 있으나 in-vivo 치료는 범위 밖.
- **F=3**: Cas9·MMLV-RT fusion 큰 단백질, 발현·정제·활성 검증 까다로움.
- **R=4**: Research reagent.
- **W=4**: Prime Medicine가 치료 IP 중심이라 research reagent 채널은 상대적 백색.
- **IP=3**: vPE 변이체 자체는 MIT IP, 라이선스 또는 후속 evolution 필요.
- **T=3**: Kit 출시 2~3년.

### item_014 — AI-designed custom enzyme (3.10, rank 13)
- **M=3**: 시장은 잠재적이나 현재 매출 미미.
- **F=2**: 천연 수준 활성 달성 사례 등장했으나 고객 요청별 case-by-case 성공률 변동 큼.
- **R=4**: Reagent/process 트랙.
- **W=3**: Codexis, Biomatter, Arzeda, Cradle, Enzymit, Generate 등 다수.
- **IP=5**: De novo backbone은 신규성·특허성 가장 강함.
- **T=2**: Service biz scale-up 4~5년.

---

## Short-list 선정 결과

상위 5개 기준선: rank 5 (Sortase A·EndoS2 동점 3.95). 6위(PAM 3.75)는 5위와 0.20 차이로 규칙(≤0.2) 충족 → 포함. 최대 7개 한도 도달.

**Short-list 7개 (최종)**:

| rank | id | item_name | weighted |
|---|---|---|---|
| 1 | item_002 | Engineered mTG for ADC site-specific conjugation | 4.20 |
| 1 | item_008 | Peptiligase / OaAEP1 C247A — green peptide ligation | 4.20 |
| 3 | item_007 | Engineered RNA ligase (splint-ligation, AOC/ASO) | 4.10 |
| 4 | item_006 | Engineered T7 RNAP variant (low-dsRNA, capping) | 4.05 |
| 5 | item_003 | Engineered Sortase A variant | 3.95 |
| 5 | item_005 | EndoS2 glycosynthase mutant | 3.95 |
| 7 | item_009 | Engineered PAM (peptide C-amidation) | 3.75 |

분포: process enzyme 5 / peptide manufacturing 2 / diagnostic·research 0 / formulation 0. ADC·AOC·mRNA·peptide 모달리티 트렌드와 정합.

다음 라운드 재검토 권장: item_001 (hyaluronidase — IP 분쟁 추이 추적), item_004 (FGE — dual-payload ADC 상용화 신호 보강), item_014 (AI-designed — 고객 case 누적 후).
