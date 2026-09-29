# papers/ — 논문 수집과 search 라운드

## 역할
`seed_papers.csv`에 적힌 논문의 원문 PDF를 합법적인 OA 경로로 모으고, 문헌 탐색을 라운드로 반복한다.

## 입력 → 출력
- 입력: `seed_papers.csv` (DOI가 적힌 논문 목록. `no` 0번이 대상 논문)
- 출력
  - `pdf/{no:02d}_{first_author}_{year}.pdf`
  - `collection_status.csv` (한 편당 한 줄)
  - `rounds/R{nn}.md` (라운드 기록. 양식: `rounds/_template.md`)

## 작업 순서

### 수집
1. DOI로 OpenAlex(`https://api.openalex.org/works/doi:<DOI>`)를 조회해 OA PDF 주소를 얻는다.
2. PDF를 받고, 파일이 `%PDF`로 시작하는지 확인한다.
3. PDF 1쪽의 제목을 CSV의 제목과 대조한다.
4. `collection_status.csv`에 `no, first_author, year, status, oa_status, license, pdf_url, local_file, note`를 적는다.

`collect.py`가 위 1–4를 그대로 한다(`python collect.py`). 에이전트가 직접 해도 되고, 이 스크립트를 실행해도 된다.

### search 라운드
처음 수집을 R00으로 본다.

1. `rounds/R{nn}.md`를 양식으로 만들고 이번 라운드의 목적을 적는다. 목적은 `wiki/gaps.md`의 공백이나 가설과 연결되어야 한다.
2. 세 경로로 후보를 찾는다: 참고문헌(backward), 인용 논문(forward, OpenAlex `cites:` 필터), 키워드.
3. 후보를 `seed_papers.csv`에 추가하고 `round`에 라운드 번호를 적는다. DOI로 중복을 거른다.
4. 위 수집 순서대로 받는다.
5. `wiki/`에 반영한 뒤, 비교표나 공백 판정이 바뀌었는지 라운드 기록에 적는다. 바뀌지 않았으면 "포화"로 닫고 `bigpicture.md`의 "현재 search 범위"를 갱신한다.

## 지킬 것
- status는 세 가지만 쓴다.
  - `collected`: 출판사 판본을 받았고 제목 대조를 통과함
  - `needs_review`: 받았지만 저자 원고나 프리프린트여서 사람이 대조해야 함
  - `needs_manual`: 받지 못함. `note`에 사유를 적는다(OA 없음, 403 차단 등)
- 봇 차단(403, CAPTCHA)은 우회하지 않는다. 사람이 브라우저나 기관 구독으로 받아 `pdf/`에 넣으면, 제목을 대조한 뒤 status를 갱신한다.
- 받지 못한 논문에 대해서는 어떤 내용도 만들지 않는다.
- `license` 열은 그림을 다시 쓸 때(`explainer/`)의 근거가 된다. 비워 두지 않는다. 모르면 `needs_review`.
- 라운드 기록은 포화든 중단이든 지우지 않는다.
