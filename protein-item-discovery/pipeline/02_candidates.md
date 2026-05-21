# Candidate Long-list — 2026-05-21

Phase A의 18개 demand signal과 효소·단백질 도메인 지식을 결합하여 **총 14개**의 사업화 후보를 도출했다.
원칙: therapeutic API 자체는 제외, 생산공정·제형변경·진단·연구·산업 효소만 포함 (SSOT: `scope/inclusion.md`, `scope/exclusion.md`).

## 요약 표

| # | 아이템명 | 효소 클래스 | 포함기준 분류 | 핵심 신호 (한 줄) |
|---|---|---|---|---|
| 1 | Next-gen recombinant hyaluronidase (non-PH20/대체 fold) for SC conversion | hyaluronidase (EC 3.2.1.35) | 제형변경 조력 | SC 전환 표준화 + Halozyme–Merck IP 분쟁으로 우회·차세대 변이체 수요 |
| 2 | Engineered microbial transglutaminase (mTG) for site-specific ADC conjugation | aminoacyltransferase (EC 2.3.2.13) | 생산공정용 효소 | ADC $13.5B·15품목 + Lonza Visp 2배 확장 (enzymatic conjugation cost-down) |
| 3 | Engineered Sortase A variant (Ca²⁺-independent, high-kcat) for ADC/peptide bioconjugation | transpeptidase (EC 3.4.22.70) | 생산공정용 효소 | ADC 차세대 conjugation + Tubulis $3.15B 인수 |
| 4 | Formylglycine-Generating Enzyme (FGE) — aldehyde-tag 기반 dual-payload ADC | sulfatase-modifying (EC 1.8.3.7) | 생산공정용 효소 | Dual-payload·branched linker ADC 차별화 |
| 5 | EndoS2 glycosynthase mutant (transglycosylation강화) — homogeneous Fc glycan | endo-β-N-acetylglucosaminidase (EC 3.2.1.96) | 생산공정용 효소 | Fc glycoengineering·biosimilar QC·차세대 효과기능 항체 |
| 6 | Engineered T7 RNA polymerase variant (low-dsRNA, co-trans capping) | DNA-directed RNA polymerase (EC 2.7.7.6) | 생산공정용 효소 | 600+ mRNA 임상; IVT 효소 $1.8B→$3.9B |
| 7 | Engineered RNA ligase (splint-ligation 기반 oligonucleotide·AOC 합성) | RNA ligase (EC 6.5.1.3) | 생산공정용 효소 | Codexis ECO Synthesis + Novartis–Avidity $12B AOC |
| 8 | Peptiligase / OaAEP1 C247A variant — green enzymatic peptide ligation | asparaginyl endopeptidase (EC 3.4.22.-) | 펩타이드 제조 | Bachem·PolyPeptide GLP-1 캐파 확장 + green chem |
| 9 | Engineered Peptide Amidating Enzyme (PAM, EC 1.14.17.3 + EC 4.3.2.5) | bifunctional amidating monooxygenase·lyase | 펩타이드 제조 | GLP-1·radioligand peptide C-terminal amide 의무 |
| 10 | Engineered IdeS/IdeZ variant (FabRICATOR class) for QC + AAV redosing enabling | cysteine protease (EC 3.4.22.-) | 진단·연구·산업 의약 인접 | mAb/ADC QC 표준 + AAV gene therapy 재투여 |
| 11 | Recombinant PNGase F + sialyltransferase·β1,4-galactosyltransferase set — glycan QC/remodel | EC 3.5.1.52 / EC 2.4.99.x | 진단·연구·산업 의약 인접 | 항체 N-glycan QC; NEB·Genovis cGMP 라인 확장 |
| 12 | Next-gen Cas12/Cas13 variant + RPA recombinase·SSB set — POC molecular Dx | RNA-guided nuclease (EC 3.1.-.-) | 진단·연구·산업 의약 인접 | SHERLOCK·DETECTR 임상 진입 |
| 13 | High-fidelity Prime Editor — vPE Cas9 + engineered MMLV-RT (research/ex-vivo grade) | nuclease + reverse transcriptase (EC 2.7.7.49) | 진단·연구·산업 의약 인접 | MIT 2025 vPE 60× 정밀도; ex-vivo CGT 제조 시약 |
| 14 | AI-designed (RFdiffusion2/3) custom enzyme — reagent-grade nuclease/ligase/polymerase | de novo designed | 진단·연구·산업 의약 인접 | RFdiffusion2/3 천연 수준 활성; Biomatter·Arzeda VC 자금 |

