# [F] 리스크 및 규제 분석

> 대상기술: **EndoS2 Glycosynthase Mutant** (Fc N-glycan 효소적 리모델링 플랫폼)
> 작성일: 2026-05-21
> 본 보고서는 치료용 항체/ADC의 Fc 글리칸을 EndoS2 변이체(예: D184M, D184Q)로 균질화하는 chemoenzymatic 리모델링 플랫폼에 대한 규제·CMC·정책·지정학·ESG·면역원성 리스크를 분석한다.

---

## F.1 규제 환경 및 인증 요건

### F.1.1 글리칸 특성분석에 대한 기본 규제 프레임워크
- **ICH Q6B (Specifications)** 및 **ICH Q5E (Comparability)** 가 글리칸 분석의 기본 골격. FDA·EMA·PMDA·NMPA 모두 탄수화물 함량, oligosaccharide profile, glycosylation site occupancy 특성분석을 요구 (EMA, ICH Q6B Scientific guideline; FDA Q6B Guidance) [확인].
- EMA는 추가적으로 **sialylation, galactosylation, mannosylation, fucosylation** 수준을 별도로 모니터링하도록 요구 (BioPharm International, "Review of Glycan Analysis Requirements") [확인].
- 2026년 FDA Grand Rounds에서 CDER 과학자가 발표한 벤치마크에 따르면, 2025년 5월 기준 FDA가 승인한 209개 치료용 항체 중 123개의 CHO 생산 항체에서 상위 10개 글리코폼이 총 글리칸의 99% 이상을 차지하며, **G0F/G1F/G2F**가 지배적 (Crystal Pharmatech, "FDA requirements and Characterization") [확인]. → EndoS2 리모델링으로 생성되는 균질 글리코폼이 이 분포에서 크게 벗어날 경우, 비교성·면역원성 추가 입증 필요.

### F.1.2 효소 리모델링 항체의 규제 선례
- 2026년 5월 현재, EndoS2 glycosynthase 변이체를 사용한 **FDA 승인 의약품은 없음** [확인]. 다만 글리코엔지니어링 항체 자체는 다수 승인됨: **Benralizumab(Fasenra), Obinutuzumab(Gazyva), Tafasitamab(Monjuvi), Inebilizumab(Uplizna), Margenza, Epcoritamab** (Biointron, "January 2025: Antibody Glycoengineering") [확인]. 이들은 대부분 **세포주 수준 글리코엔지니어링**(FUT8 KO, GlymaxX 등)이며 효소적 in vitro 리모델링은 아님.
- **Daiichi Sankyo**는 GlycoT Therapeutics(메릴랜드대 Lai-Xi Wang lab 스핀오프)의 효소적 글리코엔지니어링 기술을 2020년 9월 sublicense (PR Newswire) [확인]. Enhertu/Datroway 등 Daiichi의 승인 ADC에 EndoS2 기반 공정이 적용되었는지는 공개되지 않음 [미확인].
- 가장 가까운 임상 선례는 **Hansa Biopharma의 imlifidase (IdeS, Streptococcus pyogenes 기원 IgG cleaving enzyme)**: EU/UK/노르웨이/호주/스위스에서 조건부 승인되어 IDEFIRIX로 판매, 2025년 ConfIdeS Phase 3 성공 및 BLA submission (Hansa Biopharma press releases, 2025) [확인]. EndoS2와 동일한 *S. pyogenes* 기원이라는 점에서 면역원성 프로파일에 대한 가장 직접적 선례 [추정].

### F.1.3 잔류 효소 및 도너 임퓨리티 규제 접근
- 잔류 EndoS2: ICH Q6B 및 USP <1132>에 따라 **잔류 HCP/공정 효소를 1–100 ppm 수준**의 ELISA 명세로 관리. 효소 활성이 잔존할 경우 medication-induced glycan stripping이 발생할 수 있어 ppm이 아닌 **picogram 수준의 활성 기반 시험**이 별도로 요구될 가능성 (Frontiers in Catalysis 2021, "Large-Scale Chemoenzymatic Glycoengineering") [확인].
- 합성 글리칸-옥사졸린 도너: **ICH M7** (잠재적 변이원성 임퓨리티) 및 **ICH Q3A/B**(원료/제품 임퓨리티) 적용 대상. 옥사졸린 모이어티는 수분에 의해 가수분해되므로 도너 합성 부산물(부분가수분해체, 보호기 잔류) 특성분석이 필요 [확인].

