#!/usr/bin/env python3
"""모든 프로젝트 페이지의 BibTeX를 공식 출처와 비교한다 (허브 레포 루트에서 실행).

  python3 _template/verify-bibtex.py

출처 우선순위: ACL Anthology .bib > 저널 DOI (Crossref) > arXiv /bibtex/.
공백 차이는 무시하고 나머지는 한 글자라도 다르면 DIFF로 표시한다.
BibTeX는 사람이 그대로 복사해 인용하므로, 손으로 쓰거나 고치지 말고 공식 출처를 그대로 붙여 넣는다.
"""
import glob, html, re, sys, time, urllib.request

def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": "mlplab-site-bibcheck/1.0"})
    return urllib.request.urlopen(req, timeout=40).read().decode("utf-8")

norm = lambda s: re.sub(r"\s+", " ", s).strip()
bad = 0
for path in sorted(glob.glob("_template/*/index.html")):
    slug = path.split("/")[1]
    if slug == "project-page-template":
        continue
    page = open(path, encoding="utf-8").read()
    m = re.search(r'<pre id="bibtex-code"><code>(.*?)</code></pre>', page, re.S)
    if not m:
        print(f"NOBIB  {slug}"); continue
    mine = html.unescape(m.group(1))
    ant = re.search(r'href="https://aclanthology\.org/([0-9a-z.\-]+)/"', page)
    doi = re.search(r'<meta name="citation_doi" content="([^"]+)"', page)
    ax = re.search(r'<meta name="citation_arxiv_id" content="([^"]+)"', page)
    if ant:
        url = f"https://aclanthology.org/{ant.group(1)}.bib"
    elif doi and not doi.group(1).startswith("10.48550"):
        url = f"https://api.crossref.org/works/{doi.group(1)}/transform/application/x-bibtex"
    elif ax:
        url = f"https://arxiv.org/bibtex/{ax.group(1)}"; time.sleep(2)
    else:
        print(f"NOSRC  {slug}"); continue
    try:
        official = get(url)
    except Exception as e:
        print(f"ERROR  {slug} {url} {e}"); bad += 1; continue
    ok = norm(mine) == norm(official)
    bad += not ok
    print(f"{'MATCH' if ok else 'DIFF '}  {slug}  ({url})")
sys.exit(1 if bad else 0)
