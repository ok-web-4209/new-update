# Hoffman Legal — SEO Growth Plan
### Goal: rank hoffman.legal at the top of South Florida attorney searches and generate consistent client leads

Prepared: July 2026 · Status: **PLAN ONLY — no implementation yet**

---

## 1. Where the site stands today (audit)

**What's already good**
- 25 clean static HTML pages: 12 criminal-defense pages, 9 personal-injury pages, 2 estate-planning pages, legal pages
- FAQPage JSON-LD on every practice page; LegalService + Attorney + AggregateRating schema on the homepage
- `sitemap.xml`, `robots.txt`, GA4 tracking installed
- One location-targeted page already exists and proves the pattern: `early-termination-probation-broward-dade-palm-beach.html`

**Critical gaps found**
| # | Gap | Why it hurts |
|---|-----|--------------|
| 1 | **No geo modifiers in title tags** — e.g. `Criminal Defense \| Hoffman Legal` | Google can't match the page to "Fort Lauderdale criminal defense lawyer" searches. Every competitor titles pages `{City} {Practice} Lawyer \| {County} ...` |
| 2 | **24 of 25 pages missing `rel=canonical`** | Duplicate-URL risk (http/https, with/without .html), diluted signals |
| 3 | **No attorney bio / About page** | E-E-A-T is decisive in legal (a "Your Money or Your Life" niche). Google rewards visible attorney credentials, bar admissions, experience |
| 4 | **Only 1 location page** for a firm serving 3 counties / ~6M people | Competitors have 10–40 city pages each; this is the single biggest traffic gap |
| 5 | Meta descriptions are body-text paragraphs, not written CTAs | Lower click-through from search results |
| 6 | `sameAs: []` empty in schema; no Avvo/Justia/FindLaw profiles linked | Directories occupy 30–50% of every legal SERP and pass authority |
| 7 | No `og:image`, `og:url`, Twitter cards, or BreadcrumbList schema | Weaker social sharing + SERP presentation |
| 8 | No blog/resources section | No way to capture long-tail question searches or show freshness |

---

## 2. Competitor analysis — who ranks and why (Task 1)

Live SERP sampling for the firm's core money keywords surfaced these consistent winners:

### Organic winners (Broward criminal defense / DUI)
| Competitor | Site | Why they rank |
|---|---|---|
| **Meltzer & Bell** | browardcriminalteam.com | 1,000+ Google reviews (dominates local pack), keyword-rich domain, deep DUI silo (first DUI, breath test, license suspension each get a page), city pages |
| **Ansara Law** | ansaralaw.com | City page for *every* Broward municipality (`/hallandale-beach.html`, `/dania-beach.html` on injury subdomain), 20 years of content history, practice hub-and-spoke |
| **Hager & Schwartz** | defendyourbrowardcase.com | `/areas-we-serve/{city}/` hub, "former prosecutors" E-E-A-T angle |
| **Erase The Case** | erasethecase.com | **Niche domination model**: one practice (expungement) × a page per county (`/locations/broward-county-expungement-lawyer/`) ranks statewide — the most directly copyable model for Hoffman's expungement & early-termination niches |
| **Wolfson & Leon, Flaxman, LWM** (injury) | — | Rank for "Dania Beach car accident lawyer" purely via community pages with local road/hospital/court details |

### Directory layer
Justia, Avvo, FindLaw, Super Lawyers, and LawInfo take 3–5 of the top-10 slots on nearly every query. You can't outrank all of them — instead **be listed in them** (free/cheap profiles, reviews, and a backlink each).

### Synthesis — the 6 ranking levers competitors use
1. **Google Business Profile + review volume** → wins the map pack, where most "near me" phone calls happen
2. **Hub-and-spoke architecture**: practice hub → sub-issue spokes → practice × city pages
3. **Exact-match geo title tags** on every page
4. **E-E-A-T**: attorney bio, credentials, case results, "former public defender/prosecutor" positioning
5. **Content depth with local specificity**: 1,200–3,000 words naming actual courthouses, jails, crash corridors
6. **Backlinks**: legal directories, Florida Bar profile, local press, chambers of commerce

Hoffman Legal already has lever 5 partially (long FAQ-rich pages) and lever 4's raw material ("former public defender") — it's missing levers 1–3 and 6 almost entirely.

---

## 3. Keyword map (Task 2)