### F.1.4 바이오시밀러 비교성 영향
- 바이오시밀러 신청 시, 효소적 리모델링이 도입되면 ICH Q5E의 "comparability"보다 **신규 제조공정/신규 활성성분에 준하는 분석**이 요구될 가능성이 큼 [추정]. EMA의 2025년 4월 "Reflection paper on a tailored clinical approach in biosimilar development"는 임상 단순화를 시사하지만 CMC 영역에서는 여전히 엄격 (Clinical Leader, 2025년 EMA draft) [확인].
- PMDA는 infliximab 바이오시밀러 심사에서 afucosylated glycan/high mannose/galactosylation 차이를 명시적으로 검토한 전례 (PMC12185665, 일본 바이오시밀러 특성분석 리뷰) [확인] → 효소 리모델링 제품도 동일한 정밀도로 심사 예상.

---

## F.2 CMC / 품질 관리 요건

### F.2.1 글리칸 분석 (필수 패널)
| 분석법 | 용도 | 채택률/규제 기대 |
|---|---|---|
| HILIC-FLR (2-AB labeling) | Released glycan profiling | FDA BLA 약 78% 채택 [확인] |
| HILIC-MS / LC-MS/MS | Glycoform identification, intact mass | EMA/FDA 표준 |
| Capillary Electrophoresis (CE-LIF) | Glycan QC release | ICH Q6B 권고 |
| Peptide mapping (glycopeptide LC-MS) | Site occupancy & site-specific glycoform | 필수 |
| Functional bioassay (ADCC, FcγRIIIa SPR) | 활성 상관 | EMA 명시적 요구 [확인] |

### F.2.2 잔류 EndoS2 통제
- **HCP-ELISA**(전체 HCP 1–100 ppm) + **anti-EndoS2 specific ELISA**(특정 효소 ppm 모니터링) 이중 통제 필요 [추정].
- 활성 잔류 효소(picogram 단위)는 **stability 동안 항체 글리칸 분해 위험**을 야기. 선례: residual hexosaminidase B가 mAb stability 중 N-glycan 분해 (PMC8365702) [확인].
- LC-MS/MS 기반 HCP identification으로 EndoS2 동정 + 충진 전 enzymatic activity assay (예: fluorescent glycan substrate hydrolysis) 필요.

### F.2.3 글리칸-옥사졸린 도너 임퓨리티
- 도너는 100배 분자몰비로 첨가되므로 **잔류 도너/가수분해체/금속촉매(SnCl₄ 등 보호기 제거 잔재)** 모니터링 필요 (Frontiers in Catalysis 2021) [확인].
- 잔류 도너의 alpha-Gal 또는 비인간 시알산(Neu5Gc) 함유 여부는 면역원성 직결 → ICH Q6B 글리칸 ID 시험에 alpha-Gal/Neu5Gc 항목 추가 권고 [추정].

### F.2.4 효소 생산 시 미생물 유래 리스크
- EndoS2는 *E. coli* 등 미생물 발현이 통상적 → **endotoxin (LAL/rFC)**, **bioburden**, **mycoplasma** 추가 통제. USP/EP/JP pharmacopoeial 한계 충족 필수 (Bioprocessing Safety Essentials 2025) [확인].
- 효소 자체가 final drug substance가 아닌 가공보조제(processing aid)로 분류될 가능성이 높으며, 이 경우 GMP 등급 효소를 ancillary material로 cGMP 공급망에서 조달 필요 [추정].

---

## F.3 정책·보조금 동향 (US/EU/Asia)

### F.3.1 미국 — BIOSECURE Act
- **FY2026 NDAA**에 BIOSECURE Act 편입, 2025년 12월 18일 대통령 서명으로 발효 (Fierce Pharma; GT Insights, 2025-11) [확인]. BGI/MGI Tech는 지정, WuXi 계열은 NDAA 최종본에서 명시 제외되었으나 OMB가 1년 내 공식 "companies of concern" 리스트 공표 의무.
- ADC/glycoengineering 측면 영향: 미국 기업 49%가 중국 CDMO 의존도 낮추겠다고 응답 (Fierce Pharma 설문). **5년 transition period** 부여. 인도 CDMO 및 한국 송도(삼성바이오로직스 등)가 대체 거점으로 부상 (Labiotech; Seoulz Korea K-Bio CDMO 2026) [확인].
- EndoS2 리모델링은 **추가 가공 단계**가 있어, 중국 CDMO에서 항체 drug substance 생산 후 미국/EU에서 효소 리모델링하는 **bifurcated supply chain** 설계가 가능 → BIOSECURE 영향 부분 완화 [추정].

