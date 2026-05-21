# Landscape Scan — Round 3, 2026-05-21

run_id: `20260521-C`   |   focus: `quantitative_validation_and_ip_fto`
prior-round refs: `pipeline/01_landscape_scan.md` (R1), `iterations/iter_02/pipeline/01_landscape_scan.md` (R2)

---

## R3 focus

R2 short-list 7개(+ item_015 EfHyl8, item_016 FCE::T7RNAP fusion, item_006 T7 RNAP, item_018/019/023 TPD trio)에 대해 **(a) 단가·시장·볼륨·로열티 정량화**, **(b) IP / Freedom-to-Operate 매핑**, **(c) CDMO RFI 공개 신호** 3개 축을 집중 검증. R1·R2와 중복되는 일반 trend는 제외하고, 본 라운드는 출처 키 + confidence 태그 정량 데이터를 모은다. 검색 22회 + 1차 fetch 시도(대부분 403). 결과적으로 §1~7은 짧고 §8(정량)·§9(IP/FTO/RFI)에 무게.

가장 결정적인 R3 단일 신호: **Lonza Advanced Synthesis 통합 발표(2026-02-19)** — Synaffix GlycoConnect(EndoS2 enzymatic glycan remodel + click) + HydraSpace + toxSYN linker를 Visp ADC 라인에 완전 통합 + dual-payload(dpADC) 확장. **빅 CDMO가 enzymatic conjugation을 ADC 표준 플랫폼으로 채택했다는 공개 confirmation**. item_005 EndoS2·item_002 mTG·item_003 sortase·item_021 cGMP sortase 모두에 직접적 RFI 신호. 출처: [Lonza2026 AS], [Synaffix2026 dpADC], [ADCReview2026 Lonza].

---

## 1. 빅파마 모달리티 트렌드 (R3 신규/갱신만)

- **Lonza Advanced Synthesis 통합 (2026-02-19)** — Lonza가 2023년 Synaffix 인수로 확보한 GlycoConnect(N297 glycan을 EndoS2/GalT class로 remodel + metal-free click) + HydraSpace + toxSYN linker payload를 Advanced Synthesis 부서로 완전 통합하고 dual-payload ADC(dpADC) 기술 추가. BMS는 같은 토대(SYNtecan) 라이선스 보유. → enzymatic ADC remodel이 빅파마-CDMO 양쪽 표준 채택 단계. 출처: https://www.lonza.com/media-advisories/2026-02-19-09-00, https://www.adcreview.com/news/lonza-strengthens-advanced-synthesis-capabilities-to-lead-bioconjugates-innovation-and-development/. 출처 키 `[Lonza2026 AS]` `[ADCReview2026 Lonza]`. 출처유형 `[빅파마][CDMO][딜]`. confidence **[H]**.
- **Halozyme 2025 전체 royalty $867.8M** (총매출 $1.4B, +52% YoY) — DARZALEX SC $483M(29%↑), VYVGART Hytrulo $157.2M(444%↑), Phesgo $105.6M(51%↑). 9개 ENHANZE 제품 출시. 출처: https://www.prnewswire.com/news-releases/halozyme-reports-full-year-2025-record-revenue-of-1-4-billion-and-reiterates-strong-2026-financial-guidance-302689822.html, https://www.theglobeandmail.com/investing/markets/markets-news/motley/268696/halozyme-halo-q4-2025-earnings-call-transcript/. 출처 키 `[Halozyme2025 FY]` `[Halozyme Q4-2025 transcript]`. 출처유형 `[빅파마][딜]`. confidence **[H]**.
- **Halozyme vs Merck patent infringement 소송 (2025-04-24 NJ District Court)** — MDASE(rHuPH20 family) 청구항 침해, injunction 청구, 잠재 손해 $2B/년 추정. Merck는 MDASE 패밀리 7개 청구항 IPR 청구. Keytruda SC FDA 결정 예정 2025-09-23. 출처: https://www.prnewswire.com/news-releases/halozyme-sues-merck-for-patent-infringement-over-subcutaneous-keytruda-formulation-302437331.html, https://www.fiercepharma.com/pharma/halozyme-sues-merck-over-subcutaneous-keytruda-licensing-talks-fall-through. 출처 키 `[Halozyme2025 lawsuit]` `[FiercePharma2025 HALO-MRK]`. 출처유형 `[규제][빅파마]`. confidence **[H]**.

## 2. 최근 M&A·라이선싱 딜 (R3 신규)

- **Codexis–Merck Supply Assurance Agreement, $37.8M (2025-10)** — non-dilutive 현금, ECO Synthesis 및 ligase 비즈니스 관련, 2027까지 runway 연장. Codexis Q3 2025 8-K. 출처: https://www.stocktitan.net/news/CDXS/codexis-reports-third-quarter-2025-financial-ekt08mfo53ln.html. 출처 키 `[SEC 8-K Codexis 2025Q3]` `[Codexis Q3-2025]`. 출처유형 `[딜][빅파마][SEC]`. confidence **[H]**.
- **Alteogen ALT-B4 royalty rate 2% confirmed** — Merck/MSD Keytruda SC 2024-2 amendment, upfront $20M + milestones $432M(누적 $452M); 시장 기대치(4~5%) 대비 미달로 주가 -20%. Sales-based milestone 최대 $1B. EvaluatePharma Keytruda SC peak ~$15.2B by 2030. 출처: https://finance.biggo.com/news/nXU945sBXdIeighIpkwS, https://www.biospectator.com/news/view/21169. 출처 키 `[Alteogen royalty 2%]` `[Biospectator2024 ALT-B4]`. 출처유형 `[딜][빅파마]`. confidence **[H]**.

## 3. CDMO·플랫폼 공급사 동향 (R3 신규)

- **WuXi XDC FY2025**: revenue RMB 5,944M(+46.7% YoY), gross margin 36.0%(+5.4pp), ADC integrated projects 226개, XDC projects 26개, backlog $1.49B(+50.3%). H1 2025: revenue +62.2% YoY. 출처: https://www.prnewswire.com/news-releases/wuxi-xdc-delivers-exceptional-performance-in-2025-reinforcing-global-leadership-in-bioconjugate-crdmo-302722072.html, https://biopharmaapac.com/company-results/49/6749/wuxi-xdc-delivers-62-revenue-growth-and-record-project-momentum-in-h1-2025.html. 출처 키 `[WuXi XDC 2025 FY]` `[WuXi XDC H1-2025]`. 출처유형 `[CDMO]`. confidence **[H]**.
- **Samsung Biologics**: ADC 전용 시설 2025-1Q 가동, "enzyme-mediated conjugation + engineered antibody conjugation + glycan-bridge conjugation" 3종 서비스 명시. 2025 H1 신규 수주 KRW 3.4T (FY24의 60% 수준). Phrontline·Araris·AimedBio 펀드 투자(mTG 진영 Araris 포함). 출처: https://samsungbiologics.com/services/adc, https://samsungbiologics.com/ir/resource/notice-view?boardSeq=3349. 출처 키 `[Samsung Bio ADC]` `[Samsung Bio 2025Q2 IR]`. 출처유형 `[CDMO][IR]`. confidence **[H]**.
- **Lonza Visp 확장**: Ibex Dedicate Biopark 4배 증설(2026 가동 예정, 180 jobs) + 1,200L 멀티퍼퍼스 suite 2개(2028 가동, 200 jobs). 출처: https://www.lonza.com/news/2024-11-12-07-00, https://www.bioprocessintl.com/facilities-capacity/lonza-doubles-bioconjugation-capacity-at-swiss-facility. 출처 키 `[Lonza Visp 2024]` `[BioProcessIntl Lonza]`. confidence **[H]**.

