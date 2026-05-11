#!/usr/bin/env python3
"""
Idempotent site-wide updates:

  1. Inject the analytics.js click-tracker (<script src="assets/analytics.js">)
     before </body> on every HTML page.
  2. Expand the "Practice Areas" nav (desktop dropdown AND mobile accordion)
     so Personal Injury is a parent item with its 9 sub-pages nested under it.
  3. Inject favicon + og:image meta tags into every page <head>.

Run from the repo root:
    python3 _scripts/inject_site_updates.py

Re-runs are safe: each block is guarded by a marker and only injected once.
"""
from __future__ import annotations

import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent

# ---------------------------------------------------------------------------
# 1. Analytics script injection
# ---------------------------------------------------------------------------
ANALYTICS_TAG = '<script src="assets/analytics.js" defer></script>'
ANALYTICS_MARKER = 'assets/analytics.js'


def inject_analytics(html: str) -> str:
    if ANALYTICS_MARKER in html:
        return html
    # Place just before </body>. Put after polish.js if present, but since we
    # use a simple </body> anchor the order is fine either way.
    return html.replace("</body>", f"  {ANALYTICS_TAG}\n</body>", 1)


# ---------------------------------------------------------------------------
# 2. Nav expansion (desktop + mobile)
# ---------------------------------------------------------------------------
# Nine Personal Injury sub-pages.
PI_SUBPAGES = [
    ("car-accidents.html", "Car Accidents"),
    ("truck-accidents.html", "Truck Accidents"),
    ("motorcycle-accidents.html", "Motorcycle Accidents"),
    ("pedestrian-accidents.html", "Pedestrian Accidents"),
    ("slip-fall-injuries.html", "Slip &amp; Fall Injuries"),
    ("premises-liability.html", "Premises Liability"),
    ("wrongful-death.html", "Wrongful Death"),
    ("dog-bites.html", "Dog Bites"),
    ("rideshare-accidents.html", "Rideshare Accidents"),
]

# --- Desktop nav --------------------------------------------------------------
# The source line on every page is exactly:
#   <a href="personal-injury.html" class="nav-dropdown-item">Personal Injury</a>
# Replace with a wrapper that shows a nested submenu on hover.
DESKTOP_PI_OLD = '<a href="personal-injury.html" class="nav-dropdown-item">Personal Injury</a>'
DESKTOP_PI_NEW = (
    '<div class="nav-dropdown-sub">'
    '<a href="personal-injury.html" class="nav-dropdown-item nav-dropdown-parent">'
    'Personal Injury '
    '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" '
    'stroke="currentColor" stroke-width="2" stroke-linecap="round" '
    'stroke-linejoin="round" aria-hidden="true">'
    '<path d="m9 6 6 6-6 6"/></svg></a>'
    '<div class="nav-subdropdown">'
    + "".join(
        f'<a href="{slug}" class="nav-dropdown-item">{label}</a>'
        for slug, label in PI_SUBPAGES
    )
    + "</div></div>"
)

# --- Mobile nav ---------------------------------------------------------------
# The mobile accordion line is exactly:
#   <a href="personal-injury.html">Personal Injury</a>
MOBILE_PI_OLD = '<a href="personal-injury.html">Personal Injury</a>'
MOBILE_PI_NEW = (
    '<div class="mobile-practice-pi">'
    '<a href="personal-injury.html" class="mobile-pi-hub">Personal Injury</a>'
    '<div class="mobile-pi-sublist">'
    + "".join(f'<a href="{slug}">{label}</a>' for slug, label in PI_SUBPAGES)
    + "</div></div>"
)

NAV_MARKER = "nav-dropdown-sub"  # Only present once the new markup is injected.

