# Scoring Result — Round 3 (Final), 2026-05-21

R2 23개 후보의 R3 정량/IP/RFI 신호 기반 재평가. 신규 후보 0개. R3 focus는 **quantitative refinement + IP carve-out + CDMO RFI confidence 상향**. 가중치·산식·short-list 룰 변경 없음 (R1·R2와 동일). 누적 활성 후보 = **23개**.

---

## 산식·가중치·confidence 정의

### 6축 (각 1~5점 정수)
1. **Market pull (M)** — 수요 신호 강도·다수성·금액 규모.
2. **Technical feasibility (F)** — 발현·정제·생산성·안정성.
3. **Regulatory lightness (R)** — 임상 불필요 정도 (process/excipient·연구시약=5).
4. **Competitive whitespace (W)** — 경쟁자 적을수록 5.
5. **IP defensibility (IP)** — 신규성·특허 가능성·기존 IP 회피.
6. **Time-to-revenue (T)** — 1~2년=5, 5년+=1.

### 가중치
**M 0.25 / F 0.20 / R 0.20 / W 0.15 / IP 0.10 / T 0.10**.
`weighted_score = 0.25·M + 0.20·F + 0.20·R + 0.15·W + 0.10·IP + 0.10·T` (5점 만점, 소수 2자리).

### confidence 태그 (iteration_plan §4)
- **H (high)**: 출처 ≥3, 정량 데이터(가격·시장규모) 보유, `[추정]` 없음.
- **M (medium)**: 출처 1~2, 일부 정량, `[추정]` 일부.
- **L (low)**: 출처 1개 미만 또는 전적 `[추정]`.

R3에서 새 정량 출처가 확보된 축은 R2 M → R3 H로 적극 상향. confidence 상승은 가중합을 바꾸지 않지만 D agent의 최종 ranking 안정성 평가에 사용됨.

### business_model 보정 (taxonomy Phase C 영향)
- L primary: T +0~1 (계약 기반 빠른 수익화).
- K primary: F +0~1, W -0~1.
- C primary (Captive/Catalog): IP +0~1.
- S primary: T 양극화.
- H primary: +0.1~0.2 보정 가능, F -0.5 가능.

R3 적용 사례: item_002·item_021의 K primary는 catalog 진입 명분 유지 → F·W 보정 없음(이미 raw에 반영). item_007/008은 L primary → T·confidence 상향 정당화. item_005의 K/L → L 격상 검토는 R3 카드에 메모하되 본 라운드 raw 점수에는 미반영(D 단계 후 결정).

### Short-list 규칙
가중합 상위 5개 + (6·7위가 5위와 0.2 이내 시) → 최대 7개.

---

## 전체 스코어 표 (R3, 23개)

