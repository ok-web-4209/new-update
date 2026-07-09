#!/usr/bin/env python3
"""Inject BreadcrumbList schema + font preconnect hints (SEO_PLAN.md Phase 1, Subtask 2).

- BreadcrumbList JSON-LD on every subpage (not the homepage), reflecting the
  practice-area hierarchy: Home > [Hub] > [Page].
- <link rel="preconnect"> for fonts.googleapis.com / fonts.gstatic.com ahead
  of the Google Fonts stylesheet (faster LCP).

Idempotent: existing breadcrumb blocks and preconnect hints are replaced,
not duplicated.
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BASE = "https://hoffman.legal/"

HOME = ("Home", BASE)
CRIMINAL = ("Criminal Defense", BASE + "criminal-defense.html")
INJURY = ("Personal Injury", BASE + "personal-injury.html")
ESTATE = ("Estate Planning", BASE + "estate-planning.html")
ET_PROBATION = ("Early Termination of Probation", BASE + "early-termination-of-probation.html")

# file -> breadcrumb trail (Home is prepended automatically)
TRAILS = {
    "criminal-defense.html": [CRIMINAL],
    "dui-defense.html": [CRIMINAL, ("DUI Defense", BASE + "dui-defense.html")],
    "drug-possession-cases.html": [CRIMINAL, ("Drug Possession Cases", BASE + "drug-possession-cases.html")],
    "theft-robbery-burglary.html": [CRIMINAL, ("Theft, Robbery & Burglary", BASE + "theft-robbery-burglary.html")],
    "assault-battery.html": [CRIMINAL, ("Assault & Battery", BASE + "assault-battery.html")],
    "sexual-battery-cases.html": [CRIMINAL, ("Sexual Battery Cases", BASE + "sexual-battery-cases.html")],
    "white-collar-crimes.html": [CRIMINAL, ("White Collar Crimes", BASE + "white-collar-crimes.html")],
    "injunctions.html": [CRIMINAL, ("Injunctions", BASE + "injunctions.html")],
    "expunge-seal-records.html": [CRIMINAL, ("Expunge & Seal Records", BASE + "expunge-seal-records.html")],
    "early-termination-of-probation.html": [CRIMINAL, ET_PROBATION],
    "early-termination-probation-broward-dade-palm-beach.html": [
        CRIMINAL,
        ET_PROBATION,
        ("Broward, Miami-Dade & Palm Beach", BASE + "early-termination-probation-broward-dade-palm-beach.html"),
    ],
    "personal-injury.html": [INJURY],
    "car-accidents.html": [INJURY, ("Car Accidents", BASE + "car-accidents.html")],
    "truck-accidents.html": [INJURY, ("Truck Accidents", BASE + "truck-accidents.html")],
    "motorcycle-accidents.html": [INJURY, ("Motorcycle Accidents", BASE + "motorcycle-accidents.html")],
    "pedestrian-accidents.html": [INJURY, ("Pedestrian Accidents", BASE + "pedestrian-accidents.html")],
    "slip-fall-injuries.html": [INJURY, ("Slip & Fall Injuries", BASE + "slip-fall-injuries.html")],
    "premises-liability.html": [INJURY, ("Premises Liability", BASE + "premises-liability.html")],
    "wrongful-death.html": [INJURY, ("Wrongful Death", BASE + "wrongful-death.html")],
    "dog-bites.html": [INJURY, ("Dog Bites", BASE + "dog-bites.html")],
    "rideshare-accidents.html": [INJURY, ("Rideshare Accidents", BASE + "rideshare-accidents.html")],
    "estate-planning.html": [ESTATE],
    "lady-bird-deed.html": [ESTATE, ("Lady Bird Deed", BASE + "lady-bird-deed.html")],
    "privacy-policy.html": [("Privacy Policy", BASE + "privacy-policy.html")],
    "terms-of-service.html": [("Terms of Service", BASE + "terms-of-service.html")],
}

BREADCRUMB_RE = re.compile(
    r'[ \t]*<script type="application/ld\+json" data-jsonld="breadcrumb">.*?</script>\n?',
    re.S,
)
PRECONNECT_RE = re.compile(r'[ \t]*<link rel="preconnect"[^>]*>\n?')
FONTS_LINK_RE = re.compile(r'[ \t]*<link href="https://fonts\.googleapis\.com[^>]*>')
TWITTER_DESC_RE = re.compile(r'[ \t]*<meta name="twitter:description"[^>]*>')

PRECONNECT = (
    '  <link rel="preconnect" href="https://fonts.googleapis.com">\n'
    '  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
)


def breadcrumb_jsonld(trail):
    items = [HOME] + trail
    data = {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": i, "name": name, "item": url}
            for i, (name, url) in enumerate(items, start=1)
        ],
    }
    body = json.dumps(data, indent=2, ensure_ascii=False)
    body = "\n".join("  " + line for line in body.splitlines())
    return (
        '  <script type="application/ld+json" data-jsonld="breadcrumb">\n'
        f"{body}\n  </script>"
    )


def process(path: Path, trail):
    html = path.read_text(encoding="utf-8")

    # Preconnect hints ahead of the Google Fonts stylesheet
    html = PRECONNECT_RE.sub("", html)
    fonts_link = FONTS_LINK_RE.search(html).group(0)
    html = html.replace(fonts_link, PRECONNECT + "\n" + fonts_link, 1)

    # Breadcrumb JSON-LD after the twitter:description meta (subpages only)
    if trail is not None:
        html = BREADCRUMB_RE.sub("", html)
        anchor = TWITTER_DESC_RE.search(html).group(0)
        html = html.replace(anchor, anchor + "\n" + breadcrumb_jsonld(trail), 1)

    path.write_text(html, encoding="utf-8")
    print(f"ok  {path.name}")


def main():
    process(ROOT / "index.html", None)
    for name, trail in TRAILS.items():
        process(ROOT / name, trail)


if __name__ == "__main__":
    main()
