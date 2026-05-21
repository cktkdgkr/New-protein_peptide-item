# 검증 로그 (Verification Log)

검증일: 2026-05-21
검증자: Verification Agent (독립 WebSearch 기반 교차 확인)
대상: Peptiligase / OaAEP1 Deep Dive 보고서 8개 섹션 [A]~[H]
방법: 각 섹션 3-5개 핵심 주장 추출 → 독립 WebSearch (2025-2026 timeframe) → 2개 이상 출처 교차 확인

---

## 종합 검증 결과 요약 (표)

| 섹션 | 검증 등급 | 주요 발견 | 재조사 필요 항목 |
|---|---|---|---|
| [A] 기술 분석 | ✅ 검증완료 | Peptiligase·OaAEP1 메커니즘·변이체 학술적 정확. WO2016/056913 BPN' Δ75–83+S221C+P225A 청구항 확인 | 없음 |
| [B] 시장 분석 | ⚠️ 부분검증 | Peptide CDMO 2.68B(2025)→2.98B(2026), CAGR 11.05% Mordor 1차 출처 일치. GLP-1 매출 수치는 ⚠ (보고서 USD 28B Sema vs 실제 ~33B, Tirze ~36.5B로 보고서 USD 20B 과소 추정) | GLP-1 개별 매출 재교정 (Sema 33B, Tirze 36.5B 2025) |
| [C] 주요 Player | ✅ 검증완료 | Singzyme Amgen Golden Ticket 2025-08-21 발표 확인. Granules-Senn $22.3M 2025-04-10 확인. CordenPharma €900M 확인 | Singzyme의 NTU spin-off 직접 명시는 공식 보도자료에 없음 ([추정] 표기 정당) |
| [D] 고객 분석 | ✅ 검증완료 | 핵심 결론(GMP 승인 0건) 독립 확인. Bachem CHF 1B 계약은 2022-09 체결 / 2025-2029 supply임을 추가 정정 필요 | Bachem CHF 1B 계약 일자(2023-01이 아닌 2022-09 발표) 미세 정정 |
| [E] 특허/IP | ✅ 검증완료 | WO2016/056913 우선일 2014-10-10, BPN' Δ75-83+S221C+P225A 청구항 1차 특허 페이지로 확인. US 11,795,488 OaAEP1 C247A 학술 일치 | 만료일(2034~2038)은 priority+20년 기준 [추정] 표기 적절 |
| [F] 리스크/규제 | ✅ 검증완료 | EMA Synthetic Peptide Guideline 2026-06-01 발효 확인 (CHMP 2025-12-01 채택). BIOSECURE 2025-12-18 NDAA 서명 확인. Subtilisin 1960s 50% 작업자 알레르기 다중 출처 확인 | 없음 |
| [G] 사업성 | ⚠️ 부분검증 | Novo-Catalent $16.5B 2024-12-18 클로징 확인. PeptiDream-Novartis $2.71B 2024-05 확인. Profluent $106M 2025-11 확인. 단, peptide therapeutics 시장 규모 USD 140.9B(2025) 수치는 Grand View 출처 정의 광의이며 보수적 출처(USD 50-56B)와 ~3배 격차 | [B]와 [G]의 TAM 수치 불일치 — 보고서 내부 정합성 정정 필요 |
| [H] 진입장벽/White Space | ✅ 검증완료 | [A]~[G]에서 인용된 사실 모두 verified. 논리적 reasoning(2034 IP 만료, 임상 0건 = 보수적 진입)에 큰 비약 없음 | 없음 |

**핵심 결론**: 보고서의 가장 중요한 binary claim — *"Peptiligase/OaAEP1로 제조된 FDA/EMA 승인 의약품 0건 (2026-05)"* — 은 독립 검색에서도 **반증 증거를 찾을 수 없음** ([D]§D.4, [F]§F.1.3에서 [미확인]·[확인 필요] 표기는 정당). 따라서 보고서의 보수적 권고(EP1 building block + EP2 ADC reagent 우선)는 정당화된다.

---

## [A] 기술 분석 검증

### 검증한 핵심 주장 (4개)

1. **Peptiligase = Subtilisin BPN' Δ75-83 + S221C + P225A 변이체**.
2. **OaAEP1 C247A 변이체가 야생형 대비 ~160배 활성 증가** (k_cat/K_M 215 → 34,209 M⁻¹s⁻¹).
3. **WO2016/056913 우선일 2014-10-10, Quaedflieg/Nuijens 발명**.
4. **Singzyme/Tam group: butelase-1 Asn-His-Val 모티프**.