| rank | id | 이름 | M | F | R | W | IP | T | weighted | short | delta R2→R3 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | item_002 | Engineered mTG (ADC) | 5(H) | 4(M) | 5(H) | 3(M) | 4(H) | 4(M) | **4.30** | ✓ | +0.10 |
| 1 | item_008 | Peptiligase / OaAEP1 C247A | 5(H) | 4(H) | 5(H) | 3(M) | 4(H) | 4(H) | **4.30** | ✓ | 0.00 |
| 3 | item_021 | cGMP Sortase A / OaAEP1 (radioligand) | 4(H) | 4(H) | 5(H) | 5(H) | 4(H) | 3(M) | **4.25** | ✓ | +0.15 |
| 4 | item_007 | Engineered RNA ligase | 4(H) | 4(M) | 5(H) | 4(M) | 4(H) | 3(M) | **4.10** | ✓ | 0.00 |
| 5 | item_003 | Engineered Sortase A | 4(M) | 4(H) | 5(H) | 3(M) | 3(M) | 4(M) | **3.95** | ✓ | 0.00 |
| 5 | item_005 | EndoS2 glycosynthase | 4(H) | 4(H) | 5(H) | 3(H) | 3(M) | 4(M) | **3.95** | ✓ | 0.00 |
| 7 | item_017 | Inorganic pyrophosphatase (IVT helper) | 4(H) | 5(H) | 5(H) | 2(H) | 2(M) | 4(M) | **3.90** | ✓ | 0.00 |
| 8 | item_006 | Engineered T7 RNAP | 4(H) | 4(H) | 5(H) | 2(H) | 3(M) | 4(M) | **3.80** |   | 0.00 |
| 9 | item_009 | Engineered PAM | 4(M) | 2(M) | 5(H) | 5(H) | 4(M) | 2(L) | **3.75** |   | 0.00 |
| 10 | item_004 | FGE (aldehyde-tag) | 3(M) | 3(M) | 5(H) | 4(M) | 4(M) | 3(L) | **3.65** |   | 0.00 |
| 10 | item_022 | dsRNA-specific nuclease | 3(M) | 3(M) | 5(H) | 4(H) | 4(M) | 3(M) | **3.65** |   | 0.00 |
| 12 | item_016 | FCE::T7RNAP fusion | 4(H) | 3(M) | 5(H) | 2(H) | 3(M) | 4(M) | **3.60** |   | 0.00 |
| 13 | item_015 | EfHyl8 PL8 hyaluronate lyase | 4(M) | 3(M) | 3(M) | 4(H) | 4(H) | 2(L) | **3.40** |   | 0.00 |
| 13 | item_019 | USP/OTUB1 DUB cocktail | 3(M) | 4(M) | 4(M) | 3(M) | 3(M) | 3(L) | **3.40** |   | 0.00 |
| 15 | item_013 | High-fidelity Prime Editor | 3(M) | 3(M) | 4(M) | 4(M) | 3(M) | 3(L) | **3.35** |   | 0.00 |
| 16 | item_010 | IdeS/IdeZ (QC) | 3(M) | 4(H) | 4(M) | 2(H) | 2(M) | 4(M) | **3.25** |   | 0.00 |
| 16 | item_011 | PNGase F + ST/GalT suite | 3(M) | 4(H) | 4(M) | 2(H) | 2(L) | 4(M) | **3.25** |   | 0.00 |
| 18 | item_018 | CRBN/VHL E3 ternary | 4(H) | 3(M) | 4(M) | 2(H) | 2(M) | 3(M) | **3.20** |   | 0.00 |
| 18 | item_023 | TPD reagent cocktail | 4(H) | 3(M) | 4(M) | 2(H) | 2(M) | 3(M) | **3.20** |   | 0.00 |
| 20 | item_001 | Next-gen hyaluronidase | 5(H) | 3(M) | 3(M) | 2(H) | 2(M) | 2(L) | **3.15** |   | 0.00 |
| 21 | item_014 | AI-designed RFdiffusion enzyme | 3(L) | 2(M) | 4(M) | 3(M) | 5(M) | 2(L) | **3.10** |   | 0.00 |
| 21 | item_020 | LCC/cutinase/AI-PETase | 3(M) | 3(M) | 4(M) | 3(M) | 3(M) | 2(L) | **3.10** |   | 0.00 |
| 23 | item_012 | Cas12/Cas13 + RPA Dx | 3(M) | 3(M) | 3(M) | 2(H) | 2(M) | 3(L) | **2.75** |   | 0.00 |

(동점 시 id 순. 검증: 가중합 = 0.25·M+0.20·F+0.20·R+0.15·W+0.10·IP+0.10·T.)

---

## R2→R3 변동 사유 (delta ≠ 0 항목)

### item_002 — Engineered mTG (ADC): 4.20 → **4.30** (delta +0.10)
- **사유 1 (IP축 3→4, confidence M→H)**: R3 §9.3 mTG cluster IP carve-out 명확화 — Ajinomoto AJICAP은 mTG-free chemical conjugation(Lys248-affinity peptide reagent)으로 mTG 카테고리와 직접 충돌 없음(`[AJICAP2023][H]`); Zedira mTG handbook은 reference info 위주로 자체 권리 약함; Hzymes는 commodity catalog. **Araris RKAA-peptide linker는 native antibody에 engineering-free mTG 적용**으로 새로운 carve-out 명분(`[ABT2025 Araris][Araris MMAE CD79b][H]`). US11786603 narrow-specificity 변이체 white-space 추가. IP를 3→4로 상향, confidence M→H.
- **사유 2 (M축 confidence M→H)**: ADC TAM $13.51B (2025) → $32.66B (2035, CAGR 9.23%) 2개 출처 교차(`[Towards Healthcare 2025 ADC][GlobeNewswire 2025 ADC]`) + Lonza Synaffix 통합 + Samsung-Araris 펀드 투자가 mTG 진영 직접 자본 흐름. M=5 유지, confidence M→H.
- 산식: 0.25·5+0.20·4+0.20·5+0.15·3+0.10·4+0.10·4 = 4.30.

