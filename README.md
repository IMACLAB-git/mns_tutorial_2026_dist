# MNS 2026 실습 배포 묶음

VS Code와 Claude Code로 논문을 모아 위키로 정리하고, 연구 질문(RQ)까지 가는 실습 자료다. 작업공간 세 개가 들어 있다. 셋 모두 논문 수집(`papers/`) → 논문 위키(`wiki/`) → 설명 페이지(`explainer/`) 구조를 쓴다.

| 폴더 | 무엇인가 | 언제 쓰나 |
|---|---|---|
| [`mns_tutorial_2026_blank/`](mns_tutorial_2026_blank/) | 실습을 처음부터 따라 하는 빈 작업공간. 규칙 문서가 없고 논문 목록과 따라하기(`GUIDE.md`, `GUIDE.html`)만 있다. | 실습할 때. **여기서 시작한다.** |
| [`mns_tutorial_2026_example/`](mns_tutorial_2026_example/) | 같은 실습을 끝까지 실행한 완성 작업공간. GUIDE의 화면을 찍을 때 Claude Code가 만든 결과물이다. | 막혔을 때 같은 단계의 파일을 보거나 복사할 때, 자기 결과와 비교할 때 |
| [`research_workspace_template/`](research_workspace_template/) | 실습 구조에 큰 그림·가설·실험·원고를 더한 빈 연구 작업공간 | 실습이 끝난 뒤 자기 주제로 연구를 시작할 때 |

세 작업공간의 관계:

```
blank ──(GUIDE를 따라 채운다)──▶ example과 같은 모양이 된다 ──(가설·실험·원고를 더한다)──▶ research_workspace_template
```

## 실습 대상

- 대상 논문: Park et al., "Field-programmable robotic folding sheet", *Nature Communications* 16, 6937 (2025)
- 비교 논문: `seed_papers.csv`의 5편(Yan 2023, Zhang 2023, Johnson 2023, Ni 2022, Liu 2021). Liu 2021은 오픈 액세스가 아니어서 원문 없이 목록에만 남는다.
- 흐름: 규칙 문서 쓰기 → 논문 수집 → 대상 논문 위키 페이지와 원문 대조 → 비교 논문과 비교표 → 공백과 RQ 후보 → (추가) 설명 페이지

## 무엇이 들어 있나

| | blank | example | research_workspace_template |
|---|---|---|---|
| 규칙 문서(`CLAUDE.md`, 폴더별 `README.md`) | 없음. 실습하며 직접 쓴다 | 있음(실습용) | 있음. 프로젝트 목표·키워드는 `채울 것`으로 비어 있다 |
| `papers/` | 논문 6편의 DOI 목록 | 목록, 수집 결과, 오픈 액세스 PDF 5편 | 빈 목록, 수집 보조 스크립트 `collect.py`, search 라운드 기록 |
| `wiki/` | 빈 폴더, 허브 폴더 틀, 빈 변경 기록 | 논문 페이지 5개, 개념 8개, 비교표, 공백과 RQ 후보(`rq.md`), 허브, 태그 어휘, 변경 기록 | 양식, 비교표·공백(`gaps.md`)·글쓰기 패턴 틀, 허브 폴더, 태그 어휘, 변경 기록 |
| `explainer/` | 빈 폴더 | 설명 페이지 `park2025.html`과 논문 그림 11장 | 규칙 `README.md` |
| 가설·실험·원고 | — | — | `bigpicture.md`, `hypotheses/`, `experiments/`, `manuscript/`, `decision_log.md` |
| 따라하기 | `GUIDE.md`, `GUIDE.html`, 화면 캡처 28장 | — | `README.md`의 단계별 요청 예 |

- example은 **사람이 원문과 대조하지 않은 상태**다. 논문 페이지는 `summarized`, RQ는 `후보`다.
- 허브(`wiki/hubs/`)는 논문을 연도·학회·저자·주제로 묶은 목차 페이지다. 스크립트로 만들지 않고, Claude가 `wiki/README.md` 규칙에 따라 논문 페이지와 함께 갱신한다.

## 시작하기

1. 준비물을 설치한다.
   - VS Code, Claude Code 확장(게시자 Anthropic, 로그인 필요)
   - Python 3와 패키지: `pip install requests pypdf pymupdf`
2. 이 묶음을 통째로 받는다. GUIDE가 `../mns_tutorial_2026_example/`처럼 옆 폴더를 가리키므로 세 폴더를 같은 위치에 둔다.
3. `mns_tutorial_2026_blank/`를 VS Code로 열고 `GUIDE.md`(또는 브라우저로 `GUIDE.html`)를 0단계부터 따라 한다. 같은 따라하기를 온라인으로도 볼 수 있다: [MNS 2026 논문에서 RQ까지](https://claude.ai/artifact/4JsAJihHA4gWtkRtBFvbTG)
4. 실습이 끝나면 `research_workspace_template/`을 복사해 자기 프로젝트 이름으로 바꾸고, 그 폴더의 `README.md`를 따라 시작한다.

## 라이선스

문서는 CC BY 4.0, 코드(`research_workspace_template/papers/collect.py`)는 MIT다(© 2026 SLEE). 논문 PDF와 그림은 각 논문의 라이선스를 따른다. 자세한 내용은 폴더마다 있는 `LICENSES.md`(템플릿은 `LICENSE.md`)에 있다.
