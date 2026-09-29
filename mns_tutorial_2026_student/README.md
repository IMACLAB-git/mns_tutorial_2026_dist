# MNS 2026 실습: 논문에서 RQ까지

VS Code와 Claude Code로 연구 작업공간을 직접 만들고, 논문 한 편을 관련 논문과 비교해 연구 질문(RQ) 후보를 도출하는 실습 자료다.

- 대상 논문: Park et al., "Field-programmable robotic folding sheet", *Nature Communications* 16, 6937 (2025)
- 하는 일: 규칙 문서(CLAUDE.md, README.md) 쓰기 → CSV로 오픈 액세스 논문 수집 → 간단한 LLM 위키 만들기 → 비교표 → 공백과 RQ 후보 → (추가) 위키로 대상 논문 설명 페이지 만들기

## 여기서 시작

1. 아래 준비물을 설치한다.
2. **[GUIDE.md](GUIDE.md)**를 열고 0단계부터 따라 한다. 단계마다 실제 VS Code 화면이 있다.
3. 막히면 `reference/`의 완성본을 보거나 복사해 다음 단계로 넘어간다.

## 준비물

- VS Code, Claude Code 확장(게시자 Anthropic, 로그인 필요)
- Python 3와 패키지: `pip install requests pypdf pymupdf`
- 인터넷 연결(OpenAlex 조회와 PDF 내려받기). 연결이 안 되면 `backup_pdf/`를 쓴다.

## 폴더

| 폴더·파일 | 내용 |
|---|---|
| `GUIDE.md` | 단계별 따라하기(0–6단계) |
| `guide_img/` | GUIDE.md의 화면 캡처 |
| `workspace/` | 실습 시작 상태. `papers/seed_papers.csv`(논문 6편의 DOI 목록) 하나만 있다. 이 폴더를 VS Code로 열고 시작한다. |
| `reference/` | 강사가 정리한 단계별 완성본: `CLAUDE.md`, `papers/`(README, 수집 스크립트, 결과 CSV), `wiki/`(README, 양식, 논문·개념 페이지, 비교표, RQ), `explainer/README.md` |
| `example_run/` | GUIDE.md를 캡처할 때 에이전트가 실제로 만든 결과물. 사람이 원문과 대조하지 않은 상태다. |
| `backup_pdf/` | 네트워크가 안 될 때 쓰는 오픈 액세스 논문 PDF 5편 |
| `LICENSES.md` | 이 자료의 라이선스(문서 CC BY 4.0, 코드 MIT)와 논문 PDF·그림의 출처·라이선스 |
| `reset.ps1` | `workspace/`를 시작 상태로 되돌린다(Windows PowerShell 전용). `seed_papers.csv`를 뺀 모든 파일을 지우니, 남길 결과가 있으면 먼저 다른 곳에 복사한다. |

## 실습에서 지키는 규칙

- 원문에 적힌 내용과 추론을 구분한다. 추론에는 `[추론]`을 붙인다.
- 주장과 수치에는 원문 위치(p. / Fig. / Table)를 적는다.
- 확인하지 못한 내용은 `needs_review`로 남긴다. 제목·DOI·수치를 지어내지 않는다.
- 에이전트가 만든 RQ는 `후보`다. 채택은 원문을 확인한 사람이 정한다.

## 이어서 연구에 쓰려면

같은 배포 묶음의 `research_workspace_template/`은 이 실습의 구조에 가설·실험·원고 폴더를 더한 빈 연구 작업공간이다. 자기 주제로 새 프로젝트를 시작할 때 복사해 쓴다.