분포: **생산공정용 6 / 제형변경 1 / 진단·연구·산업 인접 5 / 펩타이드 제조 2 / 기타 0**.

---

## 후보 상세 카드

### 후보 1 — Next-gen recombinant hyaluronidase (non-PH20 또는 차세대 PH20 변이체)
1. **아이템명**: Next-gen recombinant hyaluronidase for SC conversion (non-PH20 fold 또는 IP-우회 PH20 변이체).
2. **효소 클래스 / 단백질 패밀리**: Hyaluronate-4-glycanohydrolase (EC 3.2.1.35), GH56 fold (PH20 계열) 또는 leech/세균 유래 hyaluronate lyase (EC 4.2.2.1, PL8 fold).
3. **메커니즘**: Hyaluronan β-1,4 glycosidic 결합 가수분해(또는 lyase 절단)로 SC 조직 ECM 일시 분해 → 대용량 항체·생물의약품 SC 흡수·확산 가능.
4. **포함기준 분류**: **제형변경 조력**.
5. **연결된 수요 신호**: Phase A §1.1 (SC 전환 표준화), §2.3 (Halozyme–Takeda vedolizumab), §2.4 (Merck Keytruda QLEX = Alteogen ALT-B4), §6.1 (Halozyme–Merck 특허 분쟁).
6. **임상 불필요성 판정 근거**: rHuPH20은 이미 부형제급 spreading factor로 다수 SC 제형(Herceptin SC, Darzalex SC, Phesgo, Opdivo SC)에서 결합제형 트랙으로 승인. 신규 변이체도 자체 단독 신약 임상이 아니라 mAb·biologic과 co-formulation으로 결합제형 트랙(상대적으로 낮은 임상 부담).
7. **사업화 시나리오 1줄**: 빅파마·biosimilar 개발사 대상 SC co-formulation 라이선스(upfront + milestone + 로열티) 또는 CDMO 통합 공급. Halozyme ENHANZE·Alteogen Hybrozyme의 제3 대안 포지셔닝.
8. **잠재 경쟁자**: Halozyme (ENHANZE/MDASE), Alteogen (Hybrozyme/ALT-B4), Sanofi/Argobio EnhanzeR `[추정]`.
9. **scope_judgement**: 경계 사례. PH20 변이체 자체의 면역원성·약물동태 데이터는 일부 임상에서 평가되나 결합제형 트랙으로 처리되고 단독 therapeutic API가 아님 → **공정/제형 용도로 한정**한 사업화 시나리오로 포함.

---

### 후보 2 — Engineered Microbial Transglutaminase (mTG) for site-specific ADC conjugation
1. **아이템명**: High-specificity mTG variant (LLQG/Q-tag 인식, narrow specificity, 면역원성 저감).
2. **효소 클래스 / 단백질 패밀리**: Protein-glutamine γ-glutamyltransferase (EC 2.3.2.13), Streptomyces mobaraensis 유래.
3. **메커니즘**: 항체(LLQG-tag 또는 N297 deglycosylated Q295) glutamine과 amine-bearing payload 간 isopeptide 결합 형성 → DAR 2 또는 4 균일 ADC.
4. **포함기준 분류**: **생산공정용 효소**.
5. **연결된 수요 신호**: Phase A §1.2 (ADC $13.5B), §2.2 (Gilead–Tubulis $3.15B), §3.1 (Lonza Visp bioconjugation 2배). Hzymes 인용("enzymatic methods…limited scalability, enzyme cost issues") = cost-down 변이체 직접 수요.
6. **임상 불필요성 판정 근거**: mTG는 효소 자체가 환자에 투여되지 않고 ADC 제조공정에서만 사용 후 정제 단계에서 제거. ADC 의약품의 임상 부담은 항체·payload·linker가 짊어짐.
7. **사업화 시나리오 1줄**: ADC CDMO(Lonza, Samsung Biologics, WuXi XDC)·생명공학사에게 GMP-grade enzyme kit + 라이선스(고정 EC + DAR 보증) 형태로 공급.
8. **잠재 경쟁자**: Innate Pharma EFAT2, Ajinomoto AJICAP, Hzymes Biotechnology, Zedira mTG.
9. **scope_judgement**: 명백 포함.

