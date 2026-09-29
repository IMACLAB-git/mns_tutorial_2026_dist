# MNS 2026 실습 예시 작업공간

`mns_tutorial_2026_blank/GUIDE.md`의 화면을 찍을 때(2026-09-29) Claude Code가 실제로 만든 작업공간이다. 규칙 문서와 결과물이 모두 들어 있어, 실습하다 막히면 해당 단계의 파일을 보거나 복사해 넘어갈 수 있다.

- 대상 논문: Park et al., "Field-programmable robotic folding sheet", *Nature Communications* 16, 6937 (2025)
- **사람이 원문과 대조하지 않은 상태**다. 논문 페이지의 `status`는 `summarized`이고, RQ의 상태는 `후보`다. 설명 페이지의 개념도처럼 에이전트가 직접 그린 그림도 원문과 대조하지 않았다.
- Claude의 결과는 실행할 때마다 달라진다. 자기 결과와 비교해 보는 용도로 쓴다.

## 폴더

| 폴더·파일 | 내용 |
|---|---|
| `CLAUDE.md` | 프로젝트 목표, 작업 흐름, 연구 키워드, 검증 규칙, RQ 형식. 6단계용 줄(5번)을 더한 상태다. |
| `papers/` | 수집 규칙 `README.md`, 논문 목록 `seed_papers.csv`, 수집 결과 `collection_status.csv`, 논문 PDF 5편 `pdf/`. Liu 2021은 오픈 액세스가 아니어서 `needs_manual`이다. |
| `wiki/` | 규칙 `README.md`, 양식, 논문 페이지 5개, 개념 페이지 8개, 비교표 `matrix.md`, 공백과 RQ 후보 `rq.md`, 목차 `index.md`, 변경 기록 `log.md`, 허브 `hubs/`, 태그 어휘 `tags.md` |
| `explainer/` | 규칙 `README.md`, 설명 페이지 `park2025.html`, 논문 그림 11장 `figures/`. `park2025.html`을 브라우저로 열면 그림과 함께 보인다. |
| `LICENSES.md` | 문서·코드 라이선스와 논문 PDF·그림의 출처·라이선스 |

## 캡처 실행 뒤에 더한 것

- 허브(`wiki/hubs/`): `python wiki/_scripts/build_hubs.py`가 논문 frontmatter로 연도·학회·저자·주제 허브를 만든다. 논문 페이지 frontmatter 아래의 `허브:` 줄도 이 스크립트가 단다.
- 태그(`wiki/tags.md`와 논문 페이지의 `tags`): `CLAUDE.md`의 연구 키워드 8개를 어휘로 옮기고, `matrix.md`와 개념 페이지를 근거로 논문마다 붙였다. 사람이 확인하지 않았다.
- 변경 기록(`wiki/log.md`): 3–6단계의 위키 변경을 GUIDE의 완료 응답과 결과 파일을 보고 사후에 적었다.

## 준비물

- VS Code, Claude Code 확장(게시자 Anthropic, 로그인 필요)
- Python 3와 패키지: `pip install requests pypdf pymupdf`

## 관련 작업공간

- `../mns_tutorial_2026_blank/`: 같은 실습을 처음부터 따라 하는 빈 작업공간과 `GUIDE.md`
- `../research_workspace_template/`: 이 구조에 큰 그림·가설·실험·원고를 더한 연구 작업공간 템플릿