Exact volumes require Google Search Console + a keyword tool (see §7 measurement), but SERP analysis gives us the target structure. Ordered by winnability × lead value:

### Tier A — Niche, low competition, high conversion (win in 1–3 months)
These match pages the firm already has; competitors are thin here:
- `early termination of probation florida` / `motion to terminate probation early broward` ✅ page exists
- `seal and expunge record broward county` / `expungement lawyer fort lauderdale` / `how to expunge a record in florida`
- `lady bird deed florida` / `lady bird deed vs living trust florida`
- `domestic violence injunction defense lawyer broward` / `fight restraining order florida`
- `withhold of adjudication florida expungement`

### Tier B — City mid-tail (win in 3–6 months) → drives the location-page build
- `dania beach criminal defense lawyer` · `dania beach car accident lawyer` (home turf, weakest competition)
- `hollywood fl criminal defense attorney` · `hollywood dui lawyer`
- `hallandale beach criminal lawyer` · `pembroke pines dui attorney` · `davie criminal defense lawyer`
- `{city} personal injury lawyer` for the same city set

### Tier C — County/metro head terms (6–12+ month targets)
- `fort lauderdale criminal defense lawyer` · `broward county criminal defense attorney`
- `dui lawyer fort lauderdale` · `personal injury lawyer fort lauderdale`
- `miami criminal defense attorney` (very hard; support with Miami-Dade pages, don't lead with it)

### Tier D — Long-tail informational (blog/FAQ fuel, continuous)
- "what happens after a first DUI in florida", "how much does it cost to seal a record in florida", "florida PIP 14 day rule", "can you expunge a felony in florida", "how long does probation early termination take"

**Title-tag formula to adopt sitewide:** `{City/County} {Practice} Lawyer | {Secondary Geo} {Practice} Attorney | Hoffman Legal`

---

## 4. Location pages strategy across Florida (Task 3)

Yes — this is the highest-leverage move, **but only if each page is genuinely unique**. Google's site-reputation/doorway-page policies penalize find-and-replace city clones. Erase The Case and Ansara prove the model works when pages carry real local substance.

### Architecture
```
/locations.html                     ← "Areas We Serve" hub (links every location page)
/criminal-defense-lawyer-fort-lauderdale.html   ← practice × city (money pages)
/dui-lawyer-hollywood-fl.html
/car-accident-lawyer-dania-beach.html
/hallandale-beach-attorney.html                 ← general city page (smaller cities)
/expungement-lawyer-broward-county.html         ← practice × county (Erase The Case model)
```

### Rollout phases (5–8 pages per batch to avoid a spam footprint)
| Phase | Geography | Pages |
|---|---|---|
| **B1 — Home turf** | Dania Beach, Hollywood, Fort Lauderdale, Hallandale Beach | Practice × city for the 3 lead practices (criminal defense, DUI, car accident/PI) ≈ 10–12 pages |
| **B2 — Rest of Broward** | Pembroke Pines, Miramar, Davie, Plantation, Sunrise, Pompano Beach, Coral Springs, Deerfield Beach, Weston | 1 strong general city page each ≈ 9 pages |
| **B3 — Niche × county** | Broward, Miami-Dade, Palm Beach | Expungement, early termination (exists), injunction defense per county ≈ 6–8 pages |
| **B4 — Miami-Dade & Palm Beach cities** | Miami, Miami Beach, Aventura, North Miami, Hialeah; West Palm Beach, Boca Raton, Delray Beach, Boynton Beach | ≈ 9–12 pages, only after B1–B3 index and GSC confirms traction |

### Mandatory uniqueness ingredients per page (≥1,200 words, ≥70% unique)
- The actual courthouse serving that city (e.g. Broward Central Courthouse, 201 SE 6th St; South Satellite Courthouse in Hollywood) and jail/booking location (BSO Main Jail)
- Local enforcement patterns: DUI checkpoint corridors, crash hotspots (I-95, US-1, A1A, Sheridan St), relevant local stats
- City-specific FAQs (different questions per city) with FAQPage schema
- `LegalService` schema with `areaServed` for that city + BreadcrumbList
- Cross-links: practice hub ↔ city page ↔ neighboring city pages; footer "Areas We Serve" block sitewide

---

## 5. Technical & on-page fixes (do first — one-time, high ROI)

1. **Rewrite all 25 title tags** with the geo formula (§3) — biggest single-day win available
2. **Add `rel=canonical`** to the 24 pages missing it
3. **Rewrite meta descriptions** as ≤155-char CTAs with phone number
4. **Create `attorney-david-hoffman.html`** (bio: former public defender, bar admissions, education, photo, Person/Attorney schema) and link it sitewide — closes the E-E-A-T hole
5. **Add `og:url`, `og:image`, Twitter card tags** to all pages; **BreadcrumbList schema** on all subpages
6. **Populate `sameAs`** in schema once directory profiles exist (§6)
7. Case results / testimonials page (with real, verifiable reviews — schema's current "6 reviews" claim must be backed by visible reviews to be safe)
8. Font loading: add `preconnect` + `display=swap` for Google Fonts (LCP)
9. Keep `sitemap.xml` current with every new page; update `lastmod` honestly

---

## 6. Off-site (requires owner action — the plan flags these, code can't do them)

1. **Google Business Profile**: claim/verify for the Dania Beach office, all relevant categories (Criminal Justice Attorney, Personal Injury Attorney, DUI…), photos, posts — this is what wins the map pack where most calls originate
2. **Review pipeline**: systematic post-case Google review requests; target 25+ reviews in 6 months (Meltzer & Bell's 1,000+ shows the ceiling)
3. **Directory profiles**: Avvo, Justia, FindLaw, Super Lawyers, Lawyers.com, LawInfo, Yelp, BBB, Florida Bar member profile, Dania Beach/Greater Fort Lauderdale chambers → citations + backlinks + `sameAs` targets
4. Longer term: local PR (case commentary to South Florida outlets), Florida legal blog guest posts

---

## 7. Content engine + measurement

- **/blog (or /resources)**: 2–4 posts/month targeting Tier D questions, each internally linking to a money page. Start with expungement-cost, first-DUI, PIP-14-day, lady-bird-deed comparisons — topics with page-one directory-only competition
- **Google Search Console**: verify property immediately (free, and it's the ground truth for Task 2's keyword volumes — replaces guesswork within 4–6 weeks)
- **GA4 conversions**: events on `tel:` clicks and contact-form submits so "more leads" is measurable
- Monthly loop: GSC query report → find pages ranking 5–20 → strengthen those pages/build supporting links

---

## 8. Execution roadmap

| Phase | Scope | Effort | Expected effect |
|---|---|---|---|
| **1. Technical/on-page fixes** (§5 items 1–5, 8–9) | All existing pages | 1 PR | Immediate relevance boost for geo queries; proper indexing |
| **2. Locations hub + B1 home-turf pages** (§4) | ~12 new pages | 2–3 PRs | Tier B rankings in weakest-competition cities within ~8–12 weeks |
| **3. B2 Broward + B3 niche×county pages** | ~16 new pages | 2–3 PRs | Countywide coverage; Tier A niche domination |
| **4. Blog engine + B4 expansion** | ongoing | 1 PR + cadence | Long-tail traffic, freshness, internal-link equity |
| **Parallel: GBP, reviews, directories** (§6) | owner tasks | checklist | Map-pack visibility — likely the largest lead source |

**Order matters**: Phase 1 before location pages (so new pages launch with correct patterns), GSC verification on day 1 (data accrues while we build).

---

## Sources consulted
- SERP sampling July 2026: [Justia Fort Lauderdale](https://www.justia.com/lawyers/criminal-law/florida/fort-lauderdale), [Meltzer & Bell](https://www.browardcriminalteam.com/), [Ansara Law](https://www.ansaralaw.com/), [Hager & Schwartz](https://www.defendyourbrowardcase.com/areas-we-serve/hallandale-beach/), [Erase The Case](https://erasethecase.com/locations/broward-county-expungement-lawyer/), [Wolfson & Leon Dania Beach](https://fortlauderdale.wolfsonlawfirm.com/dania-beach.html), [Flaxman Law Dania Beach](https://flaxmanlaw.com/dania-beach-personal-injury/), [Baez Law Hollywood](https://www.baezlawfirm.com/hollywood-fl-criminal-defense-lawyer/), [Avvo Hallandale](https://www.avvo.com/criminal-defense-lawyer/fl/hallandale_beach.html), [Super Lawyers](https://attorneys.superlawyers.com/criminal-defense/florida/fort-lauderdale/), [Broward SAO seal/expunge](https://browardsao.com/seal-or-expunge-a-criminal-record/)
