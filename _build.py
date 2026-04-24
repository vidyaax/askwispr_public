"""Convert the legal markdown files into standalone HTML pages.

Usage (from this folder):
    python _build.py

Reads /Users/rahul/git/wispr_whatsapp_agent/legal/*.md and writes sibling
HTML files next to this script.
"""
from __future__ import annotations

import pathlib

import markdown

SRC = pathlib.Path("/Users/rahul/git/wispr_whatsapp_agent/legal")
DST = pathlib.Path(__file__).resolve().parent

PAGES = [
    ("privacy-policy.md", "privacy-policy.html", "Privacy Policy — AskWispr"),
    ("terms-of-service.md", "terms-of-service.html", "Terms of Service — AskWispr"),
    ("data-deletion.md", "data-deletion.html", "Data Deletion — AskWispr"),
]

TEMPLATE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width,initial-scale=1" />
<meta name="robots" content="index,follow" />
<title>{title}</title>
<link rel="stylesheet" href="style.css" />
</head>
<body>
<main class="prose">
{body}
<hr />
<p class="footer">
<a href="index.html">All legal documents</a> ·
<a href="privacy-policy.html">Privacy Policy</a> ·
<a href="terms-of-service.html">Terms of Service</a> ·
<a href="data-deletion.html">Data Deletion</a>
</p>
</main>
</body>
</html>
"""

INDEX_TEMPLATE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width,initial-scale=1" />
<title>AskWispr — Legal</title>
<link rel="stylesheet" href="style.css" />
</head>
<body>
<main class="prose">
<h1>AskWispr — Legal</h1>
<p>
AskWispr is a software platform operated by <strong>Vidyaax</strong>.
It powers multilingual, AI-assisted customer-support assistants on
WhatsApp for businesses .
</p>
<ul>
<li><a href="privacy-policy.html">Privacy Policy</a></li>
<li><a href="terms-of-service.html">Terms of Service</a></li>
<li><a href="data-deletion.html">Data Deletion Instructions</a></li>
</ul>
<p class="footer">
Contact: <a href="mailto:privacy@vidyaax.com">privacy@vidyaax.com</a>
</p>
</main>
</body>
</html>
"""

CSS = """:root {
  --fg: #1f2328;
  --muted: #656d76;
  --rule: #d1d9e0;
  --bg: #ffffff;
  --code-bg: #f6f8fa;
  --accent: #0969da;
  --th-bg: #f6f8fa;
}

* { box-sizing: border-box; }

body {
  margin: 0;
  color: var(--fg);
  background: var(--bg);
  font: 16px/1.6 -apple-system, BlinkMacSystemFont, "Segoe UI",
        "Helvetica Neue", Arial, "Noto Sans", sans-serif;
}

.prose {
  max-width: 780px;
  margin: 0 auto;
  padding: 48px 24px 64px;
}

h1, h2, h3 { line-height: 1.25; margin-top: 1.8em; }
h1 { font-size: 1.9rem; margin-top: 0; }
h2 { font-size: 1.35rem; border-bottom: 1px solid var(--rule); padding-bottom: .3em; }
h3 { font-size: 1.1rem; }

p, ul, ol, table { margin: 0 0 1em; }
ul, ol { padding-left: 1.4em; }
li + li { margin-top: .2em; }

a { color: var(--accent); text-decoration: none; }
a:hover { text-decoration: underline; }

hr { border: 0; border-top: 1px solid var(--rule); margin: 2em 0; }

em { color: var(--muted); }

code {
  background: var(--code-bg);
  padding: .15em .35em;
  border-radius: 4px;
  font-size: .92em;
  font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
}

table {
  width: 100%;
  border-collapse: collapse;
  font-size: .95rem;
}

th, td {
  border: 1px solid var(--rule);
  padding: .5em .7em;
  text-align: left;
  vertical-align: top;
}

th { background: var(--th-bg); font-weight: 600; }

.footer {
  color: var(--muted);
  font-size: .9rem;
  margin-top: 2em;
}

@media (max-width: 560px) {
  .prose { padding: 24px 16px 48px; }
  h1 { font-size: 1.55rem; }
  table, th, td { font-size: .9rem; }
}
"""


def build() -> None:
    md = markdown.Markdown(extensions=["tables", "fenced_code", "sane_lists"])
    for src_name, dst_name, title in PAGES:
        text = (SRC / src_name).read_text(encoding="utf-8")
        body_html = md.reset().convert(text)
        (DST / dst_name).write_text(
            TEMPLATE.format(title=title, body=body_html),
            encoding="utf-8",
        )
        print(f"wrote {dst_name}")
    (DST / "index.html").write_text(INDEX_TEMPLATE, encoding="utf-8")
    print("wrote index.html")
    (DST / "style.css").write_text(CSS, encoding="utf-8")
    print("wrote style.css")


if __name__ == "__main__":
    build()