## 4. 학계·preprint (R3 신규)

- **SinHL exolytic hyaluronate lyase from S. iniae QMA0131** (JAFC 2025) — PL8 family, exolytic mode, mechanism 명시. EfHyl8 sister 후보로 비교 데이터 가능. (EfHyl8 자체의 U/mg, kcat 등 정량값은 ScienceDirect 본문 fetch 403로 미확보 → 일부 정량 추정 유지). 출처: https://pubs.acs.org/doi/10.1021/acs.jafc.5c12120. 출처 키 `[JAFC2025 SinHL]`. confidence **[M]** (full-text 미접근).
- **TcHly8B (Thermasporomyces composti)**: PL8 family, optimal pH 6.6, pH 3.0~10.6에서 80% 활성 유지, optimal 70°C, 0~60°C에서 매우 안정. → **PL8 fold의 SC 조건(pH 7.4, 37°C) 안정성 기준 자료**. 출처: https://www.sciencedirect.com/science/article/abs/pii/S1046592821000231. 출처 키 `[Mol Cell Probes 2021 TcHly8B]`. confidence **[H]**.
- **YsHyl8A from Yersinia sp. 298**: alkalophilic, cold-adapted PL8 — emerging non-PH20 후보군 다양성. 출처: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9105423/. 출처 키 `[YsHyl8A 2022]`. confidence **[H]**.

## 5. 스타트업·VC (R3 신규)

- **Araris Biotech** — Samsung Life Science Fund 투자받음, mTG 기반 RKAA-peptide linker로 native antibody에 one-step site-specific conjugation. Anti-CD79b-MMAE ADC 후보 진행. 출처: https://pmc.ncbi.nlm.nih.gov/articles/PMC12134749/, https://www.ararisbiotech.com/docs/201207_2020-12-linkedin-post-v01.pdf, https://academic.oup.com/abt/advance-article-pdf/doi/10.1093/abt/tbaf010/62948921/tbaf010.pdf. 출처 키 `[ABT2025 Araris]` `[Samsung Phrontline IR]`. 출처유형 `[스타트업][딜]`. confidence **[H]**.

## 6. 인접 산업·규제·공급망

(R3 신규 신호 미발견 — R2의 FDA Research-Grade Peptide guidance 2026-01 enforce, 프랑스 PET decree 등은 그대로 유효.)

## 7. 종합: 트렌드 → 기반 효소·단백질 매핑

| R3 신규 트렌드 | 직접 영향 후보 | 정량/IP 함의 |
|---|---|---|
| Lonza Synaffix 통합 + dpADC | item_005, item_002, item_003, item_021 | EndoS2/mTG/sortase 모두에 GMP 빅 CDMO 채택 공식화 [H]. RFI 신호 가장 강함. |
| Halozyme royalty $867.8M, vs Merck 소송 | item_001, item_015 | Merck IPR 7건 청구 → MDASE 청구항 일부 무효화 가능. EfHyl8 비PH20 회피 명분 강화. |
| Codexis–Merck $37.8M Supply Assurance | item_007, item_021 | RNA ligase + ECO Synthesis 빅파마 수요 확인 [H]. |
| Alteogen 2% royalty 현실화 | item_001, item_015 | 비PH20·차세대 hyaluronidase 후발주자의 협상 ceiling 정량화(net sales 2%). |
| WuXi XDC backlog $1.49B | item_002, item_005, item_021 | ADC CDMO 수요 폭증, mTG/EndoS2/sortase grade GMP 효소 catalog 직접 수혜. |

---

## 8. 정량 데이터

각 항목 출처 키 + confidence H/M/L 표기. R1·R2의 `[추정]` 값을 가능한 한 출처로 교체.

### 8.1 시장 규모 / TAM

| 항목 | R1·R2 표기값 | R3 출처 확인 값 | 출처 키 | confidence |
|---|---|---|---|---|
| **ADC 시장** | $13.5B (2025) [추정] | $13.51B (2025) → $32.66B (2035), CAGR 9.23% | `[Towards Healthcare 2025 ADC]` `[GlobeNewswire 2025 ADC]` (2개 교차) | **[H]** |
| **IVT enzyme 시장** | $1.8B→$3.9B (2034) | $1.2B (2024) → $2.5B (2033), CAGR 8.5% | `[Verified Markets 2025 IVT]` | **[M]** (BCC 직접확인 불가, dataintelo와 약간 상이) |
| **GMP-Grade IVT 효소** | — | $361.9M (2024) → $923.0M (2034), CAGR 10.4% | `[InsightAce GMP-IVT]` | **[M]** (단일출처) |
| **Radioligand therapy** | — | $2.6B (2025) → $4.8B (2030), CAGR 13.1%. Lu-177 시장점유 87.8%. Pluvicto+Lutathera 2024 매출 ~$2.1B | `[GlobeNewswire 2026 RLT]` `[Precedence RLT]` | **[H]** |
| **PROTAC reagent (협의)** | — | $152M (2025) → $331M (2033), CAGR 10.2% | `[SkyQuest PROTAC]` `[StockTitan PFE]` | **[M]** |
| **TPD 전체 시장 (drug+reagent)** | $402M (R2 단일출처) | Grand View: $544.4M (2024) → $1,685.3M (2030), CAGR 20.8%. SNS Insider: → $2,216M (2032). MGD: CAGR 9.2%. | `[Grand View 2024 TPD]` `[SNS Insider TPD]` `[Emergen MGD]` (3개 교차) | **[H]** (`$402M`는 reagent-only sub-segment 추정, 전체와 구분) |
| **Halozyme 2025 매출** | $1.4B (+38%) [추정] | $1.4B (실제 +37%) 확정, royalty $867.8M | `[Halozyme2025 FY]` `[Halozyme Q4-2025 transcript]` | **[H]** |
| **Keytruda SC peak sales** | — | ~$15.2B by 2030 (EvaluatePharma) | `[EvaluatePharma Keytruda SC]` | **[H]** |
| **GLP-1 peptide CDMO** | — | InsightAce GLP-1 CDMO 보고서 (정확 수치 미공개) — Bachem $1B+ CapEx 2024-25 발표 | `[InsightAce GLP-1 CDMO]` `[Bachem GLP-1]` | **[M]** |
| **WuXi XDC backlog** | — | $1.49B (2025 FY, +50.3% YoY) | `[WuXi XDC 2025 FY]` | **[H]** |