---

### 후보 3 — Engineered Sortase A variant (Ca²⁺-독립·high-kcat)
1. **아이템명**: Calcium-independent, evolved Sortase A (eSrtA 7M, SrtA 2A-9 변이체).
2. **효소 클래스 / 단백질 패밀리**: Sortase A transpeptidase (EC 3.4.22.70), S. aureus 유래 sortase 패밀리.
3. **메커니즘**: LPETG motif 인식, threonine-glycine 사이 절단 후 N-말단 oligoglycine acceptor와 isopeptide 결합 → 펩타이드·단백질·소분자·핵산 site-specific 결합.
4. **포함기준 분류**: **생산공정용 효소**.
5. **연결된 수요 신호**: Phase A §1.2 (ADC 차세대 conjugation), §1.4 (radioligand peptide–chelator ligation), §2.1 (AOC bioconjugation).
6. **임상 불필요성 판정 근거**: 결합반응 효소로서 제품 출하 전 정제 제거. ADC·AOC·radioligand peptide의 conjugation 시약.
7. **사업화 시나리오 1줄**: ADC·AOC·radioligand CDMO 및 biotech에 evolved SrtA enzyme + matched peptide tag 디자인 컨설팅 묶음 라이선스.
8. **잠재 경쟁자**: NBE-Therapeutics(SMAC 기술, Boehringer 인수 후), academic spin-out (Liu/Ploegh group derivatives).
9. **scope_judgement**: 명백 포함.

---

### 후보 4 — Formylglycine-Generating Enzyme (FGE) for aldehyde-tag dual-payload ADC
1. **아이템명**: Engineered FGE (anaerobic·고활성 변이체) for SMARTag aldehyde-tag conjugation.
2. **효소 클래스 / 단백질 패밀리**: Sulfatase-modifying factor 1 (SUMF1, EC 1.8.3.7), copper-dependent monooxygenase.
3. **메커니즘**: CXPXR consensus motif 내 cysteine을 formylglycine(fGly, 알데하이드)으로 산화. fGly는 HIPS·oxime conjugation으로 payload와 정량적으로 결합.
4. **포함기준 분류**: **생산공정용 효소**.
5. **연결된 수요 신호**: Phase A §1.2 (차세대 conjugation), §3.1 (CDMO enzymatic 채택 확대).
6. **임상 불필요성 판정 근거**: ADC 제조의 in-vitro modification 시약. 인체 투여 없음.
7. **사업화 시나리오 1줄**: ADC 디벨로퍼·CDMO에 FGE enzyme + aldehyde-tag 항체 설계 패키지 공급(Catalent SMARTag 대안).
8. **잠재 경쟁자**: Catalent (Redwood SMARTag 인수), R&D Systems FGE reagent.
9. **scope_judgement**: 명백 포함.

---

### 후보 5 — EndoS2 glycosynthase mutant (transglycosylation 강화)
1. **아이템명**: EndoS2 D184M / Q맥-class glycosynthase mutant for one-pot Fc glycan remodeling.
2. **효소 클래스 / 단백질 패밀리**: Endo-β-N-acetylglucosaminidase (EC 3.2.1.96), GH18, Streptococcus pyogenes EndoS/EndoS2 계열.
3. **메커니즘**: Fc N297 N-glycan trimming → synthase mutant가 균일 oxazoline donor를 transfer → homogeneous afucosylated G2 또는 sialylated glycan 장착. ADCC 강화·biosimilar 균질화.
4. **포함기준 분류**: **생산공정용 효소**.
5. **연결된 수요 신호**: Phase A §6.3 (NEB cGMP glycosidase 라인업 확장), §1.2 (차세대 ADC), §1.1 (biosimilar SC 시장 확대 시 QC 수요).
6. **임상 불필요성 판정 근거**: 항체 in-vitro 후처리 효소; 정제 단계에서 제거.
7. **사업화 시나리오 1줄**: 항체·ADC CDMO 및 Fc engineering biotech에 cGMP grade EndoS2 mutant + donor sugar 공급.
8. **잠재 경쟁자**: Genovis (GlycINATOR/GlyCLICK), Synaffix(Lonza, 인수)의 GlycoConnect, NEB Remove-iT EndoS2.
9. **scope_judgement**: 명백 포함.

