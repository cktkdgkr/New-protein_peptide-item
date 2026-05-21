# Business Model Taxonomy — Phase B 사업화 형태 분류 축

Round 2부터 Phase B(Candidate Generator)는 모든 후보 카드에 아래 **사업화 형태(business_model)** 축을 필수로 기재한다. 한 후보가 여러 형태를 동시에 가질 수 있으므로 **primary + secondary** 두 단계로 표기.

## 분류 코드

| 코드 | 명칭 | 정의 | 대표 사례 |
|---|---|---|---|
| **L** | Licensing | 효소 단백질·균주·공정 IP를 외부에 라이선스. upfront + milestone + 로열티 구조. 자체 GMP 생산은 없거나 보조. | Halozyme ENHANZE, Alteogen Hybrozyme, Codexis CodeEvolver |
| **K** | Kit / Reagent Sales | GMP·Research-grade enzyme을 단위(mg/g/U)로 판매. catalog 또는 cGMP custom 모두 포함. | NEB(Hi-T7, BoxFastQ), Aldevron(T7 RNAP), Genovis(FabRICATOR) |
| **C** | CDMO Captive Use | 효소를 외부 판매하지 않고 자사 CDMO·CMO 공정에 내재화. capacity·gross margin 확보가 목적. | Lonza Visp bioconjugation 자체 효소, Bachem peptiligase 내재화 시나리오 |
| **S** | Services / Custom Engineering | "Custom enzyme as a service" — 고객 사양에 맞춰 효소를 설계·발현·검증해 IP 또는 enzyme을 deliver. | Biomatter, Cradle Bio, Generate Biomedicines |
| **H** | Hybrid | 위 모델 2개 이상을 패키지로 제공. | L+K (라이선스 + GMP kit 공급), K+S (kit + custom variant 서비스) 등 |

## Phase B 카드 기재 형식
```
business_model:
  primary: K
  secondary: L
  rationale: GMP enzyme kit 판매가 주력이며, ADC CDMO 라이선스가 보조 매출.
```

## Phase C 스코어링 영향
사업화 형태는 6축 점수에 다음과 같이 간접 반영된다 (Scorer가 참고):
- **L (Licensing)**: Time-to-revenue ↑ (계약 기반, 비교적 빠름), Whitespace는 IP 분쟁 위험으로 변동.
- **K (Kit/Reagent)**: Feasibility ↑ (catalog 채널 단순), Whitespace ↓ (혼잡한 catalog 시장 다수).
- **C (Captive)**: IP defensibility ↑ (내부 know-how), Market pull은 자사 capacity 의존.
- **S (Services)**: IP defensibility 양면, Time-to-revenue 양극화(빠른 PoC vs cGMP service 셋업).
- **H (Hybrid)**: 일반적으로 가중합 +0.1~0.2 효과 가능. 단 운영 복잡성으로 Feasibility -0.5 penalty 가능.

## Phase D 디제스트 영향
Digest Writer는 short-list을 사업화 형태별로 그룹화한 표를 추가한다 — 경영진이 "라이선스 vs 키트" 의사결정을 바로 할 수 있도록.

## 매핑 가이드 (R1 short-list 7개 사후 분류 예시)
| id | item | primary | secondary | 비고 |
|---|---|---|---|---|
| item_002 | Engineered mTG (ADC) | K | L | GMP enzyme kit + Q-tag 설계 라이선스 |
| item_003 | Engineered Sortase A | L | K | 라이선스 + tag 설계 컨설팅 + enzyme 공급 |
| item_005 | EndoS2 glycosynthase | K | L | enzyme + donor sugar 패키지 |
| item_006 | Engineered T7 RNAP | K | — | NEB/Aldevron 류 catalog 채널 |
| item_007 | Engineered RNA ligase | L | K | Codexis ECO 모델 |
| item_008 | Peptiligase / OaAEP1 C247A | L | K | EnzyTag/EnzyPep 모델 |
| item_009 | Engineered PAM | K | — | cGMP supplier 부재 → kit가 주력 |

이 사후 분류는 R2 Phase B가 공식화하고 카드에 기재해야 한다.
