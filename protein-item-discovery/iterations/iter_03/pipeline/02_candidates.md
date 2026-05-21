# Candidate Long-list — Round 3, 2026-05-21

R3 focus: **Quantitative Refinement + IP/FTO + CDMO RFI**. 신규 후보 추가는 **0개** (강한 신규 신호는 모두 기존 23개 카드의 정량·IP 보강으로 흡수 가능). 핵심 작업은 누적 23개 카드의 정량 단가·시장규모·IP carve-out·CDMO RFI 신호 보강.

원칙: therapeutic API 자체 제외; 생산공정·제형변경·진단·연구·산업 효소만 (SSOT: `scope/inclusion.md`, `scope/exclusion.md`). R3 정량/IP 출처는 `iterations/iter_03/pipeline/01_landscape_scan.md`의 출처 키 체계를 따른다.

---

## 라운드 통계

- **유지(maintained_at_round_3)**: 23개 (item_001~023, 단 item_024는 R2에서 이미 merged).
- **신규(new_at_round_3)**: **0개**.
  - R3 §1의 Lonza Synaffix 통합 신호는 신규 카드(예: "enzymatic glycan-click hybrid kit") 분리보다는 item_005(EndoS2) + item_002(mTG) + item_021(sortase)에 RFI 신호로 흡수하는 것이 cannibalization 방지 측면에서 유리.
  - Araris RKAA-peptide linker는 item_002 mTG의 carve-out 변이체로 흡수 (별도 카드 분리 시 mTG 카드와 자기잠식).
  - 따라서 **신규 분리하지 않는다**는 의사결정을 명시.
- **부활**: 0건.
- **병합**: 0건.
- **드롭**: 0건. R3 정량/IP 정보로 명백히 out-of-scope이 된 후보 없음.
  - 경계 사례 재평가: item_001, item_010, item_013, item_020 모두 R3에서도 scope 유지 (상세 §R3 보강 카드 참조).
- **누적 활성 후보 수**: **23개** (변동 없음).

---

## R3 보강 요약 표 (23개)

각 후보별 R3 핵심 변경 1줄. 변경 없음(no_change)인 경우도 명시.

