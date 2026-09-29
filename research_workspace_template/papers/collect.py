"""수집 보조 스크립트. papers/ 폴더에서 실행한다. 에이전트가 직접 수집해도 되고, 이 스크립트를 써도 된다.

    python collect.py

seed_papers.csv -> pdf/, collection_status.csv (규칙: README.md)
"""
import csv
import io
import pathlib
import re

import requests
from pypdf import PdfReader

HERE = pathlib.Path(__file__).parent
# nature.com은 쿠키 확인 리다이렉트를 거치므로 세션으로 쿠키를 유지한다
SESSION = requests.Session()
SESSION.headers["User-Agent"] = "Mozilla/5.0 (paper-collection)"


def get(url):
    r = SESSION.get(url, timeout=60)
    r.raise_for_status()
    return r.content


def norm(s):
    return re.sub(r"[^a-z0-9]", "", s.lower())


def collect(row):
    out = {k: row[k] for k in ("no", "first_author", "year")}
    out.update(status="needs_manual", oa_status="", license="", pdf_url="", local_file="", note="")
    try:
        work = SESSION.get("https://api.openalex.org/works/doi:" + row["doi"], timeout=60).json()
    except Exception as e:
        out["note"] = f"OpenAlex 조회 실패: {e}"
        return out
    best = work.get("best_oa_location") or {}
    out["oa_status"] = work["open_access"]["oa_status"]
    out["license"] = best.get("license") or ""
    out["pdf_url"] = best.get("pdf_url") or ""
    if not out["pdf_url"]:
        out["note"] = "OA 없음"
        return out
    try:
        data = get(out["pdf_url"])
    except Exception as e:
        out["note"] = f"다운로드 실패(차단 가능): {e}"
        return out
    if not data.startswith(b"%PDF"):
        out["note"] = "PDF가 아님(랜딩 페이지 또는 차단)"
        return out
    name = f"pdf/{int(row['no']):02d}_{row['first_author']}_{row['year']}.pdf"
    (HERE / "pdf").mkdir(exist_ok=True)
    (HERE / name).write_bytes(data)
    out["local_file"] = name
    page1 = PdfReader(io.BytesIO(data)).pages[0].extract_text() or ""
    if norm(row["title"])[:40] in norm(page1):
        out["status"] = "collected"
        out["note"] = "1쪽 제목 대조 통과"
    else:
        out["status"] = "needs_review"
        out["note"] = "1쪽 제목 대조 실패: 사람이 확인"
    return out


def main():
    rows = list(csv.DictReader(open(HERE / "seed_papers.csv", encoding="utf-8")))
    if not rows:
        print("seed_papers.csv에 논문이 없습니다. DOI를 먼저 적어 주세요.")
        return
    results = []
    for row in rows:
        r = collect(row)
        print(r["no"], r["first_author"], r["year"], r["status"], r["note"])
        results.append(r)
    with open(HERE / "collection_status.csv", "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(results[0]))
        w.writeheader()
        w.writerows(results)


if __name__ == "__main__":
    main()
