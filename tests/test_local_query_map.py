"""Offline structural safeguards for the 2026-10-07 local query-to-page map.

Checks the unmerged local-query review draft in this repository. Static
structure only: no network, no browser, no form submission, no ranking
measurement, no tracking. Exit non-zero on any failure.
"""

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
FAILS: list[str] = []


def check(name: str, condition: bool, detail: str = "") -> None:
    if not condition:
        FAILS.append(f"{name}{(' — ' + detail) if detail else ''}")


def page(rel: str) -> str:
    return (ROOT / rel).read_text(encoding="utf-8")


CITY = {
    "pearl-thrift-store.html": {
        "city": "Pearl",
        "address": "434 N Bierdeman Rd, Pearl, MS 39208",
        "heading_id": "visit-pearl",
        "cross_link": ("byram-thrift-store.html", "Thrift store in Byram, MS"),
    },
    "byram-thrift-store.html": {
        "city": "Byram",
        "address": "6787 S Siwell Rd STE D, Byram, MS 39272",
        "heading_id": "visit-byram",
        "cross_link": ("pearl-thrift-store.html", "Thrift store in Pearl, MS"),
    },
}

for rel, spec in CITY.items():
    html = page(rel)
    city = spec["city"]

    # Exactly one H1, still the audited city phrase; title unchanged.
    check(f"{rel}: single H1", len(re.findall(r"<h1>", html, re.I)) == 1)
    check(f"{rel}: H1 text", f"Thrift Store in {city}, MS" in html)
    check(f"{rel}: title", f"<title>Thrift Store in {city}, MS | SuperThrift</title>" in html)

    # Canonical tag and posted address/hours preserved verbatim.
    check(f"{rel}: canonical", f'href="https://superthriftdeals.org/{rel}"' in html)
    check(f"{rel}: address", spec["address"] in html)
    check(
        f"{rel}: posted hours",
        "Monday&ndash;Saturday: 8:00 AM&ndash;6:00 PM<br>Sunday: Closed" in html,
    )

    # Answer-first opening names the store type and the address.
    first_p = re.search(r"<h1>.*?</h1>\s*<p>(.*?)</p>", html, re.S)
    check(f"{rel}: answer paragraph present", bool(first_p))
    if first_p:
        text = re.sub(r"\s+", " ", first_p.group(1))
        check(f"{rel}: answer mentions thrift store", "thrift store at" in text)
        check(f"{rel}: answer carries address", spec["address"] in text)

    # Mission sentence retained as its own following paragraph.
    second_p = re.search(r"</h1>\s*<p>.*?</p>\s*<p>(.*?)</p>", html, re.S)
    check(f"{rel}: mission paragraph present", bool(second_p))
    if second_p:
        check(
            f"{rel}: mission text",
            "community programs and outreach through Mercy House" in second_p.group(1),
        )

    # Revised visit H2 keeps its existing ID.
    check(
        f"{rel}: visit H2",
        f'Where is SuperThrift in {city}, MS?</h2>' in html
        and f'id="{spec["heading_id"]}"' in html,
    )

    # Shorter description in the approved range.
    desc = re.search(r'<meta name="description" content="([^"]+)"', html)
    check(f"{rel}: description present", bool(desc))
    if desc:
        d = desc.group(1)
        check(f"{rel}: description length", 120 <= len(d) <= 160, f"len={len(d)}")
        check(f"{rel}: description city", f"in {city}, MS for affordable secondhand" in d)

    # Descriptive footer cross-link; exact target retained.
    target, label = spec["cross_link"]
    check(f"{rel}: footer cross-link", f'<a href="{target}">{label}</a>' in html)

    # Existing donation-section destinations preserved.
    check(f"{rel}: accepted-items link", 'href="index.html#what-we-accept"' in html)
    check(f"{rel}: pickup link", 'href="index.html#schedule-pickup"' in html)
    check(f"{rel}: directions link", "maps.google.com/?q=" in html)

# Homepage: only the two location-card labels changed.
home = page("index.html")
check("home: Pearl card label",
      'href="pearl-thrift-store.html" class="link-arrow">Thrift store in Pearl, MS'
      " — hours &amp; directions</a>" in home)
check("home: Byram card label",
      'href="byram-thrift-store.html" class="link-arrow">Thrift store in Byram, MS'
      " — hours &amp; directions</a>" in home)
check("home: H1 unchanged",
      "Donate Usable Goods or Shop Affordable Finds in Pearl and Byram, MS" in home)
check("home: sections intact", all(
    f'id="{anchor}"' in home for anchor in ("locations", "what-we-accept", "schedule-pickup")))

# Untouched files: privacy policy, sitemap, workflow, form transport.
privacy = page("privacy-policy.html")
check("privacy: H1 unchanged", "MERCY HOUSE ATC PRIVACY POLICY" in privacy)
sitemap = page("sitemap.xml")
check("sitemap: four existing entries", sitemap.count("<loc>") == 4)
for loc in (
    "https://superthriftdeals.org/",
    "https://superthriftdeals.org/pearl-thrift-store.html",
    "https://superthriftdeals.org/byram-thrift-store.html",
    "https://superthriftdeals.org/privacy-policy.html",
):
    check(f"sitemap: entry {loc}", f"<loc>{loc}</loc>" in sitemap)
check("form: transport preserved",
      'action="https://formspree.io/f/xzdekbzd"' in home)
check("workflow: deploy untouched",
      "cloudflare/pages-action@v1" in page(".github/workflows/deploy.yml"))

if FAILS:
    print(f"FAIL ({len(FAILS)}):")
    for f in FAILS:
        print(f"  - {f}")
    sys.exit(1)
print("PASS: local query map structural checks — all checks passed.")
