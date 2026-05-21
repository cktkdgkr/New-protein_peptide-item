# Protein/Peptide Item Discovery — Round 2 Digest 2026-05-21

run_id: `20260521-B`   |   focus: `deferred_and_boost`   |   scope SSOT: `scope/inclusion.md`, `scope/exclusion.md`

---

## 1. Round 2 한 페이지 요약

- **R2가 한 일**: R1에서 보류·`[추정]`이던 5개 영역(TPD reagents / PETase·cutinase / non-PH20 hyaluronidase / radioligand enzymatic conjugation / mRNA aux 효소)을 표적 스캔해 **fresh signal 18개** 추가, **부활 후보 2건**(item_023 TPD cocktail / item_024 PET cutinase → item_020 흡수) + **신규 후보 8건**(item_015~022)을 정식 카드화. 누적 활성 후보 = **23개**(R1 14 + 부활 활성 1 + 신규 8).
- R1 14개에 `business_model`(L/K/C/S/H) + `lifecycle` 필드를 사후 부여, 모든 6축 점수에 confidence H/M/L 태그 적용.
- 가장 결정적인 R2 신호 2건: (1) **EfHyl8 학계 보고 (JAFC 2025)** — non-PH20 SC 확산 효소의 첫 명시적 후보, (2) **ARV-471(vepdegestrant) FDA 승인 (2026.5.1) + DUBTAC 모달리티화** — TPD 시약 시장의 본격 commercial 진입.

### R2 Top 3 short-list

| 순위 | 아이템 | 가중합 | 한 줄 사유 (R1 대비 변동) |
|---|---|---|---|
| 1 | **item_008** Peptiligase / OaAEP1 C247A | **4.30** ▲ | FDA Research-Grade Peptide guidance(2026.1 enforcement) → 효소적 ligation이 cGMP 부담 완화 수단으로 가시화. T 3→4. (R1 1위 유지, +0.10) |
| 2 | **item_002** Engineered mTG (ADC site-specific) | **4.20** | ADC $13.5B + Lonza Visp 2배 확장 — R2 변동 없음 (R1 1위→2위, 점수 동일) |
| 3 (tie) | **item_007** Engineered RNA ligase / **item_021** cGMP Sortase A · OaAEP1 (radioligand) | **4.10** | item_021 = R2 신규 진입, AZ–Fusion $2.4B 클로징 + Aktis Phase 0 + Research-Grade Peptide guidance의 직접 수혜 |

### Short-list 변동 요약 (R1 7개 → R2 7개)

| 변동 | id | weighted | 사유 |
|---|---|---|---|
| IN  | **item_021** cGMP Sortase A · OaAEP1 (radioligand) | new 4.10 | radioligand site-specific ligation 신규 white-space, 출처 3+ 정량 |
| IN  | **item_017** Inorganic pyrophosphatase (IVT helper) | new 3.90 | IVT yield +15-25% 정량 데이터, F=5(H) 최고치 |
| OUT | **item_006** Engineered T7 RNAP | 4.05 → 3.80 | TriLink CleanCap M6 cost race + item_016 fusion에 의해 M=5→4 강등 |
| OUT | **item_009** Engineered PAM | 3.75 (변동 없음) | 점수 동일하나 cap 7개 도달로 제외 (R2 raw 9위로 밀림) |

유지된 5개: item_002 / item_003 / item_005 / item_007 / item_008.

---

## 2. R2 신규/갱신 시장 신호 Top 5

