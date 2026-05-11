#!/usr/bin/env python3
"""
Inject the modern polish pass into every HTML page:
  1. <link rel="stylesheet" href="assets/polish.css"> before </head>
  2. Shared DOM (progress bar, sticky CTA bar, back-to-top button) + script
     tag before </body>
  3. On index.html only, replace broken footer "#" links with real targets.
  4. Add data-reveal attributes to a handful of key sections on index.html.

Idempotent: re-running is a no-op after the first successful pass.
"""
from __future__ import annotations
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent

POLISH_CSS_TAG = '<link rel="stylesheet" href="assets/polish.css">'
POLISH_JS_TAG = '<script src="assets/polish.js" defer></script>'

# Shared widgets appended just before </body>. One template, all pages.
SHARED_WIDGETS = """
  <!-- Modern polish: reading progress + back-to-top + sticky mobile CTA -->
  <div class="read-progress" aria-hidden="true"></div>
  <button class="back-to-top" type="button" aria-label="Back to top">
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="18 15 12 9 6 15"/></svg>
  </button>
  <nav class="mobile-cta-bar" aria-label="Quick contact">
    <a class="mcb-call" href="tel:9544594236" aria-label="Call Hoffman Legal">
      <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></svg>
      Call Now
    </a>
    <a class="mcb-consult" href="__CONSULT__">
      <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></svg>
      Free Consult
    </a>
  </nav>
"""

INJECT_MARKER = "<!-- Modern polish: reading progress + back-to-top + sticky mobile CTA -->"
CSS_MARKER = 'href="assets/polish.css"'


def inject_head(html: str) -> str:
    if CSS_MARKER in html:
        return html
    return html.replace("</head>", f"  {POLISH_CSS_TAG}\n</head>", 1)


def inject_body(html: str, is_index: bool) -> str:
    if INJECT_MARKER in html:
        return html

    consult_href = "#contact" if is_index else "index.html#contact"
    widgets = SHARED_WIDGETS.replace("__CONSULT__", consult_href)

    # Place widgets + script right before </body>
    return html.replace(
        "</body>",
        f"{widgets}\n  {POLISH_JS_TAG}\n</body>",
        1,
    )


def patch_index_footer(html: str) -> str:
    """Replace the broken href='#' links in index.html's footer-links block."""
    # Be very targeted: only within the specific footer-links block.
    pattern = re.compile(
        r'(<div class="footer-links">\s*)'
        r'<a href="#">Privacy Policy</a>'
        r'(\s*<span class="footer-links-dot"></span>\s*)'
        r'<a href="#">Terms of Service</a>',
        re.MULTILINE,
    )
    replacement = (
        r'\1<a href="privacy-policy.html">Privacy Policy</a>'
        r'\2<a href="terms-of-service.html">Terms of Service</a>'
    )
    return pattern.sub(replacement, html, count=1)


def add_reveal_to_index(html: str) -> str:
    """Tag a handful of key landmark sections with data-reveal."""
    # Skip if already tagged.
    if 'data-reveal' in html:
        return html

    replacements = [
        # Practice areas grid — stagger children
        ('<div class="practice-grid">', '<div class="practice-grid" data-reveal>'),
        # Why-us grid
        ('<div class="why-grid">', '<div class="why-grid" data-reveal>'),
        # Reviews summary + grid
        ('<div class="reviews-summary">', '<div class="reviews-summary" data-reveal>'),
        ('<div class="reviews-grid" id="reviewsGrid">',
         '<div class="reviews-grid" id="reviewsGrid" data-reveal data-reveal-delay="1">'),
        # Strategy block
        ('<div class="strategy-content">', '<div class="strategy-content" data-reveal>'),
        # Attorney content
        ('<div class="attorney-content">', '<div class="attorney-content" data-reveal>'),
        # Contact grid
        ('<div class="contact-grid">', '<div class="contact-grid" data-reveal>'),
    ]
    for old, new in replacements:
        html = html.replace(old, new, 1)
    return html


def add_reveal_to_service(html: str) -> str:
    if 'data-reveal' in html:
        return html
    # Tag each content-card on service pages so they reveal progressively.
    # Limit to the first 6 to keep things light.
    count = [0]
    def repl(match):
        count[0] += 1
        delay = min(count[0], 3)
        return f'<section class="content-card" data-reveal data-reveal-delay="{delay}">'
    new_html, _ = re.subn(
        r'<section class="content-card">',
        repl,
        html,
        count=6,
    )
    # Also tag the hero intro + sidebar + cta box once each.
    new_html = new_html.replace(
        '<section class="service-hero">',
        '<section class="service-hero" data-reveal>',
        1,
    )
    new_html = new_html.replace(
        '<section class="service-cta-box">',
        '<section class="service-cta-box" data-reveal>',
        1,
    )
    return new_html


def main() -> int:
    html_files = sorted(p for p in ROOT.glob("*.html"))
    if not html_files:
        print("No HTML files found in", ROOT)
        return 1

    changed = 0
    for path in html_files:
        original = path.read_text(encoding="utf-8")
        updated = original

        updated = inject_head(updated)
        updated = inject_body(updated, is_index=(path.name == "index.html"))

        if path.name == "index.html":
            updated = patch_index_footer(updated)
            updated = add_reveal_to_index(updated)
        else:
            updated = add_reveal_to_service(updated)

        if updated != original:
            path.write_text(updated, encoding="utf-8")
            changed += 1
            print(f"  patched: {path.name}")
        else:
            print(f"  skipped: {path.name}")

    print(f"\n{changed}/{len(html_files)} files patched.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
