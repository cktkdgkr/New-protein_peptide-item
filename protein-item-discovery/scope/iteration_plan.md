# Iteration Plan — A→B→C→D 루프의 라운드별 초점

본 프로젝트는 같은 4-Phase 파이프라인(A landscape → B candidate → C scoring → D digest)을 **최소 3회 이상** 반복(loop)하여 사업화 후보 발굴의 정밀도를 점진적으로 높인다.

## 1. 루프 운영 원칙
- **최소 반복 횟수**: 3회. `state/run_state.json`의 `config.min_iterations = 3`.
- **자동 체이닝**: 한 라운드의 D(digest) 완료 시 `current_iteration < min_iterations`이면 메인 Orchestrator가 다음 라운드의 A를 자동으로 호출한다.
- **3회 완료 후**: 추가 라운드는 사용자 승인 후에만 진행. 단, 아래 quality-gate가 발동되면 메인이 사용자에게 확인 1회 후 즉시 R4를 제안한다.
- **각 라운드의 산출 위치**: `iterations/iter_NN/{pipeline,candidates,data,digest.md}` 폴더 (NN=두 자리 zero-pad).
- **누적(현행 상태) 산출**: 가장 최신 라운드의 점수가 `data/candidates_current.csv`로 미러됨. 라운드별 점수 변화는 `data/candidates_history.csv`에 append.

## 2. 라운드별 Focus

### Round 1 — Broad Scan (완료, 2026-05-21)
- focus: 단백질·펩타이드 효소의 demand signal을 가장 넓게 훑는다.
- 산출: `pipeline/01_landscape_scan.md`(루트), `pipeline/02_candidates.md`, `pipeline/03_scored.md`, `reports/digest_20260521.md` (이전 호환 위해 루트에 유지).
- 결과: 18 signal → 14 candidate → 7 short-list.

### Round 2 — Deferred & Boost Areas
- focus 1 (deferred 부활 검토): R1에서 시장 검증 부족으로 보류된 후보를 재스캔 후 보강.
  - TPD 관련 E3 ligase·deubiquitinase·E1·E2 시약 시장 (R1 §1.3).
  - PETase / MHETase / cutinase의 의약품 PET 포장재 ESG 시나리오 (R1 §6.4).
- focus 2 (Phase A 보강 검색 영역):
  - **non-PH20 hyaluronidase** — leech-derived hyaluronidase, 세균 hyaluronate lyase(PL8), chondroitinase 변이체의 SC 확산 잠재력.
  - **radioligand peptide-chelator의 enzymatic conjugation** — Pluvicto 후속 트렌드, PeptiDream/Aktis/Fusion 공정 발표, sortase/OaAEP1/subtiligase를 활용한 site-specific chelator-peptide 결합.
  - **mRNA capping / polyA enzyme 차세대 변이체** — vaccinia/faustovirus capping enzyme, polyA polymerase, RNase H/III 정제용 효소, IVT helper enzyme.
- focus 3 (Phase B 강화): 모든 후보 카드에 **사업화 형태(business_model)** 축 추가 — `scope/business_model_taxonomy.md` 참조 (L/K/C/S/H).
- focus 4 (Phase C 강화): R1에서 [추정]으로 표기된 단가·볼륨 수치를 `scope/pricing_sources.md` 화이트리스트 출처로 부분 정량화. 새 출처가 보강된 항목은 `confidence` 태그 상향.
- 산출 위치: `iterations/iter_02/`.

### Round 3 — Quantitative Validation & IP/FTO Deep-Dive
- focus 1: Short-list 7개(+ R2에서 추가된 후보) 각각에 대해 **단가·볼륨·시장 규모를 정량화**(가능한 한 [추정] 제거).
- focus 2: **IP / Freedom-to-Operate 분석**.
  - Halozyme vs Merck Keytruda SC 소송 진행 상황 + 핵심 청구항.
  - Codexis ECO Synthesis ligase 핵심 특허 청구항.
  - mTG cluster 특허(Ajinomoto, Hzymes, Zedira) 회피 여부.
  - EnzyPep peptiligase vs OaAEP1 C247A 청구항 비교.
  - NBE/Boehringer SMAC sortase 특허.
- focus 3: **CDMO RFI 가설** — Lonza Visp, Samsung Bio, WuXi XDC의 enzymatic conjugation 채택 의향에 대한 공개 신호(IR, JPM, 컨퍼런스 발표) 추적.
- focus 4: 라운드 종료 시 **consolidated_digest** 생성 — 점수 궤적 + confidence + 최종 ranking 안정성 평가.
- 산출 위치: `iterations/iter_03/`. 종료 시 `reports/consolidated_digest_<YYYYMMDD>.md` 생성.

### Round 4+ — Quality-Gate Triggered
다음 트리거 중 하나가 발생하면 메인이 사용자에게 1회 확인 후 R4를 제안한다.
- Phase A에서 새 빅파마 M&A 딜(≥$1B in scope)이 등장.
- Phase C에서 short-list 상위 5개의 가중합 표준편차가 R2→R3 사이 0.15 이상 변동.
- 외부 IP 분쟁 결과 공시(Halozyme vs Merck 등) 발생.
- 사용자의 명시적 신규 키워드 추가.

## 3. 라운드별 데이터 카드 규칙
- **신규 후보**: id를 직전 라운드 마지막 +1부터 부여 (R1 = item_001~014 → R2 신규는 item_015~).
- **부활(deferred → revived)**: 새 id 부여하지 않고 R1에서 사용했던 working name을 유지하되 `revived_from: round_N` 메모.
- **병합**: 동일 효소가 여러 후보로 분리돼 있던 경우 id 중 더 작은 쪽을 유지하고 다른 쪽 카드는 `merged_into: item_XXX`로 폐기 표시. 점수 재산정.
- **사망(drop)**: 신규 정보로 명백히 out-of-scope 판정 시 `dropped_at: round_N` 메모 후 점수 갱신 중단.

## 4. confidence 태그 정의 (Phase C 강화용)
각 6축 점수 옆에 `[confidence: H|M|L]`:
- **H (high)**: 출처 ≥3개, 정량 데이터(가격·시장규모) 보유, [추정] 없음.
- **M (medium)**: 출처 1~2개, 일부 정량 데이터, [추정] 일부.
- **L (low)**: 출처 1개 미만 또는 전적으로 [추정].

가중합은 변하지 않되, confidence 분포가 D agent의 final ranking 안정성 평가에 사용됨.
