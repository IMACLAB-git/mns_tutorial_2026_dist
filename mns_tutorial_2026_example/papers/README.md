# papers/ — 논문 수집

## 역할
`seed_papers.csv`에 적힌 논문의 원문 PDF를 합법적인 OA 경로로 모은다.

## 입력 → 출력
- 입력: `seed_papers.csv` (DOI가 적힌 논문 목록. `no` 0번이 대상 논문)
- 출력: `pdf/{no:02d}_{first_author}_{year}.pdf`, `collection_status.csv` (한 편당 한 줄)

## 작업 순서
1. DOI로 OpenAlex(`https://api.openalex.org/works/doi:<DOI>`)를 조회해 OA PDF 주소를 얻는다.
2. PDF를 받고, 파일이 `%PDF`로 시작하는지 확인한다.
3. PDF 1쪽의 제목을 CSV의 제목과 대조한다.
4. `collection_status.csv`에 `no, first_author, year, status, oa_status, license, pdf_url, local_file, note`를 적는다.

## 지킬 것
- status는 세 가지만 쓴다.
  - `collected`: 출판사 판본을 받았고 제목 대조를 통과함
  - `needs_review`: 받았지만 저자 원고나 프리프린트여서 사람이 대조해야 함
  - `needs_manual`: 받지 못함. `note`에 사유를 적는다(OA 없음, 403 차단 등)
- 봇 차단(403, CAPTCHA)은 우회하지 않는다.
- 받지 못한 논문에 대해서는 어떤 내용도 만들지 않는다.
