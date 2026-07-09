#!/usr/bin/env python3
"""Inject SEO metadata across all pages (SEO_PLAN.md Phase 1, Subtask 1).

For every page:
  - Rewrite <title> with the geo formula: {Practice} | {Geo} | Hoffman Legal
  - Rewrite meta description as a <=155 char CTA with the firm phone number
  - Add rel=canonical
  - Add og:title, og:description, og:type, og:url, og:site_name
  - Add twitter:title, twitter:description

Idempotent: existing tags are replaced, missing tags are inserted after the
meta description. og:image / twitter:card tags (already present sitewide)
are left untouched.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BASE = "https://hoffman.legal/"

# file -> (title, meta description)
META = {
    "index.html": (
        "Dania Beach Criminal Defense &amp; Personal Injury Lawyer | Hoffman Legal",
        "Florida attorney David Hoffman defends criminal, DUI &amp; injury cases in Broward, Miami-Dade &amp; Palm Beach. Free 24/7 consultation: (954) 459-4236.",
    ),
    "criminal-defense.html": (
        "Broward County Criminal Defense Lawyer | South Florida | Hoffman Legal",
        "Broward County criminal defense lawyer &amp; former public defender fighting felony and misdemeanor charges. Free 24/7 consultation: (954) 459-4236.",
    ),
    "dui-defense.html": (
        "Broward County DUI Lawyer | DUI Defense Attorney | Hoffman Legal",
        "Arrested for DUI in Broward County? Hoffman Legal challenges the stop, breath test &amp; license suspension. Free 24/7 consultation: (954) 459-4236.",
    ),
    "drug-possession-cases.html": (
        "Drug Possession Defense Lawyer | Broward County, FL | Hoffman Legal",
        "Facing drug possession charges in Broward County? Former public defender David Hoffman fights for the best outcome. Free consultation: (954) 459-4236.",
    ),
    "theft-robbery-burglary.html": (
        "Theft, Robbery &amp; Burglary Lawyer | Broward County, FL | Hoffman Legal",
        "Charged with theft, robbery, or burglary in Broward County, FL? Protect your record and your freedom. Free 24/7 consultation: (954) 459-4236.",
    ),
    "assault-battery.html": (
        "Assault &amp; Battery Defense Lawyer | Broward County, FL | Hoffman Legal",
        "Assault &amp; battery defense lawyer in Broward County, FL. Former public defender building your strongest defense. Free consultation: (954) 459-4236.",
    ),
    "sexual-battery-cases.html": (
        "Sexual Battery Defense Lawyer | Broward County, FL | Hoffman Legal",
        "Accused of sexual battery in Florida? Discreet, aggressive defense from a former public defender. Free confidential consultation: (954) 459-4236.",
    ),
    "white-collar-crimes.html": (
        "White Collar Crime Defense Lawyer | Broward County, FL | Hoffman Legal",
        "White collar crime defense in Broward County: fraud, embezzlement &amp; financial charges. Free confidential consultation: (954) 459-4236.",
    ),
    "injunctions.html": (
        "Injunction Defense Lawyer | Broward County, FL | Hoffman Legal",
        "Fighting a restraining order or injunction in Broward County, FL? Protect your rights at the hearing. Free consultation: (954) 459-4236.",
    ),
    "expunge-seal-records.html": (
        "Seal &amp; Expunge Criminal Records | Broward County, FL | Hoffman Legal",
        "Seal or expunge your criminal record in Broward County, FL. Eligibility review, filing &amp; court appearance. Free consultation: (954) 459-4236.",
    ),
    "early-termination-of-probation.html": (
        "Early Termination of Probation Lawyer | Florida | Hoffman Legal",
        "End your Florida probation early. Hoffman Legal prepares and argues early termination motions statewide. Free consultation: (954) 459-4236.",
    ),
    # Geo title/description already set when this page was built; keep them.
    "early-termination-probation-broward-dade-palm-beach.html": (None, None),
    "personal-injury.html": (
        "Broward County Personal Injury Lawyer | South Florida | Hoffman Legal",
        "Broward County personal injury lawyer fighting for full compensation after South Florida accidents. Free consultation: (954) 459-4236.",
    ),
    "car-accidents.html": (
        "Broward County Car Accident Lawyer | South Florida | Hoffman Legal",
        "Car accident lawyer serving Broward County &amp; South Florida. Insurance claims, PIP &amp; injury lawsuits. Free consultation: (954) 459-4236.",
    ),
    "truck-accidents.html": (
        "Truck Accident Lawyer | Broward County, FL | Hoffman Legal",
        "Truck accident lawyer in Broward County, FL. Holding trucking companies accountable for serious injuries. Free consultation: (954) 459-4236.",
    ),
    "motorcycle-accidents.html": (
        "Motorcycle Accident Lawyer | Broward County, FL | Hoffman Legal",
        "Motorcycle accident lawyer serving Broward County &amp; South Florida riders. Get full compensation. Free consultation: (954) 459-4236.",
    ),
    "pedestrian-accidents.html": (
        "Pedestrian Accident Lawyer | Broward County, FL | Hoffman Legal",
        "Hit by a car in South Florida? Pedestrian accident lawyer serving Broward County. Free consultation: (954) 459-4236.",
    ),
    "slip-fall-injuries.html": (
        "Slip &amp; Fall Injury Lawyer | Broward County, FL | Hoffman Legal",
        "Slip &amp; fall injury lawyer in Broward County, FL. Holding property owners accountable for negligence. Free consultation: (954) 459-4236.",
    ),
    "premises-liability.html": (
        "Premises Liability Lawyer | Broward County, FL | Hoffman Legal",
        "Injured on unsafe property in South Florida? Premises liability lawyer serving Broward County. Free consultation: (954) 459-4236.",
    ),
    "wrongful-death.html": (
        "Wrongful Death Lawyer | Broward County, FL | Hoffman Legal",
        "Compassionate wrongful death lawyer serving Broward County &amp; South Florida families. Free confidential consultation: (954) 459-4236.",
    ),
    "dog-bites.html": (
        "Dog Bite Injury Lawyer | Broward County, FL | Hoffman Legal",
        "Dog bite injury lawyer in Broward County, FL. Florida strict liability holds owners responsible. Free consultation: (954) 459-4236.",
    ),
    "rideshare-accidents.html": (
        "Uber &amp; Lyft Accident Lawyer | Broward County, FL | Hoffman Legal",
        "Injured in an Uber or Lyft accident in South Florida? Rideshare accident lawyer serving Broward County. Free consultation: (954) 459-4236.",
    ),
    "estate-planning.html": (
        "Florida Estate Planning Attorney | Wills &amp; Trusts | Hoffman Legal",
        "Florida estate planning attorney for wills, trusts, powers of attorney &amp; lady bird deeds. Plan with confidence. Free consultation: (954) 459-4236.",
    ),
    "lady-bird-deed.html": (
        "Lady Bird Deed Attorney in Florida | Hoffman Legal",
        "Florida lady bird deed attorney. Avoid probate &amp; keep control of your home with an enhanced life estate deed. Free consultation: (954) 459-4236.",
    ),
    "privacy-policy.html": (
        "Privacy Policy | Hoffman Legal",
        "Privacy policy for hoffman.legal, the website of Hoffman Legal, a law firm in Dania Beach, Florida.",
    ),
    "terms-of-service.html": (
        "Terms of Service | Hoffman Legal",
        "Terms of service for hoffman.legal, the website of Hoffman Legal, a law firm in Dania Beach, Florida.",
    ),
}

TITLE_RE = re.compile(r"<title>.*?</title>", re.S)
DESC_RE = re.compile(r'[ \t]*<meta name="description" content="[^"]*">')


def strip_tag(html, pattern):
    """Remove an existing head tag (whole line) matching regex pattern."""
    return re.sub(r"[ \t]*" + pattern + r"\n?", "", html)


def process(path: Path):
    html = path.read_text(encoding="utf-8")
    name = path.name
    url = BASE if name == "index.html" else BASE + name

    title_override, desc_override = META[name]

    # 1. Title
    if title_override:
        html = TITLE_RE.sub(f"<title>{title_override}</title>", html, count=1)

    # 2. Meta description
    if desc_override:
        html = DESC_RE.sub(
            f'  <meta name="description" content="{desc_override}">', html, count=1
        )

    # Current (possibly just-rewritten) values drive the og/twitter tags
    title_now = TITLE_RE.search(html).group(0)[7:-8]
    desc_now = re.search(r'<meta name="description" content="([^"]*)"', html).group(1)

    # 3. Drop stale versions of tags we own, then insert one canonical block
    for pat in (
        r'<link rel="canonical"[^>]*>',
        r'<meta property="og:title"[^>]*>',
        r'<meta property="og:description"[^>]*>',
        r'<meta property="og:type"[^>]*>',
        r'<meta property="og:url"[^>]*>',
        r'<meta property="og:site_name"[^>]*>',
        r'<meta name="twitter:title"[^>]*>',
        r'<meta name="twitter:description"[^>]*>',
    ):
        html = strip_tag(html, pat)

    block = "\n".join(
        [
            f'  <link rel="canonical" href="{url}">',
            f'  <meta property="og:title" content="{title_now}">',
            f'  <meta property="og:description" content="{desc_now}">',
            '  <meta property="og:type" content="website">',
            f'  <meta property="og:url" content="{url}">',
            '  <meta property="og:site_name" content="Hoffman Legal">',
            f'  <meta name="twitter:title" content="{title_now}">',
            f'  <meta name="twitter:description" content="{desc_now}">',
        ]
    )

    desc_line = DESC_RE.search(html).group(0)
    html = html.replace(desc_line, desc_line + "\n" + block, 1)

    path.write_text(html, encoding="utf-8")
    print(f"ok  {name}")


def main():
    missing = [n for n in META if not (ROOT / n).exists()]
    if missing:
        sys.exit(f"missing files: {missing}")
    for name in META:
        process(ROOT / name)


if __name__ == "__main__":
    main()
