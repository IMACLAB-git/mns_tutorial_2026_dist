"""wiki/papers/*.md의 frontmatter로 허브(wiki/hubs/의 years/, venues/, authors/, topics/)를 만든다.

- 허브 폴더 네 개는 이 스크립트가 통째로 다시 만든다. 손으로 고치지 말고 논문 frontmatter를 고친 뒤 다시 실행한다.
- 논문 페이지마다 frontmatter 바로 아래의 "허브:" 줄을 갱신한다.
- 주제 허브는 wiki/tags.md에 있는 태그로만 만든다. 어휘 밖의 태그는 문제로 보고한다.
- 입력이 같으면 두 번째 실행에서 바뀌는 파일이 0이어야 한다.

실행(저장소 루트에서): python wiki/_scripts/build_hubs.py
"""
import glob
import os
import re
import sys
import unicodedata
from collections import Counter, defaultdict

WIKI = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HUB_ROOT = os.path.join(WIKI, "hubs")
HUBS = {"years": "연도", "venues": "학회·저널", "authors": "저자", "topics": "주제"}
HUB_NOTES = {
    "authors": "제1저자와 마지막 저자만 연결한다. 저자 목록이 \"외\"나 \"et al.\"로 줄어 있으면 제1저자만 연결한다.\n\n",
    "topics": "`wiki/tags.md`에 있는 태그만 만든다.\n\n",
}
ETAL = re.compile(r"\s*(외|et\s+al\.?)\s*$", re.I)


def read(path):
    with open(path, encoding="utf-8", newline="") as f:
        raw = f.read()
    return raw.replace("\r\n", "\n"), "\r\n" in raw


def write(path, text, crlf=False):
    with open(path, "w", encoding="utf-8", newline="\r\n" if crlf else "\n") as f:
        f.write(text)


def parse_front(text):
    m = re.match(r"---\n(.*?)\n---\n", text, re.S)
    if not m:
        return None, None
    fm, key = {}, None
    for line in m.group(1).split("\n"):
        item = re.match(r"\s*-\s+(.*)", line)
        if item and key:  # YAML 블록 목록
            fm[key] = (fm[key] + ", " if fm[key] else "") + item.group(1).strip()
            continue
        kv = re.match(r"([A-Za-z_]+):\s*(.*)", line)
        if kv:
            key, value = kv.group(1), kv.group(2)
            if not value.startswith(('"', "'")):
                value = value.split(" #")[0]
            fm[key] = value.strip()
    return fm, m.end()


def parse_list(value):
    value = (value or "").strip()
    if value.startswith("[") and value.endswith("]"):
        value = value[1:-1]
    return [x.strip().strip("\"'") for x in value.split(",") if x.strip().strip("\"'")]


def key_authors(value):
    names = parse_list(value)
    truncated = any(ETAL.search(n) for n in names)
    names = [n for n in (ETAL.sub("", n).strip() for n in names) if n]
    if not names:
        return []
    if truncated or len(names) == 1:
        return names[:1]
    return [names[0], names[-1]]


def venue_name(value):
    # "Nature Communications 16:6937"처럼 뒤에 붙은 권·쪽 번호를 뗀다
    return re.sub(r"[\s,]+\d[\d:()\-–, ]*$", "", (value or "").strip().strip("\"'")).strip()


def slug(s):
    s = unicodedata.normalize("NFKD", s)
    s = unicodedata.normalize("NFC", "".join(c for c in s if not unicodedata.combining(c))).lower()
    return re.sub(r"[^\w]+", "-", s).strip("-_") or "unknown"


def load_vocab():
    path = os.path.join(WIKI, "tags.md")
    if not os.path.exists(path):
        return set()
    text = re.sub(r"<!--.*?-->", "", read(path)[0], flags=re.S)
    return set(re.findall(r"^\s*[-*]\s+`([^`]+)`", text, re.M))


