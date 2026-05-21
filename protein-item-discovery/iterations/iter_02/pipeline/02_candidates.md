# Candidate Long-list — Round 2, 2026-05-21

R2 focus: **Deferred & Boost**. R1 14개 후보에 `business_model`·`lifecycle` 필드를 사후 부여하고, R2 landscape에서 도출된 부활 2개 + 신규 8개를 정식 카드화한다. 중복은 병합 처리.

원칙: therapeutic API 자체는 제외; 생산공정·제형변경·진단·연구·산업 효소만 포함 (SSOT: `scope/inclusion.md`, `scope/exclusion.md`). 사업화 형태 코드는 `scope/business_model_taxonomy.md`의 L/K/C/S/H.

---

## 라운드 통계

- **R1 유지(maintained_at_round_2)**: 14개 (item_001~014). business_model 사후 부여 완료.
- **R2 부활(revived_from_round_1)**: 2개 → 1개는 R2 신규와 병합되어 사실상 활성 1개.
  - item_023 TPD reagent cocktail (revived) — 활성.
  - item_024 Engineered cutinase / LCC variant (revived) — **merged_into item_020**.
- **R2 신규(new_at_round_2)**: 8개 (item_015~022). item_020에 부활 카드(item_024)가 병합됨 → 신규 자체는 8개 유지, 그 중 item_020이 부활분을 흡수.
- **병합**: 1건 (item_024 → item_020).
- **드롭**: 0건.
- **누적 활성 후보 수**: **14 (R1 유지) + 1 (부활 활성) + 8 (R2 신규) = 23개**. 단 item_020이 item_024의 부활분을 흡수했으므로 별도 카운트하면 14 + 1 + 8 = 23, 또는 부활을 신규에 흡수해서 14 + 0 + 8 + 1 = 23으로도 일관. **확정 누적 활성 후보 = 23개**.

---

## 요약 표 (누적 활성 23개)

★ 표기는 R1 short-list 7개 (item_002, 008, 007, 006, 003, 005, 009).

