# [D] 고객 / 응용분야 분석

> **조사 대상**: mRNA 기반 치료제 (functional protein replacement, 단 RNAi/siRNA 및 예방백신 제외) — in vivo gene editing 포함
> **기준일**: 2026-05-22
> **핵심 질문**: "이 modality가 실제로 어디에 쓰일 수 있고, 어디는 불가능한가?"

---

## D.1 질환 세그먼트 매핑 매트릭스 (★ 핵심 표)

판정 기준:
- **가능 (Feasible)**: Phase 3 진입 + 임상 PoC 확립, 또는 approved.
- **경계 (Borderline)**: Phase 1/2 PoC 시그널은 있으나 핵심 risk (immunogenicity, durability, delivery) 미해결.
- **불가능 (Infeasible)**: 임상 실패 이력 또는 modality 자체의 근본적 한계 (전달, 발현량, 세포 tropism).

| # | 세그먼트 | 환자 규모 (US/Global) | 현 SoC | 미충족 needs | mRNA 기술 feasibility | 임상 evidence (2026-05) | 판정 | 불가능/경계 시 정확한 원인 |
|---|---|---|---|---|---|---|---|---|
| 1 | **HAE (Hereditary Angioedema)** — in vivo CRISPR | US ~8,000 / Global 50K | Takhzyro(lanadelumab) 월투여, berotralstat 경구 | 평생 예방투약, breakthrough attack | ★★★★★ Hepatic KLKB1 KO, one-shot | **Phase 3 HAELO positive topline 2026-04-27** (Intellia lonvo-z), BLA H2 2026, 출시 H1 2027 | **가능 (highest)** | — |
| 2 | **ATTR amyloidosis (polyneuropathy/cardiomyopathy)** — in vivo CRISPR | US ~150K (ATTRwt+v) / Global 수십만 | Vutrisiran(siRNA), Tafamidis, Acoramidis | 진행 정지보다 reversal, one-shot | ★★★★★ Hepatic TTR KO | **Phase 3 MAGNITUDE 진행중** (nex-z, 2025-09 Grade 4 liver AE로 일시 hold → 2026-03-02 FDA hold 해제), MAGNITUDE-2 enrollment 90%+ | **가능 (단, hepatotoxicity risk 모니터링 필수)** | 1건의 Grade 4 간독성 → modality 전반의 hepatic risk 환기 |
| 3 | **HeFH / ASCVD (PCSK9)** — in vivo base editing | HeFH US ~1.3M, ASCVD 수천만 | Statin, PCSK9 mAb(Repatha/Praluent), inclisiran (siRNA) | 평생 복약 순응도, one-shot 대안 | ★★★★ Hepatic PCSK9 base edit | Verve VERVE-102 Heart-2 Phase 1b: LDL-C 평균 -53%, 최대 -69%; Phase 2 시작 H2 2025 | **가능 (경계 — 대형 시장이라 안전성 bar 매우 높음)** | One-time, permanent edit → 부작용 reversibility 없음. 대규모 cardiovascular outcome trial 필요. |
| 4 | **HoFH / refractory hypercholesterolemia (ANGPTL3)** — in vivo base editing | HoFH ~1,300 US (rare) | Evkeeza(evinacumab), LDL apheresis | One-shot, 비간성 ANGPTL3 inhibition 부재 | ★★★★ Hepatic ANGPTL3 KO | Verve VERVE-201 Pulse-1 Phase 1b 진행중 | **경계** | 환자 규모 작고 Phase 1b 단계, LNP의 LDLR-independent uptake 필요 (해결됨) |
| 5 | **AATD (Alpha-1 Antitrypsin Deficiency)** — base editing / RNA editing | US ~100K (PiZZ) | Augmentation therapy (Prolastin 주 1회 IV) | 폐기능 보호, 간질환 동시 해결 | ★★★ Base editing (Beam), RNA editing (Wave/Korro) | **Beam BEAM-302 Phase 1/2: 60mg+ 단회투여로 mutant AAT 80% 감소 + 정상 AAT 생성**, pivotal cohort H2 2026 / Wave WVE-006 SC 투여 / Korro KRRO-110 실패 → KRRO-111 재시작 | **가능 (Beam만)** | RNA editing 접근(Korro)은 임상에서 PoC 실패. Base editing(Beam)은 강한 시그널. |
| 6 | **Hepatic UCD: OTC deficiency** | US ~1,000–2,000 | 단백 제한식, ammonia scavenger, 간이식 | 안전한 ureagenesis 회복 | ★★★ Hepatic OTC mRNA (multi-dose) | **Arcturus ARCT-810 Phase 2** (interim 2025-06-30): RUF 29% → 43.7%, 2/3 환자 RUF >50%, ammonia 정상화 | **가능 (Phase 2 PoC 확립, 단 chronic redosing 필요)** | — |
| 7 | **Hepatic organic acidemia: PA (Propionic Acidemia)** | US ~200–500 / Global 매우 희소 | 단백 제한식, 카르니틴, 간이식 | metabolic decompensation 방지 | ★★★ Dual mRNA (PCCA+PCCB), multi-dose | **Moderna mRNA-3927 (Recordati 파트너) Phase 1/2 registrational, target enrollment 도달, data readout 2026 예상.** 초기: 대사붕괴 risk -70% | **가능 (경계 — pivotal data 대기)** | 두 단백질(α/β) 동시 발현 필요, 평생 IV redosing |
| 8 | **Hepatic MMA (Methylmalonic Acidemia)** | US ~1,000 | 단백 제한식, 간/신이식 | 동상 | ★★★ Hepatic MUT mRNA | **Moderna mRNA-3705 FDA START 프로그램 선정, registrational study 2026 개시 예정** | **가능 (경계)** | Phase 1/2에서 PD 시그널 보고. Pivotal 시작 직전. |
| 9 | **GSD1a (Glycogen Storage Disease type 1a)** | US ~600 | 야간 cornstarch, 빈번 식이, 간이식 | 정상혈당 유지, 간선종 예방 | ★★ Hepatic G6PC mRNA | **Moderna mRNA-3745 Phase 1/2: 2025-11 Phase 2 미진행 결정 (drop)** | **불가능 (현시점)** | Moderna 자체 deprioritization — 효능/안전성 또는 chronic redosing burden 부족. 학계 잔존 관심. |
| 10 | **PKU (Phenylketonuria)** | US ~16,500 | 식이제한, Kuvan(sapropterin), Palynziq(pegvaliase 주사) | 식이자유, palynziq 면역반응 회피 | ★★ Hepatic PAH mRNA | Moderna 파이프라인 게재(전임상~Phase 1 추정), 임상 단계 공시 데이터 빈약 [추정] | **경계** | Palynziq가 이미 SoC 강력 → mRNA의 차별화 bar 높음. |
| 11 | **Crigler-Najjar type 1** | Global <200 | 광선요법(평생 야간 12h+), 간이식 | 광선요법 대체 | ★★ Hepatic UGT1A1 mRNA | **mRNA-3351 (Moderna→IRDiRC 무상기증)** Phase 1 — 현재 활성 임상 정보 제한적 [미확인] | **경계** | 시장 너무 작아 commercial sustainability 낮음. |
| 12 | **Hemophilia A/B** | US A: 20K, B: 4K | Factor VIII/IX, emicizumab(A), AAV 유전자치료(Hemgenix, Roctavian) | One-shot, 항체 환자 | ★ mRNA F8/F9 가능하나 AAV 1회투여 vs mRNA 평생투여 비교열위 | mRNA 임상 단계 프로그램 부재 [미확인] | **경계 → 불가능** | AAV(Hemgenix $3.5M 1회) 및 emicizumab(SC 주 1회)이 이미 강력. mRNA의 niche 협소. |
| 13 | **Factor VII deficiency** | Global <2,000 | rFVIIa (NovoSeven) on-demand | bleed prophylaxis | ★ Hepatic F7 mRNA 가능 | 임상 없음 [미확인] | **경계** | 시장 극소형. |
| 14 | **CFTR / Cystic Fibrosis (inhaled mRNA)** | US ~40K, 그중 ~10% Trikafta 부적격 | Trikafta(elexa/teza/iva) 90%+ 환자 cover | Trikafta 부적격 ~10% (class I mutations) | ★ Inhaled mRNA delivery | **Translate Bio MRT5005 (2021): Phase 1/2 efficacy 실패** / **Vertex VX-522 (2025-05): 폐 염증 tolerability 이슈로 Phase 1/2 중단·프로그램 종료** | **불가능 (현시점)** | **두 차례의 inhaled mRNA 시도 모두 실패.** LNP의 폐 inflammation, 점액·섬모 장벽이 핵심. Trikafta 시장 점유 강력. |
| 15 | **Primary ciliary dyskinesia (PCD)** | US ~5,000 | symptomatic only | 근본치료 부재 | ★ inhaled mRNA (DNAH/DNAI 등 매우 큰 cDNA) | 전임상 [추정] | **불가능** | CFTR보다 더 큰 단백질·다양한 변이 + CFTR 실패의 동일 delivery 장벽. |
| 16 | **Cardiac regeneration / VEGF (post-MI, HFpEF)** | 수백만 (큰 시장) | GDMT (ARNI, SGLT2i, MRA, β-blocker), CABG, devices | 심근재생 자체 | ★ Intramyocardial VEGF mRNA | **AZD8601 EPICCURE Phase 2a (2021): 1차 안전성 충족, exploratory endpoint trend.** 그러나 **AstraZeneca 2022 drop**, Moderna 2023 drop. | **불가능 (현시점)** | 임상 PoC efficacy 부족 + 투여경로(CABG 동시 주사) impractical. |
| 17 | **In vivo CAR-T (B-cell autoimmune: SLE, RA, MS)** | SLE US ~300K | belimumab, anifrolumab, immunosuppressants; ex vivo CD19 CAR-T 임상 | one-shot deep B-cell reset without lymphodepletion | ★★★★ tLNP + CAR mRNA (CD8 또는 CD3 targeted) | **MagicRNA HN2301 SLE 5명, NEJM 2026** (in vivo CAR-T proof) / **Capstan CPTX2309 Phase 1 2025-06 start** (AbbVie $2.1B 인수, 2025-06) / 다수 follow-on | **가능 (가장 hot한 신흥 영역)** | — (단, durability/안전성 확립 전) |
| 18 | **In vivo CAR-T (B-cell oncology: NHL, ALL, CLL)** | US NHL ~80K/yr | ex vivo CAR-T (Yescarta, Kymriah, Breyanzi) | manufacturing-free, ramp-up, access | ★★★ tLNP CAR mRNA | NCT07362602 (CD20 in vivo), Orbital OTX-201 (BMS $1.5B 2025-10) Phase 1 추정 | **경계** | 기존 ex vivo CAR-T이 강력. 효능 동등성 입증 필요. |
| 19 | **Cancer immuno-oncology — intratumoral mRNA cytokine** | 다수 고형암 | Checkpoint, chemo, RT | non-vaccine immunostim, cold tumor → hot | ★★ Intratumoral self-replicating mRNA (IL-12 등) | **Strand STX-001 Phase 1 ASCO 2025**: 안전성+anti-tumor signal in CPI-refractory | **경계** | Intratumoral 한정, 전이암 systemic effect 미증명. |
| 20 | **Cancer — systemic mRNA-encoded bispecific/checkpoint** | 다수 | mAb 기성품 | manufacturing scale, polyclonality | ★★ Systemic LNP, hepatic expression of secreted protein | mRNA-encoded TCE Phase 1 first-in-human 안전성 보고 (논문 다수); BNT327은 mRNA 아님 — protein bispecific. mRNA-encoded TCE는 BioNTech/CureVac 전임상 단계 다수 | **경계** | 기존 protein bispecific(BNT327 등)과 차별화 필요. Hepatic 발현 protein이 systemic exposure 충분한지 검증중. |
| 21 | **CNS (rare neurometabolic: e.g., NPC, MPS, Rett)** | 수백–수천 | enzyme replacement (일부), 대증 | BBB 투과 | 0 BBB 투과 LNP 부재, intrathecal LNP 데이터 극소 | 임상 mRNA 프로그램 부재 [미확인] | **불가능 (현시점)** | **BBB 절대 장벽**. AAV9 systemic, IT AAV가 SoC 경쟁. |
| 22 | **Muscle (DMD, LGMD)** | DMD US ~12K | corticosteroid, AAV micro-dystrophin (Elevidys) | 전신 근육 도달 | 0 LNP 근육 tropism 미개발 | 임상 부재 | **불가능 (현시점)** | LNP의 muscle delivery efficiency 1% 미만. Dystrophin은 너무 큰 단백질이라 micro-construct 필요, AAV가 우위. |
| 23 | **Kidney (Alport, ADPKD)** | ADPKD 미국 ~140K | tolvaptan(ADPKD), 신이식 | 신장 특이 delivery | 0 LNP의 신장 tropism 부재 | 임상 부재 | **불가능 (현시점)** | Glomerular filtration로 LNP 신장 도달 불가, peritubular endocytosis 비효율. |
| 24 | **Eye (LCA, RP, AMD)** | LCA 2,000 US | Luxturna(AAV2 RPE65), 대증 | 광수용체/RPE 표적 | ★★ Intravitreal/subretinal LNP — biodistribution 우회 | 임상 mRNA-LNP 안구 프로그램 전임상 단계 [추정] | **경계** | AAV(Luxturna)가 이미 approved. mRNA 차별화 = 비통합·재투여 가능, 그러나 임상 미진. |
| 25 | **Dermatology (epidermolysis bullosa 등)** | DEB US ~1,000 | Vyjuvek(HSV vector topical) | systemic skin coverage | ★ Topical/SC LNP | mRNA 임상 부재 | **경계 → 불가능** | Vyjuvek (KB-103) topical viral vector approved 2023이 이미 SoC. |
| 26 | **Sickle cell / β-thalassemia (ex vivo)** | SCD US ~100K | hydroxyurea, transfusion, BMT, **Casgevy** | 만성 통증, accessibility | N/A — Casgevy는 ex vivo CRISPR (mRNA encoded Cas9), in vivo mRNA 아님 | Casgevy 2023-12 FDA 승인, $2.2M | **(scope 외) 가능 ex vivo** | In vivo mRNA로의 SCD 치료는 골수 표적 LNP 미해결로 **불가능**. |
| 27 | **HBV chronic (functional cure)** | Global 296M | nucleos(t)ide analog, IFN | HBsAg seroclearance | ★★ Hepatic anti-HBs mRNA / siRNA combo (참고) | mRNA-encoded anti-HBsAg 전임상 (PMC9426588) | **경계** | siRNA(VIR-2218, JNJ-3989)와의 경쟁. |