---

### 후보 6 — Engineered T7 RNA polymerase variant (low-dsRNA, co-trans capping)
1. **아이템명**: Low-immunogenicity T7 RNAP variant for cGMP IVT mRNA.
2. **효소 클래스 / 단백질 패밀리**: DNA-directed RNA polymerase (EC 2.7.7.6), single-subunit T7-like RNAP.
3. **메커니즘**: DNA template 인식 후 mRNA 합성. 변이체는 promoter loop·thumb 변이로 abortive·dsRNA byproduct 감소 + co-transcriptional capping 효율 증가.
4. **포함기준 분류**: **생산공정용 효소**.
5. **연결된 수요 신호**: Phase A §4.2 (engineered T7 paper, T7 RNAP 시장 $1.8B→$3.9B 2034).
6. **임상 불필요성 판정 근거**: in-vitro mRNA 합성 효소. 제품(mRNA 백신·치료제) 출하 전 정제 단계에서 제거.
7. **사업화 시나리오 1줄**: 600+ mRNA 임상 보유 빅파마·biotech·CDMO(Moderna, Pfizer, BioNTech, CureVac, Aldevron, Trilink)에 cGMP T7 enzyme kit 직접 판매 또는 라이선스.
8. **잠재 경쟁자**: NEB Hi-T7, Aldevron CleanCap T7, Trilink, Thermo (TranscriptAid), Promega.
9. **scope_judgement**: 명백 포함.

---

### 후보 7 — Engineered RNA Ligase (splint ligation, oligonucleotide·AOC 합성)
1. **아이템명**: Engineered T4 RNA ligase 2 / RtcB variant for cGMP splint ligation of siRNA·ASO·AOC.
2. **효소 클래스 / 단백질 패밀리**: RNA ligase (EC 6.5.1.3), T4 Rnl1/Rnl2 또는 RtcB(EC 6.5.1.8).
3. **메커니즘**: 5′-phosphate와 3′-OH oligonucleotide를 splint DNA 가이드 하에 phosphodiester 결합. 긴 siRNA/AOC를 fragment ligation으로 저비용 합성.
4. **포함기준 분류**: **생산공정용 효소**.
5. **연결된 수요 신호**: Phase A §3.3 (Codexis ECO Synthesis ligase 빅파마 첫 수주), §2.1 (Novartis–Avidity $12B AOC).
6. **임상 불필요성 판정 근거**: in-vitro 핵산 합성 효소. 정제 후 제거.
7. **사업화 시나리오 1줄**: 올리고 CDMO(Nitto Avecia, GenScript, Bachem oligo, Cytiva)와 RNA 치료제 개발사에 enzymatic synthesis enzyme + 공정 라이선스.
8. **잠재 경쟁자**: Codexis ECO Synthesis ligase, NEB SplintR, Moderna in-house ligase team `[추정]`.
9. **scope_judgement**: 명백 포함.

---