### item_021 — cGMP Sortase A / OaAEP1 (radioligand): 4.10 → **4.25** (delta +0.15)
- **사유 1 (W축 4→5, confidence H 유지)**: R3 §9.6 NBE SMAC (WO2014140317A1, Boehringer Ingelheim 자본)은 **ADC sortase 영역 한정**이며 radioligand peptide-chelator 영역에는 직접 청구항 적용 없음(`[NBE SMAC WO2014140317A1][H]`). USPTO 10556024(sortase 18F radiolabeling)는 chelator-tag 변이체로 carve-out 가능. **radioligand peptide-chelator white-space 직접 경쟁자 미확정 → W=4→5**. Radioligand TAM $2.6B (2025) → $4.8B (2030, CAGR 13.1%) 정량 확정(`[GlobeNewswire 2026 RLT][Precedence RLT]`).
- **사유 2 (IP축 confidence M→H)**: NBE SMAC carve-out 명확화 + USPTO 10556024 carve-out 가능성 + radioligand application white-space. IP=4 유지, confidence M→H.
- 산식: 0.25·4+0.20·4+0.20·5+0.15·5+0.10·4+0.10·3 = 4.25.

(나머지 21개 후보 delta = 0.00. R3 신호 영향은 confidence 태그로만 반영.)

---

## 주요 confidence 상향 (raw score 미변동 항목)

### item_005 — EndoS2 glycosynthase (3.95 유지, confidence 대폭 상향)
- **M축 M→H**: **Lonza Advanced Synthesis Synaffix GlycoConnect 통합 (2026-02-19)** = EndoS2 enzymatic glycan remodel + click이 ADC GMP 라인의 명시 step으로 진입(`[Lonza2026 AS][ADCReview2026 Lonza][H]`). dpADC 확장(`[Synaffix2026 dpADC]`). ADC TAM 정량(`[Towards Healthcare 2025 ADC][GlobeNewswire 2025 ADC]`). 3개 이상 출처.
- **W축 M→H**: Synaffix는 Lonza/BMS 라이선스 독점이나 EndoS2 D184M 변이체(Genovis FabRICATOR-Z/GlycINATOR)·EndoF/EndoH 대체 fold carve-out 여지로 W=3 유지하되 confidence H 상향.
- raw score 3.95 유지하나 **rank stability 측면에서 Top-5 안정성 크게 향상**. business_model L primary 격상 검토는 D 단계로 이관.

### item_007 — Engineered RNA ligase (4.10 유지, IP confidence M→H)
- **IP축 confidence M→H**: Codexis–Merck $37.8M Supply Assurance Agreement(2025-10, `[SEC 8-K Codexis 2025Q3][H]`) + Codexis Q1 2025 첫 ECO Synthesis 수주(`[SEC 8-K Codexis 2025Q1]`) + Roche dsDNA ligase license $6.0M Q1-2024 인식(`[Codexis Q1-2025]`) + Bachem TIDES 2025 co-presentation. Codexis variant 청구항 + Roche 글로벌 라이선스가 IP=4 정량 근거 강화.
- W축 4→5 고려했으나 radioligand는 별도 카드(item_021)로 분리되어 있어 RNA ligase 본 영역은 Codexis 진영 dominance — W=4 유지.