| # | 신호 | 출처 키 | 한 줄 함의 |
|---|---|---|---|
| 1 | **ARV-471 (vepdegestrant) FDA 승인 (2026.5.1)** — oral PROTAC 첫 신약 | `[Biochempeg PROTAC]` `[Promega TPD]` | PROTAC QC·screening enzyme 시장의 임상→시판 단계 본격 진입. item_018·019·023 직접 동력. |
| 2 | **EfHyl8 (E. faecalis PL8 hyaluronate lyase) — JAFC 2025** | `[JAFC2025 EfHyl8]` `[ScienceDirect2025 EfHyl8]` `[Springer2024 HylP]` | 비PH20 fold·메커니즘 → Halozyme/Alteogen IP 우회 명분. item_015의 IP=4(H), W=4(H) 핵심 근거. |
| 3 | **FCE::T7RNAP fusion + 2′-O-MTase one-pot Cap-1** (NEB·Takara·KACTUS GMP) vs **TriLink CleanCap M6** | `[TriLink2025 CleanCap]` `[NEB M2081]` `[KACTUS DMF038029]` | enzymatic capping이 chemical analog와 cost race; FCE fusion이 응전. item_006 강등·item_016 신설의 직접 원인. |
| 4 | **AstraZeneca–Fusion $2.4B 2026 Q1 클로징 + Ac-225 supply 통합** + Aktis-275 64Cu-PD-29875 Phase 0 + PeptiDream 두번째 program | `[AZ2024 Fusion]` `[BioSpace2025 PeptiDream]` | radiopharma 공정 throughput 압박 → cGMP enzymatic conjugation 채택 명분. item_021 신규 진입 직접 동력. |
| 5 | **Carbios Wankai JV (50 kt/년) 가동 + 프랑스 €1,000/톤 sensitive-contact 보너스 (2025.9 decree)** + Epoch Biodesign 누적 $50M+ | `[Carbios2025 Wankai]` `[TechCrunch2025 Epoch]` `[Crystals2026 CtCut]` | PETase·LCC variant의 의약 PET 포장재 ESG 응용 incentive. item_020 부활·신설 근거. |

보조 신호: Huons HYDIZYME BLA(3rd-tier human PH20), Hzymes yeast PPase non-animal GMP(+15-25% yield), DUBTAC first-in-class (Angew 2025), ShortCut RNase III off-target 보고.

---

## 3. 후보 풀 갱신 통계

| 구분 | 개수 | id 범위 |
|---|---|---|
| R1 유지 (maintained_at_round_2) | 14 | item_001~014 |
| R2 부활 (revived_from_round_1, 활성) | 1 | item_023 (TPD cocktail) |
| R2 신규 (new_at_round_2) | 8 | item_015~022 |
| 병합 (merged_into) | 1 | item_024 → item_020 |
| 드롭 (dropped_at_round_2) | 0 | — |
| **누적 활성 후보** | **23** | — |

### business_model primary 분포 (활성 23개)

| L (Licensing) | K (Kit/Reagent) | C (Captive/Catalog) | S (Service) | H (Hybrid) |
|---|---|---|---|---|
| 3 (item_003, 007, 008) | 12 (item_001, 002, 004, 005, 006, 009, 010, 011, 012, 013, 015, 021) | 6 (item_016, 017, 018, 019, 022, 023) | 2 (item_014, 020) | 0 |

### 포함기준 분류 분포 (활성 23개)

| 생산공정용 효소 | 제형변경 조력 | 진단·연구·산업 의약 인접 | 펩타이드 제조 |
|---|---|---|---|
| 9 (item_002, 003, 004, 005, 006, 007, 016, 017, 022) | 2 (item_001, 015) | 9 (item_010, 011, 012, 013, 014, 018, 019, 020, 023) | 3 (item_008, 009, 021) |

---

## 4. Short-list 상세 (7개)

각 항목: 정의 + business_model + 6축 점수 막대 + 가중합 + (R1→R2 delta).
가중치: M 0.25 / F 0.20 / R 0.20 / W 0.15 / IP 0.10 / T 0.10.

### #1 item_008 — Peptiligase / OaAEP1 C247A — green enzymatic peptide ligation  `L / K`
- **정의**: Asparaginyl endopeptidase (butelase-1 family) variant — SPPS fragment 효소 ligation으로 GLP-1·인슐린·radioligand peptide 제조.
- 6축 (confidence): M `█████` 5(H) | F `████░` 4(H) | R `█████` 5(H) | W `███░░` 3(M) | IP `████░` 4(M) | T `████░` 4(M) ▲
- **가중합 = 4.30 ▲ (+0.10 vs R1)** — T 3→4, FDA Research-Grade Peptide guidance(2026.1 enforce) 직격.