### 후보 8 — Peptiligase / OaAEP1 C247A variant — Green enzymatic peptide ligation
1. **아이템명**: OaAEP1 C247A 또는 peptiligase variant for cGMP-grade green enzymatic peptide ligation (GLP-1 등 32–40mer).
2. **효소 클래스 / 단백질 패밀리**: Asparaginyl endopeptidase / engineered subtilisin (EC 3.4.22.- / 3.4.21.-), butelase-1 / OaAEP1 패밀리.
3. **메커니즘**: P1 Asn/Asp residue 인식, acyl-enzyme intermediate → 새 N-말단 nucleophile과 ligation. SPPS fragment 2~3개를 효소 ligation으로 결합 → 용매·시간·step yield 개선.
4. **포함기준 분류**: **펩타이드 제조**.
5. **연결된 수요 신호**: Phase A §3.2 (Bachem·PolyPeptide 캐파 2배 + Peptiligase EnzyTag 파트너십), §4.4 (OaAEP1 C247A 140× 개선 paper).
6. **임상 불필요성 판정 근거**: 효소는 in-vitro peptide ligation에서만 사용 후 정제 제거; GLP-1 등 펩타이드 의약품 임상 부담은 펩타이드 자체가 짊어짐.
7. **사업화 시나리오 1줄**: 펩타이드 CDMO(Bachem, PolyPeptide, Lonza Peptides, CordenPharma)에 enzymatic ligation kit + 공정 라이선스(EnzyTag·EnzyPep 대안).
8. **잠재 경쟁자**: EnzyPep (peptiligase, Fresenius Kabi/EnzyTag), Sumitomo/Genovis, academic OaAEP1 spin-out.
9. **scope_judgement**: 명백 포함 (펩타이드 자체가 아니라 ligation 효소).

---

### 후보 9 — Engineered Peptide Amidating Enzyme (PAM)
1. **아이템명**: cGMP-grade recombinant Peptidylglycine α-amidating monooxygenase (PAM) bifunctional enzyme.
2. **효소 클래스 / 단백질 패밀리**: Bifunctional: PHM (EC 1.14.17.3, copper monooxygenase) + PAL (EC 4.3.2.5, lyase). 인간·해양 유래.
3. **메커니즘**: Peptide-Gly의 C-terminal glycine을 hydroxyl-glycine 중간체로 산화 후 α-amide + glyoxylate 분해. GLP-1·calcitonin·oxytocin·radioligand 펩타이드의 C-terminal amide 형성 (활성에 필수).
4. **포함기준 분류**: **펩타이드 제조**.
5. **연결된 수요 신호**: Phase A §3.2 (GLP-1 CDMO 확장), §1.4 (radioligand peptide).
6. **임상 불필요성 판정 근거**: in-vitro peptide 후처리 효소; 정제 후 잔류 제거. 효소 자체는 의약품 아님.
7. **사업화 시나리오 1줄**: 펩타이드 CDMO·GLP-1 biosimilar 개발사에 GMP grade PAM enzyme 공급 — 현재 시장에 cGMP supplier가 매우 적은 화이트스페이스(Unigene·Enzon 후속).
8. **잠재 경쟁자**: Unigene Laboratories (PAM 특허 만료 후 plateau), Strongbridge Biopharma, Akzo Nobel Diosynth `[추정]`.
9. **scope_judgement**: 명백 포함.

---

### 후보 10 — Engineered IdeS/IdeZ variant (FabRICATOR class, QC + AAV redosing)
1. **아이템명**: Next-gen IdeS/IdeZ variant (subtype-broad, low-immunogenicity engineered).
2. **효소 클래스 / 단백질 패밀리**: Cysteine protease (EC 3.4.22.-), Streptococcus pyogenes IdeS / S. equi IdeZ.
3. **메커니즘**: IgG hinge region(CPPC 아래 G237) 특이 절단 → F(ab′)2 + Fc/2. 항체 QC LC-MS·subunit 분석 표준; 또는 환자 혈청 IgG 절단으로 AAV gene therapy 재투여 가능케 함(연구·전임상 응용).
4. **포함기준 분류**: **진단·연구·산업 의약 인접**.
5. **연결된 수요 신호**: Phase A §6.3 (Genovis FabRICATOR QC 표준 + AAV redosing 응용), §1.2 (ADC QC 수요 증가).
6. **임상 불필요성 판정 근거**: QC·분석용은 인체 투여 없음. AAV redosing 치료용으로 환자에게 투여하는 시나리오는 본 후보 카드의 범위가 아님(scope_judgement 참고). **연구·QC·CDMO ex-vivo 시약 시나리오만 후보화**.
7. **사업화 시나리오 1줄**: 바이오의약 QC lab·CDMO·CRO·bioanalytical 공급사(SCIEX, Waters)에 cGMP IdeS/IdeZ kit + LC-MS 워크플로 공급.
8. **잠재 경쟁자**: Genovis (FabRICATOR/FabRICATOR Z), Promega SmartEnzymes, NEB enzymatic IgG digestion.
9. **scope_judgement**: 경계 사례. IdeS는 동시에 Hansa Biopharma의 imlifidase(Idefirix)라는 therapeutic API(이식 desensitization 신약 승인)로도 사용됨 → 인체 투여 신약은 본 프로젝트 범위 밖. **QC·분석·연구·CDMO 시약 시나리오로 한정**해 후보화.