> 총 27개 세그먼트 매핑. **가능 6, 경계 12, 불가능 9** (Casgevy ex vivo는 별도).

---

## D.2 세그먼트별 상세 분석

### D.2.1 Hepatic protein replacement — 가장 합리적인 first wave

**왜 hepatic이 유리한가**: LNP의 ApoE-mediated LDLR 흡수 → 간세포 자연 tropism. 발현이 시작되는 데 4–8h, peak 24–48h, 단백질에 따라 1–4주 지속. Multi-dose가 필수이며 IV infusion이 일반적.

**핵심 프로그램 4종 (2026-05)**:
1. **Arcturus ARCT-810 (OTC deficiency)** — Phase 2 multi-dose interim (2025-06): RUF 29% → 43.7%; ammonia 정상화 28일 지속. 3시간 IV regimen으로 IRR 해소. 강한 시그널.
2. **Moderna mRNA-3927 (PA)** — Phase 1/2 registrational, 등록 완료, 2026 readout 예정. 대사붕괴 risk -70%.
3. **Moderna mRNA-3705 (MMA)** — FDA START 프로그램 (희귀질환 가속화), registrational 2026 시작.
4. **Moderna mRNA-3745 (GSD1a)** — **2025-11 drop**. 핵심 경계 신호 — 모든 hepatic monogenic이 mRNA로 성공하는 것은 아님.

