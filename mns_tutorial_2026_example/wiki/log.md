# 위키 변경 기록

위키(`wiki/`)를 실제로 바꾼 날짜와 내용을 최신순으로 간략하게 적는다.

> 3–6단계 기록은 캡처 실행(2026-09-29) 때 남기지 않았다. 실행 뒤에 `mns_tutorial_2026_blank/GUIDE.md`의 완료 응답 화면과 결과 파일을 보고 사후에 적었다. 실행 시각은 남아 있지 않다.

<!--
## YYYY-MM-DD — 한 줄 제목

- 입력: 논문 식별자, 문헌 목록 파일
- 생성·수정·건너뛴 파일:
- 상태 변화: (예: Park2025 새 페이지 → summarized)
- matrix.md·rq.md에 미친 영향: 없으면 "영향 없음"
- 중단 또는 사람 승인 이유:
-->

## 2026-09-29 — 허브와 태그 추가 (캡처 실행 뒤)

- 입력: 사용자 결정(허브 구조 추가). 태그 어휘는 `CLAUDE.md`의 "연구 키워드" 8개를 옮겼다.
- 생성: `_scripts/build_hubs.py`, `tags.md`, `hubs/`(연도 3, 학회·저널 1, 저자 10, 주제 8), 이 기록.
- 수정: 논문 페이지 5개에 `tags`와 `허브:` 줄 추가. `README.md`, `index.md`, `papers/_template.md`에 허브 안내 추가. 본문은 고치지 않았다.
- 태그 근거: `matrix.md`의 각 열과 `concepts/` 페이지. Yan2023은 붙일 태그가 없다(전기열 구동이지만 면에 분포한 이중층이 아니라 개별 실 형태, [분산 전기열 구동](concepts/distributed-electrothermal-actuation.md)). Zhang2023에는 `programmable-folding`을 붙이지 않았다(crease가 제작 때 정해짐, [Field-programmability](concepts/field-programmability.md)).
- 상태 변화: 없음. 모두 `summarized`.
- matrix.md·rq.md에 미친 영향: 영향 없음.
- 사람 승인 필요: 논문별 태그 배정.

## 2026-09-29 — 6단계: 설명 페이지 작성 중 위키와 원문의 차이 발견

- 입력: 위키 전체(논문 페이지 5개, 개념 페이지 8개, `matrix.md`, `rq.md`)를 배경지식으로 `explainer/park2025.html`을 만들었다.
- 위키 변경: 없음.
- 발견: [Field-programmability](concepts/field-programmability.md)의 "개념은 display engineering과 programmable logic device(FPGA)에서 따왔다" (Park2025 p. 1)가 원문보다 강한 표현이다. 원문(p. 1)은 분산 구조를 택한 착안점으로 쓴 문장이다. 설명 페이지에는 원문대로 적었고 위키는 고치지 않았다.
- 사람 승인 필요: 위 문장을 원문대로 고칠지.

## 2026-09-29 — 5단계: 공백과 RQ 후보

- 입력: `matrix.md`, 논문 페이지 5개.
- 생성: `rq.md`. 공백 G1–G3과 RQ 후보 3개(RQ1 형상 되먹임, RQ2 강제 대류 냉각, RQ3 networked vs pixelated domain). 근거가 약한 공백 후보 2개(무전력 형상 유지, RNI로 접촉 감지)는 RQ로 만들지 않고 "RQ로 만들지 않은 공백 후보"에 남겼다.
- 판정 기준의 값 가운데 원문에서 오지 않은 것은 "(제안)"으로 표시했다.
- 원문 대조: RQ1의 근거 공백에서 원문 사실과 추론을 나눴다. "온도 폐루프는 하중에 의한 형상 변화를 보정하지 못한다"는 여러 문장을 합친 추론이다.
- 상태 변화: RQ 3개 모두 `후보`.
- 사람 승인 필요: RQ 채택, "(제안)" 값.

## 2026-09-29 — 4단계: 비교 논문 4편과 비교표

- 입력: `collected` 4편(Yan 2023, Zhang 2023, Johnson 2023, Ni 2022). 논문마다 서브에이전트가 따로 읽었다.
- 생성: 논문 페이지 4개, 개념 페이지 3개(자기 센싱, 형상 역설계, 무전력 형상 유지), `matrix.md`.
- 수정: 기존 개념 페이지 5개에 네 논문의 내용 추가, `index.md`.
- 건너뜀: Liu 2021(`needs_manual`, 원문 없음). 페이지를 만들지 않았고 비교표에 넣지 않았다.
- 원문 대조: 비교표에 넣은 핵심 수치 19개를 PDF에서 다시 확인했다. Zhang2023에서 원문이 아니라 모델 지식에 기댄 항목(레귤레이터 제품 계열) 하나를 "제조사 사양과 대조 필요"로 바꿨다.
- `needs_review`: Johnson 공 이동 속도 계산이 맞지 않음, Zhang 모드 코드 011/110이 엇갈림, Ni의 "RSEM"은 RMSE의 오기로 보임.
- 발견: Park 2025는 Ni 2022를 networked domain으로 분류했지만, Ni 원문에서는 리본이 서로 분리된 독립 채널이다([공간 주소 지정 방식](concepts/spatial-addressing.md)).
- 상태 변화: 새 페이지 4개 → `summarized`.
- matrix.md·rq.md에 미친 영향: `matrix.md` 새로 만듦. 속도 수치는 논문마다 지표가 달라 서로 비교하지 않는다고 적었다.

## 2026-09-29 — 3단계: 대상 논문 페이지와 원문 대조

- 입력: `papers/pdf/00_Park_2025.pdf`.
- 생성: `papers/Park2025.md`, 개념 페이지 5개(field-programmability, spatial-addressing, distributed-electrothermal-actuation, resistive-network-imaging, closed-loop-shape-control), `index.md`.
- `needs_review`: 원문 안의 불일치(1000회 반복시험 R²가 p. 3에서 "> 0.95", Fig. 2f에서 "> 0.93"), 보충자료에만 있는 수치, 본문에 없는 조건(풍속 같은 외란의 정량값, GA 디코딩 실행 위치).
- 원문 대조 후 수정(사람 요청): 핵심 주장 표 2행의 "고정 힌지 없이"가 원문보다 강한 표현이어서 "고정 힌지에 의존하지 않고"로 바꾸고, 원문 위치에 p. 6 Discussion을 더했다.
- 상태 변화: Park2025 새 페이지 → `summarized`.
- matrix.md·rq.md에 미친 영향: 아직 없음(두 파일 모두 없음).
