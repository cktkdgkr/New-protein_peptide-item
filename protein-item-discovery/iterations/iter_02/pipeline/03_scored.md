# Scoring Result — Round 2, 2026-05-21

R1 14개 후보의 R2 신호 기반 재평가 + R2 신규 8개(item_015~022) + 부활 1개(item_023) 첫 스코어. 모든 점수에 confidence H/M/L 태그 적용. 누적 활성 후보 = **23개** (item_024는 item_020에 병합).

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

### business_model 보정 (taxonomy Phase C 영향, R2부터 적용)
- L primary: T +0~1 (계약 기반 빠른 수익화).
- K primary: F +0~1, W -0~1 (catalog 채널 단순화 vs 혼잡).
- C primary (Captive/Catalog): IP +0~1 (내부 know-how).
- S primary: T 양극화.
- H primary: +0.1~0.2 가중합 보정 가능 (F -0.5 가능).

### Short-list 규칙
가중합 상위 5개 + (6·7위가 5위와 0.2 이내 시) → 최대 7개.

---

## 전체 스코어 표 (R2, 23개)

| rank | id | 이름 | M | F | R | W | IP | T | weighted | short | delta R1→R2 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | item_008 | Peptiligase / OaAEP1 C247A | 5(H) | 4(H) | 5(H) | 3(M) | 4(M) | 4(M) | **4.30** | ✓ | +0.10 |
| 2 | item_002 | Engineered mTG (ADC) | 5(H) | 4(M) | 5(H) | 3(M) | 3(M) | 4(M) | **4.20** | ✓ | 0.00 |
| 3 | item_007 | Engineered RNA ligase | 4(H) | 4(M) | 5(H) | 4(M) | 4(M) | 3(M) | **4.10** | ✓ | 0.00 |
| 3 | item_021 | cGMP Sortase A / OaAEP1 (radioligand) | 4(H) | 4(H) | 5(H) | 4(H) | 4(M) | 3(M) | **4.10** | ✓ | new |
| 5 | item_003 | Engineered Sortase A | 4(M) | 4(H) | 5(H) | 3(M) | 3(M) | 4(M) | **3.95** | ✓ | 0.00 |
| 5 | item_005 | EndoS2 glycosynthase | 4(M) | 4(H) | 5(H) | 3(M) | 3(M) | 4(M) | **3.95** | ✓ | 0.00 |
| 7 | item_017 | Inorganic pyrophosphatase (IVT helper) | 4(H) | 5(H) | 5(H) | 2(H) | 2(M) | 4(M) | **3.90** | ✓ | new |
| 8 | item_006 | Engineered T7 RNAP | 4(H) | 4(H) | 5(H) | 2(H) | 3(M) | 4(M) | **3.80** |   | -0.25 |
| 9 | item_009 | Engineered PAM | 4(M) | 2(M) | 5(H) | 5(H) | 4(M) | 2(L) | **3.75** |   | 0.00 |
| 10 | item_004 | FGE (aldehyde-tag) | 3(M) | 3(M) | 5(H) | 4(M) | 4(M) | 3(L) | **3.65** |   | 0.00 |
| 10 | item_022 | dsRNA-specific nuclease | 3(M) | 3(M) | 5(H) | 4(H) | 4(M) | 3(M) | **3.65** |   | new |
| 12 | item_016 | FCE::T7RNAP fusion (one-pot Cap-1) | 4(H) | 3(M) | 5(H) | 2(H) | 3(M) | 4(M) | **3.60** |   | new |
| 13 | item_015 | EfHyl8 PL8 hyaluronate lyase | 4(M) | 3(M) | 3(M) | 4(H) | 4(H) | 2(L) | **3.40** |   | new |
| 13 | item_019 | USP/OTUB1 DUB cocktail | 3(M) | 4(M) | 4(M) | 3(M) | 3(M) | 3(L) | **3.40** |   | new |
| 15 | item_013 | High-fidelity Prime Editor | 3(M) | 3(M) | 4(M) | 4(M) | 3(M) | 3(L) | **3.35** |   | 0.00 |
| 16 | item_010 | IdeS/IdeZ (QC) | 3(M) | 4(H) | 4(M) | 2(H) | 2(M) | 4(M) | **3.25** |   | 0.00 |
| 16 | item_011 | PNGase F + ST/GalT suite | 3(M) | 4(H) | 4(M) | 2(H) | 2(L) | 4(M) | **3.25** |   | 0.00 |
| 18 | item_018 | CRBN/VHL E3 ternary reagent | 4(H) | 3(M) | 4(M) | 2(H) | 2(M) | 3(M) | **3.20** |   | new |
| 18 | item_023 | TPD reagent cocktail (E1+E2+E3+DUB) | 4(H) | 3(M) | 4(M) | 2(H) | 2(M) | 3(M) | **3.20** |   | revived |
| 20 | item_001 | Next-gen hyaluronidase | 5(H) | 3(M) | 3(M) | 2(H) | 2(M) | 2(L) | **3.15** |   | 0.00 |
| 21 | item_014 | AI-designed RFdiffusion enzyme | 3(L) | 2(M) | 4(M) | 3(M) | 5(M) | 2(L) | **3.10** |   | 0.00 |
| 21 | item_020 | LCC/cutinase/AI-PETase (pharma PET) | 3(M) | 3(M) | 4(M) | 3(M) | 3(M) | 2(L) | **3.10** |   | new |
| 23 | item_012 | Cas12/Cas13 + RPA Dx | 3(M) | 3(M) | 3(M) | 2(H) | 2(M) | 3(L) | **2.75** |   | 0.00 |