**Hemophilia/Crigler-Najjar 관점**: AAV·기성 SoC가 이미 강해 mRNA niche 협소.

### D.2.2 In vivo gene editing (Hepatic) — 차세대 메가 카테고리

**HAE (Intellia lonvo-z, 구 NTLA-2002)**: 2026-04-27 Phase 3 HAELO topline 양성, **세계 최초 in vivo gene editing 임상 성공**. BLA H2 2026, US launch H1 2027 목표. ★ in vivo 편집의 reference proof point.

**ATTR (Intellia nex-z, 구 NTLA-2001)**: MAGNITUDE / MAGNITUDE-2 Phase 3. 2025-09 Grade 4 간독성(transaminase + bilirubin) 1건 → 일시 hold. **2026-03-02 FDA hold 해제**, enrollment 재개중. 1건의 SAE가 modality 전반의 hepatotoxicity 환기.

**Verve VERVE-102 (PCSK9)**: Heart-2 Phase 1b — LDL-C 평균 -53%, 최대 -69%, 안전성 양호. Phase 2 진입. 대형 시장 (HeFH/ASCVD) 진입이 진정한 commercial test.

**Beam BEAM-302 (AATD)**: Phase 1/2에서 mutant AAT -80%, normal AAT 생성 — 첫 dual readout (KO + KI 효과). Pivotal H2 2026.

