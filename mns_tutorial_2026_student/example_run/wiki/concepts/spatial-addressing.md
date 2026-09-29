# 공간 주소 지정 방식 (Spatial addressing)

## 정의
분산된 구동 요소(픽셀, 셀, 저항 세그먼트, 리본, pouch)에 에너지나 명령을 공간적으로 골라서 전달하는 배선·제어 방식이다. 비교표([matrix.md](../matrix.md))의 "주소 지정" 열에 해당한다.

## 유형 (Park 2025의 분류)
Park 2025는 기존 방식을 다음처럼 나누었다 (Park2025 p. 1–2).
- **direct addressing**: 요소마다 개별 배선을 둔다. 인용: ref. 10, 44
- **matrix addressing**: 행·열로 배선한다. 인용: ref. 45
- **networked domain + periphery electrode**: 연결된 도메인을 가장자리 전극으로 자극한다. 인용: ref. 46–48

### 인용 논문 원문과 대조한 결과
| Park의 분류 | 인용 논문 | 대조 결과 | 근거 |
|---|---|---|---|
| direct addressing | ref. 10 = [Johnson2023](../papers/Johnson2023.md) | **맞음.** 셀마다 전용 구동 회로(optoelectronic half-bridge)와 HV 센서가 있다. 다만 HV 전원·MCU는 1 × 10 모듈 단위로 공유하는 **계층형** direct addressing이다 | Johnson2023 p. 3; p. 8; Fig. 1e; Fig. 2c |
| networked domain + periphery electrode | ref. 48 = [Ni2022](../papers/Ni2022.md) | **절반만 맞음.** 리본은 서로 분리된(isolated) 독립 채널이다. 전류가 연결된 도메인 안에서 여러 경로로 나뉘지 않고, 리본 8개 각각에 직접 설정된다. [추론] 전류가 표면 가장자리의 리본 끝에서 들어가므로 "periphery"는 맞지만, 전기적 "networked domain"은 아니다. 결합은 막을 통한 기계적 결합이다 | Ni2022 p. 2; p. 8; Fig. 1d, g |
| networked domain + periphery electrode | ref. 46 = Liu 2021 | `needs_review`: 원문 미확보(`needs_manual`) | — |
| matrix addressing | ref. 45 | 수집 대상이 아니라 대조하지 않았다 | — |

[추론] 대조 결과로 보면, 수집한 논문 가운데 전기적으로 연결된 도메인을 소수의 전극으로 구동하는 **networked domain은 Park 2025뿐**이다.

## 논문별 내용
- [Park2025](../papers/Park2025.md): 전극을 격자 전체(8 × 8)에 두는 **networked domain**을 썼다. 저항(308개)이 전극(64개)보다 많아 저항별 개별 주소 지정성을 잃는다. 그 대신 singular value 분석에서 유의한 singular value가 다른 networked 설계보다 많아 접힘 구성의 자유도가 높다고 주장한다 (p. 3; p. 7 Methods; Supp. Fig. 1은 미확보). 원하는 전력 분포에 맞는 전극 전압은 GA로 역산한다 (p. 8).
- [Johnson2023](../papers/Johnson2023.md): 셀 100개가 각각 전용 half-bridge(충전·방전 optocoupler 2개)와 HV 센서를 가진 direct addressing이다. 저자는 "100 independently-addressable electrohydraulic actuators"라고 적었다 (p. 3; p. 8; Fig. 2c). 모듈 확장은 circuit pin addressing, 센서 신호 임피던스, 전력 때문에 한계가 있다고 밝혔다 (p. 8). 개별 주소 지정 덕분에 일부 셀은 센서로, 일부 셀은 구동기로 나눠 쓸 수 있다 (p. 6; Fig. 4e, f).
- [Ni2022](../papers/Ni2022.md): 4 × 4 cross-bar의 리본 8개가 각각 독립 제어 채널이다. 채널마다 전류 크기와 방향(0 ~ ±0.5 A)을 정한다 (p. 2). 전류를 5단계만 써도 5⁸ ≈ 0.4 million 조합이 된다 (p. 3). 리본 수를 늘려도 최대 변형은 거의 같고 형상 충실도가 오른다 (p. 3; Fig. 1h).
- [Zhang2023](../papers/Zhang2023.md): **공압** direct addressing이다. pouch마다 직경 1 mm 튜브와 솔레노이드 밸브가 있다 (p. 7–8). 이진 가압 코드가 모드를 유일하게 정하지는 않는다. 같은 코드가 pouch 압력 90 kPa에서는 순수 굽힘, 20 kPa에서는 굽힘+수축이 된다 (p. 5; Fig. 3c, g).
- [Yan2023](../papers/Yan2023.md): 분산 요소의 공간 주소 지정은 없다 [추론]. 대신 반도체 MUX 자리에 재료 내장 기계식 2-to-1 multiplexer(OMS)를 두고, 논리 출력이 배선으로 정해진 액추에이터에 전력을 보낸다 (p. 2; Fig. 1b; Fig. 5c; Fig. 6b).

## 관련 개념
- [Field-programmability](field-programmability.md)
- [분산 전기열 구동](distributed-electrothermal-actuation.md)
- [형상 역설계](inverse-shape-design.md)