| id | 아이템 | 효소 클래스 | 포함기준 분류 | business_model (primary/secondary) | lifecycle | 핵심 신호 (한 줄) |
|---|---|---|---|---|---|---|
| item_001 | Next-gen recombinant hyaluronidase (non-PH20 / 차세대 PH20) | hyaluronidase EC 3.2.1.35 / lyase EC 4.2.2.1 | 제형변경 | K / L | maintained_at_round_2 | SC 전환 표준화 + Halozyme–Merck IP 분쟁 (R2 §6.1 HYDIZYME BLA로 보강) |
| item_002 ★ | Engineered mTG (ADC site-specific conjugation) | aminoacyltransferase EC 2.3.2.13 | 생산공정 | K / L | maintained_at_round_2 | ADC $13.5B + Lonza Visp 2배 확장 |
| item_003 ★ | Engineered Sortase A variant | transpeptidase EC 3.4.22.70 | 생산공정 | L / K | maintained_at_round_2 | ADC 차세대 conjugation; (R2 §8.4 radioligand site-specific ligation 응용 확장) |
| item_004 | FGE (aldehyde-tag dual-payload ADC) | EC 1.8.3.7 | 생산공정 | K / S | maintained_at_round_2 | Dual-payload ADC 차별화 |
| item_005 ★ | EndoS2 glycosynthase mutant | endo-β-N-GlcNAcase EC 3.2.1.96 | 생산공정 | K / L | maintained_at_round_2 | Fc glycoengineering, biosimilar QC |
| item_006 ★ | Engineered T7 RNAP (low-dsRNA, co-trans capping) | RNAP EC 2.7.7.6 | 생산공정 | K / — | maintained_at_round_2 | 600+ mRNA 임상; (R2 §3.2 FCE::T7RNAP fusion 연계 시 item_016과 협력 검토) |
| item_007 ★ | Engineered RNA ligase (splint, AOC) | RNA ligase EC 6.5.1.3 | 생산공정 | L / K | maintained_at_round_2 | Codexis ECO + Novartis–Avidity $12B AOC |
| item_008 ★ | Peptiligase / OaAEP1 C247A | EC 3.4.22.- | 펩타이드 제조 | L / K | maintained_at_round_2 | Bachem/PolyPeptide GLP-1 캐파; (R2 §6.3 FDA Research-Grade Peptide guidance로 cGMP grade 수요 증가) |
| item_009 ★ | Engineered PAM (peptide amidation) | EC 1.14.17.3 + 4.3.2.5 | 펩타이드 제조 | K / S | maintained_at_round_2 | GLP-1·radioligand C-term amide 의무 |
| item_010 | IdeS/IdeZ variant (FabRICATOR class) | cysteine protease EC 3.4.22.- | 진단·연구·산업 | K / — | maintained_at_round_2 | mAb/ADC QC + AAV redosing 연구 |
| item_011 | PNGase F + ST + GalT suite (glycan QC) | EC 3.5.1.52 / 2.4.99.x / 2.4.1.38 | 진단·연구·산업 | K / — | maintained_at_round_2 | Biosimilar N-glycan QC |
| item_012 | Cas12/Cas13 + RPA/Bst set (POC molecular Dx) | EC 3.1.-.- + EC 2.7.7.7 | 진단·연구·산업 | K / L | maintained_at_round_2 | SHERLOCK/DETECTR 임상 진입 |
| item_013 | High-fidelity Prime Editor (vPE + MMLV-RT) | EC 3.1.-.- + EC 2.7.7.49 | 진단·연구·산업 | K / S | maintained_at_round_2 | MIT 2025 vPE 60× 정밀도 |
| item_014 | AI-designed RFdiffusion2/3 custom enzyme | de novo | 진단·연구·산업 | S / L | maintained_at_round_2 | Baker lab + Biomatter VC |
| item_015 | EfHyl8 PL8 hyaluronate lyase (non-PH20 SC 확산) | lyase EC 4.2.2.1 | 제형변경 | K / L | new_at_round_2 | JAFC 2025 SC 확산 + safety 보고 |
| item_016 | FCE::T7RNAP fusion (one-pot Cap-1) | EC 2.7.7.50 + 2.7.7.6 | 생산공정 | C / K | new_at_round_2 | TriLink CleanCap M6 cost race 응전 |
| item_017 | Inorganic pyrophosphatase (IVT helper, GMP) | EC 3.6.1.1 | 생산공정 | C / — | new_at_round_2 | IVT yield +15-25%, non-animal GMP |
| item_018 | CRBN/VHL E3 ligase ternary complex reagent | EC 6.3.2.- | 진단·연구·산업 | C / — | new_at_round_2 | ARV-471 FDA 승인 → PROTAC QC 시약 |
| item_019 | USP7/USP28/OTUB1 DUB cocktail (DUBTAC) | EC 3.4.19.12 | 진단·연구·산업 | C / — | new_at_round_2 | DUBTAC 모달리티 등장 |
| item_020 | Engineered LCC / cutinase + AI-designed PETase (의약 PET 포장재 분해) | EC 3.1.1.101 | 진단·연구·산업 (ESG/산업) | S / L | new_at_round_2 (absorbs item_024) | Carbios+Epoch+CtCut; 프랑스 €1,000/t 보너스 |
| item_021 | cGMP sortase A / OaAEP1 C247A (radioligand peptide-chelator) | EC 3.4.22.- | 펩타이드 제조 | K / L | new_at_round_2 | Aktis Phase 0 + AZ-Fusion 클로징 (관련: item_003, item_008 응용 확장) |
| item_022 | dsRNA-specific engineered nuclease (RNase III 대체) | EC 3.1.26.3 | 생산공정 | C / S | new_at_round_2 | ShortCut RNase III off-target 보고 |
| item_023 | TPD reagent cocktail (E1+E2+E3+DUB) | EC 6.3.2.- + 3.4.19.12 외 | 진단·연구·산업 | C / K | revived_from_round_1 | ARV-471 승인 + DUBTAC; 시장 $402M, CAGR 8.6% (item_018·019의 상위 패키지) |
| ~~item_024~~ | ~~Engineered cutinase / LCC variant (PET 의약 포장)~~ | — | — | — | **merged_into_item_020** | 동일 기술군 → item_020에 흡수 |

---

## R1 카드 사후 보강 (business_model 필드 부여) — 14개

각 카드의 business_model 분류는 `scope/business_model_taxonomy.md`의 매핑 가이드 + 라운드 1 사업화 시나리오에 근거. 모든 R1 카드 `lifecycle: maintained_at_round_2`.

- **item_001 Next-gen hyaluronidase** — `business_model: K (primary) / L (secondary)`. rationale: GMP 효소 + co-formulation 라이선스. *R2 신호 연결*: R2 §6.1 HYDIZYME BLA·RYBREVANT FASPRO 승인으로 3rd-tier 시장 형성 확인; R2 §4.1 EfHyl8 등장으로 non-PH20 대체 효소 경쟁구도 변화.
- **item_002 Engineered mTG** ★ — `K / L`. GMP enzyme kit + Q-tag 설계 라이선스.
- **item_003 Engineered Sortase A** ★ — `L / K`. 라이선스 + tag 설계 컨설팅 + enzyme 공급. *R2 연결*: R2 §8.4 radioligand site-specific ligation 응용으로 item_021과 평행 카드.
- **item_004 FGE (aldehyde-tag)** — `K / S`. enzyme + aldehyde-tag 항체 설계 서비스.
- **item_005 EndoS2 glycosynthase** ★ — `K / L`. enzyme + donor sugar 패키지.
- **item_006 Engineered T7 RNAP** ★ — `K / —`. NEB/Aldevron 류 catalog 채널. *R2 연결*: R2 §3.2 FCE::T7RNAP fusion (item_016) 등장으로 협력 또는 cannibalize 가능성.
- **item_007 Engineered RNA ligase** ★ — `L / K`. Codexis ECO 모델.
- **item_008 Peptiligase / OaAEP1 C247A** ★ — `L / K`. EnzyTag/EnzyPep 모델. *R2 연결*: R2 §6.3 FDA Research-Grade Peptide guidance enforcement (2026.1)로 cGMP grade 수요 증가; item_021과 평행 카드.
- **item_009 Engineered PAM** ★ — `K / S`. cGMP supplier 화이트스페이스 → kit 주력 + custom service 보조.
- **item_010 IdeS/IdeZ variant** — `K / —`. Genovis FabRICATOR 류 catalog 단일 채널.
- **item_011 PNGase F + ST + GalT suite** — `K / —`. NEB/Genovis 류 catalog.
- **item_012 Cas12/Cas13 + RPA/Bst set** — `K / L`. kit 공급 + IP 라이선스 dual.
- **item_013 High-fidelity Prime Editor** — `K / S`. research kit + ex-vivo CGT custom service.
- **item_014 AI-designed RFdiffusion2/3 custom enzyme** — `S / L`. "Custom enzyme as a service" → IP 라이선스.

