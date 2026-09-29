# 폐루프 형상 제어 (Closed-loop shape control)

## 정의
형상 변형 시스템에서 상태를 측정해 구동 입력을 되먹임하는 제어다. 비교할 때는 **무엇을 되먹이는지**(온도 같은 구동 상태인지, 곡률·변위 같은 형상 자체인지)를 구분해야 한다.

## 논문별 비교
| 논문 | 되먹임 변수 | 센서 위치 | 루프 속도 (측정 조건) | 원문 위치 |
|---|---|---|---|---|
| [Park2025](../papers/Park2025.md) | 온도 (곡률은 간접) | 내부: 구동 저항 자체(RNI) | 대역폭 약 0.1 Hz (개루프 < 0.03 Hz). 조화 입력 주파수 응답, 온도·곡률 | p. 4; Fig. 3a; Fig. 4c |
| [Johnson2023](../papers/Johnson2023.md) | **셀 변형(형상)** + 내부 전압 루프 | 내부: 셀별 자석 + magnetometer (구동기와 별개) | 변형 루프 200 Hz 주기, 대역폭 20 Hz. 진폭 0.4 mm(중심 1.4 mm)의 작은 신호 | p. 5; p. 9 Eq. 13; Fig. 4a, b |
| [Yan2023](../papers/Yan2023.md) | 외부 접촉 이벤트 (이진) | 외부 접촉 센서 | 해당 없음 (이벤트 기반) | p. 5–7 |
| [Zhang2023](../papers/Zhang2023.md) | 없음 (개루프) | 없음 | 해당 없음 | p. 8 |
| [Ni2022](../papers/Ni2022.md) | 없음 (라이브러리 조회 개루프) | 외부 3D-DIC (기록·라이브러리 구축용) | 해당 없음 | p. 5; p. 8 |

> 루프 속도 칸의 값들은 구동 물리, 변형 종류, 진폭, 측정 방식이 모두 달라서 같은 조건의 성능으로 비교할 수 없다.

## 논문별 내용
- [Park2025](../papers/Park2025.md)
  - 되먹임 변수는 **온도**다. RNI 추정값을 morphing basis 영역별로 모은다. 곡률은 온도–곡률 선형 관계를 통해 간접적으로 서보된다 (p. 4; Fig. 3a(ii)(iii)).
  - 제어기는 PI(P = 0.4, I = 0.009)이고 duty cycle을 조절한다 (p. 9).
  - 바람과 주변 온도 외란에서도 형상을 유지한다 (p. 5; Fig. 4e, f).
  - 저자가 intrinsic shape sensing을 향후 과제로 들었다 (p. 6).
- [Johnson2023](../papers/Johnson2023.md)
  - 형상(셀 변형 ẑ)을 직접 되먹이는 cascade 구조이고, 셀마다 독립적으로 푼다 (p. 3; p. 5; Fig. 4a).
  - 변형 루프는 내부 외란(HASEL 전하 잔류)과 외부 외란을 제거해, 전압 조절만 쓸 때보다 형상이 정확하다. 이는 그림으로만 보였고 정량 오차는 없다 (p. 6; Fig. 4c).
  - 대역폭 한계의 원인은 HASEL 동특성과 통신 지연이다 (p. 5).
- [Yan2023](../papers/Yan2023.md) (대비): 접촉 → 논리 게이트 → 구동의 이진 sense-decide-act다. [추론] 구동 결과는 되먹이지 않는다 (p. 5–7). 차량 궤적은 저자가 "open-loop"라고 적었다 (p. 8).
- [Zhang2023](../papers/Zhang2023.md) (대비): 센서가 없는 개루프다 (p. 8). Abstract는 "precisely controlled"라고 적었지만(p. 1) 추종 오차는 본문에 없다. 저자는 실시간 self-perception을 위한 센싱 통합을 향후 과제로 들었다 (p. 7).
- [Ni2022](../papers/Ni2022.md) (대비): 약 7000개 형상 라이브러리에서 입력을 조회하는 개루프다 (p. 5). 진동 잡음 상쇄도 전류 세기를 바꿔 가며 최적값을 찾은 것이고, 자동 폐루프라는 서술은 없다 (p. 6; Fig. 5b caption).

## 관련 개념
- [자기 센싱 (Self-sensing)](self-sensing.md)
- [Resistive Network Imaging (RNI)](resistive-network-imaging.md)
- [분산 전기열 구동](distributed-electrothermal-actuation.md)
