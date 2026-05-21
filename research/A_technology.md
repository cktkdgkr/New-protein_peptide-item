# [A] 기술 분석: EndoS2 Glycosynthase Mutant (Fc Glycan Remodeling)

> 조사 기준일: 2026-05-21 / 조사자: Research Agent A (Technology Analysis)
> 대상 기술: Streptococcus pyogenes 유래 endo-β-N-acetylglucosaminidase EndoS2의 glycosynthase 변이체 (D184M, D184Q 등)를 활용한 항체 Fc 부위 N-glycan site-specific 재조합 (chemoenzymatic remodeling) 플랫폼

---

## A.1 핵심 기술 원리 및 작동 방식

### A.1.1 EndoS2 wild-type의 효소학적 특성
EndoS2는 CAZy GH18 (glycoside hydrolase family 18) 패밀리에 속하는 endo-β-N-acetylglucosaminidase로, *Streptococcus pyogenes* serotype M49 균주에서 분리되었다. 기존 EndoS와 약 37% 서열 동일성을 가지며, IgG Fc 영역의 Asn297에 부착된 N-linked glycan의 가장 안쪽 두 개의 GlcNAc 잔기 사이 β-1,4 결합을 가수분해한다 (Source: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3778708/, pub date: 2013-09-23).

**기질 특이성 (substrate specificity):**
- EndoS: 주로 complex-type biantennary glycan만 절단
- EndoS2: complex-type biantennary (bisected/non-bisected), high-mannose (HM), hybrid type 모두에 작용하는 광범위 특이성. IgG뿐 아니라 α1-acid glycoprotein에도 작용 (Source: https://academic.oup.com/glycob/article/25/10/1053/1988622, pub date: 2015-05-21).
- 구조적 차이: EndoS와 EndoS2의 결합부 conformation 차이로 Fc 기질 접촉면이 다름 (Source: https://www.jbc.org/article/S0021-9258(24)01742-3/fulltext, pub date: 2024-05-03).

**촉매 메커니즘:** GH18 패밀리 특유의 substrate-assisted mechanism — 기질 내 2-acetamido 그룹의 카르보닐 산소가 인접 anomeric 탄소를 공격하여 oxazolinium ion 중간체를 형성한다. EndoS2의 Asp-184가 일반 산/염기 촉매 및 oxazolinium 안정화를 담당한다 (Source: https://pubs.acs.org/doi/10.1021/acscentsci.8b00917, pub date: 2019-04-03).

### A.1.2 Glycosynthase 변이로의 전환
Wang lab(University of Maryland)이 2016년 *JACS*에 보고한 체계적 site-directed mutagenesis에서 Asp-184 위치를 19개 아미노산으로 치환하여 평가한 결과, **D184M, D184Q, D184C, D184N** 등이 가수분해 활성을 잃고 transglycosylation 활성만 유지하는 "glycosynthase" 변이체로 확인되었다. D184M은 D184C 다음으로 높은 transglycosylation 활성을 보였으며, hydrolysis activity는 미미하여 실용적으로 가장 우수한 변이체로 평가된다 (Source: https://pmc.ncbi.nlm.nih.gov/articles/PMC4974367/, pub date: 2016-07-13).

**작동 원리:** Asp184가 oxazolinium ion 중간체에 대한 기여를 잃기 때문에, 이미 활성화된 형태인 합성 glycan oxazoline donor를 외부에서 공급하면 GlcNAc-acceptor (탈당화된 항체의 core GlcNAc-Asn297)에 대한 transglycosylation은 가능하나, 생성된 product (천연 glycoform)에 대한 재가수분해는 일어나지 않는다 (Source: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2640449/, pub date: 2009-02).

### A.1.3 반응 조건 및 수율
- **기질:** EndoS2 wild-type으로 천연 항체를 처리하여 Fc-(Fucα1,6)GlcNAc-IgG (GlcNAc-Fc) acceptor 생성 후, EndoS2-D184M + 합성 glycan oxazoline donor로 두 번째 단계 진행 (Source: https://pmc.ncbi.nlm.nih.gov/articles/PMC5837956/, pub date: 2018-03-09).
- **반응 시간:** D184M는 10분 이내에 glycan transfer 완결 가능. D184Q보다 훨씬 효율적 (Source: https://pmc.ncbi.nlm.nih.gov/articles/PMC4974367/, pub date: 2016-07-13).
- **수율:** Herceptin 대상 S2G2F (sialylated biantennary, fucosylated) glycoform 형성 시 거의 정량적 (>95%) 전환 보고. Glycan oxazoline 당량을 늘리면 완전 전환 가능 (Source: https://pmc.ncbi.nlm.nih.gov/articles/PMC5837956/, pub date: 2018-03-09).
- **donor 당량:** EndoSz-D234M (비교 enzyme)은 G2S2 20 eq, 20 분; EndoS-D233M는 G2S2 40 eq, 50 분 필요 — EndoS2-D184M은 이 둘 사이로 추정 (Source: https://pmc.ncbi.nlm.nih.gov/articles/PMC11200250/, pub date: 2024-06-13).
- **Acceptor 호환성:** core-fucosylated GlcNAc-Fc 및 non-fucosylated GlcNAc-Fc 모두에 효율적으로 작용 (Source: https://pmc.ncbi.nlm.nih.gov/articles/PMC4974367/, pub date: 2016-07-13).

---

## A.2 기술 성숙도 (TRL)

**종합 평가: TRL 7-8 (상업 도입 진행 중, 일부 GMP 공급 확립)** [추정]

| 근거 | TRL 수준 | 비고 |
|------|---------|------|
| Wang lab 2016 *JACS* 최초 보고, 다수 후속 논문 | TRL 4-5 (기초/응용 검증) | (Source: PMC4974367) |
| Genovis의 GlycINATOR (EndoS2 wild-type), TransGLYCIT (glycosynthase) 상용 제품화 | TRL 8 (분석/연구급 상용) | (Source: https://www.genovis.com/smartenzymes/applications/transglycosylation-of-igg/, pub date: 미확인) |
| Synaffix/Lonza GlycoConnect® — engineered endoglycosidase + glycosyltransferase 기반 ADC 임상 진입 | TRL 7-8 | DS9606 phase 1 (NCT05394675), 40명 환자 투여, 4명 PR (Source: https://pmc.ncbi.nlm.nih.gov/articles/PMC11575643/, pub date: 2024-11-15) |
| ProBioGen GlymaxX (경쟁: cell-line 기반) phase 3 임상 진입 | 비교 기준 — TRL 8-9 | (Source: https://www.biotechnewswire.ai/202112172302/, pub date: 2021-12-17) |
| Genovis 2026년 3월 ADC용 EndoS2 비독점 라이선스 체결 (US biotech), 프로그램당 약 USD 20M 마일스톤 | TRL 7-8 상업화 가시화 | (Source: https://investor.genovis.com/en/mfn_news/genovis-enters-non-exclusive-license-agreement-for-endos2-enzyme-technology-for-antibody-drug-conjugate-adc-development-and-commercialization/, pub date: 2026-03) |
| JNKN003 (chemoenzymatic ADC) phase 3 진입 (2023-12), ORR 56.3% | TRL 8 (해당 ADC 한정) | (Source: PMC11575643) |

EndoS2-D184M 자체는 분석시약(GMP-grade enzyme)으로 상업 공급이 이미 진행 중이며 (Genovis), ADC 등 의약품 응용은 임상 1-3상 단계의 자산이 다수 존재한다. 다만 EndoS2 glycosynthase로 remodeling된 항체 자체가 FDA/EMA 승인된 사례는 [미확인].

---

## A.3 기술적 난제 및 한계

### A.3.1 Glycan oxazoline donor 공급/비용
- 활성화 glycan oxazoline은 SGP(sialylglycopeptide, egg yolk 유래)로부터 enzymatic trimming 및 chemical oxazoline 활성화를 거쳐 합성한다. 250 g egg yolk powder에서 약 200 mg SGP 회수 가능 — gram-scale 가능하지만 ADC GMP 생산에는 부족 (Source: https://www.ncbi.nlm.nih.gov/pubmed/25124522, pub date: 2014-08-10).
- One-pot으로 free sialoglycan을 functionalized glycan oxazoline으로 직접 전환하는 방법이 2021년 보고되었으나, 합성 sialyl/fucosyl donor의 cGMP-급 공급망은 아직 제한적 (Source: https://pmc.ncbi.nlm.nih.gov/articles/PMC8857982/, pub date: 2021-08-05).
- 비대칭(asymmetric), tri-/tetra-antennary, sialyl-fucosyl-bisecting 등 복잡 glycoform donor의 합성 비용은 mg당 수천 USD 수준 [추정] — 대량 ADC 공정에 부담.

### A.3.2 제품 가수분해(byproduct hydrolysis) 잔류 위험
- D184M은 hydrolysis가 "marginal"하지만 완전 0은 아님. 장기 반응이나 고온 조건에서 잔류 가수분해가 product yield 손실 유발 가능 (Source: PMC4974367, 2016-07-13).
- D184C는 transglycosylation 활성은 더 높지만 cysteine의 자유 thiol 때문에 산화/dimer 형성 우려로 GMP에 부적합 [추정].

### A.3.3 반응 재현성 및 스케일업
- EndoS2-D184M 촉매 반응은 batch-to-batch 변동성이 보고됨 — single 반응으로 완결되기도 하나, 추가 enzyme/oxazoline이 필요한 경우도 존재 (Source: https://www.frontiersin.org/journals/catalysis/articles/10.3389/fctls.2021.810779/full, pub date: 2022-01-20).
- 대규모 chemoenzymatic glycoengineering 성공 사례 보고는 small scale에 한정. 100+ g 스케일 GMP 공정 데이터 [미확인].

### A.3.4 항체 안정성
- EndoS2 wild-type에 의한 deglycosylation 단계에서 Fc 변성 위험. 일반적으로 pH 7.0-7.5, 25-37°C 조건에서 항체 안정성 유지 가능하나 일부 IgG4/sub-class에서 aggregation 위험 [추정].
- Aglycosylated intermediate (GlcNAc-Fc)는 unfolding/thermal stability 감소 가능성 — 빠른 reglycosylation 필요.

### A.3.5 Donor library 한계
- EndoS2-D184M의 acceptor pocket이 비교적 큰 편이지만, 비전형 glycan(예: O-acetylated sialic acid, Lewis X/Y 함유 항원 mimetic)에 대해서는 전이 효율 저하 [추정].
- LacNAc-based donor 모두 활성 — broad scope이나, 매우 큰 functional payload-conjugated donor는 trasferase activity 감소 가능 (Source: https://patents.google.com/patent/US11008601B2/en).

### A.3.6 규제·특성 분석 도전
- FDA/EMA는 glycoform 단위 batch-to-batch 일관성, functional bioassay 상관성, 미시·거시 heterogeneity 정량을 요구 (Source: https://cbs.crystalpharmatech.com/news-and-events/antibody-glycosylation-characterization-and-fda-requirements, pub date: 미확인).
- Remodeling 후 잔류 GlcNAc-Fc(미반응), wild-type EndoS2 잔류 enzyme, oxazoline 부산물 등 process-related impurity가 새로 발생. CDER FDA Grand Rounds 2026 보고 — 209개 승인 항체의 glycan profile benchmark 작업 진행 중 (Source: https://www.fda.gov/drugs/regulatory-science-action/novel-method-rapid-glycan-profiling-therapeutic-monoclonal-antibodies, pub date: 미확인).

---

## A.4 대체/경쟁 기술 비교

| 기술 | 출처/소유자 | 기질 범위 | 대표 변이/조건 | 효율(T/H) | 임상/상용 단계 | IP 현황 |
|------|------------|----------|---------------|----------|---------------|---------|
| **EndoS2 glycosynthase (D184M/Q)** | Wang lab (UMd) / Genovis license | Complex, HM, hybrid, biantennary; core-Fuc 무관 | D184M, 10분 완결 | 매우 높음 (residual hydrolysis 미미) | TRL 7-8, Genovis 상용, ADC 라이선스 다수 | US11008601B2 외 다수 (UMd) |
| **EndoS glycosynthase (D233M/Q)** | Wang/Davis lab / Tarentis 등 | Biantennary complex only | D233M, 50분, G2S2 40eq | 중상 (D233M = D233Q의 7-8x) | TRL 6-7 | Genovis license, Synaffix 사용 |
| **EndoSz-D234M** | Academia Sinica 2024 | Biantennary CT; sialylated | D234M, 20분, G2S2 20eq | EndoS-D233M 대비 우수 | TRL 5 (학술 단계) | (Source: PMC11200250, 2024-06-13) |
| **EndoF3-D165A/Q** | Wang lab | Core-fucosylated tri-antennary CT; Fab N-glycan에도 작용 | D165A/Q | 중간 | TRL 4-5 | (Source: PMC4861498) |
| **Endo-M (Mucor hiemalis)** | Yamamoto, Tokyo Univ. of Pharm | HM, hybrid; CT는 약함 | N175Q 등 | 중간 | TRL 5 (분석 reagent) | Asahi Glycoworks 등 |
| **Endo-CC (Coprinopsis cinerea)** | Tokyo Univ. Agri / 일본 그룹 | IgE 등 비-IgG에도 효율적 | N180H | 중하 | TRL 4 | [미확인] |
| **Endo-Om (Ogataea minuta)** | 일본 yeast 유래 | [미확인] | [미확인] | [미확인] | TRL 3-4 [추정] | [미확인] |
| **GlymaxX (cell-line afucosylation)** | ProBioGen | CHO 발현계에서 RMD 도입으로 afucosylation | 유전자 도입 | 전체적 afucosylation (>90%) | TRL 9 (phase 3 임상 다수) | ProBioGen 독점 |
| **Potelligent (FUT8 KO)** | Kyowa Hakko Kirin / BioWa | CHO FUT8 KO → afucosyl IgG | KO | >95% afucosyl | TRL 9 (mogamulizumab 승인) | BioWa license |
| **GlycoConnect (Synaffix/Lonza)** | Synaffix (Lonza acquired 2023) | Engineered endoglycosidase + glycosyltransferase로 6-azidoGalNAc 도입 | 두-효소 one-pot + click | 균질 ADC | TRL 7-8, 다수 임상 라이선스 | Synaffix 독점 |
| **GlycoFi (Pichia 변형)** | Merck (acquired) | Yeast humanized N-glycan pathway | 유전자 도입 | >90% homogeneity | TRL 8-9 | Merck 독점 |
| **Chemical 합성 glycan** | Various academic | 전합성 by Boons, Wong | N/A | mg-g 스케일 한정 | TRL 3-4 | 다수 패밀리 |

**핵심 비교 결론:**
- **EndoS2-D184M의 가장 큰 차별점은 (1) HM/hybrid/CT 모두 처리 가능한 broad substrate scope, (2) 잔류 가수분해가 미미하여 product yield 우수, (3) core-fucosylated/non-fucosylated 모두 호환.** EndoS-D233M보다 효율이 높고 EndoF3보다 acceptor 범위가 넓다 (Source: PMC4974367).
- **Cell-line 기반(Potelligent/GlymaxX)은 임상 성숙도가 가장 높지만, glycoform이 단일 변경(afucosylation)에 국한.** EndoS2 chemoenzymatic은 sialylation, asymmetric glycan 등 다양한 site-specific design 가능하나 비용·스케일 측면에서 더 도전적.

---

## A.5 기술 발전 로드맵 (2024-2026 최신 동향)

### A.5.1 새로운 glycosynthase 발굴 (2024)
- **EndoSz-D234M** (*Streptococcus equi* subsp. *zooepidemicus* Sz105 유래) — 2024년 *JACS Au* 보고. D234M 변이로 EndoS-D233M 대비 G2S2 donor 당량 절반(20 eq), 반응 시간 절반(20분)으로 동등 수율 달성. Herceptin, Perjeta, Erbitux, Rituxan, Humira, Keytruda, Bavencio 등 10개 mAb에 적용. 결과적으로 mAb-G2S2가 ADCC를 3-26배 강화 (Source: https://pubs.acs.org/doi/10.1021/jacsau.4c00004, pub date: 2024-06-13).

### A.5.2 One-pot 및 immobilized reactor
- Microbial transglutaminase(MTG)를 이용해 Q-tag 부착된 EndoS2-WT 및 D184M을 agarose에 site-specific 고정화하여 one-pot deglycosylation-reglycosylation 흐름 구축. 1-2시간 ambient 온도에서 균질 항체 생산 (Source: https://pmc.ncbi.nlm.nih.gov/articles/PMC5837956/, pub date: 2018-03-09).
- CBD(cellulose-binding domain) fusion EndoS — 80-90% loading efficiency로 one-step 정제 및 immobilization (Source: https://www.sciencedirect.com/science/article/abs/pii/S004520681930080X).

### A.5.3 ADC 임상 진입 (2024-2025)
- **DS9606** (anti-claudin-6 + pyrrolodiazepine) — chemoenzymatic glycan remodeling 기반. Phase 1 (NCT05394675) 40명 환자, 4명 PR. 2024년 9월 데이터 공개 (Source: https://pmc.ncbi.nlm.nih.gov/articles/PMC11575643/, pub date: 2024-11-15).
- **JNKN003** — 2023년 12월 phase 3 진입, ORR 56.3%, DCR 90.6% (Source: PMC11575643).
- **JSKN016** (Alphamab anti-TROP2/HER3 bispecific ADC) — 2024 초 phase 1 진입 (Source: PMC11575643).
- Synaffix/Lonza — 2025년 9월 Qurient와 dual-payload ADC 라이선스, Sidewinder Therapeutics와 bispecific ADC multi-target license (Source: https://www.prnewswire.com/news-releases/lonzas-synaffix-collaborates-with-qurient-therapeutics-to-enable-development-of-dual-payload-adc-302566442.html, pub date: 2025-09).
- Genovis — 2026년 3월 US biotech와 EndoS2 비독점 ADC 라이선스, 프로그램당 약 USD 20M 마일스톤 (Source: https://investor.genovis.com/en/mfn_news/genovis-enters-non-exclusive-license-agreement-for-endos2-enzyme-technology-for-antibody-drug-conjugate-adc-development-and-commercialization/, pub date: 2026-03).

### A.5.4 Donor scope 확장 및 AI 효소 설계
- Functionalized azido/alkyne-bearing glycan oxazoline의 one-pot 합성 (2021): GlycoConnect-like 6-azidoGalNAc, 그 외 sialyl-biantennary 등 (Source: PMC8857982).
- AI 기반 효소 설계 (de novo / directed evolution): 2025년 *ScienceDirect* "From traditional to AI-driven" 리뷰 — ML로 fitness landscape을 모델링하여 directed evolution 가속화. EndoS2 자체에 적용된 AI 설계 발표는 [미확인] (Source: https://www.sciencedirect.com/science/article/abs/pii/S0734975025002745, pub date: 2025).
- Click-chemistry enabled directed evolution of glycosynthases — 2020 bioRxiv 등 방법론 정립 (Source: https://www.biorxiv.org/content/10.1101/2020.03.23.001982.full.pdf).

### A.5.5 종합 IgG glycoengineering 리뷰 (2024-2025)
- *RSC Medicinal Chemistry* (2025): "Technical, preclinical, and clinical developments of Fc-glycan-specific antibody–drug conjugates" — Fc N-glycan을 anchor로 활용한 site-specific ADC의 균질성, 친수성, PK, therapeutic index 개선 (Source: https://pubs.rsc.org/en/content/articlehtml/2025/md/d4md00637b, pub date: 2025).
- PNAS 2025: cell-based 방법으로 Fc-GlcNAc 및 Fc-SCT-enriched 항체 생산, ADCC/CDC 향상 (Source: https://www.pnas.org/doi/10.1073/pnas.2423853122, pub date: 2025-02).

---

## A.6 핵심 요소기술 및 공급망

### A.6.1 효소(Enzyme) 공급
| 공급사 | 제품 | 등급/용도 | 비고 |
|--------|------|----------|------|
| **Genovis (스웨덴)** | GlycINATOR (EndoS2 WT), TransGLYCIT (glycosynthase 키트), GlycINATOR Immobilized | research → GMP-equivalent | ADC용 비독점 라이선스 체결 (2026-03). 최대 USD 20M/program (Source: Genovis IR) |
| **New England Biolabs (NEB)** | EndoS2 (Remove-iT)... | research grade | (Source: 미확인 — 일부 EndoS 변종만 카탈로그 명시) |
| **MedChemExpress** | EndoS2 catalyzing enzyme | research grade | (Source: https://www.medchemexpress.com/endo-%CE%B2-n-acetylglucosaminidase-endo-s2.html) |
| **Asahi Glycoworks (Asahi Kasei)** | Endo-M 계열 enzyme | research/manufacturing | (Source: 미확인) |
| **Ludger** | analytical 효소 / glycan standards | analytical | (Source: 미확인) |

### A.6.2 Glycan oxazoline donor 공급
- **출발물질 SGP(sialylglycopeptide):** Tokyo Chemical Industry (TCI), Fushimi Pharmaceutical (일본) 등에서 상용 (Source: https://pubs.rsc.org/en/content/articlehtml/2022/ob/d2ob00615d).
- **Custom oxazoline 합성:** Sussex Research (캐나다), Synthose, OmegaChem, BOC Sciences 등이 mg-g 스케일 custom 합성 [추정].
- **공급 위험:** Sialyl-biantennary-fucosyl-bisecting 등 복잡 donor는 ad-hoc 합성에 의존, GMP-grade 단일 공급원이 부재 (single-source risk 높음). Egg yolk 원료 SGP는 가축 식품·전염병 영향을 받을 수 있어 supply chain 다변화 필요 [추정].

### A.6.3 효소 재조합 발현
- 대부분 E. coli (BL21 등) 기반 발현, 약 40-50 mg/L 수율 (Source: ScienceDirect S004520681930080X).
- High-density fed-batch 발현 데이터 [미확인]. CMC를 위한 host-cell protein, endotoxin 제거 등 downstream은 표준 mAb 공정과 별도 최적화 필요.

### A.6.4 IP 풍경
- **University of Maryland (Lai-Xi Wang):** US11008601B2, WO2017124084A1 — EndoS2 D184M/Q glycosynthase 변이 (Source: https://patents.google.com/patent/US11008601B2/en).
- **Synaffix (Lonza):** GlycoConnect 관련 패밀리 다수.
- **ProBioGen:** GlymaxX cell-line 기술 패밀리.
- **WO2022226420A2:** Fc glycan remodeling platform for site-specific ADC conjugation (Source: https://patents.google.com/patent/WO2022226420A2/en).

### A.6.5 단일 공급원 의존성 및 위험
- **효소:** Genovis가 EndoS2 ADC-grade 시장 사실상 단일 공급원 [추정]. 비독점 라이선스 모델이라 다수 licensee 가능하지만, enzyme 자체 GMP 생산은 Genovis 의존.
- **Donor:** 일본의 SGP 추출 인프라(TCI, Fushimi 등) 의존도 높음. 미국·유럽 GMP 등급 donor 합성 능력 [미확인]/제한적 [추정].
- **IP:** Wang/UMd 기반 패밀리가 핵심 — 라이선스 필요. EndoSz-D234M 등 새로운 enzyme은 IP 회피 가능성 있으나 검증 필요.

---

## 핵심 출처 목록

1. Li T, Tong X, Yang Q, Giddens JP, Wang L-X. *Glycosynthase Mutants of Endoglycosidase S2 Show Potent Transglycosylation Activity and Remarkably Relaxed Substrate Specificity for Antibody Glycosylation Remodeling.* J Biol Chem 2016. https://pmc.ncbi.nlm.nih.gov/articles/PMC4974367/ (pub date: 2016-07-13)
2. Sjögren J, Cosgrave EFJ, Allhorn M, et al. *EndoS and EndoS2 hydrolyze Fc-glycans on therapeutic antibodies with different glycoform selectivity.* Glycobiology 2015. https://academic.oup.com/glycob/article/25/10/1053/1988622 (pub date: 2015-05-21)
3. Klontz EH, et al. *Molecular Basis of Broad Spectrum N-Glycan Specificity and Processing of Therapeutic IgG mAbs by Endoglycosidase S2.* ACS Cent Sci 2019. https://pubs.acs.org/doi/10.1021/acscentsci.8b00917 (pub date: 2019-04-03)
4. Trastoy B, et al. *The IgG-specific endoglycosidases EndoS and EndoS2 are distinguished by conformation and antibody recognition.* J Biol Chem 2024. https://www.jbc.org/article/S0021-9258(24)01742-3/fulltext (pub date: 2024-05-03)
5. Sjögren J, et al. *EndoS2 is a unique and conserved enzyme of serotype M49 group A Streptococcus.* Biochem J 2013. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3778708/ (pub date: 2013-09-23)
6. Lu Y-C, et al. *Structure-Based High-Efficiency Homogeneous Antibody Platform by Endoglycosidase Sz.* JACS Au 2024. https://pubs.acs.org/doi/10.1021/jacsau.4c00004 (pub date: 2024-06-13)
7. Wang L-X et al. *US Patent 11,008,601B2 — Endo-S2 mutants as glycosynthases.* https://patents.google.com/patent/US11008601B2/en
8. Manabe S, et al. *Site-specific immobilization of endoglycosidases for streamlined chemoenzymatic glycan remodeling of antibodies.* Bioconjug Chem 2018. https://pmc.ncbi.nlm.nih.gov/articles/PMC5837956/ (pub date: 2018-03-09)
9. *Technical, preclinical, and clinical developments of Fc-glycan-specific antibody–drug conjugates.* RSC Med Chem 2025. https://pubs.rsc.org/en/content/articlehtml/2025/md/d4md00637b ; PMC: https://pmc.ncbi.nlm.nih.gov/articles/PMC11575643/ (pub date: 2024-11-15)
10. van Geel R, et al. *Enzymatic glycan remodeling–metal free click (GlycoConnect™).* MAbs 2022. https://www.tandfonline.com/doi/full/10.1080/19420862.2022.2078466 (pub date: 2022-06-02)
11. Liu C-P, et al. *One-Pot Conversion of Free Sialoglycans to Functionalized Glycan Oxazolines and Efficient Synthesis of Homogeneous ADCs.* Bioconjug Chem 2021. https://pmc.ncbi.nlm.nih.gov/articles/PMC8857982/ (pub date: 2021-08-05)
12. Liu L, Prudden AR, Bosman GP, Boons G-J. *A simplified procedure for gram-scale production of sialylglycopeptide (SGP) from egg yolks.* Carbohydr Res 2014. https://pubmed.ncbi.nlm.nih.gov/25124522/ (pub date: 2014-08-10)
13. Genovis Investor Relations. *Genovis Enters Non-Exclusive License Agreement for EndoS2 Enzyme Technology for ADC Development.* https://investor.genovis.com/en/mfn_news/genovis-enters-non-exclusive-license-agreement-for-endos2-enzyme-technology-for-antibody-drug-conjugate-adc-development-and-commercialization/ (pub date: 2026-03)
14. Genovis product page: TransGLYCIT (Glycan Remodeling Technology). https://www.genovis.com/products/glycan-remodeling-technology/transglycit/
15. *Challenges and Opportunities for the Large-Scale Chemoenzymatic Glycoengineering of Therapeutic N-Glycosylated mAbs.* Front Catal 2022. https://www.frontiersin.org/journals/catalysis/articles/10.3389/fctls.2021.810779/full (pub date: 2022-01-20)
16. Giddens JP, et al. *Endo-F3 Glycosynthase Mutants Enable Chemoenzymatic Synthesis of Core-fucosylated Triantennary Complex Type Glycopeptides/Glycoproteins.* J Biol Chem 2016. https://pmc.ncbi.nlm.nih.gov/articles/PMC4861498/ (pub date: 2016-03-11)
17. ProBioGen GlymaxX product page. https://www.probiogen.de/genetic-glyco-engineering-adcc-glymaxx.html (pub date: 미확인)
18. Lonza/Synaffix–Qurient dual-payload ADC collaboration. https://www.prnewswire.com/news-releases/lonzas-synaffix-collaborates-with-qurient-therapeutics-to-enable-development-of-dual-payload-adc-302566442.html (pub date: 2025-09)
19. Tong X, et al. *Generation and Comparative Kinetic Analysis of New Glycosynthase Mutants from S. pyogenes Endoglycosidases for Antibody Glycoengineering.* mBio 2018. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6202118/ (pub date: 2018-10-23)
20. WO2022226420A2 — Fc glycan remodeling platform for site-specific antibody conjugation. https://patents.google.com/patent/WO2022226420A2/en

---

*[추정] 또는 [미확인] 표기는 신뢰성 확보를 위해 2차 검증을 권장함.*