---

### 후보 11 — Recombinant PNGase F + sialyltransferase·galactosyltransferase set (glycan QC/remodeling)
1. **아이템명**: cGMP-grade glycoengineering enzyme suite (PNGase F + α2,6-sialyltransferase + β1,4-galactosyltransferase + GlcNAc transferase).
2. **효소 클래스 / 단백질 패밀리**: Peptide-N-glycosidase F (EC 3.5.1.52, GH18 같은 fold), ST6Gal1·ST3Gal3 (EC 2.4.99.1/4), β1,4-GalT (EC 2.4.1.38).
3. **메커니즘**: PNGase F가 항체 N-glycan을 전부 분리(QC용). transferase set는 균질 glycoform(예: G2S2) 합성 — biosimilar comparability·ADCC 강화.
4. **포함기준 분류**: **진단·연구·산업 의약 인접** (QC) / **생산공정용 효소** (glycan remodeling). 본 후보는 의약 인접 분석용으로 분류.
5. **연결된 수요 신호**: Phase A §6.3 (NEB cGMP grade glycosidase 라인업), §1.1 (biosimilar 시장 확대 시 N-glycan QC).
6. **임상 불필요성 판정 근거**: in-vitro 분석·remodeling 시약.
7. **사업화 시나리오 1줄**: Biosimilar·ADC·항체 CDMO·QC lab에 enzyme set + 표준 워크플로(Halo·Genovis 대안) 공급.
8. **잠재 경쟁자**: NEB (Rapid PNGase F), Genovis (GlycINATOR), Agilent AdvanceBio, Promega.
9. **scope_judgement**: 명백 포함.

---

### 후보 12 — Next-gen Cas12/Cas13 variant + isothermal amplification 효소 (POC molecular Dx)
1. **아이템명**: SHERLOCK/DETECTR 차세대 효소 패키지 (LwaCas13a variant + LbCas12a variant + Bst LF · recombinase UvsX · SSB gp32).
2. **효소 클래스 / 단백질 패밀리**: RNA-guided nuclease (EC 3.1.-.-) + strand-displacement DNA polymerase (Bst, EC 2.7.7.7) + recombinase (UvsX) + SSB.
3. **메커니즘**: 등온증폭(RPA/LAMP)으로 표적 핵산 증폭, gRNA-가이드 Cas12/Cas13가 표적 인식 후 collateral nuclease로 reporter 절단 → fluorescence/LFA 신호.
4. **포함기준 분류**: **진단·연구·산업 의약 인접**.
5. **연결된 수요 신호**: Phase A §6.2 (SHERLOCK COVID EUA, DETECTR HPV CE 99.3%).
6. **임상 불필요성 판정 근거**: 체외진단(IVD) 트랙 — 인체 투여 없음.
7. **사업화 시나리오 1줄**: POC Dx 개발사(Sherlock Bio, Mammoth Bio, Caspr Biotech)·진단 OEM(Roche, Abbott, BD)에 enzyme kit + 라이선스 공급.
8. **잠재 경쟁자**: NEB (Cas12·Cas13·Bst), TwistDx (RPA), Mammoth Biosciences IP, Sherlock Biosciences IP.
9. **scope_judgement**: 명백 포함.

---