---

## R2 신규·부활 카드 상세

### item_015 — EfHyl8 PL8 hyaluronate lyase (non-PH20 SC 확산 효소)

1. **아이템명**: EfHyl8 (Enterococcus faecalis 유래 PL8 family hyaluronate lyase) — non-PH20 SC drug-diffusion 보조 효소.
2. **효소 클래스 / 단백질 패밀리**: Hyaluronate lyase (EC 4.2.2.1), Polysaccharide Lyase family 8 (PL8). 도메인 구조: CBM70 (carbohydrate-binding module) + β-sheet domain + C-terminal PL8 catalytic domain. 기원: Enterococcus faecalis.
3. **메커니즘**: Hyaluronan β-1,4 결합을 β-elimination으로 절단(가수분해가 아닌 lyase 방식) → unsaturated disaccharide 생성. PH20과는 fold·반응 메커니즘이 완전히 다름 → Halozyme/Alteogen IP 우회 명분.
4. **포함기준 분류**: **제형변경 조력** (SC 흡수·확산 보조).
5. **business_model**:
   - primary: **K** (Kit/Reagent) — GMP/research-grade enzyme catalog + biopharma 공급.
   - secondary: **L** (Licensing) — non-PH20 fold 신규 IP를 mAb co-formulation에 라이선스.
   - rationale: GMP 단백질 공급이 1차 수익, IP 자체가 PH20 우회 가치를 가지므로 L 병행.
6. **연결된 수요 신호**: R2 §4.1 (EfHyl8 JAFC 2025 SC 확산 + safety 보고), R2 §6.1 (HYDIZYME BLA + RYBREVANT FASPRO 승인 → 3rd-tier 시장), R2 §8.3 (SinHL·HylP 비교군), R1 §1.1·6.1 (SC 전환 트렌드 + Halozyme–Merck 분쟁).
7. **임상 불필요성 판정 근거**: SC co-formulation 보조 효소. mAb biologic과 co-formulation 트랙(결합제형 임상 부담은 약물 자체가 짊어짐). EfHyl8 단독 신약 임상 시나리오는 본 카드 범위 외.
8. **사업화 시나리오 1줄**: 빅파마 mAb SC 전환·biosimilar SC 개발사에 non-PH20 hyaluronate lyase로 IP 우회 옵션 공급 (Halozyme ENHANZE·Alteogen Hybrozyme의 3rd-tier 대안).
9. **잠재 경쟁자**: Halozyme rHuPH20 (ENHANZE), Alteogen ALT-B4 (Hybrozyme), Huonslab HYDIZYME (3rd-tier PH20). 비PH20 진영은 학술 단계, 상업 진입자 미확정.
10. **scope_judgement**: 경계 사례 (SC co-formulation 트랙). 결합제형 트랙으로 한정해 포함. EfHyl8의 단독 신약 시나리오는 명시적 out-of-scope.
11. **lifecycle**: `new_at_round_2`.

---

### item_016 — FCE::T7RNAP fusion / FCE + 2′-O-MTase one-pot Cap-1 system

1. **아이템명**: FCE (Faustovirus Capping Enzyme)::T7 RNAP fusion 또는 FCE + vaccinia 2′-O-MTase one-pot Cap-1 합성 시스템 (one-pot cGMP IVT mRNA capping).
2. **효소 클래스 / 단백질 패밀리**: Faustovirus capping enzyme (single-subunit triphosphatase + guanylyltransferase + N7-methyltransferase, EC 2.7.7.50 / 2.1.1.56) + DNA-directed RNA polymerase (T7 RNAP, EC 2.7.7.6) fusion; 또는 FCE + vaccinia mRNA Cap 2′-O-methyltransferase (EC 2.1.1.57) one-pot.
3. **메커니즘**: T7 RNAP가 IVT로 5′-triphosphate RNA를 합성, FCE가 동일 반응 chamber에서 triphosphatase·GT·N7-MTase 3-step을 단일 효소로 수행해 Cap-0 형성, 2′-O-MTase가 첫 nucleotide ribose 2′-OH를 메틸화해 Cap-1 완성. 25 U FCE로 100 μg RNA를 1 h 안에 capping (55 °C 내성).
4. **포함기준 분류**: **생산공정용 효소** (mRNA IVT).
5. **business_model**:
   - primary: **C** (Captive CDMO use) — 자사 cGMP IVT 라인에 내재화하여 capping 단계 cost-down.
   - secondary: **K** (Kit) — NEB·Takara·KACTUS류 catalog 채널로 GMP enzyme 단위 판매.
   - rationale: TriLink CleanCap M6와의 cost race이므로 captive 내재화가 차별점; 동시에 K로도 매출 다원화.
