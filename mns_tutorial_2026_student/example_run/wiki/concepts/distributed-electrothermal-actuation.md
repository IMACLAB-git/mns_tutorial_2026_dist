# 분산 전기열 구동 (Distributed electrothermal actuation)

## 정의
면에 분포시킨 저항 발열체(Joule heating)로 온도 분포를 만들고, 열팽창 계수가 다른 층의 차이(bilayer)로 국소 굽힘이나 접힘을 일으키는 구동 방식이다.

## 논문별 내용
- [Park2025](../papers/Park2025.md)
  - 재료: Ni 저항 네트워크 + PI(CTE 45 ppm/K) / PDMS(CTE 340 ppm/K) 이중층 + SU-8 microrod (p. 3).
  - 방향: 중립 온도 Tκ=0(100 °C)보다 높게 또는 낮게 가열하는 정도로 양방향 접힘을 만든다. 되돌아올 때는 수동 냉각을 쓴다 (p. 2; p. 3).
  - 국소성: 박막이라 대류가 열 축적보다 우세해서 온도 반응이 국소적이라고 해석했다. 곡률의 82.8 ± 6.80 %가 자극 영역에 집중된다 (p. 3; Fig. 2a, d).
  - 제어 입력: PWM duty cycle(주기 8 ms). duty cycle–온도는 R² > 0.993으로 선형이다 (p. 3).

## 다른 수집 논문과의 대비
분산 bilayer 전기열 구동을 쓰는 논문은 수집한 논문 중 Park 2025뿐이다. 나머지 논문의 Joule 가열 사용 방식은 다음과 같다.
- [Yan2023](../papers/Yan2023.md): CSCP 열 인공근육도 Joule 가열로 수축하는 열 액추에이터다. 다만 면에 분포한 bilayer가 아니라 개별 실 형태다 (p. 3; p. 10).
  - 냉각이 동작 주기를 제한한다. reset에 냉각 약 3 s가 들어가 주기가 약 3.2 s다 (p. 4).
  - 냉각 공기는 CSCP 열전도를 1.13에서 2.58 × 10⁻² W/°C로 올리지만, 작동 임계 전압도 1.2 V에서 1.8 V로 올린다 (p. 3–4; Fig. 2c).
  - [추론] 냉각을 강화해 속도를 얻으면 구동 전력이 늘어나는 교환 관계가 있다.
- [Ni2022](../papers/Ni2022.md): Joule 가열은 구동이 아니라 형상 고정용 갈륨을 녹이는 데만 쓴다(0.5 A, 30 s 이내) (p. 5).
- [Johnson2023](../papers/Johnson2023.md): 열 기반 구동과 달리 표면 열이 거의 없어 표면이 실온을 유지한다고 주장한다 (p. 4). 이 주장을 뒷받침하는 정량 온도 데이터는 본문에 없다.

## 관련 개념
- [공간 주소 지정 방식](spatial-addressing.md)
- [Resistive Network Imaging (RNI)](resistive-network-imaging.md)
- [무전력 형상 유지](shape-retention.md)