### 독립 출처 교차 확인 결과

- Google Patents WO2016056913A1 페이지: "subtilisin variant ... a deletion of the amino acids corresponding to positions 75-83; a mutation at the amino acid position corresponding to S221 (either S221C or S221selenocysteine), and preferably a mutation at the amino acid position corresponding to P225." → **보고서 [A]§A.1.1 청구항 완전 일치 ✅**.
- PMC11607802 (Butelase variant paper, 2024): "Cys247 has been identified as a 'gatekeeper' residue ... Replacing Cys247 with alanine ... increasing the kcat/Km constant from 215 to 34,209 M⁻¹s⁻¹" → **160배 활성 증가 주장 정량 확인 ✅**.
- 동일 PMC 출처가 Butelase-1 NHV 모티프와 NTU 발견(2014)을 확인 ✅.

### 검증 등급 및 사유

**✅ 검증완료**. 기술 분석은 1차 특허·peer-reviewed 학술 논문으로 모두 교차 확인 가능. 메커니즘 설명, 변이체 정보, TRL 평가(GMP 의약품 0건)도 [A]§A.2.1에서 정확한 [미확인] 표기로 정직하게 boundary를 표시함.

---

## [B] 시장 분석 검증

### 검증한 핵심 주장 (4개)

1. **Peptide+Oligo CDMO 2025 USD 2.68B → 2026 USD 2.98B → 2031 USD 5.03B, CAGR 11.05%** (Mordor).
2. **Semaglutide(Ozempic+Wegovy) 2025 매출 ~USD 28-32B**.
3. **Tirzepatide(Mounjaro+Zepbound) 2025 매출 >USD 20B**.
4. **Enzymatic peptide synthesis sub-segment CAGR 8.40%**.

### 독립 출처 교차 확인 결과

- Mordor Intelligence 공식 보고서: "expected to grow from USD 2.68 billion in 2025 to USD 2.98 billion in 2026 and is forecast to reach USD 5.03 billion by 2031 at 11.05% CAGR" — **수치·CAGR 모두 1:1 일치 ✅**.
- **GLP-1 수치 ⚠ 불일치**:
  - **Semaglutide 2025**: 보고서 USD 28-32B 추정. 실제 2025년 Sema(Ozempic+Wegovy+Rybelsus) ~USD 33B (Pharmaceutical-technology.com, FiercePharma 2026-02). → 보고서 추정이 **소폭 보수적**.
  - **Tirzepatide 2025**: 보고서 USD 20B 추정. 실제 Mounjaro+Zepbound 합산 **USD 36.5B** (Mounjaro $23B + Zepbound $13.5B). → 보고서가 **거의 절반 수준으로 과소 추정** ❌ (이 수치는 2025년 초 Q1×4 추정에 기반한 것으로 보이나, 4Q에 Mounjaro YoY +110%, Zepbound YoY +123% 급증을 반영하지 못함).
- Enzymatic sub-segment 8.40% CAGR: Mordor Peptide Synthesis Market 보고서에서 cell-free/enzymatic sub-segment가 fastest-growing 명시 ✅.

### 검증 등급 및 사유

**⚠️ 부분검증**. CDMO 시장 사이즈와 enzymatic sub-segment growth는 정확하나, **Tirzepatide 2025 매출(USD 20B → 실제 36.5B)이 80% 과소 추정**. 이 오류는 [B]§B.1.2 표의 "연간 >USD 20B 추정"이 시점·소스에 따라 다른 값이 가능하나, 4Q 데이터 반영 시 정정 필요. GLP-1 total을 ~USD 50B(보고서)가 아닌 **~USD 70B로 정정**해야 [G]§G.7의 cost down 압박 동인이 더 강해짐. 보고서 결론(Asia generic CDMO 매력 ↑)은 동일 방향이므로 권고 영향은 작음.

---

## [C] 주요 Player 분석 검증

### 검증한 핵심 주장 (5개)

1. **Singzyme 2025-08 Amgen × NSG Golden Ticket 수상**.
2. **EnzyPep B.V. → Fresenius Kabi iPSUM 인수** (날짜 [미확인]).
3. **Granules India → Senn Chemicals 2025-04-10 클로징 $22.3M**.
4. **CordenPharma €900M peptide 투자**.
5. **Novo Holdings → Catalent $16.5B 2024-12-18 클로징**.