# --- CSS shim inserted once per page so the new nav renders correctly ---------
NAV_CSS = """
    /* Practice Areas → Personal Injury expandable subnav (added by inject_site_updates.py) */
    .nav-dropdown-sub { position: relative; }
    .nav-dropdown-sub .nav-dropdown-parent {
      display: flex; align-items: center; justify-content: space-between; gap: 0.5rem;
    }
    .nav-dropdown-sub .nav-dropdown-parent svg { width: 12px; height: 12px; opacity: 0.7; }
    .nav-subdropdown {
      position: absolute; top: 0; left: 100%;
      min-width: 16rem;
      background: var(--background);
      border: 1px solid var(--border);
      box-shadow: 0 10px 40px rgba(0, 0, 0, 0.4);
      opacity: 0; visibility: hidden; transform: translateX(-6px);
      transition: opacity 0.2s, visibility 0.2s, transform 0.2s;
      z-index: 60;
    }
    .nav-dropdown-sub:hover .nav-subdropdown,
    .nav-dropdown-sub:focus-within .nav-subdropdown {
      opacity: 1; visibility: visible; transform: translateX(0);
    }
    /* Mobile PI nested list inside the practice accordion */
    .mobile-practice-pi { display: block; }
    .mobile-pi-hub {
      display: block; padding: 0.5rem 0; color: var(--muted-foreground);
      font-weight: 600;
    }
    .mobile-pi-sublist {
      display: block; padding-left: 1rem;
      border-left: 1px solid rgba(191, 155, 107, 0.25);
      margin: 0.25rem 0 0.5rem;
    }
    .mobile-pi-sublist a {
      display: block; padding: 0.4rem 0; font-size: 0.95rem;
      color: var(--muted-foreground);
    }
    .mobile-pi-sublist a:hover { color: var(--primary); }
"""
NAV_CSS_MARKER = "Practice Areas → Personal Injury expandable subnav"


def inject_nav(html: str) -> str:
    """Expand Personal Injury in both desktop dropdown and mobile accordion."""
    if NAV_MARKER in html:
        return html

    out = html

    # Desktop — replace the plain Personal Injury <a> with the expandable wrapper.
    # Only touch the single occurrence inside the nav-dropdown (not sidebars).
    out = out.replace(DESKTOP_PI_OLD, DESKTOP_PI_NEW, 1)

    # Mobile — the mobile accordion version uses just the slug+label anchor.
    out = out.replace(MOBILE_PI_OLD, MOBILE_PI_NEW, 1)

    # CSS shim: insert before </style> in the first <style> block (the page's
    # main stylesheet). All HTML pages here have an inline <style>.
    if NAV_CSS_MARKER not in out and "</style>" in out:
        out = out.replace("</style>", NAV_CSS + "\n  </style>", 1)

    return out


# ---------------------------------------------------------------------------
# 3. Favicon + OG meta injection
# ---------------------------------------------------------------------------
FAVICON_BLOCK = """  <link rel="icon" type="image/svg+xml" href="favicon.svg">
  <link rel="alternate icon" type="image/png" sizes="32x32" href="favicon.svg">
  <link rel="apple-touch-icon" href="favicon.svg">
  <meta property="og:image" content="https://hoffman.legal/dhh-headshot.jpg">
  <meta property="og:image:alt" content="Attorney David Hoffman, Hoffman Legal">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:image" content="https://hoffman.legal/dhh-headshot.jpg">
"""
FAVICON_MARKER = 'href="favicon.svg"'


def inject_favicon(html: str) -> str:
    if FAVICON_MARKER in html:
        return html
    return html.replace("</head>", FAVICON_BLOCK + "</head>", 1)


# ---------------------------------------------------------------------------
# Driver
# ---------------------------------------------------------------------------
def main() -> int:
    html_files = sorted(p for p in ROOT.glob("*.html"))
    if not html_files:
        print("No HTML files found in", ROOT)
        return 1

    changed = 0
    for path in html_files:
        original = path.read_text(encoding="utf-8")
        updated = original
        updated = inject_analytics(updated)
        updated = inject_nav(updated)
        updated = inject_favicon(updated)

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
