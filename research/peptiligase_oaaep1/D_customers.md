# [D] 고객 분석 — Peptiligase / OaAEP1 (효소적 펩타이드 라이게이션)

작성일: 2026-05-21 / 작성자: Research Agent [D] — Customer Analysis
대상 기술: Peptiligase / Omniligase-1 (engineered subtilisin, EnzyPep / Fresenius Kabi iPSUM) 및 OaAEP1 (engineered C247A asparaginyl endopeptidase, Oldenlandia affinis)

> 본 보고서는 "발표된 파트너십"과 "GMP 상용 적용"을 엄격히 구분하여 기재한다. 효소적 펩타이드 합성(EPS/CEPS) 영역의 다수 사례는 여전히 process development / kilogram-scale pilot 수준이며, 상업적 GMP 적용은 매우 제한적이다.

---

## D.1 주요 고객 세그먼트 및 페르소나

### D.1.1 Big Pharma — Peptide / GLP-1 originator
GLP-1·GIP 이중 작용제, 장사슬 펩타이드(>30 mer) 신약 개발 capacity 병목과 PMI 부담을 동시에 안고 있는 segment.

| 기업 | 핵심 파이프라인 | 관련성 (Peptiligase / OaAEP1) |
|---|---|---|
| Novo Nordisk | Semaglutide(Ozempic/Wegovy), Liraglutide, CagriSema | $6B+ API 시설 증설(2024-2029)에도 capacity 부족 (FiercePharma, 2024). Fresenius Kabi 특허군(US10920258B2)이 semaglutide·liraglutide·GLP-1을 chemo-enzymatic으로 합성하는 방법을 청구 — Novo가 직접 채택했다는 공식 정보는 없으나 jurisdiction별 FTO 협상 대상으로 추정 [추정]. |
| Eli Lilly | Tirzepatide(Mounjaro/Zepbound), Retatrutide, Orforglipron | 2026 Angew. Chem. 논문(Jalan et al., DOI 10.1002/anie.202520060)에서 Native Chemical Ligation + TFF 기반의 두 fragment 융합법으로 multi-gram 합성 공개 — 효소 ligation은 아니지만 fragment condensation 채택 의지 확인. Lilly는 자체 hybrid SPPS/LPPS 4-fragment convergent 공정도 발표(OPRD, 2021). 효소 ligation은 후속 후보로 평가 중 [추정]. |
| Pfizer | Danuglipron(경구 GLP-1, 2025 중단), 다음 후보 | Danuglipron 중단 후 capacity 부담은 낮으나 peptide modality 재진입 시 enzymatic 옵션 평가 가능. |
| AstraZeneca | Cotadutide(GLP-1/Glucagon), AZD5004 | Bayer/Bicycle 협력 등 cyclic peptide modality에 관심. CDMO outsourcing 비중 큼. |
| Roche, AbbVie, Sanofi, BMS | 펩타이드 ADC, cyclic peptide, GLP-1 추격 | Sanofi는 Insulin 영역 큰 capacity 보유(인슐린 자체는 fermentation 기반). 단, peptide-conjugate 영역에서 OaAEP1-매개 site-specific labeling이 후보 [추정]. |

**페르소나(가상)**: "Global API supply 책임자" — 분기별 capacity utilization 보고가 KPI. SPPS column의 ~30-40 mer 한계와 PMI ≥13,000 부담(ACS GCI PR Peptide 보고서, J. Org. Chem. 2024, 89, 4644)에 시달리며, 신규 modality의 jurisdiction-specific FTO 검토를 매월 IP 변호사와 진행.

### D.1.2 GLP-1 Biosimilar / Generic 제조사
2026년 3월 인도 시장 semaglutide 물질특허 만료를 기점으로 본격적 1차 진입군 형성. 미국·EU는 2031/2033 예정. (BusinessToday, 2026-03-19; IQVIA, 2026-04)