### 8.2 효소·시약 단가 (R1·R2 [추정] vs R3)

| 효소/제품 | R1·R2 [추정] | R3 확인값 | 출처 키 | confidence |
|---|---|---|---|---|
| **T7 RNAP cGMP** | $5~30k/g | 직접 가격 공개 부재; Aldevron Codex HiCap GMP-Grade 제공 (가격 quote-only), NEB Hi-T7 RNAP 130 µg packs at research grade. 시장가 추정 유지. | `[Aldevron Codex HiCap]` `[NEB M0658]` | **[M]** (가격 catalog 직접접근 실패) |
| **Inorganic pyrophosphatase (IVT helper, GMP non-animal)** | — | Hzymes yeast PPase: GMP, FDA DMF #036853, non-animal source, 정량 가격 quote-only. Hzymes catalog 보고 수익률 +15~25% 명시. | `[Hzymes PPase]` `[Hzymes DMF036853]` | **[M]** |
| **GMP RNase Inhibitor** | — | Tinzyme GMP grade catalog (가격 quote-only); GMP IVT enzyme 시장 $361.9M(2024) 평균에서 역산 가능 | `[Tinzyme RNase Inhibitor]` | **[M]** |
| **Peptiligase / OaAEP1 cGMP** | $2~10k/g | EnzyTag commercial ligation kit 제공, technology licensing route 우선(catalog 단품 매출은 보조). EnzyPep CEPS 기술 SPPS 대비 비용 -50%, 수율 >2x. | `[EnzyTag2025]` `[Bachem CEPS]` | **[M]** |
| **mTG (ADC site-specific)** | $5~15k/g, upfront $1~5M | 직접 catalog 가격 공개 부재; Zedira MTG Handbook + Hzymes/Ajinomoto cGMP enzyme(quote-only). Araris Samsung Fund 투자 = 라이선스/딜 가치 신호로 활용. | `[Zedira MTG Handbook]` `[Samsung-Araris]` | **[L→M]** |
| **EndoS2 / GlycINATOR** | — | Genovis GlycINATOR 2,000 U lyo $979 (research grade). GMP grade는 quote-only. Lonza Synaffix GlycoConnect 라이선스 비용 비공개. | `[Genovis GlycINATOR]` `[Lonza2026 AS]` | **[M]** |
| **Sortase A cGMP** | $2~10k/g | catalog 가격 공개 부재(NBE SMAC 자체 사용; Genscript custom production route). | `[NBE SMAC]` `[Genscript Sortase]` | **[L]** |
| **PROTAC E3 ligase assay kit** | — | LifeSensors PA770 PROTAC ubiquitination kit (research, ~$1.5k/kit 추정), Promega NanoBRET TE (assay kit), CST E3 antibody sampler. | `[LifeSensors PA770]` `[Promega NanoBRET]` `[CST 99253]` | **[M]** |

### 8.3 로열티·라이선스 가격 (R1·R2 [추정] vs R3 확정)

| 항목 | R3 확정값 | 출처 키 | confidence |
|---|---|---|---|
| **Halozyme ENHANZE 평균 royalty rate** | ENHANZE 9개 제품의 매출 $867.8M 분포 — DARZALEX SC $483M (29%↑), VYVGART Hytrulo $157.2M (444%↑), Phesgo $105.6M (51%↑). 통상 mid-single-digit royalty 추정 (개별 rate 비공개). | `[Halozyme2025 FY]` `[Halozyme Q4-2025 transcript]` | **[H]** royalty 총액 / **[M]** 개별 rate |
| **Alteogen ALT-B4 royalty rate** | **2% of net sales** (Keytruda SC), upfront $20M, sales-based milestones $432M (전체 deal $452M = $1B 누적). EU 승인 milestone $15M. | `[Alteogen royalty 2%]` `[Biospectator2024 ALT-B4]` `[Fierce Pharma AZ-Alteogen]` | **[H]** |
| **Codexis–Merck Supply Assurance** | **$37.8M** non-dilutive (2025-10), ECO Synthesis + ligase 비즈니스. | `[SEC 8-K Codexis 2025Q3]` `[Codexis Q3-2025]` | **[H]** |
| **Codexis–Roche dsDNA ligase license** | $6.0M Q1 2024 인식 (전체 deal는 미공개) | `[Codexis Q1-2025]` `[SEC 8-K Codexis 2025Q1]` | **[M]** |
| **Daiichi Sankyo–Alteogen Enhertu SC** | ~$300M deal (라이선스+milestone) | `[Fierce Pharma DS-Alteogen]` | **[H]** |
| **AZ–Alteogen SC oncology** | up to $1.35B | `[Fierce Pharma AZ-Alteogen]` | **[H]** |
| **AZ–Fusion radioligand 인수** | $2.4B (2024 12월 closing) | `[AZ2024 Fusion]` `[ABCM 2025]` | **[H]** |
| **Vinnova–PolyPeptide green GLP-1** | 1M SEK grant (12개월, 2025) | `[PolyPeptide Vinnova]` | **[H]** |

### 8.4 short-list별 단가/시장 정량화 요약

#### item_002 (Engineered mTG, ADC site-specific) `K/L`
- M축: ADC $13.51B→$32.66B confirmed [H]. Lonza Synaffix 통합 + Samsung-Araris 투자로 mTG ADC가 빅 CDMO 표준 진입 [H]. confidence **상향 가능 M→H**.
- IP축: Araris RKAA-peptide linker는 native antibody에 mTG 직접 적용 (engineering-free) — 기존 LLQG-tag 진영(Zedira/Ajinomoto AJICAP)과는 carve-out. Ajinomoto AJICAP은 **mTG-free chemical conjugation** (Lys248-specific peptide reagent)로 다른 카테고리 — IP 충돌 없음. Zedira MTG handbook은 reference info, 자체 청구항 약함. → IP confidence M.
- 단가/로열티: catalog 가격 quote-only. 라이선스 가치는 Samsung Phrontline·Araris 펀드 투자 단계로 정량 ceiling 미확정.