### F.3.2 미국 — IRA (Inflation Reduction Act)
- 2026년 1월 첫 협상가격 발효, list price 38–79% 할인 (PMC12661528; CRS R47872) [확인].
- 11–13년차 가격협상 진입 시점에 Fc-engineered 프리미엄 항체는 가격 압박. 다만 바이오시밀러 출시 평균 18년이라는 시간 차이로 인해 **innovator는 IRA 협상 압력, biosimilar는 진입 지연** 동시 직면.
- EndoS2 리모델링 제품은 "기존 항체의 next-gen lifecycle management" 전략으로 활용 가능하나, IRA가 "단순한 제형 변경 같은 신제품화"를 견제하는 방향이므로 임상적 차별화 입증 부담 [추정].

### F.3.3 EU — Biotech Act & Pharma Package
- 2025년 12월 16일 European Commission이 **EU Biotech Act** 공식 제안. 2026년 말~2027년 채택 예상, 2027–2028년 시행 (White & Case; Inside EU Life Sciences) [확인].
- 핵심: biomanufacturing cluster, advanced therapy centers of excellence, **EU 내 제조역량 확보 의무화**(공급망 자율성). EIB 협력 Health Biotech Investment Pilot 가동.
- EndoS2 플랫폼 보유 기업은 EU 클러스터 입점 시 보조금/세제 혜택 수혜 가능 [추정].

### F.3.4 한국 — K-Bio CDMO Act, 송도 ADC 클러스터
- **MFDS**가 2026년 말까지 "CDMO 규제지원 특별법" 시행 예정 (KBR, 2025) [확인]. ADC 제조운영표준 별도 수립 명시.
- 삼성바이오로직스 송도 2,487억 원 부지 확보(ADC·항체백신·펩타이드·세포유전자치료제) (Seoulz, 2026) [확인]. EndoS2 같은 효소 리모델링은 ADC payload 부착 전 단계로 통합 가능.
- K-Biopharma Next Bridge 프로그램 — R&D, 상업화 컨설팅, 해외 액셀러레이터 입주 지원.

### F.3.5 일본 — PMDA, AMED
- PMDA는 ICH 정합성 높고 글리칸 비교 심사에 경험 풍부 (infliximab 바이오시밀러 사례) [확인].
- AMED의 첨단 modalities 지원 트렌드는 ADC/Fc 엔지니어링에 우호적 [추정].

### F.3.6 중국 — NMPA
- 2025년 NMPA 289개 NDA 승인, 자국 ADC(Kelun-Biotech SKB105 등) IND 활발 (BioSpace, Nature 2026 NMPA review) [확인]. ICH 가입 후 글로벌 정합 강화.

---

## F.4 지정학적 리스크

| 리스크 영역 | 내용 | 평가 |
|---|---|---|
| **탄수화물 chemistry 공급망** | 글리칸-옥사졸린 도너의 carbohydrate building block(SCT, sialyl complex 등) 합성은 다수가 중국/일본 carbohydrate 회사에 집중 [추정]. BIOSECURE 직접 대상은 아니나 export control 확장 가능성 | 중 |
| **EndoS2 효소 공급** | 학술적 라이선스는 메릴랜드대(Lai-Xi Wang) 중심. 상업 GMP 등급 효소 공급사 한정 (Genovis, GlycoT, Synaffix 등) | 중 |
| **항체 drug substance** | WuXi Biologics 등 중국 CDMO 의존 시 BIOSECURE 영향 | 상 (2027–2030 transition) |
| **US-China 디커플링** | 임상 데이터 상호 수용 약화 시 글로벌 임상 비용 상승 | 중 |
| **EU 자율성 강화** | EU Biotech Act가 EU 내 제조 보조금 + 비EU 의존도 축소 → 멀티 사이트 제조전략 필요 | 중 |

---

## F.5 ESG / 환경 이슈

- **단일사용(SUB) 플라스틱 폐기물**: 글로벌 바이오프로세싱이 연간 수백 톤 플라스틱 폐기 (BioProcess International, "Green Imperative Part Two") [확인]. EndoS2 리모델링은 별도의 reactor step을 추가하므로 SUB 폐기물 추가 발생.
- **재활용 솔루션**: Thermo Fisher DynaDrive bio-based film (net-negative carbon), Sartorius/Cytiva 재활용 프로그램 [확인].
- **미생물 효소 생산의 지속가능성**: *E. coli* 발효는 CHO 대비 자원 효율 우수 (배양시간↓, 배지 단순). 단, IPTG 등 inducer 폐수 처리 필요 [추정].
- **Animal-free claims**: EndoS2 변이체 + 합성 글리칸 도너는 동물 유래 성분 zero 청구 가능 → ESG 마케팅 우위 [확인 가능].
- EU 규제 흐름이 환경 책임 강화 방향이므로 향후 ESG 공시(CSRD) 영향 (European Pharmaceutical Manufacturer, 2025) [확인].