- **Sun Pharma**: 'Noveltreat', 'Sematrinity' 브랜드 출시 발표 (인도, 2026Q2).
- **Cipla**: Delhi 고등법원 승소 후 비특허국 수출 허가, launch 평가 중.
- **Dr. Reddy's**: 인도 1차 진입군.
- **Zydus, Mankind, Lupin**: 인도 first-movers.
- **Biocon**: Ajanta Pharma 와 26개국(아프리카·중동·중앙아시아) 공급 계약 (Business Standard, 2025-12-23). Ajanta 승인은 2026 말~2027 초 전망.
- **Sandoz**: 캐나다·미국 향 biosimilar semaglutide 준비.
- **Hikma, Teva**: 후속.

**니즈**: 인도/신흥국 생산은 가격경쟁(원료 cost per kg 압박)이 극심하며 SPPS 기반 raw material(Fmoc-AA, DMF, HBTU/HATU)의 30-40% 비중을 enzymatic ligation으로 대체 시 PMI·waste 처리비 절감 가능. 단, **CMC 변경 부담**과 **레퍼런스 의약품과의 동등성 입증**이 진입 장벽 → 초기에는 SPPS-only 공정 선호.

### D.1.3 Cyclic Peptide Biotech
헤드-투-테일 환형화·N-to-side chain bridging 등 화학적으로 까다로운 macrocyclization에 OaAEP1 / butelase / sortase 활용 가능.

- **Bicycle Therapeutics (UK)**: 9-20 mer bicyclic peptide(TMEM, BDC) 플랫폼. 공식 manufacturing은 화학적 cysteine alkylation (2,6-bis(bromomethyl)pyridine 등 small-molecule scaffold) 기반 — **OaAEP1을 채택했다는 공식 자료는 없음 [미확인]**. 2026년 Q1 nuzefatide pevedotin(EphA2-BDC) Phase 1/2 데이터 발표 (AACR 2026). Bayer·Novartis와 radio-conjugate 협력. Eckert & Ziegler 가 isotope CDMO.
- **Pepscan (현재 Biosynth Peptide Division)**: 2022-06 Biosynth Carbosynth가 인수. CEPS 서비스 직접 제공.
- **Unnatural Products / Recursion (Cyclica 인수)**: AI-driven cyclic peptide discovery. 합성은 외주.
- **Lytica**: cyclic peptide 항생제.
- **Protagonist Therapeutics, Peptidream, Ra Pharma(UCB 인수)**: macrocyclic peptide 파이프라인 보유.
- **Circle Pharma**: macrocyclic small molecule(엄밀히 peptide 아님).

### D.1.4 Peptide CDMO (효소 공급자의 직접 고객)
EnzyPep 자체가 Fresenius Kabi iPSUM에 통합(2018-2019 단계적)되었기 때문에, 외부 CDMO는 EnzyTag B.V. 또는 Sigma-Aldrich(SAE0068) 경로로 효소 입수 또는 자체 라이센싱.