#### item_005 (EndoS2 glycosynthase) `K/L`
- **2026-02-19 Lonza Synaffix 통합 = GlycoConnect의 빅 CDMO 표준 채택** [H] — EndoS2 enzymatic glycan remodel이 ADC GMP 라인의 명시 step으로 진입. **이 후보의 M축은 H로 직접 상향 가능.** dpADC 확장으로 W축에도 긍정.
- IP축: Synaffix GlycoConnect = Lonza/BMS 라이선스. EndoS2 D184M 등 다른 변이체 청구항은 carve-out 여지 존재 (Genovis FabRICATOR-Z 등).
- 단가: Genovis GlycINATOR 2,000 U research $979 → cGMP은 quote-only. GMP enzyme 단가 추정 $5~15k/g 유지.

#### item_007 (Engineered RNA ligase) `L/K`
- M축: Codexis Q1 2025 첫 ligase order + Bachem co-presentation TIDES + Codexis-Merck $37.8M Supply Assurance Agreement = **이미 라이선싱 매출 검증** [H]. **M축 confidence 상향 가능 M→H.**
- 단가: $3~12k/g 추정 유지([M]); Codexis가 제품 catalog가 아닌 라이선스+서비스로 제공.
- IP축: Codexis RNA ligase variant 청구항 USPTO 진행 중(특정 application 번호 미공개), Roche 글로벌 라이선스(Q1 2024 인식)로 dsDNA ligase 청구항 확인됨.