(동점 시 id 순. 검증: 가중합 = 0.25·M+0.20·F+0.20·R+0.15·W+0.10·IP+0.10·T)

---

## R1 후보 14개 — 변동 사유 (delta ≠ 0인 항목만)

### item_006 — Engineered T7 RNAP: 4.05 → **3.80** (delta −0.25)
- **사유**: R2 §3.1 TriLink CleanCap M6 출시(2025.5) 데이터 — 단백질 발현 +30%, dsRNA -85%, 제조비 -20~40%. 250+ IND 의존. **효소적 capping (FCE 진영)이 chemical analog에 cost·성능에서 밀리는 신호** + R2 §3.2 FCE::T7RNAP fusion(item_016 신규)이 단독 T7 RNAP를 cannibalize 가능. → **M=5→4** (시장 점유 압박 가시화). confidence는 H로 상향(NEB·Aldevron·TriLink·Yeasen 등 다수 출처 + 정량 데이터). K primary 보정으로 W ↓ 압력 존재하나 이미 2/5 최소치.
- 산식: 0.25·4+0.20·4+0.20·5+0.15·2+0.10·3+0.10·4 = 3.80.

### item_008 — Peptiligase / OaAEP1 C247A: 4.20 → **4.30** (delta +0.10)
- **사유**: R2 §6.3 FDA Research-Grade Peptide Final Guidance (2025.3 발표, **2026.1부터 enforcement**) — 503B compounding의 인체용 peptide는 ≥99% 순도 + cGMP 의무화. 효소적 ligation이 chromatographic 부담 완화 옵션으로 부상. + R2 §8.4의 radioligand 응용 명분(item_021 평행 카드). → **T=3→4** (규제 driven 즉각 수요). L primary 보정으로 T +0~1 적용 (라이선스 기반 빠른 수익화). confidence는 M→H 상향.
- 산식: 0.25·5+0.20·4+0.20·5+0.15·3+0.10·4+0.10·4 = 4.30.

(나머지 12개 R1 후보 delta = 0.00. R2 신호 영향은 confidence 태그로만 반영.)

---

## R2 신규·부활 9개 — 6축 reasoning + confidence 사유

### item_015 — EfHyl8 PL8 hyaluronate lyase (3.40, rank 13) [new]
- **M=4 (M)**: SC 전환 시장은 강하나 non-PH20 sub-segment는 emerging. 출처 R2 §6.1 [PRN2025 RYBREVANT], R2 §4.1 [JAFC2025].
- **F=3 (M)**: PL8 fold 비교적 발현 가능(Bacillus 분비 시스템 보고 R2 §8.3 HylP), 그러나 cGMP 등급은 미검증. `[추정]` 일부.
- **R=3 (M)**: SC co-formulation 트랙이라 단독 임상 면제이나 PK/면역원성 동반 부담.
- **W=4 (H)**: Halozyme(rHuPH20)·Alteogen(ALT-B4)·Huons(HYDIZYME)는 PH20 진영, EfHyl8는 비PH20 첫 명시적 후보 → 비PH20 진영 sole entrant 가능. 출처 3+ (JAFC2025, ScienceDirect 2025, HylP Springer 2024).
- **IP=4 (H)**: PH20과 fold·메커니즘이 완전 다름 → Halozyme/Alteogen IP 직접 우회. 신규 학술 보고로 prior art 단순.
- **T=2 (L)**: cGMP scale-up + co-formulation 검증까지 4~5년.
- business_model = K/L → F 보정은 적용하지 않음(아직 catalog 없음).