6. **연결된 수요 신호**: R2 §3.1 (TriLink CleanCap M6 2025.5 출시 + 단백질 발현 +30% / dsRNA -85% / 제조비 -20-40% 데이터), R2 §3.2 (FCE::T7RNAP fusion + 2′-O-MTase one-pot 다공급자화 — NEB·Yeasen·Tinzyme·SignalChemDx·KACTUS·Hzymes), R1 §4.2 (T7 RNAP 시장 $1.8B→$3.9B 2034).
7. **임상 불필요성 판정 근거**: in-vitro mRNA 합성·capping 효소. mRNA 제품 출하 전 정제 단계에서 제거. 효소 자체 인체 투여 없음.
8. **사업화 시나리오 1줄**: mRNA CDMO(Aldevron, TriLink, Moderna captive, BioNTech)·600+ mRNA 임상 보유 biotech에 one-pot Cap-1 fusion enzyme + cGMP DMF 패키지 공급, CleanCap analog cost race에 효소 진영 응전.
9. **잠재 경쟁자**: NEB Faustovirus Capping Enzyme (M2081), Takara/Clontech FCE, KACTUS GMP-grade 2′-O-MTase (DMF #038029), Yeasen/Hzymes/Tinzyme, TriLink CleanCap (chemical analog, 가장 큰 위협).
10. **scope_judgement**: 명백 포함.
11. **lifecycle**: `new_at_round_2`.

---

### item_017 — Inorganic Pyrophosphatase (IVT helper, GMP non-animal source)

1. **아이템명**: Yeast 또는 E. coli inorganic pyrophosphatase (PPase) — cGMP grade, non-animal source, IVT mRNA helper.
2. **효소 클래스 / 단백질 패밀리**: Inorganic diphosphatase (EC 3.6.1.1), Family I (yeast/E. coli) 또는 Family II (bacterial). 기원: Saccharomyces cerevisiae 또는 E. coli.
3. **메커니즘**: T7 RNAP IVT 반응에서 부산물로 축적되는 PPi(pyrophosphate)를 2 Pi(phosphate)로 가수분해해 T7 RNAP 피드백 억제 해제 → RNA yield +15-25%. NTP 가수분해와는 무관(특이성).
4. **포함기준 분류**: **생산공정용 효소** (mRNA IVT helper).
5. **business_model**:
   - primary: **C** (Captive) — IVT 공정 helper로 자사 라인 내재화 (margin 개선).
   - secondary: — (단일 모델로 출발; 추후 K 확장 가능).
   - rationale: yeast PPase가 NEB/Synthego/Hzymes 등 K 진영에 이미 포화 → 신규 진입자는 captive 또는 OEM 모델이 차별점.
6. **연결된 수요 신호**: R2 §3.3 (Hzymes yeast PPase RNA yield +15-25%, non-animal GMP), R1 §4.2 (mRNA 시장 확장), R2 §8.5 (NEB·Synthego·Canvax cGMP PPase 라인업 다극화).
7. **임상 불필요성 판정 근거**: in-vitro IVT helper 효소. 제품(mRNA) 출하 전 정제 단계에서 제거.
8. **사업화 시나리오 1줄**: mRNA CDMO·IVT 키트 공급사에 non-animal source cGMP PPase OEM 또는 captive 공급 (한국·중국 공급망 다극화 진입).
9. **잠재 경쟁자**: NEB Inorganic Pyrophosphatase, Hzymes yeast PPase, Synthego, Canvax, Yeasen.
10. **scope_judgement**: 명백 포함.
11. **lifecycle**: `new_at_round_2`.

---

### item_018 — CRBN/VHL E3 ligase ternary complex assay reagent

1. **아이템명**: Recombinant CRBN (Cereblon) / VHL E3 ligase ternary complex + NanoLuc/NanoBRET-fused 변이체 (PROTAC QC·screening 시약).
2. **효소 클래스 / 단백질 패밀리**: Ubiquitin protein ligase (E3, EC 6.3.2.-). CRBN: CRL4^CRBN cullin RING ligase 어댑터; VHL: CRL2^VHL. 인간 유래 재조합.
3. **메커니즘**: PROTAC 소분자가 E3 ligase와 target POI를 ternary complex로 결합 → polyubiquitination → 26S proteasome 분해. NanoBRET·NanoLuc fusion은 in-vitro·intracellular ternary complex 형성을 luminescence로 측정.
4. **포함기준 분류**: **진단·연구·산업 의약 인접** (PROTAC screening + QC 시약).
5. **business_model**:
   - primary: **C** (Captive/Catalog reagent) — Promega/BPS/R&D Systems 류 catalog 모델.
   - secondary: — (단일 catalog; custom 서비스 추가 가능).
   - rationale: Promega NanoBRET TE kits가 이미 표준화 — catalog 진입이 주력. 단 Promega 표기 시 C는 본 분류표 정의상 "captive CDMO use"보다는 catalog reagent 의미로 해석.
6. **연결된 수요 신호**: R2 §1.1 (ARV-471 vepdegestrant FDA 승인 2026.5.1), R2 §8.1 (Promega NanoBRET TE E3 ligase assay kit + Ternary Complex Starter Kits, R&D Systems UBE1, BPS Bioscience USP screening kit + Molecular Glue Degradation Agent Market $402M / CAGR 8.6%).
7. **임상 불필요성 판정 근거**: in-vitro PROTAC screening·QC 시약. 인체 투여 없음.
8. **사업화 시나리오 1줄**: PROTAC·molecular glue 개발 biotech·빅파마·CRO에 CRBN/VHL ternary assay enzyme + NanoBRET kit 공급 (Promega·BPS·R&D Systems 대안).
9. **잠재 경쟁자**: Promega (NanoBRET TE E3 ligase assays + Ternary Complex Starter Kits), BPS Bioscience, R&D Systems / Bio-Techne (UBE1 E-305·306·307), Thermo Fisher recombinant E3.
10. **scope_judgement**: 명백 포함.
11. **lifecycle**: `new_at_round_2`.

---

### item_019 — USP7/USP28/OTUB1 recombinant DUB cocktail (DUBTAC 시약 라인)

1. **아이템명**: Recombinant DUB (deubiquitinase) cocktail — USP7, USP5, USP28, OTUB1 — for DUBTAC ternary complex screening + DUB inhibitor screening.
2. **효소 클래스 / 단백질 패밀리**: Ubiquitin-specific peptidase / OTU family (EC 3.4.19.12). USP family: cysteine protease, ubiquitin Gly76 isopeptide bond cleavage; OTU family: 다른 catalytic fold이나 같은 EC.
3. **메커니즘**: Ubiquitin chain의 isopeptide 결합 절단 → polyubiquitin 제거. DUBTAC은 POI에 DUB를 끌어와 ubiquitin을 제거해 단백질을 안정화(분해 반대 방향).
4. **포함기준 분류**: **진단·연구·산업 의약 인접** (DUBTAC screening + DUB inhibitor screening 시약).
5. **business_model**:
   - primary: **C** (Catalog reagent) — BPS Bioscience류 catalog가 표준.
   - secondary: — (단일 모델).
   - rationale: research-grade catalog가 1차 매출; cGMP DMF는 PROTAC 진영보다 늦음 — Captive/CDMO 진입은 시기상조.
6. **연결된 수요 신호**: R2 §4.3 (DUBTAC J. Med. Chem. 2025.3 종설 + Angew. Chem. 2025 first-in-class cGAS-stabilizing DUBTAC + USP28-based DUBTAC), R2 §8.1 (BPS Bioscience USP5/USP7 screening kit catalog, Bio-Techne UBE1).
7. **임상 불필요성 판정 근거**: in-vitro DUBTAC·DUB inhibitor screening 시약.
8. **사업화 시나리오 1줄**: DUBTAC·DUB inhibitor 개발 biotech·CRO에 USP7/USP28/OTUB1 재조합 cocktail + NanoBRET 표준 워크플로 공급.
9. **잠재 경쟁자**: BPS Bioscience (USP5/USP7/UBE1), R&D Systems, Bio-Techne, Boston Biochem (R&D 자회사) DUB 카탈로그.
10. **scope_judgement**: 명백 포함.
11. **lifecycle**: `new_at_round_2`.

---

### item_020 — Engineered LCC / cutinase + AI-designed PETase (의약품 PET 포장재 분해)

(item_024 부활 카드의 내용을 흡수)

1. **아이템명**: Engineered LCC variant (Carbios C-ZYME class) + Chaetomium thermophilum cutinase (CtCutWT / S136A) + AI-designed PETase (Epoch class) — 의약품 PET 1차 포장재 (vial · blister · multilayer) ESG 분해 효소 라인.
2. **효소 클래스 / 단백질 패밀리**: Cutinase (EC 3.1.1.74) / Polyester hydrolase / PETase (EC 3.1.1.101) / MHETase (EC 3.1.1.102). α/β hydrolase fold, serine catalytic triad. 기원: Leaf-branch Compost Cutinase (LCC, metagenomic), Chaetomium thermophilum, Humicola insolens (HiC), Ideonella sakaiensis (PETase/MHETase), AI-designed de novo.
3. **메커니즘**: PET의 ester 결합을 가수분해 → BHET·MHET·TPA + EG. LCC ICCG variant·CtCutS136A는 70 °C 부근 PET glass transition 영역에서 최대 활성; AI-designed 효소는 mild 조건에서 동등 활성 시도.
4. **포함기준 분류**: **진단·연구·산업 의약 인접** (ESG/산업효소, 의약 PET 1차 포장재 재활용).
5. **business_model**:
   - primary: **S** (Service / substrate-as-service) — Carbios 모델: 효소 자체 판매보다 PET 재활용 공정·기지를 의약 포장 공급자에 서비스로 제공.
   - secondary: **L** (Licensing) — engineered variant IP 라이선스.
   - rationale: Carbios C-ZYME가 plant operator 모델 + IP 라이선스 hybrid → 본 카드도 S+L 권장.
6. **연결된 수요 신호**: R2 §4.2 (Chaetomium thermophilum cutinase CtCutWT/CtCutS136A 결정구조, Kollicoat pH-responsive 고정화 80% activity 유지), R2 §5.1 (Epoch Biodesign 누적 $50M+ AI-designed enzymes, Inditex·lululemon·Extantia 투자), R2 §6.2 (Carbios Longlaville 50 kt/년 + Wankai China JV + 프랑스 €1,000/톤 sensitive-contact 보너스 2025.9 decree), R1 §6.4 (PETase 카테고리 R1 deferred).
7. **임상 불필요성 판정 근거**: 산업효소·환경효소. 의약품 1차 포장재 폐기물 분해. 인체 투여 없음, 의약 잔류물 없음.
8. **사업화 시나리오 1줄**: 의약 PET vial·blister·multilayer 포장 제조사(Schott, SGD Pharma, AptarGroup, West Pharma)·재활용 사업자에 LCC variant + cutinase + AI PETase 라인 + 공정 라이선스 공급 (Carbios 대안·후속). 프랑스 sensitive-contact 보너스 정책으로 ESG inventive.
9. **잠재 경쟁자**: Carbios (C-ZYME LCC variant, Longlaville·Wankai JV), Epoch Biodesign (AI-designed enzymes, $50M+), Wankai New Materials, Novonesis (구 Novozymes) HiC, Samsara Eco.
10. **scope_judgement**: 경계 사례. 의약 PET 포장재 분해는 의약 직접 적용은 아니나 "의약 인접 ESG"로 inclusion §4 (산업효소 의약 인접 확장)에 포함. **의약 1차 포장재 시나리오로 한정**.
11. **lifecycle**: `new_at_round_2` (absorbs `item_024 revived_from_round_1`).

---

### item_021 — cGMP sortase A / OaAEP1 C247A (radioligand peptide-chelator site-specific ligation)

1. **아이템명**: cGMP-grade Sortase A variant + OaAEP1 C247A — radioligand peptide-chelator site-specific enzymatic conjugation.
2. **효소 클래스 / 단백질 패밀리**: Sortase A transpeptidase (EC 3.4.22.70, S. aureus) + asparaginyl endopeptidase (EC 3.4.22.-, Oldenlandia affinis butelase/OaAEP1 family).
3. **메커니즘**: Sortase A: LPXTG motif 인식 → threonine-glycine 절단 후 oligoglycine 또는 click handle 부착 chelator와 isopeptide 결합. OaAEP1 C247A: NGL motif 인식 → ligation. → peptide ligand에 DOTA·DOTAGA·HEHA·NETA·NOTA chelator를 site-specific으로 결합 → ⁶⁴Cu·¹⁷⁷Lu·²²⁵Ac·²¹²Pb 등 라벨링.
4. **포함기준 분류**: **펩타이드 제조** (radioligand peptide-chelator conjugation).
5. **business_model**:
   - primary: **K** (Kit/Reagent) — cGMP-grade enzyme + matched peptide tag (LPXTG / NGL) 디자인 패키지 공급.
   - secondary: **L** (Licensing) — radiopharma CDMO·biotech에 process 라이선스.
   - rationale: radiopharma는 short half-life (Ac-225 t½=9.9d)로 throughput 압박이 강함 → captive보다 enzyme+process kit 공급이 적합.
6. **연결된 수요 신호**: R2 §1.2 (Aktis-275 64Cu-PD-29875 Phase 0), R2 §2.1 (AstraZeneca–Fusion $2.4B 2026 Q1 클로징 + actinium-225 supply 통합), R2 §6.3 (FDA Research-Grade Peptide guidance 2025.3 → 2026.1 enforcement, cGMP grade peptide ligase 수요 증대), R2 §8.4 (Sortase A 18F radiolabeling USPTO 10556024 특허), R1 §1.4 (radioligand 트렌드), R1 §4.4 (OaAEP1 C247A 140× 개선).
7. **임상 불필요성 판정 근거**: in-vitro peptide-chelator 결합 효소. 정제 후 잔류 제거 (peptide·chelator 자체가 임상 부담을 짊어짐). 효소 자체 인체 투여 없음.
8. **사업화 시나리오 1줄**: Radiopharma CDMO(Lantheus, Curium, Novartis radioligand 공정, Aktis, PeptiDream)에 cGMP sortase A·OaAEP1 enzyme + chelator-tag conjugation 표준 워크플로 공급.
9. **잠재 경쟁자**: NBE-Therapeutics(Boehringer 인수, SMAC sortase IP), EnzyPep/EnzyTag (peptiligase) — 단 radioligand 응용은 직접 경쟁자 미확정 새 시장. 관련: item_003 (Sortase A, ADC 위주), item_008 (OaAEP1, peptide manufacturing 위주)의 **응용 확장** 카드.
10. **scope_judgement**: 명백 포함. item_003·008과 효소 자체는 같지만 cGMP grade + radioligand 응용 시나리오 차별화로 별도 카드 유지.
11. **lifecycle**: `new_at_round_2` (관련: item_003, item_008 응용 확장).

---

### item_022 — dsRNA-specific engineered nuclease (RNase III 대체, IVT mRNA 정제)

1. **아이템명**: dsRNA-specific engineered endoribonuclease — RNase III variant + dsRNA-binding domain (dsRBD) 추가 또는 AI-designed dsRNA-specific nuclease (ShortCut RNase III off-target 문제 해소용).
2. **효소 클래스 / 단백질 패밀리**: Ribonuclease III (EC 3.1.26.3) family. E. coli RNase III + MBP fusion 기존 (ShortCut), 차세대는 dsRBD 추가 또는 AI-designed novel scaffold.
3. **메커니즘**: IVT mRNA 부산물로 형성되는 dsRNA(immunogenic byproduct)를 dsRBD가 인식 → RNase III 도메인이 절단. 차세대 변이체는 ssRNA 2차구조에 대한 off-target 절단을 억제 (specificity 강화).
4. **포함기준 분류**: **생산공정용 효소** (mRNA IVT 정제).
5. **business_model**:
   - primary: **C** (Captive/Catalog reagent) — IVT 공정 정제 단계 enzyme.
   - secondary: **S** (Custom Engineering) — 고객 mRNA 시퀀스별 specificity tuned variant 서비스.
   - rationale: ShortCut의 한계가 학계에 명확히 보고됐으므로 customized variant 서비스 가능성 큼.
6. **연결된 수요 신호**: R2 §4.4 (J. Chromatogr. 2024.12 종설: ShortCut RNase III off-target ssRNA 2차구조 절단 보고, dsRNA 제거 specificity 개선 차세대 효소 빈자리), R2 §8.5 (mRNA aux 효소 풀라인업 다극화 트렌드), R1 §4.2 (mRNA 시장 확장).
7. **임상 불필요성 판정 근거**: in-vitro mRNA 정제 helper 효소. 제품 출하 전 chromatography로 제거.
8. **사업화 시나리오 1줄**: mRNA CDMO·biotech에 dsRNA-specific 차세대 nuclease + ssRNA off-target 회피 표준 워크플로 공급 (ShortCut RNase III 후속 시장 선점).
9. **잠재 경쟁자**: NEB ShortCut RNase III (E. coli RNase III + MBP fusion, 기존 표준), Aldevron dsRNA removal, TriLink dsRNA removal, AI-designed nuclease 진영 (Biomatter, Cradle).
10. **scope_judgement**: 명백 포함.
11. **lifecycle**: `new_at_round_2`.

---

### item_023 — TPD reagent cocktail (E1+E2+E3+DUB recombinant cascade)

(R1 §1.3 deferred → R2 부활)

1. **아이템명**: TPD (Targeted Protein Degradation) reagent cocktail — UBA1/UBA6 (E1) + UBE2D2/UBE2L3 (E2) + CRBN/VHL/MDM2/cIAP (E3) + USP7/USP5/USP28/OTUB1 (DUB) — TPD 모달리티 전체를 커버하는 in-vitro ubiquitin cascade screening 시약 라인.
2. **효소 클래스 / 단백질 패밀리**: 다중 EC — E1 (EC 6.2.1.45, ubiquitin-activating), E2 (EC 2.3.2.23, ubiquitin-conjugating), E3 (EC 6.3.2.-, ubiquitin ligase, RING/HECT/RBR class), DUB (EC 3.4.19.12, ubiquitin-specific peptidase).
3. **메커니즘**: E1이 ATP-dependent로 ubiquitin을 활성화 → thioester 결합으로 E2에 전달 → E3가 substrate (PROTAC ternary 또는 DUBTAC 경우 안정화 표적)에 ubiquitin 부착 → DUB가 ubiquitin chain 제거. 완전한 cascade 시약 패키지로 PROTAC·DUBTAC·molecular glue screening QC.
4. **포함기준 분류**: **진단·연구·산업 의약 인접** (TPD 모달리티 screening·QC).
5. **business_model**:
   - primary: **C** (Catalog reagent) — Promega·BPS·R&D Systems·Bio-Techne 류 catalog.
   - secondary: **K** (Kit / custom packaging) — 고객 표적별 E3·DUB 조합 cGMP kit.
   - rationale: 개별 효소(item_018, 019)는 단품 catalog로 진입; 본 cocktail은 풀 cascade 패키지로 상위 SKU 차별화.
6. **연결된 수요 신호**: R1 §1.3 (TPD 모달리티 학계 형성), R2 §1.1 (ARV-471 vepdegestrant FDA 승인 2026.5.1 — PROTAC 첫 신약 승인), R2 §4.3 (DUBTAC 모달리티화 + USP7/USP28 first-in-class), R2 §8.1 (Promega·BPS·R&D Systems 풀라인업 + Molecular Glue Degradation Agent Market $402M / CAGR 8.6%).
7. **임상 불필요성 판정 근거**: in-vitro TPD screening·QC 시약. 인체 투여 없음.
8. **사업화 시나리오 1줄**: PROTAC·DUBTAC·molecular glue 개발 빅파마·biotech·CRO에 ubiquitin cascade 풀 cocktail catalog + 표적별 custom kit 공급 (Promega·BPS·R&D Systems 통합 대안).
9. **잠재 경쟁자**: Promega (NanoBRET TE + Ternary Complex Starter Kits), BPS Bioscience (UBE1 80301, USP5 78832, USP7 79256), R&D Systems / Bio-Techne (UBE1 E-305·306·307), Boston Biochem (DUB 라인).
10. **scope_judgement**: 명백 포함. item_018, item_019의 상위 통합 패키지 카드로 위치.
11. **lifecycle**: `revived_from_round_1`.

---

### ~~item_024~~ — Engineered cutinase / LCC variant (PET 의약 포장)

- **lifecycle**: `merged_into_item_020`.
- **rationale**: R2에서 부활 권장된 카드와 신규 권장 item_020(Engineered LCC + cutinase + AI-PETase)이 동일 효소 패밀리·동일 응용(의약 PET 포장재 분해)에 속하므로, `scope/iteration_plan.md` §3 병합 규칙에 따라 더 작은 id인 item_020을 유지하고 본 카드는 폐기 표시. item_020 본문에 부활 카드 내용 흡수 표기.

---

## 메타

### lifecycle 분포

| lifecycle | 개수 | id |
|---|---|---|
| maintained_at_round_2 | 14 | item_001~014 |
| new_at_round_2 | 8 | item_015~022 |
| revived_from_round_1 (활성) | 1 | item_023 |
| merged_into_item_020 | 1 | item_024 |
| dropped_at_round_2 | 0 | — |
| **누적 활성** | **23** | — |

### business_model 분포 (primary 기준, 활성 23개)

| 코드 | 명칭 | 개수 | id |
|---|---|---|---|
| L | Licensing | 3 | item_003, item_007, item_008 |
| K | Kit/Reagent Sales | 11 | item_001, 002, 004, 005, 006, 009, 010, 011, 012, 013, 015, 021 (count=12 — 정정: 12) |
| C | Captive / Catalog | 7 | item_016, 017, 018, 019, 022, 023 (count=6 — 정정: 6) |
| S | Services / Custom Engineering | 2 | item_014, 020 |
| H | Hybrid | 0 | — |

**정정 집계**: L=3 / K=12 / C=6 / S=2 / H=0 → 합계 23. (K 분류에 item_021 포함, 본문 표기와 일치.)

### business_model 분포 (secondary 기준, 활성 23개)

- L: 6 (item_002, 005, 015, 020, 021, 023이 보조 L로 잡힘 — 부분 집계)
- K: 7 (item_003, 007, 008, 012, 016, 018→없음·재확인, 023)
- S: 3 (item_004, 009, 013)
- C: 0
- 미지정(—): 다수 (item_006, 010, 011, 014, 017, 019, 022)

(secondary는 카드별로 미지정 비율이 높아 분포는 참고용. 본 라운드는 primary 분포가 디제스트에서 핵심.)

### 포함기준 분류 분포 (활성 23개)

| 분류 | 개수 | id |
|---|---|---|
| 생산공정용 효소 | 8 | item_002, 003, 004, 005, 006, 007, 016, 017, 022 (count=9) |
| 제형변경 조력 | 2 | item_001, item_015 |
| 진단·연구·산업 의약 인접 | 9 | item_010, 011, 012, 013, 014, 018, 019, 020, 023 |
| 펩타이드 제조 | 3 | item_008, 009, 021 |
| 기타 | 0 | — |

**정정 집계**: 생산공정 9 / 제형변경 2 / 진단·연구·산업 9 / 펩타이드 3 / 기타 0 → 합계 23.

### 라운드별 흐름 요약

| 라운드 | 신규 | 부활 | 병합 | 드롭 | 유지 | 누적 활성 |
|---|---|---|---|---|---|---|
| R1 | 14 | 0 | 0 | 0 | — | 14 |
| R2 | 8 | 1 (활성) | 1 (item_024→020) | 0 | 14 | **23** |

### 특이 사항

1. **EfHyl8 (item_015)**: R1에서 [추정]이던 non-PH20 hyaluronate lyase가 학계에서 명시적 SC 확산 후보로 첫 명명 → item_001 (R1 기존 hyaluronidase 카드)의 경쟁구도가 R2에서 본격 변화. Phase C에서 item_001과 item_015의 점수 차이가 IP 우회 명분으로 좁혀질 가능성.
2. **TPD 패키지 구조**: item_018 (E3 ternary) + item_019 (DUB cocktail) + item_023 (전체 cascade cocktail) 3단 계층 구조로 분리. Phase C 스코어링에서 cross-cannibalization 평가 필요.
3. **item_021 vs item_003/008**: 효소 자체는 동일하지만 cGMP grade + radioligand 응용으로 별도 카드 유지. R3에서 단가·볼륨 정량화 시 통합 검토 가능.
4. **item_006 vs item_016**: T7 RNAP 단독 (R1) vs FCE::T7RNAP fusion (R2) — fusion이 단독 T7 RNAP를 cannibalize할 가능성. R3에서 협력/대체 시나리오 평가.
