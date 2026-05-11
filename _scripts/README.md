# _scripts

Build-time helpers for editing site content at scale. These scripts only touch
local HTML files — they do not run at page load and are not served to visitors.

## What's here

| File | Purpose |
| --- | --- |
| `inject_polish.py` | Injects shared polish widgets (progress bar, back-to-top, sticky mobile CTA) and the `assets/polish.css` / `assets/polish.js` tags into every `*.html` page. Also rewrites the footer Privacy/Terms links on `index.html`. |
| `inject_faqs.py` | Renders FAQ accordions and `FAQPage` JSON-LD into each practice-area page, reading content from `faq_data.py`. |
| `faq_data.py` | The source of truth for every practice-area FAQ. Edit here, then re-run `inject_faqs.py`. |

All scripts are **idempotent** — running them twice is a no-op.

## Typical workflow

Edit an FAQ answer or add a new question:

1. Open `_scripts/faq_data.py` and update the list for the relevant page.
2. From the repo root, run:
   ```
   python3 _scripts/inject_faqs.py
   ```
3. Inspect the changed HTML, commit, and push.

Add a new practice-area page:

1. Copy an existing service page (e.g. `dui-defense.html`) and rename.
2. Replace content as appropriate.
3. Add an entry for the new filename to `FAQS` in `faq_data.py`.
4. Run `python3 _scripts/inject_faqs.py` to add FAQs.
5. Run `python3 _scripts/inject_polish.py` to wire up shared widgets.

## Why scripts instead of editing HTML directly?

Twenty-two practice-area pages share the same structure. A small script keeps
the content consistent, makes future refreshes trivial (one edit, re-run), and
prevents drift between pages. The generated HTML is still perfectly readable
and hand-editable if needed.