| id | 아이템 | R3 핵심 변경 (정량/IP/RFI/business_model) |
|---|---|---|
| item_001 | Next-gen hyaluronidase (PH20·non-PH20) | Halozyme FY25 royalty $867.8M 정량 확정 + Merck IPR 7건 청구 진행 → MDASE 일부 청구항 무효화 가능 모니터; Alteogen ALT-B4 2% royalty ceiling 정량 확보; scope_judgement: SC co-formulation 트랙으로 한정 유지 (단독 신약 out-of-scope) |
| item_002 ★ | Engineered mTG (ADC) | ADC TAM $13.51B→$32.66B 2035 (CAGR 9.23%) 정량; Ajinomoto AJICAP은 enzyme-free → carve-out; Zedira/Hzymes는 commodity GMP catalog; Araris RKAA-peptide linker는 native antibody에 engineering-free 적용 = mTG IP carve-out (US11786603 narrow-specificity 변이체); Samsung Bio (Phrontline·Araris 투자) RFI [H]; business_model 유지 K/L |
| item_003 ★ | Engineered Sortase A | Caltech US10202593B2 (eSrtA 7M/2A-9 Liu lab) carve-out 자명; NBE SMAC WO2014140317A1는 ADC sortase 별도 라인 (Boehringer 자본); commodity화 추세로 IP=3(M) 유지; 응용은 item_021(radioligand)·ADC 양쪽 driver |
| item_004 | FGE (aldehyde-tag) | R3 신규 정량 신호 미확보; aldehyde-tag dual-payload 진영은 Lonza Synaffix dpADC 발표로 간접 수혜 가능 (PoC), 단 enzymatic remodel route는 EndoS2 진영이 우세; no major change |
| item_005 ★ | EndoS2 glycosynthase | **Lonza Advanced Synthesis Synaffix GlycoConnect 2026-02-19 통합 = 빅 CDMO 표준 채택 공식 confirmation [H]** — EndoS2 enzymatic glycan remodel + click이 ADC GMP 라인 명시 step. dpADC 확장으로 W축 긍정. Genovis GlycINATOR 2,000 U research $979 catalog 확인; business_model: K/L 유지하나 L primary 격상 검토(Synaffix 라이선스가 매출의 핵심) |
| item_006 ★ | Engineered T7 RNAP | IVT enzyme TAM $1.2B (2024)→$2.5B (2033, CAGR 8.5%) [M]; GMP-Grade IVT 효소 $361.9M→$923M (CAGR 10.4%) [M]; TriLink CleanCap M6 cost race 압박 유지; 추가 강등 신호 없음, R2 강등(4.05→3.80) 그대로 유효 |
| item_007 ★ | Engineered RNA ligase | **Codexis–Merck $37.8M Supply Assurance Agreement 2025-10 [SEC 8-K H]** + Roche dsDNA ligase license $6.0M Q1-2024 인식; Bachem TIDES 2025 co-presentation; M축 confidence M→H 상향; IP=4(M→H) 상향 가능 |
| item_008 ★ | Peptiligase / OaAEP1 C247A | **US10883132B2 (Fresenius Kabi Ipsum) chemo-enzymatic GLP-1 청구항 패밀리 확인 [H]**; OaAEP1 (C13 family asparaginyl, cysteine protease) vs peptiligase (subtilisin BPN' Y217, S8 family serine protease) = fold·family·EC class 완전 다름 → carve-out 자명; PolyPeptide Vinnova 1M SEK 그린 GLP-1; FDA Research-Grade Peptide 2026.1 enforce; IP M→H, T M→H 상향 |
| item_009 ★ | Engineered PAM | R3 신규 정량 신호 미확보; GLP-1·radioligand C-term amide 의무 그대로; cGMP supplier 화이트스페이스 유지; no major change |
| item_010 | IdeS/IdeZ variant | R3 신규 신호 미확보; Genovis FabRICATOR 카탈로그 독점 구도 유지; scope_judgement 재평가: AAV redosing 연구 시나리오는 그대로 진단·연구 카테고리에 포함, no major change |
| item_011 | PNGase F + ST + GalT suite | R3 신규 신호 미확보; biosimilar glycan QC commodity catalog 그대로; no major change |
| item_012 | Cas12/Cas13 + RPA/Bst | R3 신규 신호 미확보; SHERLOCK/DETECTR 임상 진행은 R2 수준 유지; no major change |
| item_013 | High-fidelity Prime Editor | R3 신규 신호 미확보; scope_judgement 재평가: research/ex-vivo grade 한정으로 inclusion §2 (진단·연구) 유지. in-vivo gene editing therapeutic은 명시적 out-of-scope. no major change |
| item_014 | AI-designed RFdiffusion2/3 custom enzyme | R3 신규 신호 미확보; Baker lab + Biomatter 트렌드 그대로; no major change |
| item_015 | EfHyl8 PL8 hyaluronate lyase (non-PH20) | **Halozyme MDASE 청구항 PH20-specific (GH56 EC 3.2.1.35) vs EfHyl8 PL8 (EC 4.2.2.1 β-elimination) = fold·메커니즘·EC 완전 다름 → IP 회피 자명 [H]**; Merck IPR 7건 청구 → MDASE 일부 무효화 시 비PH20 진입장벽 더 낮아짐; PL8 family 학계 다양성 확장 (SinHL/TcHly8B/YsHyl8A); Alteogen 2% royalty ceiling 정량; EfHyl8 specific activity/kcat 미확보 (R4 과제) |
| item_016 | FCE::T7RNAP fusion | **NEB 패밀리 4국가 청구항 (CA3147797A1 + WO2021041260A1 + US20210054016A1 + AU2021424650A1) 확인 + H3C2 fusion 자체 청구 [H]**; 신규 진입자는 linker engineering·Cap-2·dual MTase fusion 등 architecture carve-out만 가능; IP=3(M) 유지 (강등 risk 약하게 존재) |
| item_017 | Inorganic pyrophosphatase | **Hzymes yeast PPase FDA DMF #036853 등록 = catalog 채택 확정 [H]**; GMP-Grade IVT $361.9M→$923M (CAGR 10.4%); 시장 혼잡 (NEB·Yeasen·Tinzyme·Hzymes·Canvax) → W=2 유지 |
| item_018 | CRBN/VHL E3 ternary | TPD TAM Grand View $544.4M (2024)→$1,685.3M (2030, CAGR 20.8%) [H, 3개 출처]; PROTAC reagent sub $152M→$331M (2033, CAGR 10.2%); Promega NanoBRET TE·BPS·R&D Systems·CST 99253·LifeSensors PA770 ($1.5k/kit 추정) 표준 catalog 다수 → W=2(H); cannibalization 메모(§아래) |
| item_019 | USP7/USP28/OTUB1 DUB cocktail | DUBTAC J. Med. Chem. 2025.3 종설 + USP28 first-in-class 진행; BPS/Boston Biochem catalog commodity; cannibalization 메모(§아래) |
| item_020 | LCC/cutinase + AI-PETase | R3 신규 정량 신호 미확보; Carbios Longlaville 50 kt/년 + 프랑스 €1,000/t bonus 그대로; scope_judgement 재평가: 의약 1차 포장재 시나리오로 한정 유지 (일반 PET 폐기물은 out-of-scope, ESG 의약 인접 경계 사례 명시) |
| item_021 | cGMP sortase/OaAEP1 (radioligand) | **Radioligand TAM $2.6B (2025)→$4.8B (2030, CAGR 13.1%) [H]**; AZ-Fusion $2.4B (2024-12 closing); Pluvicto+Lutathera 2024 ~$2.1B 매출; NBE SMAC WO2014140317A1는 ADC 영역, **radioligand peptide-chelator는 청구항 밖** → W=4(H) 정량 근거 강화; USPTO 10556024 sortase 18F는 chelator-tag 변이체로 carve-out 가능; IP=4(M→H) 상향 가능 |
| item_022 | dsRNA-specific engineered nuclease | R3 신규 신호 미확보; ShortCut RNase III off-target 보고 그대로; no major change |
| item_023 | TPD reagent cocktail (E1+E2+E3+DUB) | TPD 전체 $544M→$1,685M (Grand View [H]); MGD $402M은 별도 sub-segment 정량으로 재분류 → 패키지화 명분 강화; cannibalization 메모(§아래) |

R3 카드 보강된 항목 수: **23/23**. business_model 조정 검토 후보: **item_005 (K/L → L/K 격상 검토)**.

---

## R1·R2 카드 보강 (23개) — R3 보강 diff

각 카드의 11항목 중 R3에서 변경된 항목만 새 값으로 명시. 모든 카드 `lifecycle: maintained_at_round_3`.

### item_001 — Next-gen recombinant hyaluronidase (non-PH20 / PH20 변이체)

- **연결된 수요 신호 (R3 추가)**:
  - R3 §1 Halozyme FY25 royalty $867.8M 정량 확정 (DARZALEX SC $483M, VYVGART Hytrulo $157.2M, Phesgo $105.6M) `[Halozyme2025 FY]` `[H]`.
  - R3 §1·9.1 Halozyme vs Merck 소송 (2025-04) + Merck IPR 7건 청구 진행 — MDASE 일부 청구항 무효화 시 시장 dynamics 변동 가능 `[Halozyme2025 lawsuit]` `[FiercePharma2025 HALO-MRK]`.
  - R3 §2 Alteogen ALT-B4 2% royalty rate 정량 확정 (upfront $20M + milestones $432M, EvaluatePharma Keytruda SC peak $15.2B by 2030) `[Alteogen royalty 2%]` `[Biospectator2024 ALT-B4]` `[H]`.
- **사업화 시나리오 1줄 (R3 정량 갱신)**: ENHANZE 평균 royalty mid-single-digit + Alteogen 2% net sales가 차세대 SC 효소 협상 ceiling으로 정량화됨; biosimilar SC 전환 driver는 Halozyme $867.8M 분포로 명시.
- **잠재 경쟁자 (R3 IP 추가)**: Halozyme rHuPH20 (US 7,767,429 → 2027-09-23 만료, patent term adjustment 1,297 days), Alteogen ALT-B4 (Hybrozyme), Huonslab HYDIZYME; Merck IPR 7건 청구 진행 — 일부 청구항 무효화 시 후발주자 진입장벽 추가 하락.
- **scope_judgement (R3 재평가)**: 경계 사례 그대로 유지. SC co-formulation 트랙으로 한정; PH20 단독 신약 시나리오는 out-of-scope. R3 정량으로 시장 driver 명확.
- **lifecycle**: `maintained_at_round_3` (Halozyme/Alteogen 정량 강화로 confidence 상향 가능 — R3 C에서 처리).

### item_002 — Engineered mTG (ADC site-specific) ★

- **연결된 수요 신호 (R3 추가)**:
  - R3 §1·7 Lonza Advanced Synthesis Synaffix 통합 (2026-02-19) + dpADC 확장 → mTG 진영 간접 수혜 `[Lonza2026 AS]` `[H]`.
  - R3 §3·9.7 Samsung Bio Phrontline·Araris·AimedBio 펀드 투자 = mTG 진영 자본 직접 유입 `[Samsung-Araris]` `[H]`.
  - R3 §8.1 ADC TAM $13.51B (2025) → $32.66B (2035, CAGR 9.23%) `[Towards Healthcare 2025 ADC]` `[GlobeNewswire 2025 ADC]` `[H]` (2개 교차).
  - R3 §5·9.3 Araris RKAA-peptide linker = native antibody에 engineering-free mTG 적용 `[ABT2025 Araris]` `[H]`.
- **사업화 시나리오 1줄 (R3 정량 갱신)**: ADC $13.51B→$32.66B 2035 시장에서 mTG enzyme catalog (quote-only, $5~15k/g 추정 유지 — `[Zedira MTG Handbook]` `[Samsung-Araris]` `[L→M]`) + Q-tag·RKAA-tag 라이선스 hybrid. Samsung Bio·Lonza·WuXi XDC 3대 ADC CDMO에 GMP enzyme + tag-design 패키지 공급.
- **잠재 경쟁자 (R3 IP carve-out 분석)**:
  - **Ajinomoto AJICAP** — enzyme-free chemical site-specific conjugation (Fc-affinity peptide reagent, Lys248/Lys288 targeting). **mTG가 아니므로 직접 IP 충돌 없음** `[AJICAP2023]` `[H]`. US10184011 등은 chemical conjugation 영역.
  - **Hzymes** — GMP mTG catalog (quote-only), DMF 등록 가능. commodity Streptomyces mTG.
  - **Zedira** — mTG handbook은 reference info 위주, 자체 권리 약함.
  - **Araris Biotech** — RKAA-peptide linker로 native antibody mTG 적용. Samsung Life Science Fund 투자받음. carve-out 가능 영역 `[ABT2025 Araris]` `[Araris MMAE CD79b]`.
  - 신규 변이체 청구항: **US11786603** (Optimized transglutaminase site-specific antibody conjugation), Cell Death Discovery 2024 새 Q-tag substrate — narrow-specificity mTG 변이체 white-space 존재.
- **business_model (R3 재검토)**: primary **K** / secondary **L** 유지. Samsung-Araris 자본 흐름은 L 가치를 지지하나 GMP catalog 단가 미공개로 primary 격상은 보류.
- **scope_judgement**: 명백 포함 (R3 변동 없음).
- **lifecycle**: `maintained_at_round_3`. (R3 C에서 IP=3→4(M→H), M=5(H)로 상향 가능 → 가중합 +0.10 → 4.30 예측.)

### item_003 — Engineered Sortase A ★

- **연결된 수요 신호 (R3 추가)**: R3 §1·3 Lonza Synaffix 통합으로 enzymatic conjugation 빅 CDMO 표준 진입 → sortase 진영 간접 RFI 신호 `[Lonza2026 AS]` `[H]`. WuXi XDC backlog $1.49B (+50.3% YoY) `[WuXi XDC 2025 FY]`.
- **잠재 경쟁자 (R3 IP 추가)**:
  - **Caltech US10202593B2** (evolved sortase eSrtA 7M / 2A-9 가속변이체, David Liu lab) — sortase variant 핵심 청구항.
  - **NBE SMAC WO2014140317A1** (Boehringer Ingelheim Venture Fund 투자) — ADC sortase 영역, NBE-002 임상.
  - **USPTO 10556024** — sortase 18F radiolabeling (chelator-tag 변이체로 carve-out 가능).
  - 일반 sortase mediated conjugation은 commodity화 추세 — variant 라이선스가 핵심.
- **business_model**: primary **L** / secondary **K** 유지.
- **scope_judgement**: 명백 포함.
- **lifecycle**: `maintained_at_round_3`. IP=3(M) 유지, 점수 변동 없음.

### item_004 — FGE (aldehyde-tag dual-payload ADC)

- **연결된 수요 신호 (R3 추가)**: R3 §1 Lonza dpADC (dual-payload ADC) 발표 → FGE aldehyde-tag dual-payload 진영 간접 PoC 신호 `[Synaffix2026 dpADC]`. 다만 enzymatic remodel route는 EndoS2 진영이 우세.
- **잠재 경쟁자 (R3 추가)**: Synaffix dpADC dual-warhead 진영 (Lonza/BMS 라이선스)가 dual-payload 시장의 메인 경쟁축으로 자리잡음.
- **lifecycle**: `maintained_at_round_3`. 점수 변동 신호 없음.

### item_005 — EndoS2 glycosynthase mutant ★

- **연결된 수요 신호 (R3 추가)**:
  - **R3 §1·7 Lonza Advanced Synthesis 통합 (2026-02-19): Synaffix GlycoConnect (EndoS2/GalT remodel + click) + HydraSpace + toxSYN linker 완전 통합 + dpADC 확장 = 빅 CDMO ADC 표준 채택 공식 confirmation** `[Lonza2026 AS]` `[ADCReview2026 Lonza]` `[Synaffix2026 dpADC]` `[H]`. **이 단일 신호가 R3 전체에서 EndoS2 진영에 가장 결정적.**
  - R3 §8.2 Genovis GlycINATOR 2,000 U lyo $979 (research grade), GMP는 quote-only `[Genovis GlycINATOR]`.
  - R3 §8.1 ADC TAM $13.51B→$32.66B 2035 (CAGR 9.23%) `[H]`.
- **사업화 시나리오 1줄 (R3 정량 갱신)**: ADC $13.51B→$32.66B 2035 시장에서 EndoS2 enzymatic glycan remodel + click handle 패키지를 Lonza Synaffix 라이선스 모델 또는 carve-out 변이체(D184M 등) catalog로 공급. cGMP enzyme 단가 $5~15k/g 유지 (`[Genovis GlycINATOR]` 기준).
- **잠재 경쟁자 (R3 IP carve-out)**:
  - **Synaffix GlycoConnect** = Lonza/BMS 라이선스 (Lonza 2023 인수 후 2026-02 완전 통합).
  - **Genovis FabRICATOR-Z / GlycINATOR** = EndoS2 D184M 등 다른 변이체로 carve-out 여지 존재.
  - 신규 진입자는 Synaffix 라이선스 외 EndoS2 변이체 IP 또는 다른 endoglycosidase fold (EndoF, EndoH) 카브 가능.
- **business_model (R3 재검토)**: 현행 K/L 유지하되 **Lonza Synaffix 통합 시점에서 라이선스 매출의 비중이 K(catalog)보다 커질 가능성** — R3 C에서 L primary 격상 정량 근거 추가 검토. 일단 K/L 유지하고 R3 C 보고를 통해 정량적으로 결정.
- **scope_judgement**: 명백 포함.
- **lifecycle**: `maintained_at_round_3`. **R3에서 가장 큰 상승 잠재력 후보** — M축 M→H 상향, W축 3→4 가능. raw score 3.95 유지하나 rank stability 강화. business_model 격상 검토는 R3 C 결과 후.

### item_006 — Engineered T7 RNAP ★

- **연결된 수요 신호 (R3 추가)**:
  - R3 §8.1 IVT enzyme TAM $1.2B (2024) → $2.5B (2033, CAGR 8.5%) `[Verified Markets 2025 IVT]` `[M]`. GMP-Grade IVT 효소 $361.9M (2024) → $923.0M (2034, CAGR 10.4%) `[InsightAce GMP-IVT]` `[M]`.
  - R3 §8.2 Aldevron Codex HiCap GMP-Grade T7 RNAP (quote-only) + NEB Hi-T7 RNAP (research) — TriLink CleanCap M6 cost race 압박 유지 `[Aldevron Codex HiCap]` `[NEB M0658]`.
- **사업화 시나리오 1줄**: 변동 없음. catalog 가격 quote-only → $5~30k/g 추정 유지 `[M]`.
- **잠재 경쟁자 (R3 추가)**: Aldevron Codex HiCap는 directed-evolution variant (Cap-1 incorporation 향상) — 별도 라인. NEB Hi-T7는 thermostable variant. fusion 진영(item_016)과는 cannibalize 또는 협력 가능.
- **lifecycle**: `maintained_at_round_3`. R2 강등(4.05→3.80) 그대로 유지, 추가 강등 신호 R3에서 미발견.

### item_007 — Engineered RNA ligase ★

- **연결된 수요 신호 (R3 추가)**:
  - **R3 §2·9.2 Codexis–Merck $37.8M non-dilutive Supply Assurance Agreement (2025-10) — ECO Synthesis + ligase 비즈니스 확장** `[SEC 8-K Codexis 2025Q3]` `[H]`. 2027까지 runway 연장.
  - R3 §9.2 Codexis Q1 2025 첫 ECO Synthesis 수주 + Roche dsDNA ligase $6.0M Q1-2024 인식 + Bachem TIDES 2025-05 co-presentation `[Codexis Q1-2025]` `[H]`.
- **사업화 시나리오 1줄 (R3 정량 갱신)**: $3~12k/g 추정 유지 (Codexis catalog 없이 라이선스+서비스) — Codexis–Merck $37.8M (Q3 2025) + Roche $6.0M (Q1 2024) 인식이 라이선싱 수익화 정량 증거.
- **잠재 경쟁자 (R3 IP)**: Codexis는 site-saturation mutagenesis variant 라이브러리로 청구 → T4 Rnl2/RtcB scaffold 자체는 commodity, variant 청구항 carve-out 가능. Roche dsDNA ligase 글로벌 라이선스 확인.
- **business_model**: primary **L** / secondary **K** 유지. Codexis 모델이 L 매출 검증.
- **lifecycle**: `maintained_at_round_3`. R3 C에서 M축 confidence M→H 상향, IP=4(M→H) 상향 가능. raw score 변동은 W 4→5 (radioligand 별도 영역) 시 +0.05 정도.

### item_008 — Peptiligase / OaAEP1 C247A ★

- **연결된 수요 신호 (R3 추가)**:
  - **R3 §9.4 US10883132B2 (Fresenius Kabi Ipsum, 2023-01 EnzyPep 양도) chemo-enzymatic semaglutide/liraglutide/GLP-1 청구항 패밀리 확인** `[US10883132B2 Fresenius]` `[H]`.
  - R3 §3·9.7 Bachem CEPS technology webinar + Codexis TIDES co-presentation `[Bachem CEPS]` `[Codexis Q1-2025]` `[H]`.
  - R3 §8.3 PolyPeptide Vinnova 1M SEK 그린 GLP-1 grant (12개월, 2025) `[PolyPeptide Vinnova]` `[H]`. Bachem $1B+ CapEx 2024-25 GLP-1 확장 `[Bachem GLP-1]`.
  - R3 §1.x FDA Research-Grade Peptide guidance 2026-01 enforce 그대로 유효.
- **사업화 시나리오 1줄 (R3 정량 갱신)**: $2~10k/g 추정 유지 `[EnzyTag2025]` `[Bachem CEPS]` `[M]` — EnzyPep CEPS는 SPPS 대비 비용 -50%, 수율 >2x. Bachem·PolyPeptide GLP-1 CapEx 확장 + Fresenius EnzyPep IP 패밀리로 라이선스 ceiling 확인.
- **잠재 경쟁자 (R3 IP carve-out)**:
  - **EnzyPep peptiligase** = subtilisin BPN' Y217 variant (**S8 family serine protease**); US10883132B2 Fresenius Kabi Ipsum 패밀리.
  - **OaAEP1 C247A** = Oldenlandia affinis butelase family, **C13 family asparaginyl endopeptidase (cysteine protease)**; US11795488B2 enzymatic peptide ligation methods + Nature Comm Chem 2024 engineered recognition motifs.
  - **두 효소는 fold·family·EC class·메커니즘 완전 다름 → 청구항 carve-out 자명** `[H]`.
- **business_model**: primary **L** / secondary **K** 유지. EnzyTag/EnzyPep 모델 + Bachem 채택.
- **lifecycle**: `maintained_at_round_3`. R3 C에서 IP=4(M→H), T=4(M→H) 상향 → raw score 4.30 유지, rank stability 강화 (top 1 유지 예상).

### item_009 — Engineered PAM ★

- **연결된 수요 신호 (R3 추가)**: R3 §8.1 GLP-1 CDMO 시장 확장 (InsightAce, Bachem $1B+ CapEx) → GLP-1·radioligand C-term amide 수요 그대로. cGMP supplier 화이트스페이스 그대로 (구체 GMP enzyme 단가 신호 미확보, $10~50k/g 추정 유지).
- **lifecycle**: `maintained_at_round_3`. 변동 없음.

### item_010 — IdeS/IdeZ variant

- **연결된 수요 신호 (R3 추가)**: WuXi XDC backlog $1.49B → mAb/ADC QC 수요 간접 수혜 `[WuXi XDC 2025 FY]`.
- **scope_judgement (R3 재평가)**: 진단·연구·산업 (FabRICATOR-class QC + AAV redosing 연구)로 유지. ex-vivo therapeutic IdeS는 명시적 out-of-scope (Hansa Biopharma Idefirix는 임상 신약).
- **lifecycle**: `maintained_at_round_3`. 변동 없음.

### item_011 — PNGase F + ST + GalT suite

- **연결된 수요 신호 (R3 추가)**: 변동 없음 (biosimilar glycan QC commodity 그대로).
- **lifecycle**: `maintained_at_round_3`. 변동 없음.

### item_012 — Cas12/Cas13 + RPA/Bst set (POC molecular Dx)

- **연결된 수요 신호 (R3 추가)**: 변동 없음.
- **lifecycle**: `maintained_at_round_3`. R2 하위권 (4.05 가중합 미달) 그대로 유지.

### item_013 — High-fidelity Prime Editor

- **scope_judgement (R3 재평가)**: research/ex-vivo grade 한정으로 inclusion §2 (진단·연구) 포함. **in-vivo gene editing therapeutic은 명시적 out-of-scope** — Prime Medicine 임상 자체는 제외 대상이나 효소(vPE + engineered MMLV-RT) 자체는 catalog 가능. 경계 사례 명시.
- **lifecycle**: `maintained_at_round_3`. 변동 없음.

### item_014 — AI-designed RFdiffusion2/3 custom enzyme

- **연결된 수요 신호 (R3 추가)**: 변동 없음 (R3에서 Biomatter/Cradle 추가 신호 미확보).
- **lifecycle**: `maintained_at_round_3`. 변동 없음.

### item_015 — EfHyl8 PL8 hyaluronate lyase (non-PH20)

- **연결된 수요 신호 (R3 추가)**:
  - **R3 §9.1 Halozyme MDASE 청구항 PH20-specific (US 7,767,429 → 2027-09-23 만료), Merck IPR 7건 청구 진행 → 일부 무효화 시 비PH20 진입장벽 더 낮아짐** `[Halozyme rHuPH20 patent]` `[Halozyme2025 lawsuit]` `[H]`.
  - R3 §1·8.3 Alteogen 2% royalty rate ceiling 정량 (Keytruda SC peak $15.2B by 2030 = 연 $300M 로열티) → 비PH20 후발주자 협상 ceiling 확인 `[Alteogen royalty 2%]` `[H]`.
  - R3 §4 PL8 family 학계 다양성 확장 — SinHL (JAFC 2025), TcHly8B (pH 3~10.6 안정, 70°C optimal), YsHyl8A (alkalophilic, cold-adapted) `[JAFC2025 SinHL]` `[Mol Cell Probes 2021 TcHly8B]` `[YsHyl8A 2022]` `[H]`.
- **사업화 시나리오 1줄 (R3 정량 갱신)**: SC 전환 mAb·biosimilar 시장 (Halozyme $867.8M FY25 royalty)에서 비PH20 PL8 lyase로 IP 회피 옵션 공급 — Alteogen 2% 또는 mid-single-digit royalty ceiling.
- **잠재 경쟁자 (R3 IP 추가)**:
  - **Halozyme rHuPH20**: PH20 (GH56, EC 3.2.1.35 hyaluronoglucosaminidase) — MDASE 패밀리 청구항 US 7,767,429 (patent term adjustment 1,297 days → 2027-09-23 만료). Merck IPR 7건 진행.
  - **Alteogen ALT-B4**: Hybrozyme variant, 2% net sales royalty (Keytruda SC).
  - **Huonslab HYDIZYME**: 3rd-tier PH20.
  - **EfHyl8 (PL8, EC 4.2.2.1 β-elimination)**: fold·메커니즘·EC class 완전 다름 → **MDASE 청구항 회피 자명** `[H]`.
- **scope_judgement (R3 재평가)**: 경계 사례 유지. SC co-formulation 트랙으로 한정. EfHyl8 단독 신약 시나리오는 out-of-scope. R3에서도 명시.
- **lifecycle**: `maintained_at_round_3`. R3 C에서 IP=4(H) 유지/강화. EfHyl8 자체 specific activity/SC diffusion zone cm² 정량값은 미확보 (R4 과제).

### item_016 — FCE::T7RNAP fusion

- **연결된 수요 신호 (R3 추가)**: R3 §8.1 IVT 시장 $1.2B→$2.5B, GMP-IVT $361.9M→$923M. TriLink CleanCap M6 chemical analog 강세 유지.
- **잠재 경쟁자 (R3 IP 추가)**:
  - **NEB Faustovirus 패밀리 4국가 청구항**: CA3147797A1 + WO2021041260A1 + US20210054016A1 + AU2021424650A1. "H3C2 fusion" (FCE-T7RNAP arrangement) 자체 청구. up to 90~95% Cap-1 incorporation.
  - 신규 진입자 carve-out 영역: **linker engineering, Cap-2 추가, dual MTase fusion** 등 새 architecture만 가능 `[H]`.
  - Aldevron Codex HiCap는 directed-evolution T7 RNAP variant — 별도 라인.
- **business_model**: primary **C** / secondary **K** 유지.
- **lifecycle**: `maintained_at_round_3`. IP=3(M) 유지하나 **강등 risk 약하게 존재** (NEB 패밀리 청구 범위 확대 시).

### item_017 — Inorganic pyrophosphatase (IVT helper)

- **연결된 수요 신호 (R3 추가)**:
  - **Hzymes yeast PPase FDA DMF #036853 등록 = catalog 채택 확정 데이터** `[Hzymes DMF036853]` `[H]`.
  - R3 §8.1 GMP-Grade IVT $361.9M (2024) → $923M (2034, CAGR 10.4%) `[InsightAce GMP-IVT]` `[M]`.
- **사업화 시나리오 1줄 (R3 정량 갱신)**: GMP-IVT $361.9M→$923M 시장에서 non-animal yeast PPase OEM 또는 captive 공급 (Hzymes DMF #036853이 채택 검증).
- **잠재 경쟁자 (R3 추가)**: NEB Inorganic PPase, Hzymes yeast PPase (DMF #036853), Synthego, Canvax, Yeasen, Tinzyme — 시장 혼잡 (W=2 유지).
- **lifecycle**: `maintained_at_round_3`. M축 confidence H 유지. 변동 없음.

### item_018 — CRBN/VHL E3 ligase ternary complex assay reagent

- **연결된 수요 신호 (R3 추가)**:
  - R3 §8.1 TPD TAM Grand View $544.4M (2024) → $1,685.3M (2030, CAGR 20.8%), SNS Insider → $2,216M (2032), MGD CAGR 9.2% `[Grand View 2024 TPD]` `[SNS Insider TPD]` `[Emergen MGD]` `[H]` (3개 교차).
  - R3 §8.1 PROTAC reagent (협의) $152M (2025) → $331M (2033, CAGR 10.2%) `[SkyQuest PROTAC]` `[StockTitan PFE]` `[M]`.
  - R3 §8.2 LifeSensors PA770 PROTAC in-vitro ubiquitination assay kit (~$1.5k/kit 추정), Promega NanoBRET TE, CST 99253 E3 sampler `[LifeSensors PA770]` `[Promega NanoBRET]` `[CST 99253]` `[M]`.
- **사업화 시나리오 1줄 (R3 정량 갱신)**: PROTAC reagent $152→$331M (2033) 시장에서 Promega·BPS·R&D Systems·CST·LifeSensors 대안으로 CRBN/VHL ternary kit 공급. ~$1.5k/kit 단가 ceiling.
- **잠재 경쟁자 (R3 추가)**: Promega NanoBRET TE + Ternary Complex Starter Kits, BPS Bioscience, R&D Systems (UBE1 E-305·306·307), CST 99253 PROTAC E3 Ligase Profiling Antibody Sampler Kit, LifeSensors PA770 PROTAC kit. 표준 catalog 다수 → W=2(H) 유지.
- **cannibalization 메모 (R3)**: item_019 (DUB cocktail) + item_023 (전체 cascade) 동일 고객 SKU 자기잠식 risk. PROTAC reagent sub $152M은 item_018만의 sub-segment로 재분류; TPD 전체 $544M은 cascade 패키지(item_023) 명분. **§TPD trio cross-cannibalization 메모 참조**.
- **lifecycle**: `maintained_at_round_3`. M축 H 유지. 변동 없음.

### item_019 — USP7/USP28/OTUB1 DUB cocktail (DUBTAC reagent)

- **연결된 수요 신호 (R3 추가)**: R3 §8.1 TPD $544M→$1,685M (CAGR 20.8%), MGD $402M sub-segment 별도 재분류 `[H]`.
- **잠재 경쟁자 (R3 추가)**: BPS Bioscience (USP5 78832, USP7 79256), R&D Systems / Bio-Techne, Boston Biochem DUB 라인. W=2 유지.
- **cannibalization 메모 (R3)**: §아래 TPD trio 메모 참조. DUB sub-segment 정량 신호는 R3에서 별도 미확보 — DUBTAC 모달리티 형성 단계.
- **lifecycle**: `maintained_at_round_3`. 변동 없음.

### item_020 — Engineered LCC/cutinase + AI-PETase

- **연결된 수요 신호 (R3 추가)**: R3에서 신규 정량 신호 미확보. Carbios Longlaville 50 kt/년 + Wankai JV + 프랑스 €1,000/t bonus 그대로 유지.
- **scope_judgement (R3 재평가)**: 경계 사례. **의약 1차 포장재 시나리오 (vial·blister·multilayer)로 한정**. 일반 PET 폐기물 분해 (음료 PET, 의류 PET)는 inclusion §4 (의약 인접 ESG)의 범위 밖 → out-of-scope. 본 카드는 의약 포장재 적용으로만 점수 계산.
- **lifecycle**: `maintained_at_round_3` (item_024 흡수 상태 그대로). 변동 없음.

### item_021 — cGMP sortase A / OaAEP1 (radioligand peptide-chelator)

- **연결된 수요 신호 (R3 추가)**:
  - **R3 §8.1 Radioligand therapy $2.6B (2025) → $4.8B (2030, CAGR 13.1%), Lu-177 87.8% 점유, Pluvicto+Lutathera 2024 ~$2.1B** `[GlobeNewswire 2026 RLT]` `[Precedence RLT]` `[H]`.
  - R3 §1·8.3 AZ–Fusion $2.4B 인수 (2024-12 closing), Aktis Phase 0, PeptiDream 두번째 program `[AZ2024 Fusion]` `[H]`.
  - R3 §9.6 NBE SMAC WO2014140317A1는 ADC sortase 영역, **radioligand peptide-chelator는 청구항 밖** → W=4(H) 정량 근거 강화 `[H]`. USPTO 10556024 sortase 18F는 chelator-tag 변이체로 carve-out 가능.
- **사업화 시나리오 1줄 (R3 정량 갱신)**: Radioligand $4.8B 2030 시장에서 cGMP sortase A·OaAEP1 + chelator-tag (DOTA·DOTAGA·NETA·NOTA) 표준 워크플로 공급. catalog 가격 미공개 (`[NBE SMAC]` `[Genscript Sortase]` `[L]`).
- **잠재 경쟁자 (R3 IP 추가)**:
  - **NBE SMAC** (WO2014140317A1, Boehringer Ingelheim) — ADC 영역 한정. NBE-002 임상.
  - **USPTO 10556024** — sortase 18F radiolabeling, chelator-tag 변이체로 carve-out 가능.
  - **EnzyTag/EnzyPep peptiligase** — peptide ligation 영역이나 radioligand 응용 미확정.
  - radioligand peptide-chelator 직접 경쟁자 미확정 — white-space 확인 `[H]`.
- **business_model**: primary **K** / secondary **L** 유지.
- **lifecycle**: `maintained_at_round_3`. R3 C에서 IP=4(M→H), W=4→5 가능성 → 가중합 +0.15 → 4.25 예측. **R3에서 가장 큰 raw score 상승 잠재력 후보 중 하나** (item_005 다음).

### item_022 — dsRNA-specific engineered nuclease

- **연결된 수요 신호 (R3 추가)**: 변동 없음. ShortCut RNase III off-target J. Chromatogr. 2024.12 종설 그대로.
- **lifecycle**: `maintained_at_round_3`. 변동 없음.

### item_023 — TPD reagent cocktail (E1+E2+E3+DUB)

- **연결된 수요 신호 (R3 추가)**:
  - **R3 §8.1 TPD 전체 시장 정량 확정 — Grand View $544.4M (2024) → $1,685.3M (2030, CAGR 20.8%), SNS Insider → $2,216M (2032), MGD CAGR 9.2%** `[Grand View 2024 TPD]` `[SNS Insider TPD]` `[Emergen MGD]` `[H]` (3개 출처 교차).
  - R2 $402M은 MGD reagent sub-segment 추정으로 재분류 — **TPD 전체와 구분**, 패키지화(item_023) 명분 강화.
  - R3 §8.2 LifeSensors PA770 ~$1.5k/kit, Promega NanoBRET TE, CST 99253.
- **사업화 시나리오 1줄 (R3 정량 갱신)**: TPD $544M→$1,685M 2030 시장에서 E1+E2+E3+DUB 통합 cascade cocktail catalog + 표적별 custom kit 공급 (Promega·BPS·R&D Systems 통합 대안).
- **cannibalization 메모 (R3)**: §아래 TPD trio 메모 참조.
- **lifecycle**: `maintained_at_round_3`. M축 H 유지. R3 정량 강화로 confidence 상향.

---

## R3 신규 카드

**없음 (0개)**. 

신규 후보 추가 미실행 사유:
1. R3 §1 Lonza Synaffix 통합 신호는 **item_005 EndoS2 + item_002 mTG + item_003 sortase + item_021 sortase**에 RFI 신호로 흡수. "enzymatic glycan-click hybrid kit" 같은 신규 카드 분리 시 item_005와 cannibalize.
2. R3 §5 Araris RKAA-peptide linker는 **item_002 mTG의 carve-out 변이체**로 흡수. 별도 카드 분리 시 mTG 후보군과 cannibalize.
3. R3 §3 Samsung Bio·WuXi XDC RFI 신호는 기존 ADC 후보(item_002·003·004·005·021)에 분산 흡수.
4. R3 §9 IP/FTO 신호는 모두 기존 후보 IP 분석에 흡수.
5. R3에서 발견된 효소·단백질 신규 카테고리 자체는 없음 — R3는 quantitative refinement focus로 정량/IP/RFI 정보만 제공.

→ **누적 활성 23개 유지**.

---

## TPD trio cross-cannibalization 메모 (item_018·019·023)

R3 정량/IP 정보로 재평가.

### 시장 정량 (R3)
| 항목 | 2024~2025 | 2030~2033 | CAGR | 출처 | confidence |
|---|---|---|---|---|---|
| TPD 전체 (drug + reagent) | $544.4M (2024) | $1,685.3M (2030) | 20.8% | `[Grand View 2024 TPD]` `[SNS Insider TPD]` `[Emergen MGD]` | H (3개 교차) |
| MGD (Molecular Glue Degrader) | — | — | 9.2% | `[Emergen MGD]` | M |
| PROTAC reagent (협의) | $152M (2025) | $331M (2033) | 10.2% | `[SkyQuest PROTAC]` `[StockTitan PFE]` | M |

R2의 $402M 단일출처 표기는 **MGD reagent sub-segment** 추정으로 재분류 — TPD 전체와 구분.

### 카드별 위치 + cannibalization 분석
- **item_018 (CRBN/VHL E3 ternary)**: PROTAC reagent sub $152→$331M의 핵심. Promega NanoBRET TE + LifeSensors PA770 표준 catalog (~$1.5k/kit). 단품 catalog 진입.
- **item_019 (USP7/USP28/OTUB1 DUB cocktail)**: DUBTAC 모달리티 형성 단계, R3에서 별도 시장 정량 미확보. BPS·Bio-Techne·Boston Biochem catalog commodity. 단품 DUB SKU.
- **item_023 (E1+E2+E3+DUB 전체 cocktail)**: TPD 전체 $544→$1,685M 패키지화 명분 강화. 상위 SKU 통합 cascade 패키지 + cGMP custom kit.

### 자기잠식 평가
- **item_018·019 (sub-segment 단품) vs item_023 (전체 패키지)**: 동일 고객(PROTAC·DUBTAC·molecular glue 개발 biotech)이지만 **SKU tier가 다름**.
  - item_018·019 = research-grade catalog (단가 ~$1.5k/kit, throughput 위주).
  - item_023 = 풀 cascade + 표적별 custom kit (단가 ~$5~10k/패키지, R&D 워크플로 전체).
- **결론**: R3 정량으로는 **패키지화(item_023)가 더 유리한 신호** (TPD 전체 시장이 sub-segment 합보다 크고 CAGR 더 높음 — 20.8% vs 10.2%).
- **권고**: 3개 카드 모두 유지. **병합·드롭 없음**. R3 C 스코어링에서 item_023의 M축이 item_018·019보다 약간 높게 평가될 가능성 — Phase D에서 상위 패키지 SKU(item_023)를 메인 enabler로, 하위 단품(item_018·019)을 보조 SKU로 positioning 권장.
- **cannibalization risk 정량**: 동일 고객 동시 수주율 ~30-50% 추정 (단품 catalog는 throughput, 패키지는 strategic 워크플로) — 자기잠식보다는 **상하 SKU tier 보완** 구조로 해석. 따라서 **별도 카드 유지가 더 유리**.

---

## 메타

### lifecycle 분포 (R3 종료시점)

| lifecycle | 개수 | id |
|---|---|---|
| maintained_at_round_3 | 23 | item_001~023 (24 제외) |
| new_at_round_3 | 0 | — |
| revived_at_round_3 | 0 | — |
| merged_at_round_3 | 0 | — |
| dropped_at_round_3 | 0 | — |
| (R2 기존) merged_into_item_020 | 1 | item_024 (활성 카운트 제외) |
| **누적 활성** | **23** | — |

### business_model 분포 (primary, 활성 23개)

| 코드 | 명칭 | 개수 | id |
|---|---|---|---|
| L | Licensing | 3 | item_003, item_007, item_008 |
| K | Kit/Reagent Sales | 12 | item_001, 002, 004, 005, 006, 009, 010, 011, 012, 013, 015, 021 |
| C | Captive / Catalog | 6 | item_016, 017, 018, 019, 022, 023 |
| S | Services / Custom Engineering | 2 | item_014, 020 |
| H | Hybrid | 0 | — |

R3 business_model 조정: **0건** (조정 검토 후보: item_005 K/L → L/K 격상 — R3 C 결과 후 재검토; 본 R3 B에서는 유지).

### business_model 분포 (secondary, 활성 23개) — 참고용
- L: 6 (item_002, 005, 015, 020, 021, 023)
- K: 7 (item_003, 007, 008, 012, 016, 018→없음, 023)
- S: 3 (item_004, 009, 013)
- C: 0
- 미지정: 다수 (item_006, 010, 011, 014, 017, 019, 022)

### 포함기준 분류 분포 (활성 23개)

| 분류 | 개수 | id |
|---|---|---|
| 생산공정용 효소 | 9 | item_002, 003, 004, 005, 006, 007, 016, 017, 022 |
| 제형변경 조력 | 2 | item_001, 015 |
| 진단·연구·산업 의약 인접 | 9 | item_010, 011, 012, 013, 014, 018, 019, 020, 023 |
| 펩타이드 제조 | 3 | item_008, 009, 021 |
| 기타 | 0 | — |

### 라운드별 흐름 요약

| 라운드 | 신규 | 부활 | 병합 | 드롭 | 유지 | 누적 활성 |
|---|---|---|---|---|---|---|
| R1 | 14 | 0 | 0 | 0 | — | 14 |
| R2 | 8 | 1 (활성) | 1 (item_024→020) | 0 | 14 | 23 |
| R3 | 0 | 0 | 0 | 0 | 23 | **23** |

### 특이 사항 (R3)

1. **item_005 EndoS2 = R3 최대 모멘텀**: Lonza Synaffix 통합으로 빅 CDMO 표준 채택 공식 confirmation. M·W 양쪽 confidence 상향 + business_model L primary 격상 검토 대상 (R3 C 결과 후).
2. **item_002 mTG IP carve-out 명확화**: Ajinomoto AJICAP은 enzyme-free 별도 카테고리 + Zedira·Hzymes commodity + Araris RKAA-peptide carve-out + US11786603 narrow-specificity 변이체 white-space. IP 3→4(M→H) 상향 가능.
3. **item_021 cGMP sortase radioligand**: NBE SMAC carve-out 명확화 + Radioligand $4.8B 2030 정량 확정으로 raw score +0.15 → 4.25 예측. 가장 큰 raw score 상승 후보.
4. **item_008 peptiligase vs OaAEP1 carve-out 자명**: 효소가 fold·family·EC class·메커니즘 완전 다름 — Fresenius US10883132B2 청구항이 OaAEP1을 직접 위협하지 않음. IP M→H, T M→H 상향. Top 1 (4.30) 유지 예상.
5. **item_015 EfHyl8 IP 회피 자명**: PL8 lyase vs PH20 glycosidase = fold·EC class 완전 다름. Merck IPR 7건 청구 진행이 추가 호재.
6. **item_006 T7 RNAP 추가 강등 없음**: R2 강등(4.05→3.80) 그대로 유효, R3에서 추가 약화 신호 미발견.
7. **item_016 FCE::T7RNAP fusion IP risk 모니터**: NEB 패밀리 4국가 청구 + H3C2 fusion 자체 청구 — IP 3→2 강등 risk 약하게 존재 (R3에서는 maintain).
8. **TPD trio (item_018·019·023) 병합·드롭 없음**: R3 정량으로 상하 SKU tier 보완 구조 — 별도 카드 유지가 더 유리.
9. **scope_judgement 경계 사례 재평가**: item_001 (SC co-formulation 한정), item_010 (FabRICATOR QC + AAV 연구 한정), item_013 (research/ex-vivo grade 한정), item_020 (의약 1차 포장재 한정) — 모두 R3에서도 inclusion 유지. **드롭 없음**.
10. **신규 후보 0개**: R3 신호는 모두 기존 카드에 흡수 가능, 별도 신규 분리 시 cannibalization risk가 더 큼.