- **Bachem (CH)**: peptide CDMO 1위. CHF 2.7B 스위스 biotech 투자(2024), Basel 인근 greenfield 추진. enzymatic 채택은 평가 단계 [추정].
- **PolyPeptide Group (CH/SE/US/IN)**: CEPS RSC Green Chemistry 논문(2019) 공동저자였으나 상업 GMP 적용 사례 미공개.
- **CordenPharma**: 2025 €1B+ 펩타이드 투자, 2028년까지 €1B 매출 목표. TAPS(TAG-Assisted Peptide Synthesis) 자체 기술 보유 — TAPS는 LPPS 변형이며 효소 ligation은 보완재. 2025 CPHI Pharma Award 수상.
- **AmbioPharm**: 자체 proprietary enzyme cyclization platform 개발 중(sortase/butelase 평가). FDA-inspected.
- **Wacker Chemie**: 미생물 발효 기반 펩타이드(Wacker Biotech), enzymatic ligation은 비주력.
- **CHIMEK, Lonza (Polypeptide JV 등)**, **Almac**: GMP peptide manufacture.
- **Biosynth (NL/CH/UK)**: Lelystad 시설에서 CEPS GMP 제공 (Biosynth's GMP Peptide 사이트, 2024). Pepscan과 vivitide 통합.

### D.1.5 Academic / Research labs
OaAEP1은 단백질 N-/C-말단 site-specific labeling, single-molecule force spectroscopy(AFM), magnetic-nanoparticle 고정화의 reagent로 활발히 사용.

- **Nanjing University** (State Key Lab of Coordination Chemistry) — OaAEP1 single-molecule force spectroscopy 다수 논문(2022-2025).
- **NTU Singapore** (James Tam 연구실): butelase-1 발견 및 cyclotide 엔지니어링.
- **Cardiff University** (Luet-Lok Wong group): "Improving the use of asparaginyl endopeptidase for biocatalytic applications" (ORCA 142484).
- **University of Groningen** (DB Janssen group): peptiligase/omniligase 모체 개발자.
- **Beijing Genomics / 중국과기대** 등 다수: AEP-based protein engineering.

Omniligase-1 reagent(SAE0068)는 Sigma-Aldrich를 통해 연구용 한정으로 판매되며, 의약·진단·in vivo 사용은 라이센스 별도(EnzyTag/Fresenius Kabi와 협의).

---

## D.2 고객 니즈 (Pain Points)

### D.2.1 SPPS 한계 — 길이, 수율, 비용
- 통상 30-40 mer 초과 시 deletion sequence, racemization 누적으로 crude purity 급격히 저하. Semaglutide(31 mer + lipid linker), Tirzepatide(39 mer + 2x AEEA + γGlu-C20 지방산) 등은 한계선상.
- SPPS는 각 amino acid의 3-5배 과량 사용 → PMI ≈ 13,000 (ACS GCI 보고서, J. Org. Chem. 2024).
- **Enzymatic fragment condensation(Omniligase-1)**: 두 unprotected fragment를 수계에서 5-10분 만에 ligation(SAE0068 product sheet) → 한 cycle당 수율 ≥90%, PMI 50-70% 절감 가능 (EnzyPep/RSC Green Chem. 2019, exenatide case study).

### D.2.2 GLP-1 capacity 병목 + 관세·공급망 리스크
- 2024-2025 미국 정치권의 tariff 논의 + Novo·Lilly 자체 capacity 부족 → 2025-Q1 FDA 부족 해소 선언 후에도 503B compounding 금지(2025-04~05) 이후 외부 capacity 수요 잔존.
- Novo Nordisk: $6B(+) API 시설 (2024-2029 단계 완공) + 미국 NC주 $4.1B + 브라질 $1.09B. Lilly: 자체 hybrid SPPS/LPPS continuous platform.
- **고객 니즈**: 동일 footprint에서 throughput 1.5-3배 증대. Enzymatic fragment ligation은 same column에서 fragment 별 병렬 합성 후 1-step water-based ligation으로 cycle time 단축.

### D.2.3 ESG / Green Chemistry 압박
- EU Green Deal: 2030 화학산업 -55% 탄소. DMF/NMP 등 reprotoxic 용매 REACH 규제 강화.
- Big pharma sustainability target: Novo Nordisk "Circular for Zero", Lilly "Net Zero by 2050", Roche "scope 3 -50% by 2030".
- 효소 ligation은 수계 반응이며 DMF/NMP 사용량을 fragment 합성 단계로 제한 → PMI 절감이 ESG KPI에 직접 반영.

### D.2.4 환형 펩타이드 합성 효율
- 화학적 macrocyclization은 dilute condition(intermolecular oligomer 회피)으로 0.1-1 mM 수준 → 부피 폭증·수율 30-50%.
- OaAEP1은 substrate-tethered acyl-enzyme intermediate를 통해 농도 의존도 낮은 환형화(typical 50-200 µM에서도 >80%) 가능 — cyclotide(MCoTI-II, kalata B1) 합성에서 입증.

### D.2.5 Site-specific labeling / Bioconjugation
- ADC, peptide-conjugate, radio-conjugate에서 균질도(DAR distribution) 향상 요구.
- OaAEP1 [C247A]: minimal recognition motif (NGL or NHV) 만 있으면 N-/C-말단 어디든 conjugation. Sortase A 대비 효소 사용량 적고 반응속도 빠름 (PMC 7372569).
- 잠재 고객: Mersana, Synaffix(Lonza 인수), ImmunoGen(AbbVie 인수), Daiichi-Sankyo, Seagen(Pfizer 인수) — 다만 현재 ADC 영역의 dominant enzymatic tool은 여전히 sortase·MTGase·FGE 계열.

---

## D.3 구매 결정 요인 (Buying Decision Factors)

1. **GMP track record 및 승인 의약품 사례 보유 여부** — *핵심 weakness*: Peptiligase/Omniligase-1 또는 OaAEP1로 만들어진 **FDA/EMA 승인 의약품은 현재(2026-05) 공식적으로 0건 [확인 필요]**. EnzyPep 사이트는 "marketed peptide APIs"라는 표현을 사용하나, 구체 제품명·승인번호를 공개하지 않음.
2. **Yield & Cost per kg** — 효소 비용은 g당 수십-수백 USD 수준(Sigma SAE0068 1 mg 단위 판매 기준 환산)으로 SPPS reagent(Fmoc-AA, HATU 등) 대비 절대값은 높지만, 효소:기질 ratio 1:100(w/w) 사용 시 unit kg API당 효소 cost는 < $5,000/kg 예상 [추정]. SPPS의 reagent + 용매 + 폐기물 처리 cost 대비 경쟁력 있는 영역(>20mer).
3. **Freedom-to-Operate (IP)** — Fresenius Kabi(구 EnzyPep) 핵심 특허(US10920258B2 = semaglutide/liraglutide chemo-enzymatic 합성, US20190031710A1 = subtilisin variant 등) 다수. EnzyPep 특허군은 **2028-2033년 만료 예정**(Coherent Market Insights, 2025) — 만료 전 라이센스 협상 필수. OaAEP1 자체는 식물 유래로 핵심 단백질 특허는 적으나 C247A 변이체 및 정제법 특허(Cardiff/NTU 등) 존재.
4. **규제 수용성** — EMA·FDA의 enzyme residual에 대한 ICH Q11 가이드라인 적용 가능. 다만 **공정 변경(CMC supplement)** 부담은 generic·biosimilar 진입자에게 큼.
5. **기질 유연성 (Substrate flexibility)** — Omniligase-1은 거의 모든 acyl donor·acceptor 조합 가능 (4세대 진화). OaAEP1은 NGL/NHV motif 선호 → motif engineering이 필요한 경우 화학적 어댑테이션 비용 발생.
6. **납기 (Deliverable timeline)** — Peptide CDMO의 customer는 6-9개월 내 GLP/GMP 공급 요구. 효소 자체의 lead time은 짧으나 process validation은 별도.

---

## D.4 도입 사례 / 레퍼런스 (표)

> **CRITICAL**: 아래 표에서 "상업·승인(commercial)" 컬럼이 비어있는 경우, 이는 발표된 publication·patent·partnership에 그치며 **GMP commercial supply** 단계로 확인된 사례가 아님을 의미한다.

| 고객사 / 사용자 | 적용 분야 / 타깃 펩타이드 | 단계 | 사용 플랫폼 | 출처 / 일자 |
|---|---|---|---|---|
| EnzyPep B.V. → Fresenius Kabi iPSUM | Exenatide (Byetta, 39 mer) chemo-enzymatic 공정 | Pilot~kg scale demonstrated (commercial GMP 적용은 미공개) | Omniligase-1 + SPPS fragment | Schmidt et al., *Green Chem.* 2019, 21, 6024 (DOI 10.1039/C9GC03600H) |
| EnzyPep / Fresenius Kabi | Semaglutide / Liraglutide / GLP-1 합성법 | 특허 단계 (US10920258B2 grant 2021-02) | Omniligase 계열 | USPTO US10920258B2, 2021-02 |
| EnzyPep / Univ. Groningen | Linear & head-to-tail cyclic peptides (insulin analog 포함) | 학술 / phage display | Omniligase-1 | Toplak et al., *Adv. Synth. Catal.* 2016; *Methods Mol. Biol.* 2019, 32512 |
| Biosynth Peptide Division (구 EnzyPep tech 일부, vivitide·Pepscan 통합) | GMP peptide & long peptide(<200 mer)  | GMP 공급 (Lelystad NL) | CEPS | Biosynth.com news, 2024 |
| EnzyTag B.V. (EnzyPep spin-off) | Omniligase Ligation Kit 판매, R&D 라이센싱 | Reagent commercial | Omniligase-1 kit | enzytag.com/ligation-kit, 2024 |
| Sigma-Aldrich (Merck KGaA) | Omniligase-1 reagent (SAE0068) 유통 | 연구용(RUO) reagent commercial | Omniligase-1 | sigmaaldrich.com SAE0068 PIS |
| Nanjing Univ. (Cao group) | 단백질 site-specific 표지 / AFM 단분자 | 학술 (2025 Chem. Eur. J.) | OaAEP1 [C247A] | 10.1002/chem.202502540 |
| NTU Singapore (James Tam group) | Butelase-1 발견, kalata B1 / cyclotide engineering | 학술 (Nature Chem. Biol. 2014) | Butelase-1 / OaAEP1 | DOI 10.1038/nchembio.1586 |
| Cardiff Univ. (Luet-Lok Wong) | OaAEP1 biocatalytic optimization | 학술 (ORCA 142484, 2021) | OaAEP1 | orca.cardiff.ac.uk/142484 |
| Lilly (Jalan et al.) | Tirzepatide NCL + TFF (효소 아닌 chemical ligation) — *비교 데이터* | Multi-gram demonstrated | NCL/desulfurization (not enzyme) | *Angew. Chem.* 2026, DOI 10.1002/anie.202520060 |
| Bicycle Therapeutics | Nuzefatide/Zelenectide pevedotin, BT7480 등 bicycle peptide | Phase 1/2 (AACR 2026) | 화학적 bis-electrophile cyclization (효소 아님) | bicycletherapeutics.com pipeline |
| Novo Nordisk / Lilly | Semaglutide / Tirzepatide GMP | Commercial (수십 ton/year) | SPPS / hybrid SPPS-LPPS (효소 ligation 공식 미적용) [추정] | Company 10-K / OPRD 2021 |

**핵심 결론**: Peptiligase/Omniligase-1 또는 OaAEP1가 **현재 시판되는 어떤 의약품의 GMP 제조에 사용되었다는 공식 확인은 부재**한다 [확인 필요]. Exenatide의 chemo-enzymatic 합성은 EnzyPep 시연(2019 Green Chem.) 수준이며, AstraZeneca/Amneal의 상용 exenatide는 일반 SPPS 기반으로 추정 [추정].

---

## D.5 가격 민감도 및 채택 장벽

### D.5.1 가격 민감도
- **Reagent grade Omniligase-1**: Sigma SAE0068 — 1 mg ~$300-500 (RUO, 환산 추정 [추정]). EnzyTag OMNI Kit (150 reactions / 1 g peptide 생산) — 수천-만달러 단위 [추정].
- **GMP grade 효소**: 별도 라이센스 + custom production. 단, 효소 사용량 1:100 (w/w) 기준 1 kg peptide 생산에 ~10 g 효소 → kg당 효소 비용은 $1k-5k 수준 [추정].
- 비교: SPPS Fmoc-amino acid 비용은 kg API당 $20k-50k(대량 구매 시 더 낮음)이며, 효소법은 fragment 단계 SPPS 비용 + 효소 + ligation 비용으로 분해되어 **총 cost는 SPPS-only 대비 10-30% 절감 가능 (>30mer 페티드 한정)** [추정, EnzyPep 공개 자료 기반].

### D.5.2 채택 장벽 (Adoption Barriers)

1. **승인 의약품 트랙 레코드 부재** — 최대 장벽. CMO/CDMO 영업 시 "어느 승인 의약품에 사용되었습니까?" 질문에 답할 사례가 없음.
2. **CMC 변경 부담** — 기존 SPPS 공정에서 enzymatic ligation 도입은 ICH Q12 lifecycle management 관점에서 PAS(Prior Approval Supplement) 수준의 regulatory submission 필요 → 12-18개월 지연.
3. **IP/FTO 비용** — Fresenius Kabi/EnzyPep 특허군 라이센스 (royalty 추정 5-10% net sales 또는 milestone-based [추정]) + EnzyTag 별도. 특허 만료 2028-2033 대기 동기 존재.
4. **Switching cost** — 기존 SPPS line은 sunk cost 큼. capacity 부족이 강하지 않으면 신공정 전환 ROI 약함.
5. **효소 생산 / 정제 부담 (OaAEP1)** — Cardiff 보고서에 따르면 OaAEP1은 zymogen으로 생산 후 acid activation + 4단계 크로마토 필요 → 자체 제조 시 부담 큼. EnzyTag 같은 상업 공급에 의존.
6. **분석 복잡성** — 효소 잔류 검출(ICH Q3A/B impurity), endotoxin(특히 OaAEP1는 E. coli 발현 시), 변성 단백질 fragment 등 새로운 impurity profile 검증 필요.
7. **인력 격차** — peptide 화학자가 효소반응 최적화 경험 부족. cross-training 필요.

### D.5.3 채택 가속 트리거 (Adoption Triggers)
- Semaglutide·Tirzepatide 후속 (Retatrutide, CagriSema) **40 mer 초과 + 다중 측쇄 변형** → SPPS 한계 가시화.
- 2028-2033 핵심 특허 만료 → Indian biosimilar group의 cost 압박 진입.
- EU Green Deal 2027-2030 PMI cap 강제 → ESG-driven mandatory adoption.
- Macrocyclic peptide drug 시장 4.76B USD (2030, 21.4% CAGR, Creative Peptides 2025) → cyclic 합성 효율이 사업가치 결정.

---

## 핵심 출처 목록

1. EnzyPep 공식 사이트 — https://www.enzypep.com/ (2024 접속)
2. EnzyTag Technology — https://enzytag.com/technology/ (제품/라이센스 정보)
3. Sigma-Aldrich Omniligase-1 SAE0068 Product Information Sheet — https://www.sigmaaldrich.com/US/en/product/sigma/sae0068
4. Toplak A. et al., "Peptiligase, an Enzyme for Efficient Chemoenzymatic Peptide Synthesis and Cyclization in Water", *Adv. Synth. Catal.* 2016, 358, 2140 — DOI 10.1002/adsc.201600017
5. Schmidt M. et al., "Sustainable, cost-efficient manufacturing of therapeutic peptides using CEPS", *Green Chem.* 2019, 21, 6024 — DOI 10.1039/C9GC03600H (exenatide case study)
6. Fresenius Kabi iPSUM US Patent 10,920,258 B2 "Chemo-enzymatic synthesis of semaglutide, liraglutide and GLP-1" (grant 2021-02-16)
7. Cui Z. et al., "Development and applications of enzymatic peptide and protein ligation", *J. Pept. Sci.* 2025 — DOI 10.1002/psc.3657
8. Nguyen GKT et al., "Butelase 1 is an Asx-specific ligase enabling peptide macrocyclization and synthesis", *Nat. Chem. Biol.* 2014, 10, 732 — DOI 10.1038/nchembio.1586
9. ACS GCI Pharmaceutical Roundtable Peptides, "Process Mass Intensity (PMI): A Holistic Analysis of Current Peptide Manufacturing Processes", *J. Org. Chem.* 2024, 89, 4644 — DOI 10.1021/acs.joc.3c01494
10. Jalan A. et al., "A Convergent Hybrid Gram-Scale Synthesis of Tirzepatide" *Angew. Chem. Int. Ed.* 2026 — DOI 10.1002/anie.202520060 (Eli Lilly, NCL approach)
11. Novo Nordisk SEC Form 6-K (2025-11-06, 2025-07-29) — capacity investments
12. FiercePharma "Novo Nordisk devotes $6B to expanding production" (2024) — fiercepharma.com
13. Business Standard "Ajanta Pharma signs pact with Biocon to sell semaglutide in 26 countries" (2025-12-23)
14. BusinessToday "Sun Pharma, Dr Reddy's...India's semaglutide market opens post patent expiry" (2026-03-19)
15. IQVIA "Off-patent Semaglutide in 2026" (2026-04)
16. Bicycle Therapeutics 8-K filings, investors.bicycletherapeutics.com news releases (2026)
17. CordenPharma "2025 Year-End CDMO Highlights" — cordenpharma.com/articles/2025-year-end-cdmo-highlights/
18. Biosynth "Peptide Division GMP inspection in Lelystad" — biosynth.com/news (2024)
19. Du et al., "FDA-approved drugs featuring macrocycles or medium-sized rings", *Arch. Pharm.* 2025 — DOI 10.1002/ardp.202400890
20. Site-Specific OaAEP1 Mediated Functional Proteins Immobilization, *Chem. Eur. J.* 2025 — DOI 10.1002/chem.202502540

---

## 200-Word Summary

Peptiligase·Omniligase-1(EnzyPep/Fresenius Kabi iPSUM)과 OaAEP1[C247A]의 잠재 고객은 (1) Big Pharma GLP-1·peptide originator(Novo Nordisk, Eli Lilly, Pfizer 등), (2) 2026년 3월 인도 semaglutide 특허 만료를 기점으로 진입하는 GLP-1 biosimilar 그룹(Sun Pharma, Cipla, Biocon-Ajanta, Dr. Reddy's, Sandoz 등), (3) cyclic peptide biotech(Bicycle Therapeutics, Pepscan-Biosynth, Unnatural Products), (4) peptide CDMO(Bachem, PolyPeptide, CordenPharma, AmbioPharm), (5) site-specific labeling/ADC 응용 학술·산업 연구실로 구분된다. 핵심 페인포인트는 SPPS의 30-40 mer 한계, PMI ≈ 13,000의 환경 부담, GLP-1 capacity 병목, 환형화 효율, ADC site-specific conjugation 균질도이다. 구매 결정 요인은 GMP 트랙레코드, 효소 cost/kg, FTO(Fresenius Kabi 특허군 2028-2033 만료), substrate flexibility, 규제 수용성이다. **결정적 weakness는 현재(2026-05) Peptiligase/Omniligase 또는 OaAEP1로 GMP 상용 제조된 승인 의약품이 공식적으로 확인되지 않는다는 점**이다. EnzyPep 사이트와 특허는 marketed API를 시사하나 제품명 미공개이며, exenatide CEPS 사례(2019 Green Chem.)도 pilot 수준이다. Tirzepatide 합성은 효소가 아닌 NCL 기반(Lilly 2026)으로 진행되고 있어, 효소 ligation은 발표된 파트너십과 GMP 상용 사이의 큰 간극을 안고 있다. 채택 가속 트리거는 후속 long-peptide 후보(Retatrutide, CagriSema), 핵심 특허 만료(2028-2033), EU Green Deal PMI 규제, macrocyclic peptide 시장 4.76B USD(2030)이다.
