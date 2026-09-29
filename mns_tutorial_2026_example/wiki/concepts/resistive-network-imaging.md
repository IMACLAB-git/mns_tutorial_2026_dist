# Resistive Network Imaging (RNI)

## 정의
연결된 저항 네트워크에서 전극 쌍을 바꿔 가며 전류를 주입하고 전압을 측정한 뒤, 역문제를 풀어 저항 분포를 재구성하는 방법이다. Electrical impedance tomography(EIT)에서 나왔다. 구동용 저항을 그대로 센서로 쓰는 self-sensing의 한 형태다.

## 논문별 내용
- [Park2025](../papers/Park2025.md)
  - 목적: 저항 변화를 Ni 온도계수(α = 0.006/K)로 온도로 바꿔 온도 분포를 추정한다 (p. 4).
  - 측정: 전극 쌍 1470회 순차 선택(drive pattern), 프레임당 14.85 ms (p. 8; p. 9).
  - 재구성: FC 3층 신경망을 sim-to-real로 학습했다(합성 데이터 400,000개). 비교 대상은 One-step GN과 Iterative GN이다 (p. 9).
  - 구동과의 공존: 구동 전류(약 200 mA)와 센싱 전류(< 2 mA)의 전력 수준 차이로 간섭을 피한다. 기능 전환은 < 1 μs다 (p. 2).
  - 장점 주장: IR 카메라와 달리 접힘에 의한 시야 가림에 영향받지 않는다 (p. 4).
  - `needs_review`: 재구성 정확도 수치는 Supp. Fig. 14, 15에만 있다(미확보).

수집한 다른 논문(Yan, Zhang, Johnson, Ni)은 RNI를 쓰지 않는다. 가장 가까운 대비는 Johnson 2023의 셀별 magnetometer 변형 센싱이다([자기 센싱](self-sensing.md) 참고).

## 관련 개념
- [자기 센싱 (Self-sensing)](self-sensing.md)
- [분산 전기열 구동](distributed-electrothermal-actuation.md)
- [폐루프 형상 제어](closed-loop-shape-control.md)