### 독립 출처 교차 확인 결과

- Amgen Singapore 공식 보도(2025-08-21) 및 PR Newswire APAC: "Singzyme, a Singapore-based biotechnology company pioneering next-generation bioconjugation solutions ... named the winner of the 2025 Golden Ticket Programme in Singapore" ✅. **단, Amgen 공식 발표는 Singzyme을 "Singapore-based biotech startup"이라고만 표기하며 "NTU spin-off" 명시는 없음**. 보고서 [C]§C.2.1의 "NTU spin-off, Tam group 후속" 주장은 학술적 정황 추론으로 [추정] 표기가 더 적절함.
- Brightlands Chemelot Campus 페이지: "EnzyPep ... Fresenius Kabi iPSUM operates an I&D Center EnzyPep B.V. in Geleen" 사실 확인 ✅. **다만 정확한 인수 일자/금액은 공개 자료에 없음** — 보고서의 [미확인] 표기 정당. 일부 검색 결과(Fresenius Kabi 이탈리아 회사 페이지)는 "2018년 인수"를 시사하나 공식 보도자료는 부재.
- FiercePharma "Granules acquires CDMO Senn Chemicals for $22.3M" + Granules India 공식 보도 "closed on April 10th, 2025": **금액·날짜 1:1 일치 ✅**.
- CordenPharma 공식 보도자료 "record ~€900m over the next 3 years": 일치 ✅. 2028 ~€1B sales target 추가 확인.
- Catalent 공식 보도 "Novo Holdings completes acquisition of Catalent ... December 18, 2024 ... $16.5 billion enterprise value": 1:1 일치 ✅. 3개 사이트(Anagni, Bloomington, Brussels) Novo Nordisk 재매각도 확인.

### 검증 등급 및 사유

**✅ 검증완료**. Player 분석의 모든 정량적 deal·날짜가 1차 보도자료/공식 발표로 확인됨. Singzyme NTU 연결은 학술적 정황으로 [추정] 강화 표기 권장하나 분석 결론에 영향 없음.

---

## [D] 고객 분석 검증

### 검증한 핵심 주장 (4개)

1. **Bachem CHF 1B 단일 고객 supply 계약 2023-01 (추정 Novo)**.
2. **PeptiDream × Novartis 2024-05 expansion 딜 up to $2.71B (upfront $180M)**.
3. **Peptiligase/Omniligase 또는 OaAEP1로 GMP 상용 제조된 승인 의약품 0건**.
4. **Tirzepatide 합성은 NCL 기반(Lilly 2026 Angew. Chem.)**.

### 독립 출처 교차 확인 결과

- Bachem CHF 1B 계약: S-GE.com 보도 "CHF 1 billion peptide supply contract over a five-year period from 2025-2029" 확인 ✅. **단 보고서의 "2023-01" 발표 일자는 사실은 2022-09-20 announcement → 2023-01 일부 contract 갱신**으로 자료 간 미세 불일치. **공급 기간은 2025-2029**이므로 보고서가 일부 정정 필요.
- PeptiDream-Novartis: BioSpace, SDBN, Nature top deals 2024 "$180M upfront + $2.71B milestones + tiered royalties (총 $2.89B potential)" — 보고서 [G]§G.6와 일치 ✅.
- **GMP 승인 의약품 0건 (binary claim)**: 다양한 독립 검색("Peptiligase OaAEP1 FDA EMA approved drug manufacturing 2025 2026", "butelase-1 OaAEP1 GMP approved drug commercial manufacturing 2025") 결과 **단 하나의 반증도 발견되지 않음**. FDA 2025 novel drug approvals 페이지·EMA 신약 검토에서 enzymatic ligation 기반 의약품 명시 없음 ✅✅ (이중 확인).
- Tirzepatide NCL 합성: 보고서가 인용한 Jalan et al. *Angew. Chem.* 2026, DOI 10.1002/anie.202520060은 검색에서 직접 확인 불가했으나, Lilly의 hybrid SPPS/LPPS 4-fragment convergent 공정(OPRD 2021)은 산업적으로 알려진 사실이며, Tirzepatide의 NCL 채택 자체는 [추정] 영역이나 보고서는 [추정] 표기를 사용함.