### D.2.3 Pulmonary CFTR — 두 번의 실패, 현재 동결

- **Translate Bio MRT5005 (Sanofi 인수 전)**: 2021 Phase 1/2 ppFEV1 개선 실패. 안전성 OK.
- **Vertex VX-522 (Moderna 파트너)**: 2025-05 폐 염증 tolerability 이슈, 2025년 후반 **프로그램 종료**. "지속적이고 해결 불가" — LNP의 폐 inflammation 본질적 한계.
- **결론**: 현재 inhaled mRNA로 CFTR replacement는 **infeasible**. Trikafta가 90% 환자 cover 중이라 unmet need도 ~10%로 축소. Next-gen LNP가 필요.

### D.2.4 Cardiac regeneration — 임상 실패로 사실상 종료

- **AZD8601 (AstraZeneca + Moderna)**: EPICCURE Phase 2a — 1차 안전성 OK, exploratory endpoint trend만. **AstraZeneca 2022 drop, Moderna 2023 drop**. CABG 동시 직접 주사라는 투여경로 자체가 비현실적.

### D.2.5 In vivo CAR-T / oncology — 가장 hot한 신흥 영역

- **MagicRNA HN2301 SLE (NEJM 2026)**: 5명 RR-SLE, 비-lymphodepleting, IV LNP→CD8 표적, **B-cell 1주 내 depletion, 안전성 양호**. In vivo CAR-T 첫 임상 PoC.
- **Capstan CPTX2309**: Phase 1 시작 2025-06, B-cell 자가면역 표적. **AbbVie 2025-06 $2.1B 인수** — 빅파마의 modality 검증.
- **Orbital OTX-201 (CD19 CAR)**: **BMS $1.5B 인수, 2025-10**, circRNA + LNP.
- **임상적 의미**: ex vivo CAR-T의 leukapheresis·lymphodepletion·6주 대기·$500K cost를 우회. 1회 IV infusion으로 transient CAR 발현 → B-cell reset → 면역 reconstitution. 만성 자가면역(SLE, RA, MS, type 1 DM, myasthenia)으로 확장 가능.
- **Strand STX-001 (Intratumoral IL-12 self-replicating mRNA)**: ASCO 2025, CPI-refractory 고형암에서 안전성+anti-tumor signal. Intratumoral 한정.

