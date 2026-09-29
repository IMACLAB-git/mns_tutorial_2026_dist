# wiki/ — 논문 위키

## 역할
수집한 논문을 한 편당 한 페이지로 정리하고, 비교표를 거쳐 RQ 후보를 만든다.

## 입력 → 출력
- 입력: `papers/pdf/`에서 `collected` 상태인 논문
- 출력
  - `wiki/papers/<성><연도>.md`: 논문 페이지 (양식: `wiki/papers/_template.md`)
  - `wiki/concepts/`: 여러 논문에 걸쳐 나오는 개념
  - `wiki/matrix.md`: 비교표
  - `wiki/rq.md`: 공백과 RQ 후보
  - `wiki/index.md`: 목차
  - `wiki/log.md`: 위키 변경 기록
  - `wiki/hubs/`(`years/`, `venues/`, `authors/`, `topics/`): 허브. `python wiki/_scripts/build_hubs.py`가 논문 frontmatter로 만든다
  - `wiki/tags.md`: 태그 어휘. 사람이 정한다

## 작업 순서
1. 논문 페이지를 양식대로 만들고 `status: summarized`로 둔다.
2. 핵심 개념은 기존 `concepts/` 페이지에 링크하고, 없을 때만 새로 만든다.
3. `matrix.md`: 행은 논문, 열은 구동 원리 | 외부 장치 | 주소 지정 | 센싱 | 제어 루프 | 속도 | 형상.
4. `rq.md`: 공백 표(공백 | 근거 논문·원문 위치 | 해석)를 쓴 뒤, 공백마다 RQ 후보를 하나씩 쓴다.
5. `index.md`에 새 페이지를 한 줄씩 추가하고, `python wiki/_scripts/build_hubs.py`로 허브와 논문 페이지의 "허브:" 줄을 다시 만든다.
6. `log.md`에 입력, 생성·수정·건너뛴 파일, 상태 변화, `matrix.md`·`rq.md`에 미친 영향(없으면 "영향 없음"), 중단이나 사람 승인 이유를 적는다.

## 지킬 것
- 모든 주장과 수치, 비교표의 칸마다 원문 위치(p. / Fig. / Table)를 적는다. 모르는 칸은 `needs_review`로 둔다.
- 측정 조건이 다른 수치를 같은 조건의 성능처럼 비교하지 않는다.
- RQ에는 조건, 비교 대상, 측정값, 판정 기준을 적고 상태는 `후보`로 둔다.
- `status: checked`, RQ 채택, 태그 어휘(`tags.md`)는 사람이 정한다. 어휘에 없는 태그는 논문 페이지에 넣지 않는다.
- 허브 폴더(`hubs/`)와 논문 페이지의 "허브:" 줄은 손으로 고치지 않는다. 논문 frontmatter를 고친 뒤 스크립트를 다시 실행한다.
