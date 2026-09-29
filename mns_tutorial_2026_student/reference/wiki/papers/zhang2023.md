---
title: Plug & play origami modules with all-purpose deformation modes
authors: Chao Zhang 외
year: 2023
venue: Nature Communications 14
doi: 10.1038/s41467-023-39980-7
source_file: papers/pdf/08_Zhang_2023.pdf
status: summarized
---

## 한 줄 요약
Kresling 오리가미에 주름과 팽창 파우치를 더해, 공압 조합만으로 한 모듈에서 굽힘·비틀림·수축과 그 조합까지 7가지 변형 모드를 고른다.

## 핵심 주장과 근거
| 주장 | 원문 위치 |
|---|---|
| 한 모듈에서 3가지 기본 모드와 4가지 조합 모드 | p.3 Fig. 3a |
| 2단 모듈 순수 굽힘 최대 약 38.8° | p.4 Fig. 3c |
| 동작 중에 모듈을 더해 작업공간을 넓힌다 | p.5 Fig. 4c–e |

## 방법·조건
- 구동: 주 챔버는 진공, 측면 파우치는 양압으로 구동한다 (p.2).
- 외부 장치: 레귤레이터, 솔레노이드 밸브, Arduino (p.8).
- 제어: 미리 짠 가압 시퀀스로 동작하는 개루프이고, 센서가 없다 (p.5–6).

## 한계
- 저자 진술: 제작 오차와 비동기 가압 때문에 비틀림이 남는다 (p.4–5). 향후 과제로 센싱 통합을 든다 (p.7).
- [추론] "decoupled"라고 하지만 순수 모드에서도 2.3–5.14 %의 부수 변형이 남는다 (p.4–5).
- [추론] 힌지 배치가 설계 시점에 고정된다. 외부 공압원이 필요하므로 Park 2025의 요구조건 (iii) "외부 구동원 배제"를 충족하지 않는다 (Park 2025 p.2).

## RQ 단서
- [추론] 모드를 고르는 방식(설계 고정 + 압력 조합)과 Park 2025의 재구성 방식(전극 전압 패턴)을 "접근 가능한 형상 수"로 비교할 수 있는가?

## 관련 개념
[addressing-schemes](../concepts/addressing-schemes.md)