### D.2.6 CNS / Muscle / Kidney / 기타 hard targets — 현시점 불가능

- **CNS**: BBB는 LNP의 절대 장벽. Intrathecal LNP 데이터 극히 제한. AAV9 systemic이 reference modality. → **불가능**.
- **Muscle (DMD 등)**: LNP의 근육 tropism <1%. Dystrophin 크기상 micro-construct만 가능 → AAV가 이미 점유. → **불가능**.
- **Kidney**: 사구체 여과로 LNP 도달 불가, 세뇨관 endocytosis 비효율. → **불가능**.
- **Eye**: intravitreal/subretinal로 biodistribution 우회 가능 → 가능성 있으나 AAV(Luxturna)가 이미 cover. → **경계**.
- **Dermatology**: Vyjuvek(topical HSV)이 EB에서 SoC. mRNA niche 협소. → **경계**.

---

## D.3 Big Pharma 파트너 perspective

| 빅파마 | mRNA 치료제 노출 (2026-05) | 신호 |
|---|---|---|
| **Sanofi** | Translate Bio 인수($3.2B, 2021) — CF MRT5005 실패, 인플루엔자 mRNA 우선. 치료제는 후순위. | 유지 (백신 중심) |
| **AstraZeneca** | AZD8601 drop (2022), Moderna 파트너십 축소 | **탈출** |
| **Moderna** | 자체 portfolio (PA/MMA/PKU/CN-1/GSD1a). GSD1a drop(2025-11), CF VX-522 drop(2025) | 부분 retrenchment, rare disease만 유지 |
| **Merck** | Moderna 개인화 cancer vaccine (mRNA-4157/INT) — vaccine scope (제외) | (scope 외) |
| **AbbVie** | **Capstan $2.1B 인수 (2025-06)** — in vivo CAR-T | **신규 진입, 강한 commitment** |
| **BMS** | **Orbital $1.5B 인수 (2025-10)** — circRNA CAR / BioNTech BNT327 파트너십 (mRNA 아님) | **신규 진입** |
| **Eli Lilly** | **Orna Therapeutics 인수 (최대 $2.4B, 2026-02)** — circRNA + 신규 LNP | **신규 진입** |
| **Vertex** | VX-522 CF 프로그램 종료(2025); Casgevy(ex vivo CRISPR) 상업화 | mRNA in vivo 후퇴 |
| **CSL** | 유전질환·혈액제제 강점; mRNA 직접 노출 제한적 [미확인] | 관망 |
| **GSK** | Wave WVE-006 (AATD) 권리 반환 — **이탈** | 이탈 |
| **BioNTech** | **CureVac 인수 (2025-12)** — mRNA 통합; oncology 중심 | strong commitment |

