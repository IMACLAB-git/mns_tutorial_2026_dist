# 연구 작업공간 템플릿

Claude Code와 함께 문헌 탐색 → 가설 → 실험 → 원고를 한 흐름으로 돌리기 위한 빈 작업공간이다. MNS 2026 실습(`mns_tutorial_2026_student`)의 논문·위키 구조에 큰 그림, 가설, 실험, 원고 폴더와 연구 원칙을 더했다.

## 시작하기

1. 이 폴더를 복사해 프로젝트 이름으로 바꾸고 VS Code로 연다.
2. `CLAUDE.md`에서 `채울 것` 주석이 달린 곳(프로젝트 목표, 연구 키워드)을 채운다. 연구 원칙은 자기 방식에 맞게 고친다.
3. `papers/seed_papers.csv`에 대상 논문(`no` 0)과 출발 논문 몇 편의 DOI를 적는다. `round`는 `R00`으로 둔다.
4. Claude Code를 열고 아래 순서로 요청한다. 단계마다 결과를 읽고, "사람이 결정하는 것"은 직접 정한다.

| 단계 | 요청 예 | 사람이 할 일 |
|---|---|---|
| 수집 | `papers/README.md 규칙에 따라 seed_papers.csv의 논문을 수집해줘.` | `needs_manual` 논문을 직접 받아 넣기 |
| 정리·비교 | `wiki/README.md 규칙에 따라 collected 논문의 페이지를 만들고, 비교 축을 제안해줘.` | 비교 축 정하기, 핵심 페이지를 원문과 대조해 `checked`로 바꾸기 |
| 공백 | `matrix.md를 만들고 gaps.md에 공백과 RQ 후보를 써줘.` | RQ 채택 |
| 큰 그림 | `gaps.md를 근거로 bigpicture.md의 최종 주장 후보 2–3개를 제안해줘. 결정은 내가 한다.` | 최종 주장 고르기 |
| 가설 | `bigpicture.md의 최종 주장을 hypotheses/README.md 규칙에 따라 최소 가설로 쪼개고, 사전 기각 기준을 제안해줘.` | 기각 기준 확인·잠금 |
| 실험 설계 | `H01의 잠긴 기각 기준으로 experiments/README.md 규칙에 따라 E00 기준선 재현과 E01 프로토콜 초안을 써줘.` | 장비·조건 확인, 실험 수행, 원데이터 넣기 |
| 판정 | `E01 data/로 분석하고 result.md에 판정을 제안해줘.` | 판정 확정 |
| search 라운드 | `papers/README.md의 라운드 규칙으로 R01을 돌려줘. 목적: G1을 이미 다룬 후속 연구가 있는지.` | 포화 판정 확인 |

판정을 확정하면 `CLAUDE.md`의 "판정이 나면 한 번에 갱신할 것" 순서대로 결과, 가설, 원고, 큰 그림, 결정 기록이 함께 바뀐다.

## 폴더

| 폴더·파일 | 내용 |
|---|---|
| `CLAUDE.md` | 프로젝트 목표, 연구 원칙, 작업 흐름, 검증 규칙, 사람이 결정하는 것. Claude Code가 대화마다 자동으로 읽는다. |
| `bigpicture.md` | 최종 주장, 가설 지도, 다음 가설, 현재 search 범위 |
| `decision_log.md` | 연구 결정 기록 |
| `papers/` | 수집 규칙, `seed_papers.csv`, 수집 보조 스크립트 `collect.py`, search 라운드 기록 `rounds/` |
| `wiki/` | 논문 페이지(글쓰기 노트 포함), 개념, 비교표 `matrix.md`, 공백과 RQ `gaps.md`, 글쓰기 패턴 `writing.md`, 목차, 변경 기록 `log.md`, 허브 `hubs/`(연도·저널·저자·주제)와 태그 어휘 `tags.md`, 허브 생성 스크립트 `_scripts/build_hubs.py` |
| `hypotheses/` | 가설 페이지 양식: 가추 근거, 최소 검증, 사전 기각 기준, 판정 |
| `experiments/` | 실험 폴더 양식: `protocol.md`, `result.md`(+ 실험마다 `data/`, `analysis/`) |
| `manuscript/` | `draft.md`: 가설마다 절을 두고 `[대기]`로 시작하는 원고 |
| `explainer/` | (선택) 위키로 대상 논문 설명 페이지를 만드는 규칙 |
| `LICENSE.md` | 이 템플릿의 라이선스(문서 CC BY 4.0, 코드 MIT) |

폴더마다 README가 네 칸(역할 / 입력 → 출력 / 작업 순서 / 지킬 것)으로 되어 있다. 규칙을 바꿀 때는 README를 고치고, 에이전트에게 "README를 다시 읽고 따라줘"라고 말한다.

## 실습 자료와 다른 점

- `wiki/rq.md` 대신 `wiki/gaps.md`: RQ는 끝이 아니라 가설로 쪼개기 전의 중간 단계다.
- 모든 판단에 근거 등급([문헌] [시뮬] [실험])을 붙인다. 가설 채택과 원고의 결과 문장은 [실험]만 근거가 된다.
- 논문 페이지에 글쓰기 노트가 있다. 두 편 이상에서 반복되는 패턴은 `wiki/writing.md`로 올린다.
- 문헌 탐색을 한 번으로 끝내지 않고 라운드로 반복한다(`papers/rounds/`).
- 논문 frontmatter로 연도·저널·저자·주제 허브를 만든다(`wiki/_scripts/build_hubs.py`). 주제 태그는 사람이 정한 어휘(`wiki/tags.md`)만 쓴다.

## 준비물

- VS Code, Claude Code 확장
- Python 3: `pip install requests pypdf pymupdf`