---

## F.6 안전성 및 면역원성 리스크

### F.6.1 잔류 EndoS2에 대한 ADA
- **건강인과 감염자 모두 항-EndoS 항체를 보유** (PMC10818452, "Immunomodulating Enzymes from Streptococcus pyogenes") [확인]. *S. pyogenes*는 광범위 자연감염원이므로 일반 인구에 사전형성 항체 존재.
- 이로 인해:
  - 잔류 effort enzyme이 ppm 수준이라도 **즉시형 과민반응 가능성**.
  - **선제적 ADA** 형성 환자에서 효소 중화 → 제조공정에서 리모델링 효율 변동은 환자 영향 미미하나, 잔류 효소 epitope 노출 시 면역복합체 위험.
- Hansa Biopharma의 **imlifidase** 임상 경험 (5년 follow-up, ESOT 2025 발표): 일회성 투여로 IgG depletion 후 안전성 양호하나, repeat dosing 시 ADA가 효능 감소 야기 (Hansa Biopharma press release, 2025) [확인]. 이는 EndoS2가 in vitro processing aid로만 사용되어 환자에 노출되지 않을 경우 위험을 크게 낮출 수 있음을 시사 [추정].

### F.6.2 비자기 글리코폼에 의한 ADA
- **Alpha-Gal (Galα1-3Gal)**: 인간 anti-Gal 항체가 순환 IgG의 ~1% (PubMed 16266320; ACS Pharm Trans Sci 2025) [확인]. 도너 합성 시 alpha-Gal 잔류 시 cetuximab과 유사한 IgE 매개 hypersensitivity 위험.
- **Neu5Gc** (CMP-Neu5Ac 합성 오류 시): 인간이 보유하지 않는 시알산, ADA/inflammation 위험. EndoS2 자체는 sialic acid를 도입하지 않지만 도너 합성에서 관리 필요 [추정].
- **균일 G0/G0F 글리코폼**: 일부 연구는 균일화가 오히려 ADCC↑, complement↑ 가져와 cytokine release risk 가능성 시사 [추정].

### F.6.3 ADC 결합 시 추가 리스크
- EndoS2로 도입한 azide/click handle을 통해 site-specific conjugation 시, payload-DAR distribution이 균일해져 비특이적 독성 감소가 기대되지만, **새로운 linker 화학 자체의 신규성**이 PK/toxicology 추가 입증 부담을 야기 (Frontiers in Catalysis 2021) [확인].

### F.6.4 바이오시밀러 적용 시 비교성
- EndoS2 리모델링 도입 시 reference product와의 차이를 ICH Q5E에서 정당화하기 어렵고, **별도 신규 BLA로 진행해야 할 가능성** [추정].

---

## F.7 종합 리스크 매트릭스 (가능성 × 영향)

| 리스크 | 가능성 | 영향 | 완화방안 | 출처 |
|---|---|---|---|---|
| 잔류 EndoS2 ppm 미달성·활성 잔존 | 중 | 상 | Affinity tag 제거 정제 + 활성기반 release assay + anti-EndoS2 specific ELISA | PMC8365702 [확인] |
| 사전형성 anti-EndoS 항체에 의한 hypersensitivity | 중 | 상 | 잔류 효소 < 1 ppm + 환자 anti-EndoS screen 옵션 | PMC10818452 [확인] |
| 합성 글리칸-옥사졸린 도너 임퓨리티 (alpha-Gal/Neu5Gc) | 중 | 상 | 도너 ICH M7 평가 + Q6B에 비인간 글리칸 시험 추가 | Frontiers Catalysis 2021 [확인] |
| BIOSECURE Act로 중국 CDMO 단절 | 상 (2027-2030) | 상 | 인도/한국 송도/EU bifurcated supply | Fierce Pharma 2025 [확인] |
| 바이오시밀러 비교성 불승인 (효소공정 차이) | 상 | 중 | Innovator 라이선스 또는 신규 BLA 경로 | EMA Reflection paper 2025 [확인] |
| IRA 가격협상 압력 | 중 | 중 | Lifecycle management + clinical differentiation | CRS R47872 [확인] |
| 도너용 carbohydrate building block 공급 집중 | 중 | 중 | 복수 supplier dual sourcing | 업계 일반 [추정] |
| EU Biotech Act EU-내 제조 요구 | 중 | 중 | EU 클러스터(Ireland, NL) 가공 시설 확보 | White & Case 2025 [확인] |
| SUB 플라스틱 폐기물 ESG 공시 부담 | 상 | 하 | Bio-based film 채택, 재활용 프로그램 가입 | BioProcess Int'l [확인] |
| Endotoxin/mycoplasma 미생물 효소 유래 | 중 | 상 | rFC + 다중 LAL + cGMP 효소 조달 | Bioprocessing Safety 2025 [확인] |
| 균일 글리코폼에 의한 enhanced ADCC → CRS | 하 | 중 | 사전 in vivo PK/Tox, dose escalation | bioRxiv 2025 alpha-gal [추정] |
| Daiichi/Synaffix/GlycoT 등 IP 분쟁 | 중 | 상 | FTO 분석 + 라이선스 사전협상 | USPTO 9434786, 11643450, 12497643 [확인] |