**해석**: ① 백신·자체 hepatic protein replacement는 Moderna 단일 leader, ② **in vivo cell engineering (CAR-T)이 2025–2026 빅파마 자본의 hottest 카테고리** (AbbVie, BMS, Lilly 신규 진입), ③ CF·cardiac은 빅파마 이탈.

## D.4 Payer / 가격 perspective

| 모달리티 | 가격 benchmark | 투여빈도 | Total cost of care (5–10년) |
|---|---|---|---|
| **ERT** (예: Cerezyme, Myozyme) | $300–500K/yr | 2주 1회 IV | $3–5M (10년) |
| **AAV one-shot** (Hemgenix $3.5M, Roctavian, Luxturna $850K, Casgevy $2.2M ex vivo) | $850K–$3.5M | 1회 | $0.85–3.5M (durability 가정) |
| **Chronic mRNA (예상)** | $250–500K/yr [추정] | 2–8주 1회 IV | $2.5–5M (10년) [추정] |
| **In vivo gene editing (Intellia lonvo-z 예상)** | $1–2.5M [추정] | 1회 | $1–2.5M (lifetime) [추정] |

**Payer 핵심 우려**:
- Chronic mRNA: AAV 1회 대비 정당화 어려움. Differentiator = redosable(항체 반응 시 중단 가능), 비통합, 소아 안전 — 이를 가격에 반영.
- In vivo edit: AAV one-shot과 직접 경쟁. **HAE에서 lonvo-z가 first proof**: Takhzyro $700K/yr·평생 vs lonvo-z 1회 $1–2.5M [추정] → 2–4년 payback. 강력.
- 희귀질환 orphan 인센티브 (Priority Review Voucher, 7년 시장독점, 50% tax credit) 유지.

## D.5 채택 장벽 (Customer side)

1. **Physician education**: 만성질환 IV centers, 대사질환 specialist 채널 (PA/MMA/OTC)는 매우 좁음. ERT infusion infrastructure 재사용 가능.
2. **Infusion infrastructure**: 1–3h IV — 기존 ERT centers 그대로 활용. In vivo edit은 단회투여로 capacity 낮음.
3. **Immune monitoring**: anti-LNP IgG/IgM, anti-PEG ADA, 보체 활성화(CARPA) 모니터링 필요. 만성 redose에서 critical.
4. **Anti-LNP ADA management**: 현재 mitigation = premedication (steroid/antihistamine), 차세대 LNP (Lipid 829 등 immune-cell tropic), N1-methylpseudouridine optimization. 그러나 cumulative exposure data 빈약.
5. **Hepatotoxicity risk**: nex-z Grade 4 case (2025-09) — modality 전반의 monitoring template 필요.
6. **소아·임신 사용**: 거의 모든 hepatic 적응증 환자는 소아 시작 → safety bar 매우 높음.
7. **Rare disease patient ID·flow**: PA/MMA/OTC는 신생아 스크리닝 + 전문 metabolic center 의존 → patient finding이 진입장벽이자 moat.

