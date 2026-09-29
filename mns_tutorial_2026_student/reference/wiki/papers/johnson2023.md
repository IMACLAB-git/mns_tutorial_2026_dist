---
title: A multifunctional soft robotic shape display with high-speed actuation, sensing, and control
authors: B. K. Johnson 외
year: 2023
venue: Nature Communications 14
doi: 10.1038/s41467-023-39842-2
source_file: papers/pdf/10_Johnson_2023.pdf
status: summarized
---

## 한 줄 요약
HASEL 전기유압 액추에이터, 자기식 변형 센서, 구동 회로를 셀 하나에 넣은 10×10 형상 디스플레이. 셀마다 변형 폐루프 제어를 한다.

## 핵심 주장과 근거
| 주장 | 원문 위치 |
|---|---|
| 0–8 kV에서 약 12 mm 변형 | p.3 Fig. 2b |
| 구동 최대 50 Hz, 전압 조절 대역폭 > 200 Hz | p.3–4 Fig. 2f–g |
| 준정적 변형 센싱 평균 오차 < 0.1 mm | p.4 Fig. 3b–c |
| 변형 폐루프 대역폭 20 Hz | p.5–6 Fig. 4b |
| 액추에이터 100개, 센서 100개, 제어 루프 200개 이상 | p.8 |

## 방법·조건
- 구동: HASEL(12개 파우치 적층), 셀 크기 60×60 mm (p.2–3).
- 주소 지정: 셀마다 전용 광전자 하프브리지 구동 회로가 있다(direct addressing) (p.3 Fig. 2c).
- 센싱: 연자성 블록 + 자력계. 고전압 간섭을 피하려고 액추에이터와 분리했다 (p.2–4).
- 제어: 전압 조절 루프 1 kHz, 변형 피드백 루프 200 Hz (p.3, p.5).

## 한계
- 저자 진술: 외부 자성 물체가 자력계를 교란하고, 설치 위치가 바뀌면 재보정이 필요하다 (p.5, p.8). 핀 수와 전력 때문에 모듈을 무한히 늘릴 수 없다 (p.8).
- [추론] 셀 수에 비례해 구동 회로와 센서가 늘어나는 구조다. 전극 64개로 저항체 308개를 구동하는 Park 2025와 확장 방식이 다르다.
- [추론] 제어하는 대상은 셀 높이(z)다. 접힘각이나 곡률이 아니다 (p.4).

## RQ 단서
- [추론] 형상(변형) 수준 폐루프가 20 Hz로 가능함을 보인 사례다. Park 2025의 온도 수준 폐루프(약 0.1 Hz, p.4)와 비교할 기준이 된다.

## 관련 개념
[addressing-schemes](../concepts/addressing-schemes.md) · [closed-loop-shape-control](../concepts/closed-loop-shape-control.md)
