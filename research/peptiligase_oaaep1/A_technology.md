# [A] 기술 분석: Peptiligase / OaAEP1

> 본 보고서는 Peptiligase(엔지니어드 subtilisin BPN' 계열)와 OaAEP1(식물 유래 asparaginyl endopeptidase 계열)를 효소 매개 펩타이드 라이게이션(enzymatic peptide ligation) 플랫폼으로 평행 분석한다. 두 효소는 모두 펩타이드 결합 형성을 촉매하지만 (i) 단백질 골격(serine protease vs cysteine protease/AEP), (ii) 인식 모티프(거의 비특이적 vs Asn/Asp-Xaa C-말단), (iii) 주 응용(선형 펩타이드 절편 축합 vs 머리-꼬리 환화/단백질 표지)에서 본질적으로 다르므로, 동일 시장 내 **상호 보완적(parallel)** 플랫폼으로 취급한다.

작성일: 2026-05-21

---

## A.1 핵심 기술 원리 및 작동 방식

### A.1.1 Peptiligase (engineered subtilisin BPN')

**계보(history).** Peptiligase 계열의 시작점은 1991년 Abrahmsén·Wells·Estell 등이 Genentech에서 보고한 **subtiligase**이다. Subtilisin BPN'의 활성 부위 Ser221을 Cys로 치환한 **thiol-subtilisin (S221C)**은 약 50년 전 화학 변형(Bender 1966 / Polgar & Bender, Neet & Koshland)으로 처음 만들어졌고, 이를 단백질 공학으로 재현하면서 Pro225 → Ala (S221C/P225A) 이중변이를 도입해 펩타이드 ligase 활성을 10배 높이고 amidase(가수분해) 활성을 100배 이상 낮춘 효소가 subtiligase이다 (Source: https://pubs.acs.org/doi/10.1021/bi00231a007, pub date: 1991; Source: https://static1.squarespace.com/static/5ce8ac5966486300019734c6/t/5f03e9cb8e53972d04713ba3/1594092005400/acs.chemrev.9b00372+%281%29.pdf, pub date: 2020-07-07).

그러나 subtiligase는 (i) Ca²⁺ 결합 도메인에 의존하여 폴딩 안정성이 낮고, (ii) 평균 ligation 수율 60–70%에서 acyl-acceptor를 10배 과량 사용해야 했다 (Source: https://www.csbj.org/article/S2001-0370(21)00053-2/fulltext, pub date: 2021-02-19).

DSM(현재 Fresenius Kabi iPSUM/EnzyPep)의 Quaedflieg·Nuijens·Toplak·Bian Zhang 그룹은 (i) 안정적이고 Ca²⁺-비의존인 subtilisin BPN' 변이체를 출발 scaffold로 채택, (ii) Ser221(원 BPN' 번호 Ser212로 표기되기도 함) → Cys, Pro225 → Ala 외에 다수의 추가 돌연변이를 도입하여 2016년 **peptiligase**를 발표했다. Peptiligase는 organic cosolvent 내성(최대 60% DMF/DMSO), T_M ≈ 66°C의 열안정성, 그리고 Cα ester (carboxamidomethyl, Cam-OH 기반 에스터)와 비보호 acyl acceptor 사이의 결합을 ≥98% ligation 수율(1.1–1.5 eq 과량) / 1 h 이내, 가수분해 부산물 거의 없음으로 촉매한다 (Source: https://advanced.onlinelibrary.wiley.com/doi/abs/10.1002/adsc.201600017, pub date: 2016-05-12; Source: https://www.iris-biotech.de/en/blog/omniligase-for-efficient-peptide-ligation/, pub date: 2021).

**Cam ester 화학.** Acyl 공여체는 SPPS로 합성한 펩타이드의 C-말단을 carboxamidomethyl (–OCH₂C(O)NH₂; "Cam") 에스터로 활성화한 형태이다. Sieber/Rink/Ramage 같은 표준 아미드 수지에서 SPPS로 제조 가능하고, 효소 친화도 향상(특히 thiol-subtilisin 변이체의 S' 포켓 결합)과 펩타이드 자체의 수용성 유지를 동시 달성한다 (Source: https://www.sciencedirect.com/science/article/abs/pii/S0040403916308188, pub date: 2016-09-07; Source: https://link.springer.com/article/10.1007/BF00811332, pub date: 1985).

**메커니즘 — 가수분해/ligation 평형 역전.** Catalytic Cys가 Cam-에스터의 카르보닐 탄소를 공격하여 **thioacyl-enzyme intermediate**를 형성한다. 이 중간체는 (i) 물(가수분해, hydrolysis) 또는 (ii) 들어오는 펩타이드의 N-말단 α-아민(aminolysis/ligation)에 의해 분해될 수 있다. Peptiligase는 활성 부위 S1' 포켓 변이(예: M222P/L217H 출발 → A225N, S2' 포켓 F189W, S4 I107V)를 통해 S/H 비율을 극대화하여 ligation 경로로의 선택성을 부여한다 (Source: https://www.csbj.org/article/S2001-0370(21)00053-2/fulltext, pub date: 2021-02-19).

**후속 변이체 라이브러리.** 같은 scaffold에서 substrate scope를 확장한 변이체군이 만들어졌다:
- **Omniligase-1**: 광범위 substrate scope (400-member acyl acceptor 라이브러리 중 250개 이상 결합 가능), 선형 및 head-to-tail 환화에 사용. EnzyPep BV가 상용화(현 Fresenius Kabi iPSUM) (Source: https://www.csbj.org/article/S2001-0370(21)00053-2/fulltext, pub date: 2021-02-19).
- **Thymoligase**: Thymosin-α1 14+14-mer fragment ligation을 위해 substrate-tailored되었으며, 결정구조 PDB 5OX2가 확보됨. 1단계 결합 ≥94% 수율, 전체 thymosin-α1 수율 55%(기존 산업 공정 대비 2배 이상) (Source: https://pubs.rsc.org/en/content/articlelanding/2018/ob/c7ob02812a, pub date: 2018-01-04; Source: https://www.rcsb.org/structure/5OX2, pub date: 2017).
- 기타: **Aviptadil ligase 변이체**(2023, VIP 28-mer chemo-enzymatic 합성) (Source: https://pubmed.ncbi.nlm.nih.gov/37774815/, pub date: 2023-09-27).

### A.1.2 OaAEP1 (asparaginyl endopeptidase)

**생물학적 기원.** OaAEP1은 cyclotide(머리-꼬리 환화된 cysteine-rich 펩타이드) 생합성으로 유명한 식물 *Oldenlandia affinis*에서 분리된 asparaginyl endopeptidase (AEP, EC 3.4.22.34)이다. AEP는 시스테인 프로테아제 슈퍼패밀리 C13에 속하며, legumain과 71% 동일성을 가지나 자연 상태에서 ligation/cyclization을 자체 촉매한다 (Source: https://www.nature.com/articles/ncomms10199, pub date: 2016-01-04; Source: https://pmc.ncbi.nlm.nih.gov/articles/PMC8209628/, pub date: 2021-06).

**촉매 메커니즘.** 활성 자리에 catalytic dyad (Cys-His)를 보유한 cysteine protease로 작동하나, ligase로서는 다음 단계로 진행한다:
1. P1 위치의 **Asn(또는 Asp)** 카르보닐 탄소를 활성 Cys가 공격하여 **thioacyl-enzyme intermediate** 형성.
2. P1' 위치의 leaving group이 떨어져나간 후, 들어오는 펩타이드의 N-말단 α-아민이 nucleophile로 작동.
3. 새로운 펩타이드 결합이 형성되고 효소가 회수됨. 인식 모티프는 **C-말단 Asx-Xaa₁-Xaa₂**(흔히 NGL, NHV, NAL 등; OaAEP1 우선 NGL) (Source: https://www.thno.org/v11p5863.htm, pub date: 2021; Source: https://pmc.ncbi.nlm.nih.gov/articles/PMC10240336/, pub date: 2023-06).

**Gatekeeper 잔기와 C247A 하이퍼활성 변이체.** OaAEP1의 야생형은 in vitro에서 ligase 활성이 비교적 낮다. Yang 그룹(Bioorganic Med Chem 2017 / Yang et al.) 등이 **Cys247 잔기**를 Ala로 치환한 **OaAEP1-C247A** 변이체를 보고했고, 이는 야생형 대비 **약 160배** 활성 증가를 보였다. Cys247은 ligation pocket으로의 nucleophile 진입 채널 역할을 하는 것으로 해석되며, C247A 변이는 butelase-1과 비교 가능한 수준의 촉매효율을 보인다 (Source: https://www.thno.org/v11p5863.htm, pub date: 2021).

또한 "gatekeeper residue"(주로 Val/Thr 위치, butelase에서는 Cys/Ala swap)들이 ligation/proteolysis 평형과 substrate scope를 결정짓는 핵심임이 구조생물학적으로 규명되어 있다 (Source: https://www.biorxiv.org/content/10.1101/2021.12.09.471967.full.pdf, pub date: 2021-12-09; Source: https://pubs.acs.org/doi/10.1021/acscatal.0c02078, pub date: 2020).

**최신 엔지니어링(2024–2025).** 2024년 *J. Am. Chem. Soc.* (Liu et al.) — recombinant asparaginyl ligase가 "Asn-Ala-Leu (NAL)" 인식 모티프와 N-말단 "Arg-Leu" nucleophile에 대해 디자인되어, OaAEP1-C247A 대비 **70배** 높고 Fe³⁺ 완충액에서 butelase-1보다 2배 높은 촉매 활성을 달성 (Source: https://pubs.acs.org/doi/10.1021/jacs.5c04693, pub date: 2025-06; Source: https://pubs.acs.org/doi/10.1021/jacs.4c11964, pub date: 2024-11). 2025 *Chem. Commun.* — single-molecule force spectroscopy를 위한 OaAEP1 표지 응용 (Source: https://pubs.rsc.org/en/content/articlelanding/2025/cc/d5cc05717e, pub date: 2025).

**핵심 차이 (Peptiligase vs OaAEP1):**
| 항목 | Peptiligase | OaAEP1 |
|---|---|---|
| 골격 | Subtilisin BPN' (serine protease) | Asparaginyl endopeptidase (cysteine protease, C13) |
| 활성 잔기 | Cys (S221C/S212C); Catalytic triad Asp-His-Cys 변형 | Cys-His dyad |
| 인식 | 거의 비특이적 (P1/P1' 폭넓음) | C-말단 Asx-Xaa₁-Xaa₂ (예: NGL, NHV, NAL) **필수** |
| Acyl donor | Cα Cam-ester (-OCH₂CONH₂) | 천연 펩타이드 (인식 모티프 필요), 별도 활성화 불필요 |
| 응용 | 선형 펩타이드 절편 축합, GLP-1/exenatide/aviptadil 등 | Head-to-tail 환화, 단백질 site-specific 표지, ADC linker |
| Scar | 거의 traceless (모든 천연 아미노산) | Asx-Xaa scar (Asn/Asp 잔류) |

---

## A.2 기술 성숙도 (TRL)

**TRL은 응용 맥락에 따라 다르게 평가**해야 한다. 본 분석에서는 NHLBI Catalyze TRL 기준(TRL 5 = pilot batch process; TRL 6 = GMP process validation; TRL 7+ = clinical-stage drug substance; TRL 9 = approved drug)을 사용한다 (Source: https://nhlbicatalyze.org/trl).

### A.2.1 Peptiligase 계열 — **TRL 6–7 (절편 축합) / TRL 5–6 (cyclization)**

- **상업적 enzyme supply**: EnzyPep BV(현재 Fresenius Kabi iPSUM I&D Center, Geleen, NL)가 GMP 등급 Omniligase-1을 공급. Iris Biotech, Bachem 등을 통해서도 연구용 시약 공급 (Source: https://www.linkedin.com/in/ana-toplak-04b79414/, pub date: 검색일 2026-05-21).
- **임상/상업 페티드**: Exenatide(39-mer), Thymosin-α1(28-mer), Aviptadil(VIP, 28-mer), Semaglutide/Liraglutide/GLP-1 류에 대한 chemo-enzymatic 공정이 patent 및 논문에 등재 (US10920258B2, US10883132B2 등; EnzyPep BV → 2025년 1월 Fresenius Kabi Ipsum SRL로 양도) (Source: https://patents.google.com/patent/US10920258B2/en, pub date: patent grant 2021-02-16). Exenatide의 경우 g-scale enzymatic 축합 및 통상 SPPS 대비 ≈2배 수율 보고 (Source: https://www.csbj.org/article/S2001-0370(21)00053-2/fulltext, pub date: 2021-02-19).
- **GMP 승인 의약품**: 2026년 5월 현재, **Peptiligase로 제조된 단일 항목이 단독 active step으로 FDA/EMA에 명시되어 승인된 상용 의약품**은 [미확인]. 다만 chemo-enzymatic 공정이 일부 generic peptide의 supply chain에 사용된다는 산업 소식(EnzyTag, Fresenius Kabi)은 다수 [추정] (Source: https://enzytag.com/technology/, pub date: 검색일 2026-05-21).
- **스케일**: 공개 자료 기준 gram–사다리 단위 scale-up이 입증됨. Kilogram-scale의 정확한 공개 수치는 [미확인] — 통상 CDMO(Fresenius, Bachem) NDA·기밀 영역.

### A.2.2 OaAEP1 계열 — **TRL 3–4 (대다수 응용) / 일부 TRL 5 (research-grade ADC linker, 단분자 immobilization)**

- **재조합 발현 확립**: E. coli에서 활성형 OaAEP1, OaAEP1b-C247A 발현 표준화 (Source: https://www.nature.com/articles/ncomms10199, pub date: 2016-01-04). 다만 Pichia pastoris 등에서의 cGMP scale 공정은 [미확인].
- **임상 의약품**: 직접적으로 OaAEP1로 제조된 승인 의약품은 **현재 없음** [미확인]. 주로 학술/discovery(phage display, cyclotide 합성), bioconjugation tool, ADC linker 후보 단계에 머무름 (Source: https://chemrxiv.org/doi/full/10.26434/chemrxiv-2024-c5xw4, pub date: 2024-02; Source: https://pmc.ncbi.nlm.nih.gov/articles/PMC10119931/, pub date: 2023-04).
- **상용 enzyme tool**: Sigma-Aldrich/Merck 및 일부 CRO에서 연구용 시약으로 판매. 본격 GMP 등급은 한정적.

### A.2.3 종합 TRL 정리

| 응용 | Peptiligase/Omniligase-1 | OaAEP1/C247A |
|---|---|---|
| 학술 합성 (peptide ligation/cyclization) | TRL 8–9 (성숙) | TRL 6–7 |
| 산업 g–kg scale peptide manufacture | **TRL 6–7** | TRL 3–4 |
| GMP API (단독 ligation step) | TRL 5–6 [추정] | TRL 2–3 |
| 단백질 표지·ADC linker | TRL 3–4 | TRL 4–5 |

---

## A.3 기술적 난제 및 한계

### A.3.1 Peptiligase 한계

1. **Cα ester (Cam-OH) building block 합성 비용**: Cam-OH 자체는 SPPS 후 추가 활성화 단계가 필요하다. SPPS 단계에서 Sieber/Rink/Ramage 수지로 직접 Cam ester를 만드는 개선법이 보고됐으나 (Source: https://www.sciencedirect.com/science/article/abs/pii/S0040403916308188, pub date: 2016-09-07), 여전히 표준 SPPS 대비 추가 비용·시간 부담.
2. **역가수분해(side hydrolysis)**: 변이체 최적화에도 S/H 비율은 substrate에 따라 달라지며, Pro/Gly 같은 특정 P1' 잔기는 결합 효율 저하.
3. **Substrate scope**: 광범위하나 일부 sterically demanding non-canonical AA(예: Aib, β-AA), 친유성 lipid-conjugated fragment에서 수율 저하 [추정].
4. **열안정성 vs 산업 공정 한계**: T_M 66°C이지만, organic cosolvent 60% 이상 환경 또는 매우 짧은 fragment(<5 AA)에서는 효율 저하.
5. **Scale 경제성 vs SPPS**: SPPS는 자동화·표준화가 완성된 반면 chemo-enzymatic은 2단계(SPPS+enzyme) 공정으로, 짧은(<25-mer) 펩타이드에서는 비용 경쟁력 약함. 그러나 30-mer 이상 (GLP-1, insulin, fuzeon T20)에서 점차 유리.

### A.3.2 OaAEP1 한계

1. **인식 모티프 의존성**: C-말단 Asx-Xaa₁-Xaa₂ (Asn/Asp + 특정 dipeptide) 시퀀스가 반드시 필요. 즉 ligation 후 Asx-Xaa **scar**가 남으며, Asn-free target은 사전에 Asn-encoded handle을 도입해야 함 (Source: https://pmc.ncbi.nlm.nih.gov/articles/PMC8209628/, pub date: 2021-06).
2. **Asn epimerization 및 succinimide 부산물 위험**: Asn–Gly junction에서 succinimide(Asn-Asp 변환, racemization) 생성은 잘 알려진 펩타이드 부반응이며, AEP-ligation 시 중간체 안정성이 영향받을 수 있음 (Source: https://www.sciencedirect.com/science/article/pii/S0021925819758554, pub date: 1987).
3. **가수분해 부반응**: AEP는 본질적으로 endopeptidase이므로 ligation 산물이 다시 가수분해될 가능성이 있고, gatekeeper 잔기 디자인으로 억제하나 완전 제거는 어려움 (Source: https://pmc.ncbi.nlm.nih.gov/articles/PMC8209628/, pub date: 2021-06).
4. **재조합 발현 어려움**: 식물 유래 효소가 E. coli에서 propeptide의 자가-처리(autoactivation)를 정확히 수행해야 활성. Acid-activation step이 필요하고, 정제 수율도 효소마다 편차. Pichia pastoris/CHO 등 GMP-적합 host에서의 일관된 발현은 [미확인].
5. **CMC 우려**: 식물 유래 propeptide의 endotoxin/host-cell-protein 잔류, 활성 회수율, immunogenicity 검토는 GMP 의약품 supply chain의 핵심 진입 장벽.
6. **응집/용해도**: OaAEP1 자체와 long substrate (>50 AA) 모두 응집 경향이 있음 [추정].

---

## A.4 대체/경쟁 기술 비교

| 기술 | 출처 | 인식 모티프 | Acyl donor | 환화 가능 | 촉매 효율 (k_cat/K_M) | Traceless 여부 | TRL/GMP precedent | 비고 |
|---|---|---|---|---|---|---|---|---|
| **Peptiligase / Omniligase-1** | Engineered subtilisin BPN' (DSM/EnzyPep) | 거의 비특이적 (P1/P1' 광범위) | Cα Cam-ester | 가능 (head-to-tail) | 10³–10⁴ M⁻¹s⁻¹ [추정] | Traceless | TRL 6–7, EnzyPep/Fresenius GMP supply | GLP-1, exenatide, thymosin, VIP에 사용 |
| **Subtiligase** | S221C/P225A subtilisin BPN' (Wells & Estell 1991) | 비특이적 | Cα ester (glycolate) | 가능 | 야생형 대비 ~10× ligase | Traceless | TRL 4 (학술) | Ca²⁺ 의존, 안정성 낮음 |
| **OaAEP1 / C247A** | *Oldenlandia affinis* AEP | C-말단 Asx-Xaa₁-Xaa₂ (NGL/NHV/NAL) | 천연 펩타이드 | **매우 적합** (cyclotide-style) | C247A: ~10⁵ M⁻¹s⁻¹ | Asx scar | TRL 3–5 | 단백질 표지, ADC linker, phage display |
| **Butelase-1** | *Clitoria ternatea* AEP | C-말단 Asx-His-Val (Asn-HV) | 천연 펩타이드 | **최강** (cyclization 속도) | ~1.34 × 10⁶ M⁻¹s⁻¹ (medium peptides) | Asx scar | TRL 4–5 | 재조합 발현 난이도 高, 최근 chaperone 공발현으로 100 mg/L 달성 |
| **Sortase A (Srt-A) 5M/7M** | *Staphylococcus aureus* | LPXTG ↔ GGG-X | LPETG... 펩타이드 | 가능 (intra-/intermolecular) | 5M/7M evolved 변이체 10²–10³ M⁻¹s⁻¹ | LPETGG scar 잔류 | TRL 5–6 (ADC tool, in vivo labeling) | 가장 잘 알려진 transpeptidase tool |
| **Trypsiligase** | Engineered trypsin (Bordusa) | YRH motif + Zn²⁺ | Peptidyl 4-guanidinophenyl ester | 가능 | 보고치 다양 | YRH scar | TRL 3 | Zn²⁺ 의존, N-/C-말단 라벨링 |
| **Subtiligase 진화 변이체** (Wells lab 후속) | Engineered | 광범위 | Glycolate ester | 가능 | 변동 | Traceless | TRL 3–4 | Activity-based protein profiling |
| **Native Chemical Ligation (NCL)** | Chem. (Kent 1994) | N-말단 Cys 필수 | C-말단 thioester | 가능 | n/a (chem) | Cys scar | TRL 9 (이미 GMP 의약품 합성에 사용, 예: Fuzeon 일부 fragment 공정) | 비효소 chemical method, hydrophobic peptide 어려움 |
| **SPPS (Fmoc/Boc)** | Chem. | n/a | n/a (residue-by-residue) | 가능 (chemical macrocyclization) | n/a | Traceless | TRL 9 (절대다수 peptide drug) | 30-mer 이상 누적 수율·정제 부담 |
| **PGM1 / ATP-grasp ligase** | Cyanobactin biosynthesis | 광범위 (engineered) | ATP 활성 | 가능 | 보고치 다양 | Scar 다양 | TRL 3 | RiPP 합성에 유리 |
| **Papain ligases** (engineered) | Plant cysteine protease | 광범위 | Activated ester | 가능 | 낮음 | Scar | TRL 2–3 | 학술 단계 |

(Sources: https://pmc.ncbi.nlm.nih.gov/articles/PMC6895249/, pub date: 2019-11-29; https://pmc.ncbi.nlm.nih.gov/articles/PMC9126251/, pub date: 2022; https://onlinelibrary.wiley.com/doi/full/10.1002/anie.202310910, pub date: 2024; https://link.springer.com/article/10.1186/s12934-024-02598-5, pub date: 2024)

핵심 시사점:
- **Peptiligase**는 *broad substrate scope + traceless + GMP-ready*라는 종합점이 가장 높음.
- **OaAEP1/butelase**는 cyclization 속도와 단백질 표지에서 우월하나 scar와 sequence 제약.
- **Sortase A**는 가장 익숙한 도구이지만 LPETGG scar와 느린 kcat가 산업 application의 발목.
- **SPPS/NCL**는 여전히 시장 표준이지만 길고 복잡한 peptide일수록 enzymatic ligation의 부가가치 증가.

---

## A.5 기술 발전 로드맵 (2024-2026)

### A.5.1 효소 공학 (directed evolution + computational design)

- **Recombinant asparaginyl ligase 70× 활성 향상 (2025)**: OaAEP1-C247A 대비 70배, butelase-1 대비 2배 (Fe³⁺ 조건)인 디자인 ligase가 *J. Am. Chem. Soc.* 2025에 보고됨 — gatekeeper + acceptor binding site 재설계 (Source: https://pubs.acs.org/doi/10.1021/jacs.5c04693, pub date: 2025-06).
- **Isopeptide ligation 확장 (2024)**: C247A 변이체가 인접 Leu가 있는 내부 Lys 잔기에 isopeptide 결합 형성 가능 — 분지형 펩타이드, ubiquitin-mimic 합성 가능 (Source: https://pubs.acs.org/doi/10.1021/jacs.4c11964, pub date: 2024-11).
- **Butelase AY 변이체 (2024)**: gatekeeper V237A/T238Y 변이로 활성·발현성 동시 개선; E. coli SHuffle T7 + chaperone 공발현으로 100 mg/L 달성 (Source: https://link.springer.com/article/10.1186/s12934-024-02598-5, pub date: 2024-10).

### A.5.2 AI/ML 기반 효소 설계

- **RFdiffusion / RFdiffusionAA / LigandMPNN**: David Baker 그룹(UW IPD)이 ligand-aware 효소 backbone 설계를 가능케 함. 활성 자리 잔기 조합을 보존한 채로 새로운 fold를 생성하는 시도가 2024–2025년 본격화 (Source: https://meilerlab.org/wp-content/uploads/2024/07/ml_enzyme_design.pdf, pub date: 2024-07).
- **RFpeptides (2024-11 발표, *Nat. Chem. Biol.* 2025-06 게재)**: cyclic peptide binder를 atomic accuracy로 디자인 — OaAEP1-mediated cyclization과 결합 시 cyclic peptide drug discovery 파이프라인 가속화 (Source: https://www.ipd.uw.edu/2024/11/introducing-rfpeptides-ai-for-cyclic-peptide-design/, pub date: 2024-11).
- **ESM-2 기반 peptide design**: PepMLM 등 protein language model이 peptide 후보 생성에 활용. 효소 자체 설계로의 확장은 진행 중 (Source: https://www.science.org/doi/10.1126/sciadv.adr8638, pub date: 2025).

### A.5.3 연속흐름(continuous flow) + 고정화

- 2024–2025년 *ChemSusChem*, *Organic Process R&D*, *Nat. Commun.* 등에서 immobilized enzyme + continuous-flow 패러다임이 일반화. Isoporous block-copolymer membrane + material-binding peptide 활용 효소 고정화 (Source: https://www.nature.com/articles/s41467-024-47007-y, pub date: 2024; Source: https://chemistry-europe.onlinelibrary.wiley.com/doi/10.1002/cssc.202402007, pub date: 2025).
- Peptiligase/Omniligase-1을 고정화하여 SPPS-effluent stream을 직접 ligation으로 연결하는 hybrid SPPS↔flow-enzyme 공정 출현 가능성 [추정].
- Vapourtec 등이 GLP-1류 pilot-scale flow synthesis 보고 (Source: https://www.vapourtec.com/news/glp-1-peptide-synthesis-scaleup/, pub date: 2024-2025).

### A.5.4 산업·CDMO 캐파 확장

- **CordenPharma**: 2025년 3월 Basel(스위스) greenfield peptide manufacturing plant 가동 ($541M 투자, 3년간 총 $1.08B 계획) (Source: https://www.dcatvci.org/features/cdmo-cmo-expansion-update-riding-the-strength-of-tides/, pub date: 2025).
- **Fresenius Kabi iPSUM**: EnzyPep 인수 후 (2019/2025년 patent 양도 완료) chemo-enzymatic peptide 플랫폼 통합 (Source: https://patents.google.com/patent/US10920258B2/en, pub date: 2021).
- **CAGR**: Peptide synthesis CDMO 시장 12.7% CAGR (2025–2034) [insightaceanalytic]; enzymatic/cell-free 분야는 6.43% CAGR [추정] (Source: https://www.insightaceanalytic.com/report/glp-1-peptide-synthesis-cdmo-market/3105, pub date: 2025).

### A.5.5 GLP-1 직접 응용

- US10920258B2 / US10883132B2 / WO2019170918A1: His-X-Glu-Gly-Thr-Phe-Thr-Ser-Asp-Val-Ser-(thio)ester acyl donor + N-말단 비보호 acceptor의 효소 ligation으로 semaglutide/liraglutide 합성 — Omniligase-1 또는 변이체 사용 (Source: https://patents.google.com/patent/US10920258B2/en, pub date: 2021-02-16).
- Novo Nordisk의 semaglutide 자체 공정은 *recombinant precursor (S. cerevisiae) + SPPS 단편 + 화학 결합* hybrid임 — chemo-enzymatic ligation은 generic 합성 또는 next-gen GLP-1 후보(retatrutide-class 등)에서 채택 가능성 [추정] (Source: https://www.researchgate.net/publication/392573822, pub date: 2025).

---

## A.6 핵심 요소기술 및 공급망

### A.6.1 Acyl donor building block

- **Cam-OH / 보호된 Cam-ester resin**: Iris Biotech, Bachem 등 specialty 시약 공급. SPPS 직접 합성 가능 (Sieber/Rink/Ramage amide resin).
- **C-말단 thioester (NCL용)**: Boc-SPPS 또는 hydrazide → thioester 변환.

### A.6.2 효소 공급 — 재조합 발현 호스트

| 효소 | 표준 host | 일반적 수율 | GMP 등급 공급사 |
|---|---|---|---|
| Peptiligase/Omniligase-1 | *B. subtilis* | >0.5 g/L | EnzyPep BV (Fresenius Kabi iPSUM), Iris Biotech (research) |
| Subtiligase | E. coli | mg/L | 학술용 plasmid (Wells lab 공개) |
| OaAEP1 / C247A | E. coli | 보고 편차 ~10–100 mg/L | 일부 specialty CRO, GMP 등급은 [미확인] |
| Butelase-1 (재조합) | E. coli SHuffle T7 + chaperone | ~100 mg/L (2024) | research-grade 위주 |
| Sortase A 5M/7M | E. coli | 100 mg/L+ | Active Motif, Sigma, BPS Bioscience |

(Sources: https://www.iris-biotech.de/en/blog/omniligase-for-efficient-peptide-ligation/, pub date: 2021; https://link.springer.com/article/10.1186/s12934-024-02598-5, pub date: 2024-10; https://bpsbioscience.com/sortase-mediated-protein-ligation, pub date: 검색일 2026-05-21)

### A.6.3 CDMO·통합공급사

- **Fresenius Kabi iPSUM** (Geleen, NL + 이탈리아) — 통합 chemo-enzymatic peptide CMC + EnzyPep IP
- **Bachem**, **PolyPeptide**, **CordenPharma**, **Lonza** — 대규모 GMP peptide CDMO. Enzymatic ligation 도입 정도는 회사별 차등.
- **EnzyTag BV** — CEPS 라이선스/위탁 ([추정] EnzyPep spin-off 또는 자매사) (Source: https://enzytag.com/technology/, pub date: 검색일 2026-05-21).
- **Sinopep-Allsino**, **Enogen** — 아시아 GMP peptide CDMO, GLP-1 capacity 확장.

### A.6.4 Substrate 제약

- **OaAEP1**: 모든 target은 C-말단 Asn-Xaa-Xaa handle을 보유해야 함 → drug substance 시 Asn-encoded handle 추가 → 추가 공정. Native Asn이 없는 단백질에서는 site-directed mutagenesis 또는 합성 핸들 부착 필요.
- **Peptiligase**: Cα Cam-ester 합성 자체가 추가 step이지만 기존 SPPS 인프라와 호환.

### A.6.5 잠재적 supply chain risk

- 단일 IP holder(Fresenius Kabi)의 Peptiligase IP 집중 → 라이선스 가격·접근성 의존도 高 [추정].
- AEP 효소는 학술 단계 IP 분산 — Singapore(NTU), 중국(Yang group), 유럽 등 다국적 출원으로 freedom-to-operate 검토 필요 [추정].

---

## 핵심 출처 목록

1. Toplak A, Nuijens T, Quaedflieg PJLM, Wu B, Janssen DB. *Peptiligase, an Enzyme for Efficient Chemoenzymatic Peptide Synthesis and Cyclization in Water.* Adv. Synth. Catal. **358**, 2140 (2016). — https://advanced.onlinelibrary.wiley.com/doi/abs/10.1002/adsc.201600017 (pub date: 2016-05-12).
2. Schmidt M, Toplak A, Quaedflieg PJLM, Nuijens T. *From thiol-subtilisin to omniligase: design and structure of a broadly applicable peptide ligase.* Comp. Struct. Biotechnol. J. **19**, 1277 (2021). — https://www.csbj.org/article/S2001-0370(21)00053-2/fulltext (pub date: 2021-02-19).
3. Weeks AM, Wells JA. *Subtiligase-Catalyzed Peptide Ligation.* Chem. Rev. **120**, 3127 (2020). — https://static1.squarespace.com/static/5ce8ac5966486300019734c6/t/5f03e9cb8e53972d04713ba3/1594092005400/acs.chemrev.9b00372+%281%29.pdf (pub date: 2020-07-07).
4. Abrahmsén L et al. *Engineering subtilisin and its substrates for efficient ligation of peptide bonds in aqueous solution.* Biochemistry **30**, 4151 (1991). — https://pubs.acs.org/doi/10.1021/bi00231a007 (pub date: 1991).
5. Nguyen GKT et al. *Butelase 1 is an Asx-specific ligase enabling peptide macrocyclization and synthesis.* Nat. Chem. Biol. **10**, 732 (2014). — https://www.nature.com/articles/nchembio.1586 (pub date: 2014).
6. Yang R et al. *Engineering Peptide Asparaginyl Ligases via Truncation.* Nat. Commun. **8**, 14199 (2017); applications and limitations review — https://pmc.ncbi.nlm.nih.gov/articles/PMC8209628/ (pub date: 2021-06).
7. Hemu X et al. *Engineered asparaginyl ligases for site-specific bioconjugation.* — https://www.thno.org/v11p5863.htm (pub date: 2021).
8. Schmidt M et al. *Design of a substrate-tailored peptiligase variant for the efficient synthesis of thymosin-α1.* Org. Biomol. Chem. **16**, 609 (2018). — https://pubs.rsc.org/en/content/articlelanding/2018/ob/c7ob02812a (pub date: 2018-01-04).
9. *Peptiligase, an enzyme for efficient chemo-enzymatic synthesis of aviptadil.* (2023). — https://pubmed.ncbi.nlm.nih.gov/37774815/ (pub date: 2023-09-27).
10. Liu et al. *Asparaginyl Ligases with Engineered Substrate Specificity for Controlled, Sequential Transpeptidation Reactions.* J. Am. Chem. Soc. (2025). — https://pubs.acs.org/doi/10.1021/jacs.5c04693 (pub date: 2025-06).
11. *Highly Efficient Transpeptidase-Catalyzed Isopeptide Ligation.* J. Am. Chem. Soc. (2024). — https://pubs.acs.org/doi/10.1021/jacs.4c11964 (pub date: 2024-11).
12. *An efficient and easily obtainable butelase variant for chemoenzymatic ligation.* Microb. Cell Fact. (2024). — https://link.springer.com/article/10.1186/s12934-024-02598-5 (pub date: 2024-10).
13. Nuijens T et al. *Chemo-enzymatic synthesis of semaglutide, liraglutide and GLP-1.* US10920258B2 / US10883132B2 / WO2019170918A1 (EnzyPep BV → Fresenius Kabi Ipsum SRL, 2025 assignment). — https://patents.google.com/patent/US10920258B2/en (grant 2021-02-16).
14. Zou X-L, Sun L-K. *Empowering Site-Specific Bioconjugations: Advances in Sortase Engineering.* Angew. Chem. Int. Ed. (2024). — https://onlinelibrary.wiley.com/doi/full/10.1002/anie.202310910 (pub date: 2024).
15. Schmidt M et al. *Efficient Enzymatic Cyclization of Disulfide-Rich Peptides by Using Peptide Ligases.* ChemBioChem (2019). — https://chemistry-europe.onlinelibrary.wiley.com/doi/abs/10.1002/cbic.201900033 (pub date: 2019).
16. Iris Biotech blog. *Omniligase-1 for Efficient Peptide Ligation.* — https://www.iris-biotech.de/en/blog/omniligase-for-efficient-peptide-ligation/ (pub date: 2021).
17. EnzyTag BV company technology page — https://enzytag.com/technology/ (검색일 2026-05-21).
18. *Asparaginyl Endopeptidase-Mediated Peptide Ligation and Cyclization for Phage Display.* ChemRxiv (2024). — https://chemrxiv.org/doi/full/10.26434/chemrxiv-2024-c5xw4 (pub date: 2024-02).
19. Institute for Protein Design. *Introducing RFpeptides — AI for cyclic peptide design.* (2024). — https://www.ipd.uw.edu/2024/11/introducing-rfpeptides-ai-for-cyclic-peptide-design/ (pub date: 2024-11).
20. DCAT Value Chain Insights. *CDMO/CMO Expansion Update: Riding the Strength of TIDES.* — https://www.dcatvci.org/features/cdmo-cmo-expansion-update-riding-the-strength-of-tides/ (pub date: 2025).
21. Patti A et al. *Advances and Challenges in the Development of Immobilized Enzymes for Batch and Flow Biocatalyzed Processes.* ChemSusChem (2025). — https://chemistry-europe.onlinelibrary.wiley.com/doi/10.1002/cssc.202402007 (pub date: 2025).
22. *OaAEP1-dependent enzymatic protein ligation and immobilization for single-molecule force spectroscopy.* Chem. Commun. (2025). — https://pubs.rsc.org/en/content/articlelanding/2025/cc/d5cc05717e (pub date: 2025).