## D.6 임상 단계별 핵심 프로그램 매트릭스 (★ 핵심 표)

| 단계 | 프로그램 | 회사 | 적응증 | 최근 데이터 | 다음 마일스톤 |
|---|---|---|---|---|---|
| **승인 (in vivo therapeutic mRNA)** | — | — | **없음** | — | — |
| **승인 (ex vivo, mRNA-Cas9)** | Casgevy (exa-cel) | Vertex/CRISPR | SCD, β-thal | 2023-12 FDA 승인 | 상업화 |
| **BLA 준비** | **Lonvo-z (구 NTLA-2002)** | Intellia | HAE | **Phase 3 HAELO positive 2026-04-27** | BLA H2 2026, launch H1 2027 |
| **Phase 3** | Nex-z (구 NTLA-2001) | Intellia | ATTRv-PN, ATTR-CM | MAGNITUDE 진행중 (hold 해제 2026-03) | enrollment 완료 H2 2026 |
| **Phase 2 (pivotal-bound)** | mRNA-3927 | Moderna/Recordati | PA | Registrational target enrollment 도달 | Data readout 2026 |
| **Phase 2** | ARCT-810 | Arcturus | OTC deficiency | RUF 29→43.7%, ammonia 정상화 (2025-06) | Phase 3 결정 |
| **Phase 2 (시작)** | mRNA-3705 | Moderna | MMA | FDA START selected | Pivotal 2026 시작 |
| **Phase 1b/2** | BEAM-302 | Beam | AATD | 60mg+ → mutant -80%, normal AAT 생성 | Pivotal cohort H2 2026 |
| **Phase 1b→2** | VERVE-102 | Verve | HeFH (PCSK9) | LDL-C -53% 평균 / -69% max | Phase 2 진행 |
| **Phase 1b** | VERVE-201 | Verve | HoFH/refractory (ANGPTL3) | 진행중 | H2 2025 update |
| **Phase 1** | CPTX2309 | Capstan (AbbVie) | B-cell autoimmune | dosed 2025-06 | Dose escalation |
| **Phase 1** | OTX-201 | Orbital (BMS) | CD19 CAR oncology | dosed 추정 2025–2026 | Initial readout |
| **Phase 1** | STX-001 (intratumoral) | Strand | Advanced solid tumors | ASCO 2025: 안전성 + anti-tumor signal | Combo with pembro |
| **Phase 1 (자가면역)** | HN2301 | MagicRNA | SLE refractory | NEJM 2026: B-cell depletion + 활성도 감소 | Dose-expansion |
| **Phase 1** | WVE-006 (RNA editing) | Wave | AATD | SC 투여 진행 | 임상 update |
| **종료/중단** | VX-522 | Vertex/Moderna | CF | 폐 염증 → 2025 program 종료 | — |
| **종료/중단** | mRNA-3745 | Moderna | GSD1a | 2025-11 deprioritized | — |
| **종료/중단** | AZD8601 | AZ/Moderna | Heart failure (VEGF) | 2022/2023 drop | — |
| **종료/중단** | MRT5005 | Translate Bio (Sanofi) | CF | Phase 1/2 efficacy 실패 | — |
| **종료/중단** | KRRO-110 (RNA editing) | Korro | AATD | Phase 1 PoC 미달 | KRRO-111로 재시작 |

---

## 핵심 출처 목록

