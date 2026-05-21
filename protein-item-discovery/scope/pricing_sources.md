# Pricing & Volume Sources — Phase C 정량화 출처 화이트리스트

Round 2~3에서 Phase C(Scorer)는 R1에 `[추정]`으로 표기된 단가·볼륨·시장 규모를 아래 출처들로 정량화한다. 새 데이터가 확보된 항목은 `confidence` 태그를 H로 상향한다.

## 1. 시장 규모·예측 리포트
- **BCC Research** — 의약 효소·진단 효소 시장 리포트.
- **Markets and Markets** — Industrial Enzymes, Therapeutic Enzymes, IVT Enzymes 시장 보고.
- **GlobalData** — Pharma Intelligence, Forecasting (covered drugs of ADC/AOC/peptide).
- **EvaluatePharma / Evaluate Vantage** — 모달리티별 sales forecast, top 100 product forecasts.
- **IQVIA Institute** — Global Use of Medicines, biologics share·SC 전환 데이터.
- **Frost & Sullivan** — biopharma supplier 시장 보고.
- **Cortellis (Clarivate)** — pipeline, deal, licensing royalty data.
- **dataintelo / Verified Market Research / Grand View Research** — 단일 효소 시장 추정 (T7 RNAP, hyaluronidase 등).

## 2. 딜 / 라이선싱 가격 신호
- **BioPharma Catalyst** — 빅파마 딜 & 임상 마일스톤.
- **Endpoints News** — deal price 분석 기사.
- **Fierce Biotech / Fierce Pharma** — M&A 가치 분석.
- **BioSpace** — 라이선싱 deals tracker.
- **SEC EDGAR** — 8-K, 10-K 공시 (Codexis ECO Synthesis 첫 수주, Halozyme 로열티 분석 등 1차 자료).
- **Nature Biotechnology** "Deals of the Year" 연례 정리.

## 3. 가격표 / Catalog
- **NEB (New England Biolabs)** — T7 RNAP, ligase, PNGase F, EndoS2 등 가격 (단위 U당, mg당).
- **Aldevron / Maravai Life Sciences** — cGMP T7 RNAP, CleanCap.
- **Trilink Biotechnologies** — IVT enzyme, mRNA reagent.
- **Thermo Fisher (TranscriptAid)** — IVT kit.
- **Promega / Roche CustomBiotech / Sigma-Aldrich** — research-grade 효소.
- **Genovis** — FabRICATOR/Z, GlycINATOR 가격 + custom GMP rate.
- **GenScript / Twist** — custom enzyme production.
- **Bachem / PolyPeptide / CordenPharma** — peptide manufacturing cost (FTE rate, kg-scale pricing).

## 4. CDMO·플랫폼 IR 자료
- **Lonza** annual report, JPM Healthcare slides (bioconjugation capacity, gross margin).
- **Samsung Biologics** IR (ADC service rate).
- **WuXi Biologics / WuXi XDC** quarterly results.
- **Catalent / Recipharm / Piramal** financial reports.
- **Halozyme Therapeutics** 10-K (ENHANZE 로열티 breakdown).
- **Alteogen** investor presentations.

## 5. 인용 규칙
- Phase C 점수 옆에 출처 명을 `[BCC2025]`, `[NEB price 2026]`, `[SEC 8-K Codexis 2025Q1]` 같은 약식 키로 표기.
- 출처 키 → URL/문서명 매핑은 `iterations/iter_NN/pipeline/03_scored.md` 끝에 reference list로 정리.
- 동일 수치를 다른 출처가 확인하면 키 2~3개 나열 (confidence H).
- 단일 출처 + 추정 보강이면 `[BCC2025 + 추정]` 형식, confidence M.
- 출처 0개 [추정]만 있으면 confidence L.

## 6. 우선 정량화 대상 (R1 [추정] 항목 추출)
| 항목 | R1 [추정] 값 | R2~R3에서 확인할 출처 |
|---|---|---|
| ADC 시장 규모 $13.5B | bioworld 단일 | EvaluatePharma, IQVIA 교차 확인 |
| IVT 효소 시장 $1.8B→$3.9B (2034) | dataintelo 단일 | BCC, Markets&Markets |
| mTG enzyme $5~15k/g, upfront $1~5M | 전적 추정 | Codexis SEC, EnzyPep 보도자료 |
| OaAEP1 cGMP enzyme $2~10k/g | 전적 추정 | EnzyTag, PolyPeptide IR |
| Halozyme 2025 매출 $1.4B (+38%) | prnewswire | Halozyme 10-K (확정) |
| RNA ligase enzyme $3~12k/g | 전적 추정 | Codexis ECO 8-K |
| T7 RNAP cGMP $5~30k/g | 전적 추정 | Aldevron price list, NEB Hi-T7 |
| PAM enzyme $10~50k/g | 전적 추정 | Unigene 특허 만료 + GMP 발현 capex |
| Hyaluronidase 라이선스 royalty 비율 | 추정 | Halozyme 10-K royalty breakdown |