def main():
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    vocab = load_vocab()
    papers, problems = [], []
    for path in sorted(glob.glob(os.path.join(WIKI, "papers", "*.md"))):
        stem = os.path.splitext(os.path.basename(path))[0]
        if stem.startswith("_") or stem == "index":
            continue
        text, crlf = read(path)
        fm, end = parse_front(text)
        if fm is None:
            problems.append(f"{stem}: frontmatter 없음")
            continue
        missing = [k for k in ("title", "authors", "year", "venue") if not parse_list(fm.get(k))]
        if missing:
            problems.append(f"{stem}: 빈 항목 {', '.join(missing)}")
        tags = parse_list(fm.get("tags"))
        unknown = [t for t in tags if t not in vocab]
        if unknown:
            problems.append(f"{stem}: tags.md에 없는 태그 {', '.join(unknown)}")
        authors = key_authors(fm.get("authors"))
        papers.append({
            "path": path, "stem": stem, "text": text, "crlf": crlf, "end": end,
            "title": (fm.get("title") or stem).strip("\"'"), "year": fm.get("year", ""),
            "venue": venue_name(fm.get("venue")), "authors": authors,
            "first": authors[0] if authors else "", "status": fm.get("status", ""),
            "tags": [t for t in dict.fromkeys(tags) if t in vocab],
        })

    # 대소문자만 다른 저널명은 가장 많이 쓴 표기로 합친다(같으면 대문자가 많은 표기)
    spellings = defaultdict(Counter)
    for p in papers:
        if p["venue"]:
            spellings[p["venue"].lower()][p["venue"]] += 1
    for p in papers:
        if p["venue"]:
            counts = spellings[p["venue"].lower()]
            p["venue"] = max(counts, key=lambda v: (counts[v], sum(c.isupper() for c in v), v))

    groups = {h: defaultdict(list) for h in HUBS}
    for p in papers:
        if p["year"]:
            groups["years"][p["year"]].append(p)
        if p["venue"]:
            groups["venues"][p["venue"]].append(p)
        for a in dict.fromkeys(p["authors"]):
            groups["authors"][a].append(p)
        for t in p["tags"]:
            groups["topics"][t].append(p)

    changed, removed = 0, 0
    for folder, label in HUBS.items():
        d = os.path.join(HUB_ROOT, folder)
        os.makedirs(d, exist_ok=True)
        files, rows = {}, []
        for key in sorted(groups[folder], key=str.lower):
            entries = sorted(groups[folder][key], key=lambda e: (e["year"], e["first"], e["stem"]))
            lines = [f"- [{e['first']} {e['year']} — {e['title']}](../../papers/{e['stem']}.md) · {e['venue']} · {e['status']}"
                     for e in entries]
            files[f"{slug(key)}.md"] = f"# {key}\n\n{HUB_NOTES.get(folder, '')}" + "\n".join(lines) + "\n"
            rows.append(f"- [{key}]({slug(key)}.md) ({len(entries)})")
        files["index.md"] = (f"# {label} 허브\n\n논문 frontmatter에서 `wiki/_scripts/build_hubs.py`가 만든다. 손으로 고치지 않는다.\n\n"
                             + HUB_NOTES.get(folder, "") + ("\n".join(rows) if rows else "- 아직 없음") + "\n")
        for name in os.listdir(d):
            if name.endswith(".md") and name not in files:
                os.remove(os.path.join(d, name))
                removed += 1
        for name, text in files.items():
            path = os.path.join(d, name)
            if not os.path.exists(path) or read(path)[0] != text:
                write(path, text)
                changed += 1

    pages_changed = 0
    for p in papers:
        parts = []
        if p["year"]:
            parts.append(f"[{p['year']}](../hubs/years/{slug(p['year'])}.md)")
        if p["venue"]:
            parts.append(f"[{p['venue']}](../hubs/venues/{slug(p['venue'])}.md)")
        parts += [f"[{a}](../hubs/authors/{slug(a)}.md)" for a in dict.fromkeys(p["authors"])]
        parts += [f"[{t}](../hubs/topics/{slug(t)}.md)" for t in p["tags"]]
        body = "\n".join(l for l in p["text"][p["end"]:].split("\n") if not l.startswith("허브: ")).lstrip("\n")
        text = p["text"][:p["end"]] + "\n허브: " + " · ".join(parts) + "\n\n" + body
        if text != p["text"]:
            write(p["path"], text, p["crlf"])
            pages_changed += 1

    print(f"논문 {len(papers)}편 · 허브: " + ", ".join(f"{HUBS[h]} {len(groups[h])}" for h in HUBS))
    print(f"바뀐 파일: 허브 {changed}, 논문 페이지 {pages_changed} · 지운 허브 {removed}")
    print(f"문제 {len(problems)}건")
    for line in problems:
        print("  -", line)
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