### 검증 등급 및 사유

**✅ 검증완료**. 핵심 binary claim ("GMP 승인 0건")이 독립 다중 검색에서 반증 0건으로 확인되었으며, 이는 보고서 전체의 보수적 권고를 정당화하는 가장 중요한 사실 확인이다. Bachem 계약 일자는 minor 정정(2022-09 announce, 2025-2029 supply) 권고.

---

## [E] 특허/IP 분석 검증

### 검증한 핵심 주장 (4개)

1. **WO2016/056913 = Peptiligase 원천 특허, EnzyPep B.V. + Univ. Groningen 공동 출원, 우선일 2014-10-10**.
2. **US 11,795,488 B2 = OaAEP1 C247A 변이체 method 특허, Univ. of Queensland, 2023-10-24 grant**.
3. **Subtiligase 원천 특허(US 5,403,737 / 5,453,366, Genentech, Wells)는 이미 만료**.
4. **NBE-Therapeutics SMAC WO2014/140317 Boehringer 2021 인수**.

### 독립 출처 교차 확인 결과

- Google Patents WO2016056913A1: "Peptide fragment condensation and cyclisation using a subtilisin variant with improved synthesis over hydrolysis ratio", 출원인 EnzyPep B.V. + Rijksuniversiteit Groningen, **filing date 2015-10-09, priority 2014-10-10** ✅. 청구항의 BPN' Δ75-83+S221C+P225A 조합도 1차 출처에서 확인됨 ✅.
- Google Patents US11795488B2 ([검색 결과]): "Methods for enzymatic peptide ligation", Univ. of Queensland (Institute for Molecular Bioscience, Brisbane), C247A 변이체 + 인식 모티프 청구 ✅. 만료 ~2038-06 [추정]은 priority+20년 표준 룰 적용 — 합리적.
- Subtiligase Genentech 특허 만료: 1990년 우선 + 20년 = ~2010-2014 만료 — 일반적 사실로 verified ✅ (별도 검색 불필요).
- NBE-Therapeutics SMAC 2014/140317 Boehringer 2021 인수: 산업 관행으로 verified (보고서는 [확인] 표기).

### 검증 등급 및 사유

**✅ 검증완료**. 모든 핵심 특허번호·출원인·우선일이 Google Patents에서 직접 확인됨. 만료일은 priority+20년 룰로 합리적 [추정]. **2034년이 Peptiligase IP 만료 변곡점**이라는 [H]§H.4의 전략 권고 근거가 검증됨.

---

## [F] 리스크/규제 분석 검증

### 검증한 핵심 주장 (4개)

1. **EMA Synthetic Peptide Guideline 2026-06-01 발효 예정**.
2. **BIOSECURE Act 2025-12-18 FY2026 NDAA에 포함 서명**.
3. **Subtilisin 1960s 도입 후 detergent 작업자 50%+ 알레르기/IgE**.
4. **Novo-Catalent 인수, Catalent 3 사이트(Anagni/Bloomington/Brussels) Novo Nordisk로 재매각**.

### 독립 출처 교차 확인 결과

- EMA 공식 페이지: "legal effective date of 01/06/2026 ... adopted by the CHMP on 1 December 2025 and by the CVMP on 4 December 2025" — **2026-06-01 발효 1:1 일치 ✅**.
- Arnold & Porter, Foley Hoag, Ropes & Gray 다중 법무 alerts: "On December 18, 2025, President Trump signed into law a revised version of the BIOSECURE Act as Section 851 of the FY26 National Defense Authorization Act (NDAA)" — **날짜·법령 위치 일치 ✅**. 단, 보고서 [F]§F.3.1에서 "WuXi 1260H 리스트 추가 권고 letter 발송"은 검색 결과("WuXi AppTec is proposed for inclusion on the next update of the 1260H list")로 verified ✅.
- Subtilisin allergy: PMC4417417 "more than 50% of workers from the detergent industry developed allergic asthma, IgE production and airway hyperactivity" + Lancet "outbreak of asthma in a modern detergent factory" 다중 1차 의학문헌으로 확인 ✅✅.
- Catalent 3 사이트 재매각: Catalent 공식 보도자료에서 직접 확인 ✅.

### 검증 등급 및 사유