### item_016 — FCE::T7RNAP fusion / FCE+2'-O-MTase one-pot Cap-1 (3.60, rank 12) [new]
- **M=4 (H)**: 600+ mRNA 임상 + IVT 효소 시장 $1.8B→$3.9B. 출처 R2 §3.1, R2 §3.2, R1 §4.2.
- **F=3 (M)**: FCE-T7RNAP fusion engineering은 가능하나 활성 균형 까다로움; one-pot 조건 최적화 필요.
- **R=5 (H)**: 명확한 process enzyme.
- **W=2 (H)**: NEB(M2081), Takara, KACTUS(DMF #038029), Yeasen, Tinzyme, Hzymes, SignalChemDx 등 매우 혼잡 + TriLink CleanCap M6 chemical analog의 강한 압박.
- **IP=3 (M)**: fusion 구성·linker 신규성 가능하나 vaccinia VCE/FCE 기본 특허 만료, 차별성 제한.
- **T=4 (M)**: catalog 진입 2~3년.
- business_model = C primary (captive) → IP +0~1 적용 가능하나 시장 혼잡으로 보정 보류.

### item_017 — Inorganic pyrophosphatase (IVT helper, GMP) (3.90, rank 7) [new, shortlist✓]
- **M=4 (H)**: RNA yield +15~25%, IVT 전수 필수. 출처 R2 §3.3 [Hzymes], R2 §8.5 [Canvax IVT data], R1 §4.2.
- **F=5 (H)**: 소형 단일 subunit, yeast/E.coli 발현 매우 잘 됨, 정제 단순.
- **R=5 (H)**: 명확한 process helper.
- **W=2 (H)**: NEB·Hzymes·Synthego·Canvax·Yeasen·Tinzyme — 매우 혼잡.
- **IP=2 (M)**: yeast PPase 자체는 commodity, 신규성 한계. non-animal source 차별화는 supply chain story.
- **T=4 (M)**: 발현·OEM 1~2년.
- business_model = C primary → captive OEM/Catalog 모델로 진입 명분 있어 가중합 0.1 boost 후보이지만, IP·W가 낮아 short-list 진입은 raw score(3.90) 자체로 달성. **R2 short-list 신규 진입.**

### item_018 — CRBN/VHL E3 ternary reagent (3.20, rank 18) [new]
- **M=4 (H)**: ARV-471 FDA 승인(2026.5.1, R2 §1.1) → PROTAC QC 시약 시장 본격화. Molecular Glue Degradation Market $402M, CAGR 8.6% (R2 §8.1).
- **F=3 (M)**: CRBN-DDB1-Cullin4 complex 발현은 multi-subunit이라 까다로움; NanoLuc fusion까지 포함.
- **R=4 (M)**: research/QC 시약.
- **W=2 (H)**: Promega(NanoBRET TE), BPS Bioscience, R&D Systems, Bio-Techne, Thermo Fisher — 표준 catalog 다수.
- **IP=2 (M)**: Promega·R&D 기본 catalog IP 강함, 신규 진입자는 변이체로만 회피 가능.
- **T=3 (M)**: catalog 진입 2~3년.
- business_model = C primary → IP +0~1 가능하나 보정 보류.

### item_019 — USP7/USP28/OTUB1 DUB cocktail (3.40, rank 13) [new]
- **M=3 (M)**: DUBTAC은 nascent 모달리티 (R2 §4.3 first-in-class 2025), PROTAC 대비 작음.
- **F=4 (M)**: cysteine protease (USP) + OTU fold, E. coli 발현 표준.
- **R=4 (M)**: research/QC 시약.
- **W=3 (M)**: BPS Bioscience(USP5 78832, USP7 79256), Boston Biochem, R&D — 일부 catalog 있으나 DUBTAC 표적 USP28·OTUB1은 빈 자리.
- **IP=3 (M)**: cocktail packaging·DUBTAC assay 워크플로 신규성.
- **T=3 (L)**: 2~3년.

### item_020 — Engineered LCC / cutinase + AI-PETase (pharma PET ESG) (3.10, rank 21) [new, absorbs item_024]
- **M=3 (M)**: 의약 PET 1차 포장재는 sub-segment, 산업 PET 재활용이 본류. 프랑스 €1,000/톤 보너스(R2 §6.2)는 incentive.
- **F=3 (M)**: LCC ICCG·CtCutS136A 등 발현 가능하나 의약 grade 검증·연속 공정 셋업 까다로움.
- **R=4 (M)**: 산업효소·환경효소, 인체 투여 없음.
- **W=3 (M)**: Carbios, Epoch Biodesign, Novonesis(HiC), Wankai JV, Samsara Eco — 산업 PET 경쟁 다수이나 pharma sub-segment는 비어 있음.
- **IP=3 (M)**: engineered variant + pharma-specific 응용 라이선스 가능.
- **T=2 (L)**: 4~5년 (pharma packaging validation 부담).
- business_model = S primary → T 양극화 적용. Carbios 재정난(R2 §6.2 controversy)으로 시기 lower bound 채택.

### item_021 — cGMP Sortase A / OaAEP1 (radioligand) (4.10, rank 3, shortlist✓) [new]
- **M=4 (H)**: AstraZeneca-Fusion $2.4B 2026Q1 클로징 + Ac-225 supply 통합 (R2 §2.1), Aktis-275 Phase 0 (R2 §1.2), FDA Research-Grade Peptide guidance 2026.1 enforce (R2 §6.3), PeptiDream 두번째 program. 다수 정량 출처.
- **F=4 (H)**: item_003/008 base enzyme 검증, OaAEP1 C247A 140× 개선(R1 §4.4). cGMP grade 셋업은 routine.
- **R=5 (H)**: process enzyme, 정제 후 제거.
- **W=4 (H)**: ADC용 sortase(NBE/Boehringer)·peptide ligase(EnzyPep)는 ADC·일반 peptide에 집중; **radioligand site-specific은 직접 경쟁자 미확정**. 신규 시장 white space.
- **IP=4 (M)**: USPTO 10556024 (sortase 18F radiolabeling) 등 기존 특허 회피 필요하나 application-specific 변이체로 신규성 확보. cGMP DMF는 진입장벽.
- **T=3 (M)**: cGMP DMF + client 검증 3~4년.
- business_model = K primary, L secondary → 빠른 수익화 + 라이선스 dual track. **R2 short-list 신규 진입.**

### item_022 — dsRNA-specific engineered nuclease (3.65, rank 10) [new]
- **M=3 (M)**: niche이지만 ShortCut RNase III 한계가 학계에 명시 (R2 §4.4 J. Chromatogr. 2024.12) → 대체 수요 확실.
- **F=3 (M)**: RNase III + dsRBD engineering 가능, AI-designed 옵션 존재. 명확한 specificity tuning은 R&D 필요.
- **R=5 (H)**: process enzyme, 정제 단계 제거.
- **W=4 (H)**: NEB ShortCut가 사실상 단독, 차세대 진입자 없음. White space 큼.
- **IP=4 (M)**: scaffold·dsRBD 추가 신규성 가능; AI-designed 옵션은 IP=5 추가 boost 가능하나 라인업 통합 카드라 4 유지.
- **T=3 (M)**: 2~3년.

### item_023 — TPD reagent cocktail (E1+E2+E3+DUB) (3.20, rank 18) [revived]
- **M=4 (H)**: ARV-471 FDA 승인 + DUBTAC 모달리티화 + $402M/CAGR 8.6% (R2 §1.1, §4.3, §8.1). 출처 다수.
- **F=3 (M)**: 다중 효소 발현 + cocktail packaging 운영 복잡.
- **R=4 (M)**: research/QC.
- **W=2 (H)**: Promega·BPS·R&D Systems·Bio-Techne·Boston Biochem가 표준 cascade catalog 보유.
- **IP=2 (M)**: cocktail 자체 신규성 약함, packaging·표적 표준화로만 차별화.
- **T=3 (M)**: 2~3년.
- item_018 + item_019의 상위 통합 패키지 카드.

---

## Short-list R2 변경 기록

**R1 short-list (7개)**: item_002, item_008, item_007, item_006, item_003, item_005, item_009.
**R2 short-list (7개)**: item_008, item_002, item_007, **item_021**, item_003, item_005, **item_017**.

| 변동 | id | weighted | 사유 |
|---|---|---|---|
| OUT | item_006 | 4.05 → 3.80 | CleanCap M6 cost race + item_016 fusion에 의한 M=5→4 강등. 3.80은 5위(3.95)와 0.15 차이로 0.2 이내이나 cap 7개 도달로 제외. |
| OUT | item_009 | 3.75 (변동 없음) | 5위(3.95)와 0.2 이내이나 cap 7개 도달로 제외. R1 raw score 7위에서 R2 raw score 9위로 밀림. |
| IN  | item_021 | new 4.10 | radioligand site-specific ligation 시장 신규 white space + AZ-Fusion·Aktis 정량 출처 3+. raw 3위. |
| IN  | item_017 | new 3.90 | IVT helper 필수 효소, RNA yield +15~25% 정량 데이터, F=5(H) 최고치. raw 7위. |

선정 룰: 가중합 상위 5개(item_008·002·007·021·003) + 6/7위가 5위(3.95)와 0.2 이내 → item_005(3.95), item_017(3.90) 포함, cap 7 도달.

---

## Quality-gate 후보

| 항목 | 변동 | 임계 |
|---|---|---|
| 단일 후보 ±1 이상 점수 변동 | **없음** | 최대 |delta| = 0.25 (item_006) |
| Top-5 가중합 표준편차 R1→R2 | 0.095 → 0.117 (Δ=+0.022) | 0.15 미만 |

→ **quality-gate 미발동.** (참고: top-5 평균은 4.10 → 4.13로 소폭 상승.)

다음 라운드 watch 항목:
- item_006 (M 추가 강등 위험 — CleanCap M6 채택률 모니터)
- item_001 vs item_015 (non-PH20 IP 우회 명분 진전 시 score 격차 좁힘)
- item_021 (cGMP 효소 단가 정량화 시 IP·T 재평가)

---

## Reference list

R2 landscape scan에서 인용한 출처 매핑 (`scope/pricing_sources.md` §5 인용 키 규칙).

### 빅파마·딜·M&A
- `[PRN2025 RYBREVANT]` — https://www.prnewswire.com/news-releases/us-fda-approves-rybrevant-faspro-amivantamab-and-hyaluronidase-lpuj-co-formulated-with-enhanze-for-the-treatment-of-advanced-egfr-mutated-non-small-cell-lung-cancer-302645429.html
- `[BioSpace2025 HYDIZYME]` — https://www.biospace.com/press-releases/huonslab-announces-submission-of-biologics-license-application-for-recombinant-human-hyaluronidase-hydizyme
- `[AZ2024 Fusion]` — https://www.astrazeneca.com/media-centre/press-releases/2024/acquisition-of-fusion-completed.html
- `[ABCM2025 Fusion]` — https://www.abcmoney.co.uk/2025/10/astrazeneca-bolsters-oncology-with-1-2-billion-fusion-buyout-amid-uk-growth/
- `[BioSpace2025 PeptiDream]` — https://www.biospace.com/press-releases/peptidream-announces-second-internal-peptide-radiopharmaceutical-therapeutic-program-targeting-claudin-18-2-for-the-potential-diagnosis-and-treatment-of-gastric-cancer

### CDMO·공급망·catalog
- `[TriLink2025 CleanCap]` — https://www.trilinkbiotech.com/press-releases/trilink-biotechnologies-debuts-its-first-mrna-synthesis-kit-with-cleancap-capping-technology
- `[Maravai2025 CleanCapM6]` — https://investors.maravai.com/news-events/press-releases/detail/64/trilink-biotechnologies-introduces-latest-mrna-capping-technology-cleancap-m6-analog
- `[NEB M2081]` — https://www.neb.com/en-us/products/m2081-faustovirus-capping-enzyme
- `[Takara FCE]` — https://www.takarabio.com/products/mrna-and-cdna-synthesis/in-vitro-transcription/rna-modification/faustovirus-capping-enzyme
- `[KACTUS DMF038029]` — https://kactusbio.com/products/mrna-cap-2-o-methyltransferase-gmp-grade-gmp-meh-ve101
- `[Hzymes PPase]` — https://www.hzymesbiotech.com/articles/yeast-inorganic-pyrophosphatase/
- `[Yeasen 10612]` — https://www.yeasenbio.com/products/10612
- `[Tinzyme PAP]` — https://www.tinzyme.com/mrna-material/e-coli-polya-polymerase/
- `[Canvax IVT]` — https://www.canvaxbiotech.com/news/inorganic-pyrophosphatase-ivt-rna-yield/
- `[Promega NanoBRET]` — https://www.promega.com/products/protein-detection/protein-degradation-protacs/nanobret-te-intracellular-e3-ligase-assays/
- `[RD E305]` — https://www.rndsystems.com/products/recombinant-human-ubiquitin-activating-enzyme-ube1-cf_e-305
- `[BPS UBE1 80301]` — https://bpsbioscience.com/ube1-uba1-flag-tag-recombinant-80301
- `[BPS USP7 79256]` — https://bpsbioscience.com/usp7-inhibitor-screening-assay-kit-79256

### 학계·preprint
- `[JAFC2025 EfHyl8]` — https://pubs.acs.org/doi/10.1021/acs.jafc.5c12120
- `[ScienceDirect2025 EfHyl8]` — https://www.sciencedirect.com/science/article/abs/pii/S0144861725008732
- `[Springer2024 HylP]` — https://link.springer.com/article/10.1007/s12010-024-04883-w
- `[Crystals2026 CtCut]` — https://www.recycling-magazine.com/2026/04/20/heat-stable-cutinase-pet-recycling/
- `[PMC11928388 CtCut]` — https://pmc.ncbi.nlm.nih.gov/articles/PMC11928388/
- `[JMC2025 DUBTAC]` — https://pubs.acs.org/doi/10.1021/acs.jmedchem.4c02975
- `[Angew2025 DUBTAC]` — https://onlinelibrary.wiley.com/doi/abs/10.1002/anie.202415168
- `[PMC12891886 DUBTAC]` — https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12891886/
- `[JChrom2024 RNaseIII]` — https://www.sciencedirect.com/science/article/abs/pii/S002196732400949X
- `[PubMed39642661]` — https://pubmed.ncbi.nlm.nih.gov/39642661/
- `[Biochempeg PROTAC]` — https://www.biochempeg.com/article/434.html
- `[Promega TPD]` — https://www.promega.com/applications/small-molecule-drug-discovery/protein-degradation-drug-discovery/e3-ternary-complex/
- `[USPTO 10556024]` — https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/10556024

### 스타트업·VC
- `[TechCrunch2025 Epoch]` — https://techcrunch.com/2025/03/05/from-high-school-science-project-to-18-3m-ai-accelerated-enzymes-are-coming-for-fast-fashions-plastic-waste/
- `[TechEU2026 Epoch]` — https://tech.eu/2026/03/25/epoch-biodesign-raises-12m-to-bring-recycled-nylon-to-scale/
- `[EUStartups2026 Epoch]` — https://www.eu-startups.com/2026/03/epoch-biodesign-raises-e10-3-million-to-use-ai-and-enzymes-to-recycle-plastic-and-textile-waste-at-commercial-scale/

### 인접산업·규제
- `[Carbios2025 H1]` — https://www.carbios.com/newsroom/en/carbios-presents-its-2025-half-year-results-and-confirms-its-objective-to-build-a-pet-biorecycling-plant-with-a-revised-timeline/
- `[Carbios2025 Wankai]` — https://www.carbios.com/newsroom/en/carbios-and-wankai-new-materials-a-subsidiary-of-zhink-group-are-committed-to-the-large-scale-deployment-of-carbios-pet-biorecycling-technology-in-asia/
- `[Labiotech2026 Carbios]` — https://www.labiotech.eu/trends-news/carbios-controversy/
- `[RealPeptides2026 FDA]` — https://www.realpeptides.co/research-peptides-legal-2026-fda-rules-explained/
- `[AnalystView2025 MG]` — https://www.analystviewmarketinsights.com/reports/report-highlight-molecular-glue-degradation-agent-market
- `[VectorBuilder polyA]` — https://en.vectorbuilder.com/resources/vector-academy/troubleshooting/mRNA-polyA-tail.html