### #2 item_002 — Engineered mTG (ADC site-specific conjugation)  `K / L`
- **정의**: Streptomyces mTG 변이체로 항체 LLQG-tag glutamine과 amine payload를 isopeptide 결합 → 균일 DAR2/4 ADC 제조.
- 6축: M `█████` 5(H) | F `████░` 4(M) | R `█████` 5(H) | W `███░░` 3(M) | IP `███░░` 3(M) | T `████░` 4(M)
- **가중합 = 4.20** (변동 없음)

### #3 (tie) item_007 — Engineered RNA ligase (splint, AOC/ASO)  `L / K`
- **정의**: T4 Rnl2 / RtcB variant로 splint DNA 가이드 fragment ligation → 긴 siRNA·AOC 저비용 합성.
- 6축: M `████░` 4(H) | F `████░` 4(M) | R `█████` 5(H) | W `████░` 4(M) | IP `████░` 4(M) | T `███░░` 3(M)
- **가중합 = 4.10** (변동 없음)

### #3 (tie) item_021 — cGMP Sortase A / OaAEP1 (radioligand peptide-chelator)  `K / L`  **NEW**
- **정의**: cGMP-grade Sortase A LPXTG + OaAEP1 C247A NGL → DOTA/HEHA/NETA chelator를 peptide ligand에 site-specific 결합, ⁶⁴Cu/¹⁷⁷Lu/²²⁵Ac 라벨링.
- 6축: M `████░` 4(H) | F `████░` 4(H) | R `█████` 5(H) | W `████░` 4(H) | IP `████░` 4(M) | T `███░░` 3(M)
- **가중합 = 4.10 (NEW)** — item_003/008의 cGMP·radioligand 응용 fork.

### #5 (tie) item_003 — Engineered Sortase A variant (Ca-independent)  `L / K`
- **정의**: eSrtA 7M/2A-9 등 directed-evolution variant — Ca²⁺ 없이 LPETG / GGGG isopeptide 결합 → ADC/AOC/radioligand.
- 6축: M `████░` 4(M) | F `████░` 4(H) | R `█████` 5(H) | W `███░░` 3(M) | IP `███░░` 3(M) | T `████░` 4(M)
- **가중합 = 3.95** (변동 없음)

### #5 (tie) item_005 — EndoS2 glycosynthase mutant (Fc glycan remodel)  `K / L`
- **정의**: S. pyogenes EndoS2 D184M class — Fc N297 균일 glycan 결합(ADCC 강화·biosimilar 균질화).
- 6축: M `████░` 4(M) | F `████░` 4(H) | R `█████` 5(H) | W `███░░` 3(M) | IP `███░░` 3(M) | T `████░` 4(M)
- **가중합 = 3.95** (변동 없음)

### #7 item_017 — Inorganic pyrophosphatase (IVT helper, GMP non-animal)  `C / —`  **NEW**
- **정의**: Yeast/E. coli PPase — T7 RNAP IVT의 PPi 피드백 억제 해제 → RNA yield +15-25%.
- 6축: M `████░` 4(H) | F `█████` 5(H) | R `█████` 5(H) | W `██░░░` 2(H) | IP `██░░░` 2(M) | T `████░` 4(M)
- **가중합 = 3.90 (NEW)** — F=5(H) 최고치, non-animal GMP가 entry 포인트.

### Short-list 사업화 형태별 그룹 표

| business_model | id | 한 줄 요약 |
|---|---|---|
| **L (Licensing)** primary | item_003, item_007, item_008 | Sortase A · RNA ligase · Peptiligase — 공정 라이선스 + 효소 공급 dual track. green chem·AOC·GLP-1 패키지. |
| **K (Kit/Reagent)** primary | item_002, item_005, item_021 | mTG · EndoS2 · cGMP sortase/OaAEP1 — GMP enzyme catalog가 1차 매출. tag·donor·chelator 설계 secondary L. |
| **C (Captive/Catalog)** primary | item_017 | Yeast/E.coli PPase — non-animal source captive OEM. K로 확장 가능. |
| **S (Service)** primary | (short-list에 없음) | item_014(AI enzyme), item_020(pharma PET)은 short-list 외. |
| **H (Hybrid)** | (없음) | — |