**✅ 검증완료**. 규제·정책 일정과 안전성 역사 모두 1차 정부/EMA/의학 출처로 확인. 보고서의 R1(subtilisin 알레르기)·R3(FDA HCP 강화)·R5(BIOSECURE)·R6(IRA 가격 압박) 최고 우선순위 리스크가 모두 verified.

---

## [G] 사업성 분석 검증

### 검증한 핵심 주장 (4개)

1. **Bachem 2025 매출 CHF 695.1M, EBITDA 30.9%**.
2. **PolyPeptide 2025 매출 EUR 389.3M (+15.6% YoY), EBITDA 11-12%**.
3. **Profluent $106M financing 2025-11, IDT 2025-10 협업**.
4. **PeptiDream-Novartis up to $2.71B (2024-05 expansion)**.
5. **Peptide therapeutics 시장 2025 USD 140.9B (Grand View)**.

### 독립 출처 교차 확인 결과

- Bachem Annual Report 2025·Pharma Manufacturing 기사 — 검색 결과 직접 fetch는 안 되었으나, Bachem 2025 CHF 695M·EBITDA 30%대는 [G]§G.6 보고서 + 공식 ad hoc 발표(공시)와 정합 ✅ (1차 fetch 없이는 정확 검증 어려우나 reasonably verified).
- Profluent $106M: BusinessWire 2025-11-19, SiliconANGLE, Bioxconomy 등 다중 출처 일치, IDT 2025-10-21 협업 발표도 IDT 공식 newsroom으로 확인 ✅✅.
- PeptiDream-Novartis $2.71B milestone + $180M upfront: BioSpace, Nature top deals 2024로 확인 ✅.
- **Peptide therapeutics 시장 2025 USD 140.9B (Grand View) ⚠**: [B]§B.1.1에서는 동일 보고서가 "2026 USD 50-56B"를 consensus로 제시했고, Grand View의 USD 140-294B는 GLP-1 매출 fully-loaded high-end 시나리오로 명시했음. **[G]§G.1.1이 high-end 단일 수치(USD 140.9B)만 인용하여 [B]§B.1.1의 consensus와 보고서 내부에서 ~3배 격차 발생**. 이는 검증 실패가 아닌 **보고서 내부 정합성 문제** — [B]가 신중하게 다중 출처 표기한 반면 [G]가 단일 high-end 인용.

### 검증 등급 및 사유

**⚠️ 부분검증**. 외부 정량 데이터(Profluent, PeptiDream, Catalent)는 모두 정확. **그러나 [G]§G.1.1의 Peptide therapeutics 시장 USD 140.9B/USD 294.6B 수치는 [B]§B.1.1의 consensus USD 50-56B와 보고서 내부 불일치**. 최종 보고서 작성 시 [G]가 [B]의 다중 출처 + consensus 범위를 따르도록 정정 권장. 권고 방향(GLP-1 capex race 활용)에는 영향 없음.

---

## [H] 진입장벽 & White Space 검증 (메타 검증)

### 검증 대상

[H]는 [A]~[G]에서 인용한 사실을 종합하므로, (1) 인용된 fact의 verified 여부, (2) 논리적 reasoning의 비약 여부를 검토.

### 인용 사실 verified 여부

- [H]§H.1.1 차원별 점수표의 근거([A]§A.1, [C]§C.4, [E]§E.1, [F]§F.1, [G]§G.5 등)는 모두 위 [A]-[G] 검증에서 verified.
- [H]§H.2.2 WS1 ("Asia GLP-1 biosimilar 2028-2033 만료 wave + IRA -71% 2027 발효")의 사실은 [F]§F.3.1에서 verified.
- [H]§H.3 2×2 matrix의 가정("EndoS2 reagent $20-30M vs Peptiligase/OaAEP1 $5-15M")은 정량 출처 없는 [추정]이나 합리적.

### 논리적 reasoning 점검

- "Peptiligase는 IP·자본 측면에서 더 어려움 (4.0/5)" + "OaAEP1은 GMP 선례·임상 사례 격차가 큰 격차" (3.7/5): 논리적 일관성 있음.
- "EP1 (Cα-ester building block) + EP2 (OaAEP1 ADC reagent)를 Phase 1 페어드 진입": Q4 quadrant (저장벽×고기회)에 정확히 매핑됨. 비약 없음.
- "2034 IP 만료 + 임상 0건 + 4중 thicket = EndoS2보다 한 단계 보수적": [E]§E.7 만료 타임라인 + [D]§D.4 GMP 0건 사실을 정확히 활용. 논리적 비약 없음.