- [Intellia HAELO Phase 3 positive topline (2026-04-27)](https://www.globenewswire.com/news-release/2026/04/27/3281473/0/en/intellia-therapeutics-reports-positive-phase-3-results-in-hereditary-angioedema-marking-a-global-first-for-in-vivo-gene-editing.html)
- [Intellia MAGNITUDE clinical hold 해제 (2026-03-02)](https://ir.intelliatx.com/news-releases/news-release-details/intellia-therapeutics-announces-fda-lift-clinical-hold-0)
- [CGTLive: Intellia ATTR Phase 3 hold (Grade 4 liver AE)](https://www.cgtlive.com/view/intellia-phase-3-trials-transthyretin-amyloidosis-gene-editing-therapy-nex-z-hold-grade-4-liver-ae)
- [Arcturus ARCT-810 Phase 2 interim (2025-06-30)](https://ir.arcturusrx.com/news-releases/news-release-details/arcturus-therapeutics-announces-positive-interim-phase-2)
- [Moderna mRNA-3927 PA registrational update / mRNA-3705 START](https://www.modernatx.com/research/product-pipeline)
- [Verve Heart-2 Phase 1b VERVE-102 positive data](https://vervetx.gcs-web.com/news-releases/news-release-details/verve-therapeutics-announces-positive-initial-data-heart-2-phase/)
- [Vertex VX-522 program termination — lung inflammation](https://www.fiercebiotech.com/biotech/vertex-drops-moderna-partnered-inhaled-cystic-fibrosis-candidate-after-unresolved)
- [Moderna GSD1a (mRNA-3745) program halted (2025-11)](https://www.biospace.com/press-releases/moderna-analyst-day-highlights-pipeline-progress-and-business-strategy-updates)
- [AstraZeneca / Moderna AZD8601 discontinuation](https://www.fiercebiotech.com/biotech/astrazeneca-axes-moderna-partnered-phase-2-heart-disease-drug-amid-other-wee-pipeline)
- [Capstan CPTX2309 Phase 1 initiation + AbbVie acquisition ($2.1B)](https://www.nature.com/articles/d41573-025-00131-w)
- [MagicRNA HN2301 SLE in vivo CAR-T — NEJM 2026](https://www.nejm.org/doi/full/10.1056/NEJMc2509522)
- [Strand STX-001 Phase 1 ASCO 2025 data](https://www.businesswire.com/news/home/20250528368906/en/Strand-Therapeutics-Announces-Initial-First-in-human-Phase-1-Data-for-STX-001-in-Patients-with-Advanced-Solid-Tumors-at-The-2025-ASCO-Annual-Meeting)
- [Beam BEAM-302 AATD Phase 1/2 data](https://www.biospace.com/drug-development/beam-one-ups-wave-as-both-show-promise-of-genetic-editing-for-aatd)
- [Wave WVE-006 / GSK 반환 (AATD)](https://www.biopharmadive.com/news/wave-gsk-reacquire-rna-editing-drug-aatd/811067/)
- [Korro KRRO-110 임상 실패](https://www.biopharmadive.com/news/korro-rna-editing-aatd-results-layoffs-restructuring/805381/)
- [BMS Orbital Therapeutics $1.5B 인수 (2025-10)](https://visionlifesciences.com/insights/biotech-licensing-deal-tracker-2026)
- [Eli Lilly / Orna Therapeutics 인수 (2026-02)](https://pubs.rsc.org/en/content/articlehtml/2026/pm/d5pm00159e)
- [BioNTech CureVac 인수 완료 (2025-12)](https://investors.biontech.de/news-releases/news-release-details/biontech-closes-acquisition-curevac-nv-including-subsequent/)
- [Casgevy FDA approval β-thal (ex vivo CRISPR + mRNA Cas9)](https://www.insideprecisionmedicine.com/topics/precision-medicine/in-another-win-for-crispr-fda-approves-casgevy-for-beta-thalassemia/)
- [Translate Bio MRT5005 CF 임상 실패](https://www.fiercebiotech.com/biotech/translate-bio-s-mrna-fails-to-improve-lung-function-cystic-fibrosis-patients)
- [Extrahepatic delivery review (RSC Pharmaceutics 2026)](https://pubs.rsc.org/en/content/articlehtml/2026/pm/d5pm00159e)
- [Chronic redosing review (Molecular Therapy 2026)](https://www.sciencedirect.com/science/article/pii/S2162253126000533)

---

*문서 길이: 약 3,300 단어 / 27개 세그먼트 매핑 완료 / 임상 evidence 2026-05 기준.*