---

## 핵심 출처 목록

1. EMA, *ICH Q6B Specifications: test procedures and acceptance criteria for biotechnological/biological products – Scientific guideline*, ema.europa.eu [확인]
2. FDA, *Q6B Specifications: Test Procedures and Acceptance Criteria for Biotechnological/Biological Products*, fda.gov [확인]
3. Crystal Pharmatech, *Antibody Glycosylation: FDA requirements and Characterization* (2025-2026 benchmark, FDA Grand Rounds 2026 referenced) [확인]
4. Li et al., *Glycosynthase Mutants of Endoglycosidase S2 Show Potent Transglycosylation Activity*, J Biol Chem (PMC4974367) [확인]
5. WO2017124084A1, *Endo-S2 mutants as glycosynthases* (Lai-Xi Wang, U Maryland) [확인]
6. Frontiers in Catalysis (2021), *Challenges and Opportunities for the Large-Scale Chemoenzymatic Glycoengineering of Therapeutic N-Glycosylated mAbs* [확인]
7. Naegeli et al., *Immunomodulating Enzymes from Streptococcus pyogenes*, PMC10818452 (2024) [확인]
8. Hansa Biopharma press releases (2025): ConfIdeS Phase 3 success, FDA BLA submission, ESOT 2025 5-yr follow-up [확인]
9. Fierce Pharma (2025-11), *BIOSECURE Act in FY2026 NDAA*; GT LLP Insights (2025-11) [확인]
10. White & Case / Inside EU Life Sciences (2025-12), *EU Biotech Act proposal* [확인]
11. KBR (2025), *MFDS readies new regulatory regime to propel bio-CDMO global expansion* [확인]
12. Seoulz (2026), *Korea K-Bio CDMO 2026: How BIOSECURE Reshaped Songdo* [확인]
13. Coye et al., *Host Cell Protein Clinical Safety Risk Assessment—An Updated Industry Review*, Biotech Bioeng 2025 (PMC12503010) [확인]
14. USP <1132> *Residual Host Cell Protein Measurement* [확인]
15. EMA (2025-04), *Reflection paper on a tailored clinical approach in biosimilar development* (draft) [확인]
16. CRS R47872, *Medicare Drug Price Negotiation Under the IRA* [확인]
17. PMC12661528 (2025), *Unintended consequences of the IRA on biosimilar market incentives* [확인]
18. BioPharm International, *A Review of Glycan Analysis Requirements* [확인]
19. PMC12185665, *Characterization of Biosimilar mAbs Approved in Japan* (PMDA infliximab review) [확인]
20. ACS Pharmacol Transl Sci (2025), *Chemically Defined Non-human Glycans Comprising Gal-α1-3-Gal Epitopes in Cetuximab Fab* [확인]
21. bioRxiv (2025-12), *Asymmetrical glycoengineering of monoclonal antibodies: new insights in α-gal immunogenicity* [확인]
22. BioProcess International, *The Green Imperative Part Two: Engineering for Sustainability in Single-Use Technologies* [확인]
23. Fishersci Lab Reporter (2025), *Bioprocessing Safety Essentials: Endotoxin, Mycoplasma, and Sterility Testing* [확인]
24. PR Newswire (2020-09), *GlycoT Therapeutics Grants Sublicense to Daiichi Sankyo* [확인]
25. Biointron (2025-01), *Antibody Glycoengineering* — list of approved glycoengineered antibodies [확인]
26. NMPA 2025 approval summary, Nature (2026) [확인]
27. Labiotech, *CDMO industry post BIOSECURE Act: who will take WuXi's place?* [확인]
28. USPTO 9434786, 11643450, 12497643 — chemoenzymatic glycoengineering patents [확인]
