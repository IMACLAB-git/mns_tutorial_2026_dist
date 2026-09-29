# 위키 목차

## 논문
- [Park2025](papers/Park2025.md) — 대상 논문. Field-programmable robotic folding sheet (Nat. Commun. 2025) · summarized
- [Yan2023](papers/Yan2023.md) — 쌍안정 origami 스위치로 센싱·연산·구동을 재료에 내장한 로봇 (Nat. Commun. 2023) · summarized
- [Zhang2023](papers/Zhang2023.md) — 한 모듈에서 7개 변형 모드를 고르는 plug-and-play 공압 origami 모듈 (Nat. Commun. 2023) · summarized
- [Johnson2023](papers/Johnson2023.md) — 셀별 HASEL 구동·자기 센싱·형상 폐루프를 갖춘 10 × 10 soft shape display (Nat. Commun. 2023) · summarized
- [Ni2022](papers/Ni2022.md) — 자기장 속 액체금속 리본의 Lorentz force로 연속 곡면을 만드는 형상 프로그래밍 표면 (Nat. Commun. 2022) · summarized

## 비교
- [matrix.md](matrix.md) — 논문 5편 × 7개 비교 축 (구동 원리, 외부 장치, 주소 지정, 센싱, 제어 루프, 속도, 형상)
- [rq.md](rq.md) — Park 2025의 공백 3개(G1–G3)와 RQ 후보 3개 · 모두 `후보`

## 개념
- [Field-programmability](concepts/field-programmability.md) — 배치 후 현장에서 형상 변형 구성을 다시 정하는 성질
- [공간 주소 지정 방식](concepts/spatial-addressing.md) — direct / matrix / networked domain 주소 지정. Park 2025 분류를 원문과 대조한 결과 포함
- [분산 전기열 구동](concepts/distributed-electrothermal-actuation.md) — Joule 가열 + 이중층 열팽창 차이로 국소 접힘
- [Resistive Network Imaging (RNI)](concepts/resistive-network-imaging.md) — 구동 저항 네트워크를 EIT 방식으로 읽는 self-sensing
- [폐루프 형상 제어](concepts/closed-loop-shape-control.md) — 되먹임 변수(온도 vs 형상)를 구분해서 비교
- [자기 센싱 (Self-sensing)](concepts/self-sensing.md) — intrinsic(구동 요소 = 센서) vs embedded(별도 내장 센서)
- [형상 역설계](concepts/inverse-shape-design.md) — 목표 형상에서 구동 입력을 역산 (GA, 형상 라이브러리)
- [무전력 형상 유지](concepts/shape-retention.md) — 쌍안정, 상변화 고정 등 입력 없이 형상 유지
