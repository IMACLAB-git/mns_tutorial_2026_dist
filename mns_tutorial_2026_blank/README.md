# MNS 2026 실습: 논문에서 RQ까지

VS Code와 Claude Code로 연구 작업공간을 직접 만들고, 논문 한 편을 관련 논문과 비교해 연구 질문(RQ) 후보를 도출하는 실습 자료다. 이 폴더가 실습 작업공간이다. 규칙 문서는 들어 있지 않고, 실습하면서 직접 쓴다.

- 대상 논문: Park et al., "Field-programmable robotic folding sheet", *Nature Communications* 16, 6937 (2025)
- 하는 일: 규칙 문서(CLAUDE.md, README.md) 쓰기 → CSV로 오픈 액세스 논문 수집 → 간단한 LLM 위키 만들기 → 비교표 → 공백과 RQ 후보 → (추가) 위키로 대상 논문 설명 페이지 만들기

## 여기서 시작

1. 아래 준비물을 설치한다.
2. 이 폴더를 VS Code에서 **File > Open Folder**로 연다.
3. **[GUIDE.md](GUIDE.md)**를 열고 0단계부터 따라 한다. 단계마다 실제 VS Code 화면이 있다. 같은 내용을 브라우저로 보려면 `GUIDE.html`을 연다(입력문 복사 버튼, 캡처 확대 보기).
4. 막히면 `../mns_tutorial_2026_example/`에서 같은 단계의 파일을 보거나 복사해 다음 단계로 넘어간다.

## 준비물

- VS Code, Claude Code 확장(게시자 Anthropic, 로그인 필요)
- Python 3와 패키지: `pip install requests pypdf pymupdf`
- 인터넷 연결(OpenAlex 조회와 PDF 내려받기). 연결이 안 되면 `../mns_tutorial_2026_example/papers/pdf/`의 PDF를 쓴다.

## 폴더

| 폴더·파일 | 내용 |
|---|---|
| `papers/` | `seed_papers.csv`: 논문 6편의 DOI 목록. `no` 0번이 대상 논문이다. |
| `wiki/` | 비어 있는 위키. `papers/`, `concepts/`, 변경 기록 `log.md`, 허브 `hubs/`(연도·학회·저자·주제)와 허브를 만드는 `_scripts/build_hubs.py`만 있다. |
| `explainer/` | 비어 있다. 6단계(추가 실습)에서 설명 페이지를 만든다. |
| `GUIDE.md` | 단계별 따라하기(0–6단계) |
| `GUIDE.html` | GUIDE.md를 브라우저용 페이지로 옮긴 것. `guide_img/`의 캡처를 불러온다. |
| `guide_img/` | GUIDE.md와 GUIDE.html의 화면 캡처 |
| `LICENSES.md` | 문서·캡처·코드 라이선스 |

## 실습에서 지키는 규칙

- 원문에 적힌 내용과 추론을 구분한다. 추론에는 `[추론]`을 붙인다.
- 주장과 수치에는 원문 위치(p. / Fig. / Table)를 적는다.
- 확인하지 못한 내용은 `needs_review`로 남긴다. 제목·DOI·수치를 지어내지 않는다.
- 에이전트가 만든 RQ는 `후보`다. 채택은 원문을 확인한 사람이 정한다.

## 관련 작업공간

- `../mns_tutorial_2026_example/`: GUIDE.md의 화면을 찍을 때 만들어진 완성 작업공간(규칙 문서, 논문 PDF, 위키, 설명 페이지)
- `../research_workspace_template/`: 이 실습 구조에 큰 그림·가설·실험·원고를 더한 연구 작업공간 템플릿. 자기 주제로 새 프로젝트를 시작할 때 복사해 쓴다.
