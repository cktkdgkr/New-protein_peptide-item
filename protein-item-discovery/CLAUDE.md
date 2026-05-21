# CLAUDE.md — Common Operating Rules (모든 에이전트 공통)

이 문서는 protein-item-discovery 프로젝트의 모든 서브에이전트(landscape-scanner, candidate-generator, scorer, digest-writer)와 메인 Orchestrator가 따르는 공통 운영 규칙이다.

## 1. 목적
단백질·펩타이드 분야에서 **사업화 가능한 신규 아이템(주로 효소·기능성 단백질)** 을 발굴하고, 임상시험이 필요한 therapeutic API는 제외한 채 생산공정용·제형변경 조력·진단·연구·산업 효소 등을 후보로 정량 평가·요약하는 다단계 리서치를 수행한다.

## 2. 사실성·검증 규칙
- 모든 사실 주장(시장 동향, M&A·라이선싱 딜, 효소의 메커니즘·특성, 회사명·제품명 등)은 **web_search/WebSearch로 검증**하고 가능하면 **WebFetch로 원문 확인**한다.
- 모든 주장 옆에는 **출처(URL 또는 출처명)** 를 남긴다.
- 검증되지 않은 추정·해석은 반드시 `[추정]` 태그를 붙인다.
- 효소·단백질의 과학적 정확성(EC 분류, 메커니즘, 기질 특이성, 발현 시스템 등)을 우선한다. 불확실하면 "불확실"이라고 명시한다.
- 동일 주장이 여러 출처에서 모순될 경우 모순 사실 자체를 기록한다.

## 3. 통신 규약
- **서브에이전트는 서로 직접 통신하지 않는다.** 모든 데이터 전달은 아래 파일 경로를 통해서만 이뤄진다.
  - A(landscape-scanner) → `pipeline/01_landscape_scan.md`
  - B(candidate-generator) → `pipeline/02_candidates.md`
  - C(scorer) → `pipeline/03_scored.md`, `data/candidates.csv`, `candidates/item_NNN_<name>.md`
  - D(digest-writer) → `reports/digest_<YYYYMMDD>.md`
- 각 서브에이전트는 종료 시 다음 3가지를 수행한다:
  1. 지정된 산출 파일을 작성/갱신
  2. `state/run_state.json`에 자기 Phase 완료 기록 (timestamp, 산출 파일 경로, 간단한 메타)
  3. 메인 Orchestrator에게는 **3~5줄 요약**만 반환

## 4. 범위(Scope) 규칙
- 포함/제외 기준은 `scope/inclusion.md`, `scope/exclusion.md`를 단일 진실원천(SSOT)으로 따른다.
- 핵심 원칙: **임상시험을 거쳐야 하는 therapeutic API 그 자체는 제외.** 단 생산공정용·제형변경 조력 효소는 최종 제품이 약이어도 그 효소 자체는 임상 신약이 아니므로 포함.
- 경계 사례(borderline)는 반드시 판정 근거를 기록한다.

## 5. 산출물 품질 기준
- Landscape Scan: 최소 8개 이상의 demand signal, 각 signal에는 출처와 출처유형 태그(빅파마/학계/스타트업/인접산업/규제/CDMO 등).
- Candidate long-list: 10~15개. 5개 미만이면 품질 미달.
- Scoring short-list: 가중합 상위 5개 이상 권장.
- 모든 산출 마크다운은 한국어 우선, 고유명사·논문 제목·회사명·기술명은 원어 병기.

## 6. 운영 메타 규칙
- 검색 쿼리는 짧고 다수·다양하게. 영어/한국어 모두 활용. 같은 페이지를 두 번 fetch하지 않는다.
- 출처가 부족하거나 너무 한쪽에 치우치면 보강 검색을 추가로 수행한다.
- 토큰 한계로 인해 일부 후보를 누락한 경우 그 사실을 명시한다.

## 7. 파일 네이밍
- `candidates/item_NNN_<short_name>.md` — NNN은 001부터 zero-padding.
- `reports/digest_YYYYMMDD.md` — UTC 기준 실행일.
- `state/run_state.json` 스키마(예시):
```json
{
  "run_id": "YYYYMMDD-HHMM",
  "phases": {
    "A_landscape": {"status": "done|pending|failed", "output": "pipeline/01_landscape_scan.md", "ts": "...", "notes": "..."},
    "B_candidates": {"status": "...", "output": "pipeline/02_candidates.md", "ts": "...", "notes": "..."},
    "C_scoring":   {"status": "...", "output": "pipeline/03_scored.md", "ts": "...", "notes": "..."},
    "D_digest":    {"status": "...", "output": "reports/digest_YYYYMMDD.md", "ts": "...", "notes": "..."}
  }
}
```
