#!/usr/bin/env python3
"""
Inject FAQ sections + FAQPage JSON-LD into each practice-area page.

- Reads FAQs from _scripts/faq_data.py
- Inserts an accessible <details>/<summary> accordion into the .service-main
  block, right before the closing </div> that precedes <aside class="service-sidebar">.
- Injects FAQPage JSON-LD into the <head> for Google rich results.
- Idempotent.
"""
from __future__ import annotations
import html
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "_scripts"))
from faq_data import FAQS, FAQ_LEDE  # noqa: E402

FAQ_MARKER = "<!-- faq-pass -->"
JSONLD_MARKER = "faq-jsonld-pass"


def render_faq_html(faqs: list[tuple[str, str]]) -> str:
    items = []
    for question, answer_html in faqs:
        items.append(
            '        <details class="faq-item">\n'
            f'          <summary>{question}</summary>\n'
            f'          <div>{answer_html}</div>\n'
            '        </details>'
        )
    items_html = "\n".join(items)
    return (
        f"{FAQ_MARKER}\n"
        '      <section class="faq-section" data-reveal aria-labelledby="faq-heading">\n'
        '        <h2 id="faq-heading">Frequently Asked Questions</h2>\n'
        f'        <p class="faq-lede">{FAQ_LEDE}</p>\n'
        '        <div class="faq-list">\n'
        f'{items_html}\n'
        '        </div>\n'
        '      </section>'
    )


def render_faq_jsonld(faqs: list[tuple[str, str]]) -> str:
    data = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {
                "@type": "Question",
                "name": q,
                "acceptedAnswer": {
                    "@type": "Answer",
                    # Strip HTML tags for the schema text — search engines want plain text.
                    "text": re.sub(r"<[^>]+>", "", a).strip(),
                },
            }
            for q, a in faqs
        ],
    }
    return (
        f'  <script type="application/ld+json" data-jsonld="{JSONLD_MARKER}">\n'
        f'{json.dumps(data, ensure_ascii=False, indent=2)}\n'
        '  </script>'
    )


def inject_into_head(page_html: str, jsonld_block: str) -> str:
    if JSONLD_MARKER in page_html:
        return page_html
    return page_html.replace("</head>", f"{jsonld_block}\n</head>", 1)


def inject_into_body(page_html: str, faq_block: str) -> str:
    if FAQ_MARKER in page_html:
        return page_html

    # Place FAQ inside .service-main, right before the wrap that introduces
    # <aside class="service-sidebar">. The existing HTML structure is:
    #   <main class="service-wrap"><div class="service-main">... sections ...</div><aside ...>...
    # We want to insert the FAQ just before "</div><aside class="service-sidebar">".
    pattern = re.compile(
        r'(</div>)(\s*<aside class="service-sidebar">)',
        re.MULTILINE,
    )
    new_html, n = pattern.subn(
        lambda m: f'\n      {faq_block}\n    {m.group(1)}{m.group(2)}',
        page_html,
        count=1,
    )
    if n == 0:
        # Fallback: try inserting right before closing </main> of service-wrap.
        new_html, n = re.subn(
            r'(</main>)',
            lambda m: f'      {faq_block}\n    {m.group(1)}',
            page_html,
            count=1,
        )
    return new_html


def main() -> int:
    changed = 0
    skipped = 0
    missing = []
    for filename, faqs in FAQS.items():
        path = ROOT / filename
        if not path.exists():
            missing.append(filename)
            continue

        original = path.read_text(encoding="utf-8")
        faq_block = render_faq_html(faqs)
        jsonld_block = render_faq_jsonld(faqs)

        updated = inject_into_head(original, jsonld_block)
        updated = inject_into_body(updated, faq_block)

        if updated != original:
            path.write_text(updated, encoding="utf-8")
            print(f"  patched: {filename}")
            changed += 1
        else:
            print(f"  skipped: {filename}")
            skipped += 1

    if missing:
        print("\nMissing files referenced in faq_data.py:")
        for m in missing:
            print(f"  - {m}")

    print(f"\n{changed} patched, {skipped} skipped, {len(missing)} missing.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