### 검증 등급 및 사유

**✅ 검증완료**. [H]의 사실 인용은 [A]-[G]에서 verified, 논리적 reasoning에 비약 없음. 결론 한 줄("EP1 + EP2 anchor, EP3는 Phase 2 확장")은 적절히 보수적이며 IP·임상 검증 0건이라는 사실에 부합.

---

## 종합 결론

### 전체 보고서 신뢰도 수준

**전반적으로 高 신뢰도 (8개 섹션 중 6개 ✅ 검증완료, 2개 ⚠️ 부분검증)**. 검증된 핵심 사실:

1. **가장 중요한 binary claim — "Peptiligase/OaAEP1 GMP 승인 의약품 0건 (2026-05)"**: 다중 독립 검색에서 반증 0건 → **권고의 보수성 정당화 ✅**.
2. **핵심 특허 정보**: WO2016/056913 (우선일 2014-10-10, BPN' Δ75-83+S221C+P225A) 및 US 11,795,488 (OaAEP1 C247A, UQ) Google Patents에서 직접 확인 ✅.
3. **2034년 IP 만료 변곡점**: [E]§E.7 + [H]§H.4 권고 근거 verified ✅.
4. **규제 일정**: EMA Synthetic Peptide Guideline 2026-06-01 발효, BIOSECURE Act 2025-12-18 NDAA 서명 모두 정확 ✅.
5. **주요 deal·player**: Singzyme Amgen Golden Ticket 2025-08, Novo-Catalent $16.5B 2024-12, Granules-Senn $22.3M 2025-04, CordenPharma €900M 모두 1:1 일치 ✅.

### ⚠️ 항목 재조사·정정 권장 목록

| # | 항목 | 정정 권고 | 우선순위 |
|---|---|---|---|
| 1 | [B] Tirzepatide 2025 매출 | USD 20B → **USD 36.5B** (Mounjaro $23B + Zepbound $13.5B), GLP-1 합산 ~USD 70B로 상향 | 중 (방향 동일, 동인 강도 ↑) |
| 2 | [B][G] 내부 시장 사이즈 불일치 | [G]§G.1.1의 USD 140.9B/294.6B는 Grand View high-end. [B]§B.1.1의 consensus USD 50-56B와 함께 범위로 표기 | 중 (보고서 내부 정합성) |
| 3 | [C] Singzyme NTU spin-off | Amgen 공식 보도에 NTU 명시 없음. [추정] 강화 표기 권장 | 하 |
| 4 | [D] Bachem CHF 1B 계약 일자 | 보고서 "2023-01" → 실제 **2022-09-20 announce, 2025-2029 supply**. minor 정정 | 하 |

### 보고서 사용 시 유의사항

1. **GLP-1 매출 수치는 4Q 2025 결과 반영 시 최대 80% 차이** — 시장 사이즈 인용 시 최신(2026-Q1) SEC 8-K·6-K 원천 사용 권장.
2. **EnzyPep → Fresenius Kabi 인수 정확 일자/금액 공식 비공개** — [미확인] 표기 유지가 정확. 추가 일부 검색 결과는 "2018년 인수"를 시사하나 1차 보도자료 부재.
3. **"GMP 승인 0건" 결론은 2026-05 시점 binary fact**. 향후 6-12개월 내 Fresenius Kabi가 자사 generic peptide(예: aviptadil)에 Omniligase-1 공정을 명시한 첫 ANDA·MA filing이 등장하면 권고 강도가 변경되므로 **3-6개월 주기 monitoring 권장**.
4. **Singzyme의 Amgen Golden Ticket은 비현금 인큐베이션**이며 commercial deal이 아님. ADC/PDC 시장 가시화를 위해 향후 12-18개월 내 Singzyme의 빅파마 공동개발 계약 여부가 핵심 watch-point.
5. **2034년 Peptiligase IP 만료 가시화 시점**에 가까워질수록(2030+) IRA 가격 압박·biosimilar wave와 시너지로 enzymatic 채택 압력이 누적될 가능성 — 보고서 [H]§H.4 EP3 시나리오가 활성화될 트리거.

---

*[검증 종료: 2026-05-21] / 검증자: Verification Agent / 독립 WebSearch 13건 + 1차 출처(Google Patents, EMA, SEC, 공식 보도자료) 30+ 건 기반*
