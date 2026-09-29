# 자기 센싱 (Self-sensing)

## 정의
장치가 외부 계측 장비(카메라, 모션캡처, IR 카메라) 없이 자기 상태(변형, 힘, 온도)를 재는 것이다. 비교할 때는 두 가지를 구분한다.
- **intrinsic**: 구동 요소 자체가 센서다.
- **embedded**: 장치 안에 따로 넣은 센서로 잰다.

또 **무엇을** 재는지(구동 상태 vs 형상)도 구분한다.

## 논문별 비교
| 논문 | 유형 | 측정 대상 | 원문 위치 |
|---|---|---|---|
| [Park2025](../papers/Park2025.md) | intrinsic: 구동 저항 = 센서 (RNI) | 온도 (형상은 재지 않음) | p. 2; p. 4; p. 6 |
| [Johnson2023](../papers/Johnson2023.md) | embedded: 셀별 자석 + magnetometer (저자 표현은 "self-sensing") | 셀 변형, 힘 | p. 2; p. 4–5; Fig. 3 |
| [Zhang2023](../papers/Zhang2023.md) | 없음 (향후 과제) | — | p. 7; p. 8 |
| [Ni2022](../papers/Ni2022.md) | 없음 (외부 3D-DIC) | — | p. 8 |
| [Yan2023](../papers/Yan2023.md) | 외부 접촉 센서만 있음. 자기 상태 센싱은 없음 [추론] | 접촉 (이진) | p. 5–6 |

## 논문별 내용
- [Park2025](../papers/Park2025.md)
  - 같은 Ni 저항이 히터이자 thermoceptor다 (p. 2).
  - 구동(약 200 mA)과 센싱(< 2 mA)의 전력 차이로 간섭을 피한다 (p. 2).
  - IR 카메라와 달리 접힘에 의한 시야 가림에 영향받지 않는다고 주장한다 (p. 4).
  - 형상은 재지 않는다. 저자는 intrinsic shape sensing 추가를 향후 과제로 들었다 (p. 6).
- [Johnson2023](../papers/Johnson2023.md)
  - 셀마다 soft magnetic block과 magnetometer로 변형을 잰다. 준정적 평균 오차는 < 0.1 mm이고, 30 Hz까지 추종한다 (p. 4; Fig. 3b, c).
  - 전압과 변형으로 힘을 추정하며, 분해능은 50 mN이다 (p. 5; Fig. 3e).
  - 자기 방식을 고른 이유는 HASEL 전기장과 분리되기 때문이다. strain sensing, capacitive self-sensing과 대비된다 (p. 3). HV 구동의 전자기 간섭이 센서 통합을 어렵게 한다고 적었다 (p. 2).
  - 한계: 외부 자성 물질이 측정을 교란하고, 장소를 옮기면 재보정해야 하며, 보정에는 모션캡처가 필요하다 (p. 5; p. 8).
- [Zhang2023](../papers/Zhang2023.md): 센서가 없고, 실시간 self-perception을 위한 센싱 통합을 향후 과제로 들었다 (p. 7).
- [Ni2022](../papers/Ni2022.md): 형상은 외부 3D-DIC로만 잰다. 측정 부피는 40 × 40 × 10 mm³이고 중앙값 오차는 약 15, 15, 7 μm다 (p. 8).

## 관련 개념
- [Resistive Network Imaging (RNI)](resistive-network-imaging.md)
- [폐루프 형상 제어](closed-loop-shape-control.md)