### 후보 13 — High-fidelity Prime Editor enzyme set (vPE Cas9 + engineered MMLV-RT, research/ex-vivo grade)
1. **아이템명**: Research-grade and ex-vivo CGT-manufacturing-grade prime editor enzyme set (vPE Cas9 nickase variant + evolved MMLV-RT).
2. **효소 클래스 / 단백질 패밀리**: Cas9 nickase variant (EC 3.1.-.-, S. pyogenes), Moloney MLV reverse transcriptase (EC 2.7.7.49).
3. **메커니즘**: pegRNA·Cas9 nickase로 표적 nick → MMLV-RT가 pegRNA 3′ extension(RT template) 복제 → edit 도입. vPE 변이체는 off-target/byproduct 60× 절감.
4. **포함기준 분류**: **진단·연구·산업 의약 인접** (research reagent + ex-vivo CGT manufacturing 시약).
5. **연결된 수요 신호**: Phase A §4.3 (MIT 2025 vPE paper).
6. **임상 불필요성 판정 근거**: 본 후보는 연구·ex-vivo 세포 편집·CRO 시약 용도로 한정. 환자에게 직접 투여되는 prime editor 치료제(Prime Medicine 등 in-vivo gene editor)는 본 프로젝트 범위 밖.
7. **사업화 시나리오 1줄**: 연구용 시약 공급사(IDT, Aldevron, GenScript)·ex-vivo CGT CDMO(Charles River, Cellares)에 enzyme set + pegRNA design 서비스 공급.
8. **잠재 경쟁자**: Prime Medicine(특허), IDT Alt-R Cas9, Aldevron SpyFi, Twist gene editing tools.
9. **scope_judgement**: 경계 사례. Cas9·RT 변이체는 in-vivo 치료제로도 쓰일 수 있으나 **research·ex-vivo manufacturing reagent 시나리오로 한정**해 후보화. 치료제 직접 투여 시나리오는 out-of-scope 명시.

---

### 후보 14 — AI-designed (RFdiffusion2/3) custom enzymes (reagent-grade)
1. **아이템명**: De novo designed enzyme as research/diagnostic reagent (custom nuclease·ligase·polymerase·esterase 등).
2. **효소 클래스 / 단백질 패밀리**: De novo (Baker lab RFdiffusion2/3, ESM-2 + ProteinMPNN 파이프라인). 자연 fold가 아닌 새 backbone + 기존 active site 기하.
3. **메커니즘**: 사용자가 제공한 active-site geometry / 기질 결합 pocket prompt로부터 backbone generation → sequence design → 발현 → 활성 검증. 천연 효소 수준 catalytic proficiency 보고됨(2025).
4. **포함기준 분류**: **진단·연구·산업 의약 인접** (단기 reagent-grade); 중기 생산공정용 진입 가능.
5. **연결된 수요 신호**: Phase A §4.1 (RFdiffusion2/3), §5.1 (Biomatter €6.5M, Arzeda NSF $32M).
6. **임상 불필요성 판정 근거**: 연구·진단·산업·CDMO 공정 시약. 인체 투여 없음.
7. **사업화 시나리오 1줄**: "Custom enzyme as a service" — 제약·진단·CDMO 고객 요청 받아 de novo 설계 후 IP 라이선스 + GMP 발현 패키지 공급(Codexis/Biomatter 대안 포지셔닝).
8. **잠재 경쟁자**: Codexis CodeEvolver, Biomatter, Arzeda, Cradle Bio, Enzymit, Generate Biomedicines.
9. **scope_judgement**: 명백 포함 (의약 therapeutic용 de novo 단백질은 별도 사례별 판정 필요하지만 본 후보는 reagent·process enzyme 시나리오로 한정).

---

### 메모
- 분포: 생산공정 6 / 제형변경 1 / 진단·연구·산업 5 / 펩타이드 제조 2 — 총 14개로 목표(12~15)에 부합.
- TPD(§1.3) E3 ligase 시약은 시장 크기 검증 부족으로 본 라운드 제외(Phase C에서 재검토 권장).
- PETase(§6.4)는 의약 직접 인접성이 약해 본 라운드 제외 (다음 회차 "탐색 후보"로 별도 표기 가능).
- 경계 사례 3건: 후보 1 (rHuPH20 결합제형 트랙), 후보 10 (IdeS — therapeutic용 imlifidase 존재), 후보 13 (prime editor — in-vivo 치료제와 분리) — 각각 scope_judgement에 한정 시나리오 명시.