---

## 5. 점수 변동 (R1 → R2)

|delta| ≥ 0.10 인 후보만 표기.

| id | 아이템 | R1 score | R2 score | delta | 사유 (1줄) |
|---|---|---|---|---|---|
| item_006 | Engineered T7 RNAP | 4.05 | **3.80** | **−0.25** ▼ | TriLink CleanCap M6 (단백질 발현 +30%, dsRNA -85%, 제조비 -20-40%, 250+ IND 의존) + item_016 fusion 등장으로 M=5→4 강등. **Short-list OUT.** |
| item_008 | Peptiligase / OaAEP1 C247A | 4.20 | **4.30** | **+0.10** ▲ | FDA Research-Grade Peptide guidance(2025.3 발표, 2026.1 enforce)로 cGMP peptide ligase 수요 즉각 부상 → T 3→4. **Top 1 유지.** |

나머지 R1 12개 후보는 delta = 0.00 (R2 신호 영향은 confidence 태그로만 반영).
신규/부활 9개(item_015~023)는 R2가 첫 스코어 → delta `new` / `revived`.

**핵심 통찰**: item_006의 −0.25는 R2 |delta| 최대치이며 quality-gate 임계(단일 후보 ±1) 미달. 그러나 mRNA capping 분야의 enzyme vs chemical analog 경쟁구도 변화가 가장 큰 라운드별 점수 신호.

---

## 6. confidence 분포 / Quality-gate

### 6축 confidence H/M/L 카운트 (전체 23개 × 6축 = 138 셀)

| 축 | H | M | L |
|---|---|---|---|
| Market (M)         | 8  | 14 | 1  |
| Feasibility (F)    | 8  | 15 | 0  |
| Regulatory (R)     | 12 | 11 | 0  |
| Whitespace (W)     | 13 | 10 | 0  |
| IP                 | 1  | 21 | 1  |
| Time-to-revenue (T)| 0  | 14 | 9  |
| **합계**           | **42** | **85** | **11** |

비율: H 30.4% / M 61.6% / L 8.0%. **IP·T 축이 confidence 약점** (IP는 거의 전부 M, T는 9개가 L — cGMP·service biz 셋업 추정 불확실).

### Top 5 weighted SD 변화
- R1 top-5 SD = **0.095**
- R2 top-5 SD = **0.117** (Δ = +0.022)
- 임계 0.15 미만 → **quality-gate 미발동**.

### Quality-gate 종합

| 항목 | 결과 |
|---|---|
| 단일 후보 ±1.0 이상 점수 변동 | 없음 (최대 |delta| = 0.25, item_006) |
| Top-5 가중합 SD ≥ 0.15 | 미발동 (0.117) |
| **종합** | **quality-gate 미발동** — R3 정상 진행 (auto-chain) |

(참고: top-5 평균 4.10 → 4.13으로 소폭 상승. short-list 평균 품질은 안정적.)

---

## 7. 위험·미지수

### R1 유지 영역 위험
- **단가 [추정] 다수**: GMP enzyme $5~30k/g 가정의 출처 다수가 [추정]. R3 정량화 필요.
- **IP 분쟁**: Halozyme vs Merck (Keytruda SC), NBE/Boehringer SMAC sortase, EnzyPep peptiligase, Codexis ECO 청구항 — FTO 미해결.
- **Scope 경계 사례**: item_001(hyaluronidase 결합제형 PK 부담), item_010(IdeS — Hansa imlifidase와 충돌), item_013(prime editor in-vivo 분리).

