# [F] 리스크 및 규제 분석

> 조사 대상: Peptiligase / OaAEP1 (효소 기반 펩타이드 라이게이션) 플랫폼  
> 작성일: 2026-05-21  
> 작성자: Research Agent [F] — Risk/Regulatory

---

## F.1 규제 환경 및 인증 요건

### F.1.1 글로벌 펩타이드 API 규제 프레임워크
- **ICH Q11 (Development and Manufacture of Drug Substances, 2012; Q&A 2017)**: 화학적 합성 의약품과 생물학적/생명공학 의약품 모두에 적용. Peptiligase·OaAEP1 기반 chemo-enzymatic 공정은 화학+효소의 하이브리드 성격을 띠므로 Q11에서 출발물질(starting material) 정의·purge 평가가 핵심 (출처: ICH Q11 Guideline, [database.ich.org](https://database.ich.org/sites/default/files/Q11%20Guideline.pdf)).
- **EMA Guideline on Development and Manufacture of Synthetic Peptides (EMA/CHMP/CVMP/QWP/295050/2024)**: 2024년 4월 컨설테이션 종료 후 최종본 채택, **2026년 6월 1일 발효 예정**. SPPS와 fragment condensation을 명시 커버하나, "chemo-enzymatic" 합성에 대한 별도 챕터는 없어 화학 합성+ICH Q5A/Q5E 원칙을 조합하여 해석해야 함 [추정] (출처: [EMA Synthetic Peptides Guideline](https://www.ema.europa.eu/en/documents/scientific-guideline/guideline-development-manufacture-synthetic-peptides_en.pdf)).
- **FDA Synthetic Peptide Guidance (2021)** (Docket FDA-2017-D-5767, "ANDAs for Certain Highly Purified Synthetic Peptide Drug Products that Refer to Listed Drugs of rDNA Origin"): 신규 불순물이 **0.5% 초과**이면 제거 의무, **0.10–0.5% 구간**은 in silico/in vitro 면역원성 평가(IVISIA) 필요. T세포 에피토프 평가 권고 (출처: [FDA Synthetic Peptide Guidance](https://www.fda.gov/media/166571/download)).
- **FDA Federal Register Notice (2024-07-25)**: "Evaluating the Immunogenicity Risk of Host Cell Proteins in Follow-On Recombinant Peptide Products" — FDA가 재조합/효소 사용 펩타이드의 HCP 평가 방법 의견 수렴. **Peptiligase·OaAEP1의 효소 잔류물(=HCP/process-related impurity)**을 follow-on 제품에서 어떻게 평가할지 직접 관련 (출처: [Federal Register 2024-16356](https://www.federalregister.gov/documents/2024/07/25/2024-16356/evaluating-the-immunogenicity-risk-of-host-cell-proteins-in-follow-on-recombinant-peptide-products)).
- **PMDA/NMPA**: 각각 ICH Q11 채택, NMPA는 2024 "Synthetic Peptide Drug Substances Technical Guidance" (중국 NMPA CDE) 공표 [추정 — 본 검색에서 직접 확인되지 않음, 미확인].

### F.1.2 효소(Peptiligase·OaAEP1) 잔류물 규제 위치
- USP <1132> Residual Host Cell Protein Measurement in Biopharmaceuticals: 일반적으로 **1–100 ng/mg (ppm)** 수준의 HCP가 ELISA로 검출되며 산업 표준 한도 (출처: [Gyros HCP overview](https://www.gyrosproteintechnologies.com/spinblog/host-cell-protein-hcp-impurities-in-biotherapeutic-drug-development-and-manufacturing); PMC HCP review).
- Peptiligase는 *E. coli* 발현, OaAEP1은 *E. coli* 봉입체 또는 *P. pastoris* 분비 발현 → **각 발현 시스템에 대응하는 HCP-ELISA kit + 효소-specific ELISA** 별도 개발 필요.
- 효소가 잔존하면 후속 안정성 시험 중 가수분해/역반응 가능 → **활성-based assay** (substrate cleavage)를 안정성 시험에 포함 권고.

### F.1.3 Peptiligase/OaAEP1 기반 승인 의약품 현황
- 2024–2026 FDA/EMA 승인 펩타이드 의약품 중 **Peptiligase 또는 OaAEP1을 핵심 공정 단계로 명시한 사례는 공개적으로 확인되지 않음** [미확인]. EnzyPep B.V.(2025-01 Fresenius Kabi iPSUM 자회사화)와 Bachem이 GLP-1 chemo-enzymatic 공정을 개발 중이나 commercial-stage filing 정보 미공개 (출처: 검색결과 EnzyPep-Fresenius Kabi 양도 사실, [PharmaCompass Fresenius Kabi AG](https://www.pharmacompass.com/who-gmp-certificate/fresenius-kabi-ag)).
- **시사점**: First-mover 출시 시 FDA·EMA 사전 미팅 (Type B/Scientific Advice) 적극 활용 필수.

### F.1.4 ICH Q5E Comparability (공정 전환 시)
- SPPS → chemo-enzymatic 공정 전환 시 ICH Q5E의 비교성(comparability) 프레임을 차용 권고: **사전 3 batch + 사후 3 batch** 병렬 특성분석, LC-MS peptide mapping, 면역원성 in silico 비교, 효능 in vitro/in vivo bridge (출처: [ICH Q5E EMA](https://www.ema.europa.eu/en/ich-q5e-biotechnological-biological-products-subject-changes-their-manufacturing-process-comparability-biotechnological-biological-products-scientific-guideline)).
- 효소 단계는 "biotechnological" 성격이 있어 Q5E 원칙 적용이 더 자연스러우나, 최종 분자가 chemically defined 펩타이드인 점에서 Q11도 병행. → **하이브리드 dossier** 구조 예상.

---

## F.2 CMC / 품질 관리 요건

### F.2.1 펩타이드 자체 불순물 (peptide-related)
- **Deletion sequence, insertion, racemization (D-amino acid), oxidation (Met/Trp), deamidation (Asn/Gln)**: FDA 2021 가이던스 적용.
- **Chemo-enzymatic 특이 불순물**:
  - **Over-ligation 부산물**: Peptiligase가 ester를 활성화 후 N-말단 nucleophile와 ligation할 때, 의도된 N-fragment 외의 펩타이드가 결합한 mis-ligated species [추정 한도 < 0.5%].
  - **Reverse hydrolysis fragment**: subtilisin은 본래 protease이므로 wild-type 활성 잔존 시 product 일부를 가수분해. Peptiligase는 hydrolysis/synthesis ratio가 < 0.01로 엔지니어링 (Toplak et al. 2016; [Frontiers in Chemistry, 2019](https://www.frontiersin.org/articles/10.3389/fchem.2019.00829/full)).
  - **Cα-ester 잔류 (Cam-ester, Gam-ester)**: 활성화된 acyl-donor가 가수분해되지 않고 남는 경우. LC-MS로 정량.
  - **OaAEP1: NGL → NG 절단 부산물** (Asn-Gly bond에서의 다이펩타이드 byproduct).
- **Specification 권고치**: 각 specified impurity ≤ 0.5%, total impurities ≤ 2.0%, unspecified ≤ 0.10% (ICH Q3A 화학약 기준 적용; 단, 면역원성 트리거 시 더 엄격).

### F.2.2 효소(공정 관련) 불순물
| 분석 대상 | 권고 방법 | 산업 표준 한도 |
|---|---|---|
| Peptiligase 단백질 잔류 | Anti-Peptiligase ELISA + LC-MS/MS | < 10 ppm (DS 기준) [추정] |
| OaAEP1 단백질 잔류 | Anti-OaAEP1 ELISA | < 10 ppm [추정] |
| *E. coli* HCP (Peptiligase 생산숙주) | Cygnus *E. coli* HCP ELISA 3G/2G | < 100 ppm |
| *P. pastoris* HCP (OaAEP1) | Cygnus *P. pastoris* HCP ELISA | < 100 ppm |
| 잔류 효소 활성 | Synthetic substrate fluorogenic assay | LOD < 0.1 U/mg |
| 엔도톡신 (LAL) | LAL-Kinetic chromogenic | < 0.5 EU/mg (parenteral) |
| 핵산 (host DNA) | qPCR | < 10 ng/dose (WHO) |

(출처: [PMC HCP Clinical Safety Review](https://pmc.ncbi.nlm.nih.gov/articles/PMC12503010/); [Biopharm International HCP](https://www.biopharminternational.com/view/host-cell-protein-measurement-and-control))

### F.2.3 분석 플랫폼 요구
- **Orthogonal RP-HPLC (2 columns) + LC-HRMS (Q-TOF/Orbitrap) peptide mapping** — ICH Q5E 원칙 적용.
- **CD spectroscopy/HDX-MS** — high-order structure (특히 cyclic peptide 의 conformation).
- **CE-SDS** — disulfide-linked variants.

---

## F.3 정책·보조금 동향 (US / EU / Asia)

### F.3.1 미국
- **BIOSECURE Act**: **2025-12-18, FY2026 NDAA에 포함 서명**. 연방 조달·보조금에서 "biotechnology companies of concern (BCC)" 거래 제한. 현재 WuXi AppTec, WuXi Biologics, WuXi XDC는 BCC 미지정이나 1260H 리스트 추가 권고 letter 발송됨. 1260H 등재 시 **970일 후** (~2028 8월) 시행, 기존 계약 5년 safe harbor (출처: [Foley Hoag analysis](https://foleyhoag.com/news-and-insights/publications/alerts-and-updates/2025/december/congress-passes-biosecure-act-here-s-what-you-need-to-know/); [Latham & Watkins](https://www.lw.com/en/insights/biosecure-act-becomes-law-limiting-grants-with-biotechnology-companies-of-concern); [Labiotech](https://www.labiotech.eu/more-news/cdmo-industry-trends-biosecure-act/)).
- **Catalent-Novo Nordisk 인수 (2024-02 발표, 11 B USD)**: Bloomington (IN, US) 등 3 사이트, **2026년부터** filling capacity 점진 확대. GLP-1 펩타이드 supply chain reshoring 신호탄 (출처: [Novo Nordisk 6-K 2024](https://www.sec.gov/Archives/edgar/data/0000353278/000117184324000577/f6k_020524.htm)).
- **IRA Medicare Negotiation (Round 2, 2027 가격 발효)**: Ozempic $959 → **$274/월 (-71%)**, Wegovy $385/월. Medicare GLP-1 Bridge 프로그램 2026-07 ~ 2027 (월 $50 copay). Medicare 총 절감 추정 $12 B/yr (출처: [Fierce Pharma](https://www.fiercepharma.com/pharma/medicare-unveils-price-reductions-15-drugs-including-novos-semaglutide); [KFF](https://www.kff.org/medicare/the-ira-has-improved-coverage-of-drugs-selected-for-medicare-price-negotiation/)).
  - **함의**: GLP-1 가격 하락 → COGS 압박 → 저비용 chemo-enzymatic 공정의 ROI 매력 ↑.

### F.3.2 유럽
- **EU Pharmaceutical Strategy + EU Critical Medicines Act (2024)** — EU 내 API 생산 강화 인센티브.
- **CSRD (Corporate Sustainability Reporting Directive)**: Wave 1 reporters FY2024 데이터 기준 2025년부터 보고 개시. 2025-12 "Omnibus I" 합의로 일부 적용 2년 연기. 펩타이드 CDMO (Bachem, PolyPeptide)는 Scope 1+2+3 emissions, EU Taxonomy 정합성 공개 의무 (출처: [Coolset CSRD](https://www.coolset.com/academy/eu-csrd-regulation-explained); [Consilium 2025-12](https://www.consilium.europa.eu/en/press/press-releases/2025/12/09/council-and-parliament-strike-a-deal-to-simplify-sustainability-reporting-and-due-diligence-requirements-and-boost-eu-competitiveness/)).

### F.3.3 한국
- **2025-01 National Bio Committee 출범** + Bio Economy 2.0 Initiative.
- **Biopharmaceutical CDMO Support Act** (제안) — 등록 CDMO 세제 혜택.
- **K-Biopharma Next Bridge** — Basel SIP 등 글로벌 액셀러레이터 입주.
- **송도 ADC/펩타이드 신규 사이트** — Samsung Biologics 등 BIOSECURE 수혜 (출처: [Seoulz K-Bio CDMO 2026](https://www.seoulz.com/korea-k-bio-cdmo-2026/); [KoreaBiomed](https://www.koreabiomed.com/news/articleView.html?idxno=30632)).

### F.3.4 일본·중국
- 일본 PMDA: ICH Q11 준수, AMED 보조금. 특별한 효소 펩타이드 incentive 미확인.
- 중국 NMPA: 자체 CDE 가이드라인 + BIOSECURE 역풍으로 WuXi 펩타이드 사업 미국 매출 압박.

### F.3.5 인도
- **DGFT FTP 2023 amend (2025-08)** — Advance Authorisation EO 기간 18 개월로 완화.
- **PLI 스킴** — API 수입 50% 감축 효과 (semaglutide 인도 특허 만료 2026-03 임박, 제네릭 러시).
- 수출 시 Drug Controller NOC 필요 — 별도 export control은 일반 API 동일 (출처: [GlobalTrade Alert India](https://globaltradealert.org/state-act/43482-india-export-policy-of-certain-pharmaceutical-ingredients-and-formulations-restricted-in-response-to-the-covid-19-pandemic/); [PengtingPeptide India](https://pengtingpeptide.com/industry-insights/indias-peptide-boom-supply/)).

---

## F.4 지정학적 리스크

1. **US-China 디커플링 (BIOSECURE)**: WuXi STA peptide business 미국 고객(GLP-1 sponsor 다수) 이전 가속. 단기적으로 CDMO 캐파 부족, 가격 상승 우려; 중장기 미국·EU·한국·일본 CDMO 반사이익.
2. **Indian API 의존 리스크**: 보호 아미노산(Fmoc-AA-OH) 인도 의존도 높음. 인도 정부의 export 제한 (역사적 COVID-19 사례) 재발 시 SPPS supply chain shock. Chemo-enzymatic은 보호 아미노산 수요를 50–70% 절감해 **이 리스크에 상대적으로 견고**.
3. **GLP-1 ingredient 집중 리스크**: 글로벌 semaglutide 원료(특히 side chain C18 acyl, Aib, MePEG-OSu) 공급 집중. 2024 GLP-1 shortage가 counterfeit·compounding 폭증 유발 (FDA 2025-02 shortage 해제, 2026-04-30 503B Bulks List 제외 제안) (출처: [Drug Topics](https://www.drugtopics.com/view/glp-1-no-longer-on-fda-s-drug-shortage-list); [Healthcare Brew 2026](https://www.healthcare-brew.com/stories/2026/03/23/fda-crackdown-unapproved-glp-1s)).
4. **유럽 에너지·솔벤트 가격**: DMF 등 dipolar aprotic 솔벤트 EU REACH SVHC 추가 잠재 — chemo-enzymatic의 솔벤트 사용 감소로 회피 가능.

---

## F.5 ESG / 환경 (PMI 비교 포함)

### F.5.1 PMI (Process Mass Intensity) 비교
| 합성방법 | PMI (kg waste / kg API) | 주요 폐기물 | CO₂ footprint [추정] | 출처 |
|---|---|---|---|---|
| 전통 SPPS (1000–5000 Da 펩타이드) | **3,000 – 15,000** | DMF/DCM/piperidine/HBTU·HATU coupling reagent, TFA cleavage, MTBE 침전 | ~ 800–3,000 kg CO₂eq/kg API | RSC Green Chem 2022 D1GC04387K; PMC9057961 |
| Green SPPS (binary green solvent, Bachem-Novo Nordisk 2021) | **~ 1,500 – 5,000** (-50%까지) | NBP/EtOAc 등 green solvent | ~ 400–1,500 | Bachem-Novo Nordisk 사례 |
| Hybrid Solution + Fragment condensation | **500 – 2,000** | 솔벤트 ↓, 보호기 ↓ | ~ 200–800 | RSC D0RA07204D |
| **Chemo-enzymatic (Peptiligase/OaAEP1)** | **100 – 500** (10–30배 ↓ vs SPPS) | Water-based buffer, organic co-solvent (DMSO/CH3CN) | ~ 50–200 | Toplak 2016; Frontiers Chem 2019; Uppsala thesis 2023 |
| Recombinant fermentation (E. coli/yeast) | **30 – 200** | 발효 broth, 정제 buffer | ~ 30–100 | Greening peptide therapeutics PMC9057961 |

(출처: [Sustainability in peptide chemistry RSC 2022](https://pubs.rsc.org/en/content/articlehtml/2022/gc/d1gc04387k); [Greening peptide therapeutics PMC9057961](https://pmc.ncbi.nlm.nih.gov/articles/PMC9057961/); [PMC10609221](https://pmc.ncbi.nlm.nih.gov/articles/PMC10609221/); [Bachem-Novo Nordisk 2021](https://www.bachem.com/news/bachem-novo-nordisk-redesign-spps-for-green-chemistry/))

> **Sheldon의 sustainability scale**: PMI > 1,000은 "pharmaceutical-grade waste burden" 최고 등급. SPPS는 fine chemical (PMI 5–50) 대비 100배 이상 비효율.

### F.5.2 솔벤트 회수·green chemistry credentials
- ACS GCI Pharmaceutical Roundtable: 펩타이드 합성을 "highest priority for greening" 카테고리에 등재.
- Peptiligase·OaAEP1은 **수성(buffer) 매질 + 10–30% organic co-solvent**로 작동 → DMF/NMP를 90% 이상 회피 가능.
- 솔벤트 회수율: SPPS 사이트 typical 60–70%; chemo-enzymatic은 buffer recycle 가능해 80–90% 가능 [추정].

### F.5.3 CSRD / EU Green Deal 함의
- 펩타이드 CDMO Scope 3 emissions의 60–80%가 솔벤트·시약 — chemo-enzymatic 전환은 Scope 3 큰 폭 감축으로 EU Taxonomy "substantial contribution to climate change mitigation" 정합성 ↑ → ESG-linked financing 금리 우대 가능.

---

## F.6 안전성 및 면역원성 리스크

### F.6.1 Subtilisin 계열 (Peptiligase) 면역원성·알레르기 위험
- **역사적 detergent 산업 outbreak**: 1960–70 년대 Carlsberg subtilisin 도입 후 **세제 공장 작업자의 50% 이상**이 occupational asthma, IgE 생성, 기도 과민반응 발생 (출처: [PMC4417417 Subtilisin allergic inflammation](https://pmc.ncbi.nlm.nih.gov/articles/PMC4417417/); [PubMed 25876764](https://pubmed.ncbi.nlm.nih.gov/25876764/)).
- **기전**: protease 활성 + PAR-2 + IL-33/ST2 + MyD88 axis로 Th2 면역반응 유도. 활성-의존성 → catalytic Ser/His를 변형해도 알레르기 위험 잔존 가능 [추정].
- **HLA-DQ8 사람 감수성 유전자**: subtilisin BPN' 과민반응의 강력한 marker (출처: [PubMed 16185928](https://pubmed.ncbi.nlm.nih.gov/16185928/)).
- **NIOSH/OSHA**: Subtilisin은 ceiling 0.00006 mg/m³ (60 ng/m³) — 가장 엄격한 직업 노출 한도 중 하나 (출처: [NIOSH NPG Subtilisins](https://www.cdc.gov/niosh/npg/npgd0572.html)).
- **완화방안**:
  - **제조 시 작업자 노출**: 폐쇄형 reactor + HEPA + 의료 감시 (annual 폐기능, IgE).
  - **API 잔류 제어**: anti-Peptiligase ELISA로 < 10 ppm 보장, in silico T-cell epitope (NetMHCII) 평가.
  - 환자 IgE/Skin prick test 시판 후 약물감시(PV) signal 모니터링.

### F.6.2 OaAEP1 (식물 유래 AEP) 알레르겐 위험
- **식물 cysteine protease** (papain, bromelain 계열)는 type I food/respiratory allergen으로 잘 알려짐. *Oldenlandia affinis* 단백질 자체의 알레르겐성 임상 데이터는 **공개 미흡** [미확인].
- **잠재 cross-reactivity**: papain·ficin·bromelain IgE 양성 환자와의 cross-reactivity 가능성 in silico/in vitro 평가 권고 [추정].
- **완화방안**: 잔류 < 1 ng/mg, HCP < 100 ppm, food allergen panel cross-reactivity 시험.

### F.6.3 HCP 잔류 면역원성
- FDA 2024-07 Federal Register: HCP의 IVISIA 평가 의무화 방향. *E. coli* HCP 중 OmpF, OmpC, GroEL은 documented immunogen.
- **Cyclic 펩타이드의 경우** (OaAEP1 라이게이션 산물): 분자 자체가 head-to-tail cyclic이라 anti-drug antibody (ADA) 생성률이 linear 대비 일반적으로 낮음(< 5%) [추정].

### F.6.4 Counterfeit / Compounded GLP-1 맥락
- 2024–2025 GLP-1 shortage 기간 미허가 compounded·counterfeit 제품 폭증, FDA 455+ AE reports (semaglutide) (출처: [Pharmacy Times FDA compound GLP-1](https://www.pharmacytimes.com/view/fda-moves-to-permanently-close-the-door-on-compounded-glp-1s)).
- **Chemo-enzymatic 정통 공급자 입장**: counterfeit 우려 ↑ → 합법 CDMO 수요 ↑ (긍정적 reflex), 단 503B Bulks List 제외(2026-04-30 제안)로 compounding 시장 축소.

---

## F.7 종합 리스크 매트릭스 (가능성 × 영향)

| # | 리스크 | 가능성 | 영향 | 완화방안 | 출처 |
|---|---|---|---|---|---|
| R1 | Peptiligase 잔류 효소의 IgE-mediated 알레르기 (subtilisin 역사) | 중 | 상 | < 10 ppm 잔류, IVISIA, PV monitoring, T-cell epitope 엔지니어링 | PMC4417417; NIOSH NPG |
| R2 | OaAEP1 식물 cysteine protease cross-reactivity (papain 계열) | 중 | 중 | 식품 allergen panel test, < 1 ng/mg | (추정 [미확인]) |
| R3 | FDA HCP-for-peptide 가이던스 강화 (2024 RFI 후 draft 예정) | 상 | 중 | 효소-specific ELISA + LC-MS/MS 미리 구축 | Federal Register 2024-16356 |
| R4 | SPPS→enzymatic 공정 전환 시 ICH Q5E comparability 부적합 | 중 | 상 | 사전 3-batch 비교, Type B meeting 사전 | ICH Q5E EMA |
| R5 | BIOSECURE Act WuXi peptide 캐파 이탈 → 산업 supply shock | 상 | 상 (단기 가격 ↑, 자사 입장에선 기회) | dual-sourcing, 한국·EU 사이트 확보 | Foley Hoag 2025-12 |
| R6 | IRA GLP-1 가격 -71% (2027 발효)로 단가·마진 압박 | 상 (확정) | 상 | 저비용 chemo-enzymatic 공정으로 COGS 절감 | Fierce Pharma; KFF |
| R7 | EMA Synthetic Peptide Guideline 2026-06 발효, chemo-enzymatic 명시 부재 → 해석 리스크 | 상 | 중 | EMA Scientific Advice 사전 신청 | EMA 2024 |
| R8 | India 보호 아미노산 export 제한 재발 | 중 | 중 | 보호 아미노산 수요 50% ↓ 가능한 enzymatic 공정 자체가 헷지 | Global Trade Alert |
| R9 | CSRD Scope 3 보고 의무 → SPPS solvent footprint 자본시장 평가 악화 | 상 | 중 | enzymatic 전환으로 CO₂/PMI 개선 보고 | Coolset CSRD; AOSh |
| R10 | DMF·NBP 등 솔벤트 REACH SVHC 등재 가능 | 하-중 | 중 | water-based enzymatic 공정으로 회피 | EU REACH (일반) |
| R11 | counterfeit/compounded GLP-1 → 정품 브랜드 손상 | 중 | 하 (B2B CDMO 직접 영향 小) | track-and-trace, DSCSA 준수 | Pharmacy Times |
| R12 | 효소 IP (EnzyPep/Fresenius 독점) 라이선스 거절·고가 | 중 | 상 | OaAEP1 (공개·academic) 활용, 자체 엔지니어링 | EnzyPep-FK 양도, 2025 |
| R13 | Endotoxin·DNA 잔류 (특히 *E. coli* 효소 시스템) | 중 | 상 | endotoxin removal column, qPCR < 10 ng/dose | WHO; USP |
| R14 | Over-ligation/mis-ligation 펩타이드 불순물 ≥ 0.5% → ANDA 거절 | 중 | 상 | mass-control, orthogonal HPLC, FDA 2021 가이던스 준수 | FDA Synthetic Peptide 2021 |
| R15 | 한국 Bio CDMO Support Act 통과 지연 시 보조금 미실현 | 중 | 하-중 | 글로벌 다원화, R&D 세액공제 활용 | Seoulz K-Bio 2026 |

**리스크 점수 합산 (가능성·영향 각 상=3/중=2/하=1)**:
- 최고우선(score≥8): R1, R5, R6, R14 — 알레르기·BIOSECURE·IRA가격·불순물 컴플라이언스.
- 고우선(score=6–7): R3, R4, R7, R9, R12, R13.
- 모니터링(score≤5): R2, R8, R10, R11, R15.

---

## 핵심 출처 목록

1. FDA Synthetic Peptide Guidance (2021): https://www.fda.gov/media/166571/download
2. FDA Federal Register 2024-16356 (HCP in follow-on recombinant peptides, 2024-07-25): https://www.federalregister.gov/documents/2024/07/25/2024-16356/
3. EMA Guideline on Synthetic Peptides (finalized 2024, 발효 2026-06-01): https://www.ema.europa.eu/en/documents/scientific-guideline/guideline-development-manufacture-synthetic-peptides_en.pdf
4. ICH Q11 Guideline + Q&A: https://database.ich.org/sites/default/files/Q11%20Guideline.pdf
5. ICH Q5E Comparability: https://www.ema.europa.eu/en/ich-q5e-biotechnological-biological-products-subject-changes-their-manufacturing-process-comparability-biotechnological-biological-products-scientific-guideline
6. Foley Hoag, "Congress Passes BIOSECURE Act" (2025-12): https://foleyhoag.com/news-and-insights/publications/alerts-and-updates/2025/december/congress-passes-biosecure-act-here-s-what-you-need-to-know/
7. Latham & Watkins, BIOSECURE Act Becomes Law: https://www.lw.com/en/insights/biosecure-act-becomes-law-limiting-grants-with-biotechnology-companies-of-concern
8. Labiotech, "CDMO industry post BIOSECURE": https://www.labiotech.eu/more-news/cdmo-industry-trends-biosecure-act/
9. Fierce Pharma, Medicare Round 2 price (2026): https://www.fiercepharma.com/pharma/medicare-unveils-price-reductions-15-drugs-including-novos-semaglutide
10. KFF Medicare Drug Negotiation: https://www.kff.org/medicare/key-facts-about-medicare-drug-price-negotiation/
11. CMS Medicare GLP-1 Bridge: https://www.cms.gov/medicare/coverage/prescription-drug-coverage/medicare-glp-1-bridge
12. RSC Green Chemistry "Sustainability in peptide chemistry" (D1GC04387K, 2022): https://pubs.rsc.org/en/content/articlehtml/2022/gc/d1gc04387k
13. RSC Advances "Greening synthesis of peptide therapeutics" (D0RA07204D): https://pubs.rsc.org/en/content/articlehtml/2020/ra/d0ra07204d
14. PMC9057961 Greening peptide therapeutics industrial perspective: https://pmc.ncbi.nlm.nih.gov/articles/PMC9057961/
15. PMC10609221 Peptides as Therapeutic Agents (Green Transition): https://pmc.ncbi.nlm.nih.gov/articles/PMC10609221/
16. Bachem-Novo Nordisk SPPS green chemistry (2021): https://www.bachem.com/news/bachem-novo-nordisk-redesign-spps-for-green-chemistry/
17. PMC4417417 Subtilisin allergic airway: https://pmc.ncbi.nlm.nih.gov/articles/PMC4417417/
18. PubMed 16185928 HLA-DQ8 subtilisin hypersensitivity: https://pubmed.ncbi.nlm.nih.gov/16185928/
19. NIOSH NPG Subtilisins: https://www.cdc.gov/niosh/npg/npgd0572.html
20. Frontiers Chemistry "Natural and Engineered Enzymes for Peptide Ligation" (2019): https://www.frontiersin.org/articles/10.3389/fchem.2019.00829/full
21. PMC12503010 HCP Clinical Safety Updated Industry Review (2025): https://pmc.ncbi.nlm.nih.gov/articles/PMC12503010/
22. PharmaCompass Fresenius Kabi AG / EnzyPep 양도: https://www.pharmacompass.com/who-gmp-certificate/fresenius-kabi-ag
23. Coolset CSRD Guide (Jul 2025): https://www.coolset.com/academy/eu-csrd-regulation-explained
24. EU Council Press Release 2025-12-09 (CSRD/CSDDD Omnibus 합의): https://www.consilium.europa.eu/en/press/press-releases/2025/12/09/
25. Drug Topics, GLP-1 off FDA shortage list: https://www.drugtopics.com/view/glp-1-no-longer-on-fda-s-drug-shortage-list
26. Healthcare Brew, FDA crackdown 2026: https://www.healthcare-brew.com/stories/2026/03/23/fda-crackdown-unapproved-glp-1s
27. Seoulz K-Bio CDMO 2026: https://www.seoulz.com/korea-k-bio-cdmo-2026/
28. KoreaBiomed Open Innovation: https://www.koreabiomed.com/news/articleView.html?idxno=30632
29. Novo Nordisk 6-K 2024-02-05 (Catalent 인수): https://www.sec.gov/Archives/edgar/data/0000353278/000117184324000577/f6k_020524.htm
30. PengtingPeptide India market & compliance: https://pengtingpeptide.com/industry-insights/indias-peptide-boom-supply/

---

*문서 끝.*