### item_008 — Peptiligase / OaAEP1 C247A (4.30 유지, IP·F·T confidence H로 상향)
- **IP축 confidence M→H**: US10883132B2(Fresenius Kabi Ipsum)는 EnzyPep peptiligase 패밀리(S8 family serine protease, subtilisin BPN' Y217 variant)에 한정. OaAEP1 C247A는 C13 family asparaginyl endopeptidase(cysteine protease) — **fold·family·EC class·메커니즘 완전 다름 → 청구항 carve-out 자명**(`[US10883132B2 Fresenius][US11795488B2][Nature Comm Chem 2024 OaAEP1][H]`).
- **T축 confidence M→H**: FDA Research-Grade Peptide guidance 2026-01 enforce 그대로 + Bachem CEPS technology webinar + PolyPeptide Vinnova 1M SEK 그린 GLP-1(`[Bachem CEPS][PolyPeptide Vinnova][H]`).
- **F축 confidence M→H**: Bachem CEPS는 SPPS 대비 비용 -50%, 수율 >2x 정량 데이터 확보.
- raw score 4.30 유지, **Top 1 자리 안정화**.

### item_015 — EfHyl8 PL8 hyaluronate lyase (3.40 유지, IP H 강화)
- **IP축 confidence H 유지 + 강화**: Halozyme rHuPH20 (PH20, GH56, EC 3.2.1.35 glycosidase) vs EfHyl8 (PL8, EC 4.2.2.1 β-elimination lyase) — fold·메커니즘·EC class 완전 다름. **MDASE 청구항 회피 자명**(`[Halozyme rHuPH20 patent][Halozyme2025 lawsuit][H]`). Merck IPR 7건 청구 진행 = 일부 무효화 시 비PH20 진영 진입장벽 추가 하락. 학계 PL8 다양성 확장(SinHL, TcHly8B, YsHyl8A).
- F·T 정량(specific activity, SC diffusion zone cm²·hr⁻¹) 미확보로 raw score 3.40 그대로(R4 과제).

### item_017 — Inorganic pyrophosphatase (3.90 유지)
- M축 H 유지. Hzymes yeast PPase FDA DMF #036853 등록 = catalog 채택 확정(`[Hzymes DMF036853][H]`). GMP-Grade IVT $361.9M (2024) → $923M (2034, CAGR 10.4%)(`[InsightAce GMP-IVT][M]`). W=2 유지(시장 혼잡).

### item_006 — Engineered T7 RNAP (3.80 유지)
- R2 강등(4.05→3.80) 그대로 유효. IVT enzyme TAM $1.2B→$2.5B 정량 확정(`[Verified Markets 2025 IVT][M]`). 추가 강등 신호 R3에서 미발견.

### item_016 — FCE::T7RNAP fusion (3.60 유지, IP 강등 risk 모니터)
- NEB Faustovirus 패밀리 4국가 청구항(`[NEB FCE WO2021041260A1][NEB FCE CA3147797A1][NEB FCE AU2021424650A1][H]`) + H3C2 fusion 자체 청구. 신규 진입자는 linker engineering·Cap-2·dual MTase fusion 등 architecture carve-out만 가능. IP=3(M) 유지하나 R4에서 청구항 범위 추가 확인 시 강등(3→2) risk 약하게 존재.

---

## confidence 변화 매트릭스 (R2 → R3)

R3에서 confidence 전이가 발생한 축만 카운트.

| 후보 | 축 | R2 | R3 | 전이 |
|---|---|---|---|---|
| item_002 | M | H | H | (유지) |
| item_002 | IP | M | H | M→H |
| item_005 | M | M | H | M→H |
| item_005 | W | M | H | M→H |
| item_007 | IP | M | H | M→H |
| item_008 | IP | M | H | M→H |
| item_008 | F | H | H | (유지) |
| item_008 | T | M | H | M→H |
| item_021 | IP | M | H | M→H |

### 카운트
- **L → M**: **0건**.
- **M → H**: **7건** (item_002 IP / item_005 M / item_005 W / item_007 IP / item_008 IP / item_008 T / item_021 IP).
- **상향 후보 수(distinct id)**: 5개 (item_002, item_005, item_007, item_008, item_021).

R3 quantitative validation focus가 가장 강하게 작동한 5개 후보 = 모두 R2 short-list 멤버. 정량 출처 확보가 short-list 후보에 집중되어 **상위권 score 안정성 향상**.

---

## Short-list R3 변경 기록

**R2 short-list (7개)**: item_008(4.30), item_002(4.20), item_007(4.10), item_021(4.10 new), item_003(3.95), item_005(3.95), item_017(3.90 new).
**R3 short-list (7개)**: item_002(4.30 ▲+0.10), item_008(4.30), item_021(4.25 ▲+0.15), item_007(4.10), item_003(3.95), item_005(3.95), item_017(3.90).

| 변동 | id | weighted | 사유 |
|---|---|---|---|
| (member 동일) | 7개 모두 R2 short-list와 동일 | — | R3 정량/IP 보강은 7개 멤버의 confidence 상향에 집중. 신규 IN/OUT 없음. |

**Rank shifts within short-list**:
- item_002: rank 2 → **공동 1** (delta +0.10).
- item_008: rank 1 → **공동 1** (no delta but item_002와 동률).
- item_021: rank 3 (tie with item_007) → **단독 3** (delta +0.15).
- item_007: rank 3 → 4 (item_021에 밀림).
- item_003·005·017: 동일 rank 유지.

선정 룰: 가중합 상위 5개(item_002·008·021·007·003) + 6/7위가 5위(3.95)와 0.2 이내 → item_005(3.95), item_017(3.90) 포함, cap 7 도달. 8위 item_006(3.80)은 5위와 0.15 차이로 0.2 이내이나 cap 도달로 제외.

**누적 short-list (R1+R2+R3 중 2회 이상 등재)** — D agent 사용:
- item_002 (R1·R2·R3 3회) ★
- item_003 (R1·R2·R3 3회) ★
- item_005 (R1·R2·R3 3회) ★
- item_007 (R1·R2·R3 3회) ★
- item_008 (R1·R2·R3 3회) ★
- item_017 (R2·R3 2회)
- item_021 (R2·R3 2회)
- item_006 (R1만 1회) — R2에서 OUT.
- item_009 (R1만 1회) — R2에서 OUT.

cumulative short-list (≥2회) = **7개**. 매우 안정적인 ranking 수렴.

---

## Quality-gate 판정

### Top-5 weighted_score 표준편차 추적

| 라운드 | top-5 가중합 | 평균 | SD |
|---|---|---|---|
| R1 | 4.20, 4.20, 4.10, 4.05, 3.95 | 4.10 | **0.095** |
| R2 | 4.30, 4.20, 4.10, 4.10, 3.95 | 4.13 | **0.117** |
| R3 | 4.30, 4.30, 4.25, 4.10, 3.95 | **4.18** | **0.136** |

- **|ΔSD(R2→R3)| = |0.136 − 0.117| = 0.019** — 임계 0.15보다 훨씬 작음.
- ΔMean(R2→R3) = +0.05 (4.13 → 4.18). 상위권이 약간 더 응집(top 3가 4.25 이상으로 묶임) + bottom 2가 정체. 분포 변화는 평탄.

### 판정: **quality-gate 미발동.**

근거:
1. ΔSD 0.019는 임계 0.15의 약 13% 수준으로 충분히 안정 범위.
2. ±1 이상 raw score 변동 후보 없음(최대 |delta| = 0.15, item_021).
3. R3는 quantitative refinement focus였으므로 점수 분포가 안정적인 것은 의도된 결과 — D 단계(consolidated digest) 진행이 정당화됨.

### 다음 라운드 watch 항목 (필요 시 R4 트리거용)
- **item_006 T7 RNAP**: R3에서 추가 강등 신호 미발견했으나 CleanCap M6 출시 후 가격 변동 시 M축 재평가 필요. 누적 short-list 미진입 위험.
- **item_016 FCE::T7RNAP fusion**: NEB 패밀리 4국가 청구항 + H3C2 fusion 자체 청구 → IP 3→2 강등 risk 존재. USPTO 청구항 범위 추가 확인 권고.
- **item_001 vs item_015 (PH20 vs 비PH20)**: Merck IPR 7건 결과 (Halozyme MDASE 일부 청구항 무효화 시) 두 후보 간 점수 격차 좁힐 잠재.
- **item_015 EfHyl8**: specific activity/kcat/SC diffusion zone cm² 정량값 (full-text 403로 R3 미확보) 확보 시 F·T 상향 가능.

---

## R3 short-list 1-pager 신규 작성

**없음 (0개)**. R3 short-list 멤버는 R2와 동일 7개. 신규 진입 후보 없음 → 신규 1-pager 미작성.

기존 1-pager 위치:
- `candidates/item_002_engineered_mTG_for_ADC.md` (R1, R2)
- `candidates/item_003_engineered_sortase_A.md` (R1, R2)
- `candidates/item_005_endoS2_glycosynthase.md` (R1, R2)
- `candidates/item_007_engineered_RNA_ligase.md` (R1, R2)
- `candidates/item_008_peptiligase_OaAEP1.md` (R1, R2)
- `iterations/iter_02/candidates/item_017_inorganic_pyrophosphatase.md`
- `iterations/iter_02/candidates/item_021_cGMP_sortase_radioligand.md`

D agent(consolidated digest)는 위 카드에서 R3 점수·confidence·IP carve-out 메모를 통합 인용.

---

## Reference list

R3 landscape scan에서 인용한 출처 (`scope/pricing_sources.md` §5 인용 키 규칙). 전체 URL 매핑은 `iterations/iter_03/pipeline/01_landscape_scan.md` Reference list 섹션 참조. 본 표는 R3 스코어링에서 결정적으로 사용된 키만 정리.

### 빅파마·딜·M&A·SEC
- `[Lonza2026 AS]` — Lonza Advanced Synthesis Synaffix 통합 (item_005·002·003·021 M·W).
- `[ADCReview2026 Lonza]` — 동상.
- `[Synaffix2026 dpADC]` — dpADC dual-payload (item_005·004).
- `[Halozyme2025 FY]` — FY25 royalty $867.8M (item_001·015 M).
- `[Halozyme Q4-2025 transcript]` — 동상.
- `[Halozyme2025 lawsuit]` — vs Merck NJ District Court (item_015 IP).
- `[Halozyme rHuPH20 patent]` — US 7,767,429 PTE 2027-09-23 (item_015 IP).
- `[SEC 8-K Codexis 2025Q1]` — 첫 ECO Synthesis 수주 (item_007 IP).
- `[SEC 8-K Codexis 2025Q3]` — Codexis-Merck $37.8M Supply Assurance (item_007 IP).
- `[Codexis Q1-2025]` — TIDES 2025 co-presentation (item_007·008 T).
- `[Codexis Q3-2025]` — 동상.
- `[Alteogen royalty 2%]` — ALT-B4 2% net sales (item_001·015 IP/M).
- `[Biospectator2024 ALT-B4]` — 동상.
- `[Fierce Pharma AZ-Alteogen]` — AZ-Alteogen $1.35B (item_001·015).
- `[AZ2024 Fusion]` — AZ-Fusion $2.4B (item_021 M).
- `[ABCM 2025]` — 동상.

### CDMO·공급망·catalog
- `[Samsung Bio ADC]` — enzyme-mediated conjugation 명시 (item_002·005·021).
- `[Samsung Bio 2025Q2 IR]` — KRW 3.4T 신규 수주 (item_002·005·021 M).
- `[Samsung-Araris]` — Phrontline·Araris 펀드 (item_002 M·IP).
- `[WuXi XDC 2025 FY]` — backlog $1.49B (item_002·005·021 M).
- `[WuXi XDC H1-2025]` — 동상.
- `[Lonza Visp 2024]` — Ibex 4배 + 1,200L suite (item_005·002·003·021).
- `[BioProcessIntl Lonza]` — 동상.
- `[Aldevron Codex HiCap]` — directed-evolution T7 RNAP variant (item_006 M).
- `[Maravai2025 CleanCapM6]` — chemical analog 강세 (item_006·016).
- `[NEB M0658]` — Hi-T7 (item_006).
- `[Hzymes PPase]` — yeast PPase catalog (item_017 M).
- `[Hzymes DMF036853]` — FDA DMF #036853 (item_017 M).
- `[Tinzyme RNase Inhibitor]` — GMP RNase Inhibitor (item_017 W).
- `[Genovis GlycINATOR]` — 2,000 U $979 research grade (item_005).
- `[Bachem GLP-1]` — $1B+ CapEx (item_008 M).
- `[Bachem CEPS]` — peptiligase webinar (item_008 F·T).
- `[EnzyTag2025]` — commercial ligation kit (item_008).
- `[PolyPeptide Vinnova]` — 1M SEK 그린 GLP-1 (item_008 M·T).

### 학계·preprint·patents
- `[JAFC2025 SinHL]` — PL8 exolytic (item_015 W).
- `[Mol Cell Probes 2021 TcHly8B]` — PL8 pH 안정성 (item_015 W).
- `[YsHyl8A 2022]` — PL8 alkalophilic (item_015 W).
- `[ABT2025 Araris]` — RKAA-peptide linker (item_002 IP).
- `[Araris MMAE CD79b]` — 동상.
- `[US10883132B2 Fresenius]` — EnzyPep GLP-1 청구항 패밀리 (item_008 IP).
- `[US11795488B2]` — OaAEP1 ligation methods (item_008 IP).
- `[Nature Comm Chem 2024 OaAEP1]` — engineered recognition motifs (item_008 IP).
- `[NEB FCE WO2021041260A1]` — NEB Faustovirus 청구 (item_016 IP).
- `[NEB FCE CA3147797A1]` — 동상.
- `[NEB FCE AU2021424650A1]` — 동상.
- `[NBE SMAC WO2014140317A1]` — ADC sortase (item_021·003 IP carve-out).
- `[NBE SMAC PLOS]` — 동상.
- `[USPTO 10556024]` — sortase 18F (item_021 IP).
- `[US11786603 mTG]` — narrow-specificity 변이체 (item_002 IP).
- `[AJICAP2023]` — enzyme-free chemical (item_002 IP carve-out).
- `[Zedira MTG Handbook]` — reference (item_002).

### 시장 보고서·정량
- `[Towards Healthcare 2025 ADC]` — ADC $13.51B→$32.66B (item_002·005·003·004 M).
- `[GlobeNewswire 2025 ADC]` — 동상.
- `[Verified Markets 2025 IVT]` — IVT $1.2B→$2.5B (item_006·016·017·022 M).
- `[InsightAce GMP-IVT]` — GMP IVT $361.9M→$923M (item_017·006·016 M).
- `[GlobeNewswire 2026 RLT]` — RLT $2.6B→$4.8B (item_021 M).
- `[Precedence RLT]` — 동상.
- `[InsightAce GLP-1 CDMO]` — (item_008·009 M).
- `[Grand View 2024 TPD]` — TPD $544M→$1,685M (item_018·019·023 M).
- `[SNS Insider TPD]` — 동상.
- `[Emergen MGD]` — MGD 별도 sub-segment (item_018·023).
- `[SkyQuest PROTAC]` — PROTAC reagent $152M→$331M (item_018 M).
- `[StockTitan PFE]` — 동상.
- `[LifeSensors PA770]` — PROTAC ubiquitination kit ~$1.5k (item_018·023).
- `[Promega NanoBRET]` — 표준 TPD catalog (item_018·023 W).
- `[CST 99253]` — E3 sampler (item_018·023 W).
- `[EvaluatePharma Keytruda SC]` — peak $15.2B (item_001·015 M).

---

## 메타

| 항목 | 값 |
|---|---|
| run_id | 20260521-C |
| 실행일 | 2026-05-21 (UTC) |
| 누적 활성 후보 수 | 23 |
| 가중치 변경 | 없음 |
| short-list 멤버 | 7 (R2와 동일) |
| confidence 상향 (M→H) | 7건 (5개 후보) |
| ±1 이상 raw 변동 | 0건 |
| 최대 |delta| | 0.15 (item_021) |
| Top-5 SD R2→R3 | 0.117 → 0.136 (Δ=+0.019) |
| Quality-gate | **미발동** |
| 누적 short-list (≥2회) | 7개 (item_002·003·005·007·008·017·021) |