### R2 신규 위험
- **EfHyl8 (item_015)**: SC 확산 효능을 학술적으로 명시했으나 **정량 비교 데이터(vs rHuPH20)** 미발표, 면역원성·PK 안정성 임상 단계 미진입. **IP 우회 명분만으로는 사업화 불충분.**
- **FCE::T7RNAP fusion (item_016)**: fusion 활성 균형·linker engineering 난이도 미검증. vaccinia VCE/FCE 기본 특허 만료지만 fusion 구성 IP 약함. NEB·KACTUS·Yeasen 등 공급사 매우 혼잡 (W=2).
- **TPD cascade cross-cannibalization**: item_018(E3 ternary) + item_019(DUB cocktail) + item_023(전체 cocktail) 3단 계층이 동일 고객을 두고 SKU 자기잠식 위험. R3에서 패키지화 vs 단품화 전략 결정 필요.
- **item_021 vs item_003/008**: 효소 자체 동일, 응용·grade만 다름 → R3에서 단가·볼륨 정량화 시 통합 또는 carve-out 결정.
- **item_006 추가 강등 가능성**: CleanCap M6 채택률 가속 시 M=4→3 추가 강등 → 4번째 OUT 후보 모니터링.
- **TPD 시장 $402M 단일 출처**: AnalystView 1건 — 교차검증 필요.

---

## 8. Round 3 제안 (focus = quantitative validation + IP/FTO)

`scope/iteration_plan.md` §2 R3 항목 기반, R2에서 특히 정량화 필요한 영역을 우선순위화:

| 우선순위 | 검증 항목 | 산출 목표 |
|---|---|---|
| **1** | **EfHyl8 vs rHuPH20 SC 확산 정량 비교 + Halozyme IP 회피 분석** | EfHyl8 hyaluronan turnover (U/mg) · SC diffusion zone (mm²·hr⁻¹) 정량; Halozyme US/EP claim 매핑 |
| **2** | **mTG cluster 특허 (Ajinomoto/Hzymes/Zedira) FTO 분석** | item_002 IP 점수 3→? 재평가 근거 확보 |
| **3** | **Codexis ECO Synthesis 핵심 청구항 + item_021 sortase·OaAEP1 radioligand 경쟁자 매핑** | item_007·item_021의 W·IP 정밀화 |
| **4** | **EnzyPep peptiligase vs OaAEP1 C247A IP claim 비교** | item_008·item_021 carve-out 가능성 판단 |
| **5** | **FCE::T7RNAP fusion 발현·활성 균형 학술 검증 + 특허 상태** | item_016 F·IP 재평가, item_006와의 협력/경쟁 시나리오 결정 |
| **6** | **TPD reagent 시장 $402M 출처 교차검증 + DUBTAC 시약 시장 sizing** | item_018·019·023 M 점수 confidence H/M 결정 |

보조: GMP enzyme 단가($5~30k/g) 출처 보강, cGMP CDMO RFI (Lonza Visp / Samsung Bio / WuXi XDC), Carbios C-ZYME pharma PET FTO.

R3 완료 후 D는 per-iter digest + **consolidated_digest** (3라운드 통합)를 작성한다.

---

## 9. 메타

| 항목 | 값 |
|---|---|
| run_id | 20260521-B |
| 실행일 | 2026-05-21 (UTC) |
| 입력 파일 | `iterations/iter_02/pipeline/{01_landscape_scan,02_candidates,03_scored}.md`, `iterations/iter_02/data/candidates.csv`, `iterations/iter_02/candidates/item_{017,021}_*.md`, `reports/digest_20260521.md` (R1), `data/candidates_history.csv` (R1+R2 38행), `state/run_state.json` |
| Phase A 소요 | 2026-05-21 07:10 → 07:45 UTC (35분, 18 fresh signal) |
| Phase B 소요 | 07:45 → 08:20 UTC (35분, 신규 8 + 부활 1 + 병합 1 + R1 14개 사후 보강) |
| Phase C 소요 | 08:20 → 09:05 UTC (45분, 23개 6축 + confidence; quality-gate 미발동) |
| Phase D 소요 | 09:05 → 본 digest 작성 |
| 재시도 | 없음 (A→B→C→D 1회 통과) |
| 한계 | (1) Top 5 신호 중 TPD 시장 $402M·CleanCap M6 +30% 발현 데이터는 일부 1차 출처 (교차검증 R3). (2) item_015 EfHyl8의 vs rHuPH20 정량 비교 부재. (3) cGMP enzyme 단가 추정은 R1과 동일하게 [추정]. (4) 이번 라운드는 per-iter digest만 작성, consolidated digest는 R3에서 작성 (min_iterations=3 미도달). |