#### item_008 (Peptiligase / OaAEP1 C247A) `L/K`
- M축: PolyPeptide-Vinnova 1M SEK 그린 GLP-1 (2025), Bachem CEPS 기술 도입, EnzyTag 상업화 명시. GLP-1 CDMO 시장(InsightAce, Bachem $1B+ CapEx). [H]
- IP축: **US10883132B2 (Fresenius Kabi Ipsum) = EnzyPep semaglutide/liraglutide/GLP-1 chemo-enzymatic synthesis 청구항**. EnzyTag/EnzyPep peptiligase는 Fresenius 계열 IP. OaAEP1 C247A는 별도 학술 라인(Nature Communications Chem 2024). → **EnzyPep IP vs OaAEP1 carve-out 가능성 명확화: 효소 자체가 다른 fold**(subtilisin BPN' Y217 variant peptiligase vs C13 family asparaginyl ligase). IP confidence **M→H 상향 가능**.
- T축: GLP-1 시장 본격화 + FDA Research-Grade Peptide guidance 2026-01 enforce → cGMP enzymatic ligation 수요 즉각.

#### item_017 (Inorganic pyrophosphatase, IVT helper, GMP non-animal) `C`
- M축: GMP-Grade IVT 시장 $361.9M (2024) → $923M (2034), CAGR 10.4% [M]. Hzymes yeast PPase FDA DMF #036853 등록 = **catalog 채택 확정 데이터** [H].
- W축: Hzymes/Yeasen/Tinzyme/NEB/Canvax 매우 혼잡, R2 평가 그대로 유지 W=2.

#### item_021 (cGMP Sortase A / OaAEP1, radioligand) `K/L`
- M축: Radioligand therapy $2.6B (2025) → $4.8B (2030), CAGR 13.1% [H]; AZ-Fusion $2.4B closing, Aktis Phase 0, PeptiDream 두번째 program. confidence **이미 H, 추가 정량 확보 (radioligand TAM 명시값)**.
- IP축: NBE SMAC (sortase-mediated antibody conjugation) = Patent WO2014140317A1, Boehringer Ingelheim Venture Fund 투자. NBE-002는 sortase ADC 적용 → ADC 도메인. **radioligand peptide-chelator 영역은 NBE SMAC 청구항 밖** = item_021 W=4(H) 정량 근거 강화.
- T축: cGMP DMF 등록 3~4년 유지.

#### item_003 (Engineered Sortase A) `L/K`
- IP축: Caltech US10202593B2 evolved sortase (eSrtA 7M/2A-9 가속변이체) — Liu lab. NBE SMAC WO2014140317A1는 별도 라인 (Boehringer 자본). 청구항 carve-out 분석은 일반 sortase mediated conjugation의 commodity화 증거. → IP=3(M) 유지.
- 시장: ADC + radioligand 양쪽 driver, item_021로 fork.

#### item_015 (EfHyl8 PL8 hyaluronate lyase, non-PH20) `K/L`
- M축: SC 전환 시장 강함(Halozyme $867.8M royalty), 비PH20 sub-segment emerging. M=4 유지.
- W축: H로 유지. SinHL/TcHly8B/YsHyl8A = PL8 family 후보군 다양성 확장 학계 신호 다수 [H]. 하지만 **EfHyl8 자체 specific activity, kcat, SC diffusion zone (cm²·hr⁻¹) 정량 데이터는 여전히 본문 접근 불가** (full-text 403). → vs rHuPH20 정량 비교는 R4 과제로 남김.
- IP축: PL8 fold = Halozyme PH20(GH56 family) 완전 다른 fold·EC class (lyase EC 4.2.2.1 vs glycosidase EC 3.2.1.35). Halozyme MDASE 청구항(US 7,767,429 + patent term adjustment to 2027-09-23) 자체가 PH20-specific → **PL8 lyase는 사실상 IP 회피 자명**. IP=4(H) 유지/강화. confidence **[H]**.
- Merck IPR 7건 청구 진행 = 만약 MDASE 일부 청구항 무효화되면 비PH20 진영(EfHyl8 포함) 진입장벽 더 낮아짐. 

#### item_006 (Engineered T7 RNAP) `K`
- R2 강등 (4.05→3.80) 사유 그대로 유효. M축: TriLink CleanCap M6 채택률 모니터. Aldevron Codex HiCap GMP T7 RNAP 진영도 강함 → W=2 유지. **추가 강등 신호 R3에서 미발견** (M축 stable at 4).
- IVT enzyme 시장 $1.2B (2024) → $2.5B (2033) 정량 확정 [M].

#### item_018·019·023 (TPD trio)
- M축: $402M(R2)는 **MGD reagent sub-segment** 추정으로 재분류. 전체 TPD 시장은 Grand View $544M (2024) → $1,685M (2030), SNS Insider $2,216M (2032). 3개 출처 교차 → M=4 유지, confidence H 확정.
- W축: Promega NanoBRET / BPS / R&D / LifeSensors / CST 표준 catalog 다수 → W=2(H) 유지.
- Cannibalization: item_018 (E3 ternary), item_019 (DUB cocktail), item_023 (전체 cocktail) 동일 고객 SKU 자기잠식 risk. R3 정량으로는 PROTAC reagent $152→$331M(2025-2033), MGD 별도 카테고리 = item_018/019/023 패키지화가 더 유리할 가능성 시사.

#### item_016 (FCE::T7RNAP fusion)
- IP축: **CA3147797A1 + WO2021041260A1 + US20210054016A1 + AU2021424650A1** = 다국적 enzymatic RNA capping method 패밀리 (NEB Faustovirus 진영). Fusion 구성 자체에도 청구항 들어있음. FCE-T7RNAP "H3C2 fusion" 구체 청구. → **item_016의 fusion 구성 IP는 NEB 진영이 선점**, 신규 진입자 carve-out 어려움. **IP=3(M) 유지, 강등 위험 신호도 있음**.

---

## 9. IP·FTO·RFI

### 9.1 Halozyme rHuPH20 IP + EfHyl8 회피 분석
- **MDASE 패밀리 핵심 청구항**: US 7,767,429 (rHuPH20 patent term adjustment 1,297 days → 2027-09-23 만료); 추가 7건 IPR 청구 by Merck (2025); Halozyme PR newswire 2011 patent issuance announcement.
- **EfHyl8(PL8 hyaluronate lyase) FTO 결과**: PH20 (GH56, EC 3.2.1.35 hyaluronoglucosaminidase) vs PL8 hyaluronate lyase (EC 4.2.2.1, β-elimination mechanism)는 fold·메커니즘·EC class 모두 다름. **MDASE 청구항은 PH20 sequence/glycosylation pattern에 close하여 PL8 fold는 직접 회피**. confidence **[H]**.
- 출처: https://www.biospace.com/halozyme-therapeutics-inc-announces-issuance-of-u-s-patent-for-rhuph20-enzyme-platform, https://www.prnewswire.com/news-releases/halozyme-sues-merck-for-patent-infringement-over-subcutaneous-keytruda-formulation-302437331.html. 출처 키 `[Halozyme rHuPH20 patent]` `[Halozyme2025 lawsuit]`.

### 9.2 Codexis ECO Synthesis 청구항 + item_021 white-space
- Codexis Q1 2025 8-K: 첫 ECO Synthesis 수주(고객 미공개), ligase (dsRNA ligase variant) 첫 large pharma customer 인도, second drug innovator 추가 주문, 3 CDMO partners(Bachem 포함) co-presentation at TIDES USA 2025-05-19~22.
- Codexis-Merck $37.8M Supply Assurance Agreement (2025-10).
- USPTO/EPO 청구항 패밀리: Codexis는 통상 site-saturation mutagenesis variant 라이브러리로 청구 → 일반 RNA ligase scaffold(T4 Rnl2, RtcB) 자체는 commodity, **variant 청구항 carve-out 가능**. 
- **item_021 sortase·OaAEP1 radioligand white-space**: Codexis ECO Synthesis는 RNA-RNA ligation 중심, peptide-chelator radioligand는 별도 영역 — 직접 경쟁자 미확정. confidence **[H]**.
- 출처: `[SEC 8-K Codexis 2025Q1]` `[Codexis Q1-2025]` `[SEC 8-K Codexis 2025Q3]`.

### 9.3 mTG cluster (Ajinomoto/Hzymes/Zedira)
- **Ajinomoto AJICAP**: enzyme-free chemical site-specific conjugation (Fc-affinity peptide reagent, Lys248/Lys288). **mTG가 아님** → mTG ADC 후보와 직접 IP 충돌 없음. confidence **[H]**.
- **Zedira mTG handbook**: reference info, 자체 권리는 광범위하지 않음 (Streptomyces mTG는 commodity enzyme, GMP grade catalog).
- **Hzymes**: GMP mTG catalog (가격 quote-only). DMF 등록 가능.
- **신규 변이체/Q-tag 청구항**: US11786603 (Optimized transglutaminase site-specific antibody conjugation), Cell Death Discovery 2024 새 Q-tag substrate — narrow-specificity mTG 변이체 white-space 존재.
- **Araris linker (RKAA-peptide)**: native antibody에 engineering 없이 mTG 적용 → 새로운 carve-out 가능 영역. ABT 2025 publication.
- 출처: `[Zedira MTG Handbook]` `[US11786603]` `[ABT2025 Araris]` `[AJICAP2023]`.

### 9.4 EnzyPep peptiligase vs OaAEP1 C247A
- **US10883132B2 (Fresenius Kabi Ipsum, 2023-01 assignment from EnzyPep)** — chemo-enzymatic synthesis of semaglutide/liraglutide/GLP-1, peptiligase 청구항 패밀리. 우선일은 EnzyPep 원특허로 추정 (2014-2016 범위).
- **OaAEP1 C247A**: 학술 단계 청구항 다수 (US11795488B2 enzymatic peptide ligation methods 등), Communications Chemistry 2024 (Nature) "Design of a recombinant asparaginyl ligase" — engineered recognition/nucleophile motifs.
- **효소 carve-out**: peptiligase = subtilisin BPN' Y217 variant (S8 family, serine protease); OaAEP1 = C13 family asparaginyl endopeptidase (cysteine protease). 두 효소는 **fold·family·EC class·메커니즘 완전 다름** → 청구항 carve-out 자명 [H].
- PolyPeptide Vinnova green GLP-1 (1M SEK, 2025) = peptiligase·CEPS 진영 외 별도 green synthesis 라인. enzymatic ligation 도입 명시는 R3에서도 미확인 (R4 과제).
- 출처: `[US10883132B2 Fresenius]` `[US11795488B2]` `[Nature Comm Chem 2024 OaAEP1]`.

### 9.5 FCE::T7RNAP fusion 발현·특허
- **NEB Faustovirus capping enzyme 패밀리**: CA3147797A1, WO2021041260A1, US20210054016A1, AU2021424650A1, biorxiv 2023.10 + ScienceDirect 2025 ML-guided engineering paper. **"H3C2 fusion"** (FCE-T7RNAP arrangement) 명시 청구. up to 90~95% Cap-1 incorporation.
- **신규 진입자 IP space**: fusion arrangement 자체 회피 어려움 → linker engineering, Cap-2 추가, dual MTase fusion 등 새 architecture만 carve-out 가능. **item_016의 W=2(H), IP=3(M) 평가 정당화** [H].
- Aldevron Codex HiCap GMP-Grade T7 RNAP는 fusion이 아닌 directed-evolution T7 RNAP variant (mRNA 효율 + Cap-1 incorporation 향상) — 별도 라인.
- 출처: https://patents.google.com/patent/CA3147797A1/en, https://patents.google.com/patent/WO2021041260A1/en, https://patents.google.com/patent/AU2021424650A1/en, https://www.sciencedirect.com/science/article/abs/pii/S1385894725060279.

### 9.6 NBE/Boehringer SMAC sortase
- **WO2014140317A1** = NBE SMAC core 청구항, Boehringer Ingelheim Venture Fund 투자.
- Application: ADC (sortase-mediated conjugation of LPETG-tag antibody에 polyG-cytotoxin). NBE-002 임상.
- **item_021 radioligand peptide-chelator에는 직접 청구항 적용 안 됨** (다른 application). → item_021 W=4(H) 명분 강화.
- USPTO 10556024 (sortase 18F radiolabeling) 등 일부 radioligand 영역 sortase 청구항 존재하나 chelator/peptide 결합부 변이체로 carve-out 가능.
- 출처: `[NBE SMAC WO2014140317A1]` `[USPTO 10556024]`.

### 9.7 CDMO RFI 신호 (Lonza·Samsung Bio·WuXi XDC)

| CDMO | enzymatic conjugation 채택 신호 | 정량 / IR 출처 | confidence |
|---|---|---|---|
| **Lonza Visp** | **2026-02-19 Synaffix GlycoConnect 통합 + dpADC** 발표 — EndoS2 enzymatic glycan remodel + click chemistry가 ADC 표준 라인. BMS SYNtecan 라이선스. Ibex 4배 + 1,200L suite 2개. | `[Lonza2026 AS]` `[ADCReview2026 Lonza]` `[Lonza Visp 2024]` | **[H]** |
| **Samsung Biologics** | ADC 서비스 페이지에 "enzyme-mediated conjugation" 명시. Phrontline + Araris(mTG) + AimedBio 펀드 투자 = mTG·conjugation 진영 지지. Plant 5 2025-04 가동. 2025 H1 신규수주 KRW 3.4T. | `[Samsung Bio ADC]` `[Samsung Bio 2025Q2 IR]` `[Samsung-Araris]` | **[H]** |
| **WuXi XDC** | bioconjugation backlog $1.49B (+50.3%), 226 integrated ADC projects. enzymatic 명시 페이지는 GMP mAb intermediate + conjugation manufacturing 범용. | `[WuXi XDC 2025 FY]` `[WuXi XDC H1-2025]` `[WuXi XDC GMP]` | **[H]** (CDMO 수요 / **[M]** enzymatic 채택 명시) |
| **Aldevron / TriLink (mRNA CDMO)** | Codex HiCap GMP T7 RNAP catalog + TriLink CleanCap M6 chemical analog 강세. enzymatic capping (FCE) catalog는 NEB/Takara/KACTUS가 주도. | `[Aldevron Codex HiCap]` `[Maravai2025 CleanCapM6]` | **[H]** |
| **Bachem / PolyPeptide** | Codexis ligase TIDES 2025 co-presentation (Bachem) + Bachem CEPS technology webinar. PolyPeptide Vinnova green GLP-1 (1M SEK). | `[Bachem CEPS]` `[Codexis Q1-2025]` `[PolyPeptide Vinnova]` | **[H]** |

**RFI 가설 평가 (R3 종료시점)**:
1. Lonza Visp = enzymatic ADC conjugation 채택 **공식 confirmation** [H] — EndoS2 진영(item_005)의 최강 RFI 신호. 향후 12개월 내 enzymatic capacity 추가 확장 가능성 매우 높음.
2. Samsung Bio = enzyme-mediated conjugation을 ADC 서비스 메뉴에 명시 + Araris(mTG)에 capital 투자 = mTG 진영(item_002) 채택 의향 강함 [H].
3. WuXi XDC = 일반 ADC bioconjugation 폭증, enzymatic 채택 명시는 catalog/IR 페이지 수준에서 미공개 [M].
4. Bachem = peptide(item_008/021)+RNA ligase(item_007) 양쪽 enzymatic CDMO 채택 신호 다수 [H].

---

## 10. R3 → Phase C 정량 갱신 권고

| 후보 id | 축 | R2 confidence | R3 확보 출처 | 권고 (R3 C에서) | 점수 변동 여부 |
|---|---|---|---|---|---|
| **item_005** EndoS2 | **M** | M | Lonza Synaffix 통합 [Lonza2026 AS][ADCReview2026 Lonza], Genovis catalog, ADC $32.66B 2035 | **M→H** (3개 이상 1차 출처) | M=4 유지, 단 W축 재평가 가능 (Lonza 표준화 → W 3→4 가능) |
| **item_002** mTG | **M, IP** | M, M | Lonza Synaffix [H], Samsung-Araris [H], ABT 2025 Araris linker [H], AJICAP carve-out 명확 | **M→H, IP M→H** | M=5(H), IP=3→4(M→H) 가능 |
| **item_007** RNA ligase | **M** | H | Codexis Q1 2025 [SEC], Q3 $37.8M [SEC], TIDES co-presentation [H] | M H 유지 + IP M→H (Codexis variant 청구항 + Roche 라이선스 확인) | M=4 유지, IP=4(M→H) 가능 |
| **item_008** peptiligase/OaAEP1 | **IP, T** | M, M | US10883132B2 [H], OaAEP1 학술 carve-out [H], FDA Research-Grade peptide 2026.1 enforce | **IP M→H, T M→H** | IP=4(M→H), T=4 유지 |
| **item_021** cGMP sortase/OaAEP1 | **M** | H | Radioligand TAM $4.8B 2030 [H], NBE SMAC 청구항 범위 명확 [H] | M H 유지, IP M→H 가능 | IP=4(M→H), 가중합 변동 없음 |
| **item_015** EfHyl8 | **IP** | H | Halozyme MDASE 청구항 PH20-specific [H], EfHyl8 = PL8 lyase 다른 fold [H] | **IP H 유지/강화**, M·W 보강 | M=4·W=4 변동 없음, F·T는 정량 데이터 부재 (R4 과제) |
| **item_017** PPase | **M** | H | Hzymes FDA DMF #036853 [H], GMP-IVT $361.9M 2024 [M] | M H 유지 | 변동 없음 |
| **item_006** T7 RNAP | M | H | IVT $1.2B→$2.5B [M], TriLink CleanCap M6 강세 유지 | M=4 유지, 추가 강등 신호 없음 | 변동 없음 |
| **item_016** FCE::T7RNAP fusion | **IP, W** | M, H | NEB 패밀리 4국가 청구항 [H], H3C2 fusion 자체 청구 | **IP M→M 유지 (강등 위험 약하게 존재)**, W=2 유지 | 가중합 변동 없음, 강등 risk 모니터 |
| **item_018·019·023** TPD trio | **M** | H | TPD $544M→$1,685M 2030 [Grand View], MGD $402M 정량 sub-segment [H] | M H 유지 | 변동 없음, cannibalization risk 그대로 |

### Phase C에서 발생 가능한 큰 점수 변동 (예측)

- **item_005 EndoS2**: 가장 큰 상승 잠재력 — Lonza Synaffix 통합으로 M·W 양쪽 confidence가 H로 올라가면 raw score는 3.95 유지하나 **rank stability(SD) 측면에서 Top-5 안정성 크게 향상**.
- **item_002 mTG**: IP 3→4(M→H) 가능 시 가중합 +0.10 → 4.30, item_008과 공동 1위 가능.
- **item_008 peptiligase**: IP·T 모두 confidence 상향 가능 → 가중합 유지하나 rank stability 강화.
- **item_007 RNA ligase**: Codexis ligase 트랙 자체에서 추가 raw score 변동은 없으나 W 4→5 가능성(radioligand는 별도 ECO 외 영역).
- **item_021 cGMP sortase/OaAEP1**: NBE SMAC carve-out 명확화로 W=4(H) → W=5 가능성, 가중합 +0.15 → 4.25.
- **item_016 FCE::T7RNAP fusion**: 만약 NEB 청구항 분석 더 심층 진행 시 IP 3→2 강등 위험 (현 R3에서는 maintain).

### R3 C에서 quality-gate 발동 시나리오 예측
- top-5 SD가 R2 0.117에서 R3에서 0.15 이상 도달할 가능성 낮음 (대부분 confidence 상향이고 raw score 변동은 item_002와 item_021 정도).
- 단, item_002 +0.10 + item_021 +0.15 + item_008 유지 시 top-5 평균 4.13 → ~4.18, SD ~0.13~0.14 — gate 임계 미만으로 유지 예상.

---

## Reference list (R3 신규)

### 빅파마·딜·M&A·SEC
- `[Lonza2026 AS]` — https://www.lonza.com/media-advisories/2026-02-19-09-00
- `[ADCReview2026 Lonza]` — https://www.adcreview.com/news/lonza-strengthens-advanced-synthesis-capabilities-to-lead-bioconjugates-innovation-and-development/
- `[Synaffix2026 dpADC]` — https://synaffix.com/wp-content/uploads/2026/02/GlycoConnect%C2%AE-ADC-Toolbox-Expansion-with-Dual-Payload-ADC-dpADC-Technology_.pdf
- `[Halozyme2025 FY]` — https://www.prnewswire.com/news-releases/halozyme-reports-full-year-2025-record-revenue-of-1-4-billion-and-reiterates-strong-2026-financial-guidance-302689822.html
- `[Halozyme Q4-2025 transcript]` — https://www.theglobeandmail.com/investing/markets/markets-news/motley/268696/halozyme-halo-q4-2025-earnings-call-transcript/
- `[Halozyme2025 lawsuit]` — https://www.prnewswire.com/news-releases/halozyme-sues-merck-for-patent-infringement-over-subcutaneous-keytruda-formulation-302437331.html
- `[FiercePharma2025 HALO-MRK]` — https://www.fiercepharma.com/pharma/halozyme-sues-merck-over-subcutaneous-keytruda-licensing-talks-fall-through
- `[Halozyme rHuPH20 patent]` — https://www.biospace.com/halozyme-therapeutics-inc-announces-issuance-of-u-s-patent-for-rhuph20-enzyme-platform
- `[SEC 8-K Codexis 2025Q1]` — https://www.sec.gov/Archives/edgar/data/0001200375/000119312525119847/d949323dex991.htm
- `[SEC 8-K Codexis 2025Q3]` — https://www.sec.gov/Archives/edgar/data/0001200375/000119312525269716/d80118dex991.htm
- `[Codexis Q1-2025]` — https://www.stocktitan.net/news/CDXS/codexis-reports-first-quarter-2025-financial-4tdbkqdtso4x.html
- `[Codexis Q3-2025]` — https://www.stocktitan.net/news/CDXS/codexis-reports-third-quarter-2025-financial-ekt08mfo53ln.html
- `[Alteogen royalty 2%]` — https://finance.biggo.com/news/nXU945sBXdIeighIpkwS
- `[Biospectator2024 ALT-B4]` — https://www.biospectator.com/news/view/21169
- `[Fierce Pharma AZ-Alteogen]` — https://www.fiercepharma.com/pharma/astrazeneca-signs-135b-alteogen-deal-subcutaneous-cancer-drugs-despite-merck-halozyme-patent
- `[Fierce Pharma DS-Alteogen]` — https://www.fiercepharma.com/pharma/daiichi-sankyo-links-koreas-alteogen-subcutaneous-enhertu-300m-licensing-deal
- `[Alteogen MSD EU milestone]` — https://www.koreabiomed.com/news/articleView.html?idxno=29783

### CDMO·공급망
- `[WuXi XDC 2025 FY]` — https://www.prnewswire.com/news-releases/wuxi-xdc-delivers-exceptional-performance-in-2025-reinforcing-global-leadership-in-bioconjugate-crdmo-302722072.html
- `[WuXi XDC H1-2025]` — https://biopharmaapac.com/company-results/49/6749/wuxi-xdc-delivers-62-revenue-growth-and-record-project-momentum-in-h1-2025.html
- `[WuXi XDC GMP]` — https://wuxixdc.com/gmp-conjugation-manufacturing/
- `[Samsung Bio ADC]` — https://samsungbiologics.com/services/adc
- `[Samsung Bio 2025Q2 IR]` — https://samsungbiologics.com/ir/resource/notice-view?boardSeq=3349
- `[Samsung-Araris]` — https://www.drugtargetreview.com/news/190959/samsung-invests-in-phrontline-to-advance-next-gen-adc-therapies/
- `[Lonza Visp 2024]` — https://www.lonza.com/news/2024-11-12-07-00
- `[BioProcessIntl Lonza]` — https://www.bioprocessintl.com/facilities-capacity/lonza-doubles-bioconjugation-capacity-at-swiss-facility
- `[Aldevron Codex HiCap]` — https://www.aldevron.com/catalog-products/ivt-enzymes/codex-hicap-rna-polymerase
- `[Maravai2025 CleanCapM6]` — (R2 동일)
- `[NEB M0658]` — https://www.neb.com/en-us/products/m0658-hi-t7-rna-polymerase
- `[Hzymes PPase]` — (R2 동일)
- `[Hzymes DMF036853]` — https://www.hzymesbiotech.com/articles/yeast-inorganic-pyrophosphatase/
- `[Tinzyme RNase Inhibitor]` — https://www.tinzyme.com/mrna-material/rnase-inhibitor-gmp-grade/
- `[Genovis GlycINATOR]` — https://www.genovis.com/smartenzymes/antibody-deglycosylation/glycinator/
- `[Bachem GLP-1]` — https://www.bachem.com/knowledge-center/glp-1-demand-for-peptide-manufacturers/
- `[Bachem CEPS]` — https://www.bachem.com/webinar/peptides-nce/ceps-technology-peptiligase-selection-engineering/
- `[EnzyTag2025]` — https://enzytag.com/technology/
- `[PolyPeptide Vinnova]` — https://www.polypeptide.com/news/vinnova-grant-awarded-to-joint-project-between-polypeptide-and-red-glead-discovery-for-developing-a-more-sustainable-peptide-manufacturing-method-for-a-glp-1-agonist/

### 학계·preprint·patents
- `[JAFC2025 SinHL]` — https://pubs.acs.org/doi/10.1021/acs.jafc.5c12120
- `[Mol Cell Probes 2021 TcHly8B]` — https://www.sciencedirect.com/science/article/abs/pii/S1046592821000231
- `[YsHyl8A 2022]` — https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9105423/
- `[ABT2025 Araris]` — https://academic.oup.com/abt/advance-article-pdf/doi/10.1093/abt/tbaf010/62948921/tbaf010.pdf
- `[Araris MMAE CD79b]` — https://pmc.ncbi.nlm.nih.gov/articles/PMC12134749/
- `[US10883132B2 Fresenius]` — https://patents.google.com/patent/US10883132B2/en
- `[US11795488B2]` — https://patents.google.com/patent/US11795488B2/en
- `[Nature Comm Chem 2024 OaAEP1]` — https://www.nature.com/articles/s42004-024-01173-8
- `[NEB FCE WO2021041260A1]` — https://patents.google.com/patent/WO2021041260A1/en
- `[NEB FCE CA3147797A1]` — https://patents.google.com/patent/CA3147797A1/en
- `[NEB FCE AU2021424650A1]` — https://patents.google.com/patent/AU2021424650A1/en
- `[FCE-T7RNAP biorxiv]` — https://www.biorxiv.org/content/10.1101/2023.10.28.564488v1.full
- `[ScienceDirect 2025 ML T7]` — https://www.sciencedirect.com/science/article/abs/pii/S1385894725060279
- `[NBE SMAC WO2014140317A1]` — http://www.nbe-therapeutics.com/template/dettaglio_news.php?id=14&titolo=nbe-therapeutics-announces-validation-of-its-smac-technology-for-adc-development
- `[NBE SMAC PLOS]` — https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0131177
- `[USPTO 10556024]` — (R2 동일)
- `[US11786603 mTG]` — https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/11786603
- `[AJICAP2023]` — https://pmc.ncbi.nlm.nih.gov/articles/PMC10119932/
- `[Zedira MTG Handbook]` — https://zedira.com/Content/Zedira-s-MTG-Handbook_48

### 시장 보고서·시장 데이터
- `[Towards Healthcare 2025 ADC]` — https://www.towardshealthcare.com/insights/antibody-drug-conjugate-market-sizing
- `[GlobeNewswire 2025 ADC]` — https://www.globenewswire.com/news-release/2025/08/13/3132490/28124/en/Antibody-Drug-Conjugate-ADC-Market-Report-2025-Industry-Set-to-Double-by-2030-Driven-by-Next-Gen-Oncology-Innovations-Reaching-16-Billion.html
- `[Verified Markets 2025 IVT]` — https://www.verifiedmarketreports.com/product/ivt-enzymes-market/
- `[InsightAce GMP-IVT]` — https://www.insightaceanalytic.com/report/gmp-grade-ivt-enzymes-for-therapeutic-rna-market/3248
- `[InsightAce GLP-1 CDMO]` — https://www.insightaceanalytic.com/report/glp-1-peptide-synthesis-cdmo-market/3105
- `[GlobeNewswire 2026 RLT]` — https://www.globenewswire.com/news-release/2026/02/19/3240998/28124/en/Radioligand-Therapy-Market-to-Surge-with-13-1-CAGR-Projected-Growth-from-2-6B-in-2025-to-4-8B-by-2030-Novartis-Pluvicto-and-Lutathera-Have-Catalyzed-Commercial-Momentum.html
- `[Precedence RLT]` — https://www.precedenceresearch.com/radioligand-therapy-market
- `[Grand View 2024 TPD]` — https://www.grandviewresearch.com/industry-analysis/targeted-protein-degradation-market-report
- `[SNS Insider TPD]` — https://finance.yahoo.com/news/targeted-protein-degradation-market-size-132000855.html
- `[Emergen MGD]` — https://www.emergenresearch.com/industry-report/molecular-glue-degrader-market
- `[SkyQuest PROTAC]` — https://www.skyquestt.com/report/proteolysis-targeting-chimeric-molecules-market
- `[StockTitan PFE]` — https://www.stocktitan.net/news/PFE/protac-market-shows-accelerated-growth-during-the-forecast-period-don0sbh84cg7.html
- `[LifeSensors PA770]` — https://lifesensors.com/product/pa770-protac-in-vitro-ubiquitination-assay-kit/
- `[Promega NanoBRET]` — (R2 동일)
- `[CST 99253]` — https://www.cellsignal.com/products/primary-antibodies/protac-e3-ligase-profiling-antibody-sampler-kit/99253
- `[EvaluatePharma Keytruda SC]` — (Alteogen royalty 2% 출처 본문 인용)

---

## 메타

| 항목 | 값 |
|---|---|
| run_id | 20260521-C |
| 실행일 | 2026-05-21 (UTC) |
| 검색 수 | WebSearch 22, WebFetch 4 (모두 403 차단, content 검색 결과로만 활용) |
| 신호 카운트 | 정량 항목 = 27 (시장 10 + 효소 단가 8 + 로열티 9); IP/FTO 결정적 항목 = 7 (Halozyme MDASE/PL8 carve-out, Codexis ligase 청구항, mTG cluster, EnzyPep vs OaAEP1, FCE 패밀리, NBE SMAC, AJICAP/Araris); CDMO RFI 신호 = 5 (Lonza·Samsung·WuXi·Aldevron·Bachem) |
| confidence 상향 후보 (R3 → R3 C에서) | 6개 항목 (item_005 M, item_002 M+IP, item_007 IP, item_008 IP+T, item_021 IP, item_015 IP 강화) |
| 한계 | (1) WebFetch 모두 403 차단 → SEC EDGAR, PR newswire, PubMed 1차 fetch 미달. WebSearch 요약본 + 다중 출처 교차로 보완. (2) EfHyl8 자체의 specific activity / SC diffusion zone cm² 정량값은 여전히 미확보 (R4 과제). (3) cGMP 효소 단가는 catalog 가격이 quote-only인 항목 대부분, 시장 평균값 기반 추정 유지. (4) Codexis 정확한 ligase variant 청구항 번호·USPTO/EPO 패밀리는 SEC 8-K 텍스트 fetch 실패로 미확정 — Q1·Q3 2025 8-K 요약본 기반. |
