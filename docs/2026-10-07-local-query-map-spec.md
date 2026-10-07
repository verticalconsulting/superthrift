# Local query-to-page map — review specification

**Status:** UNPUBLISHED — review draft, not approved for production.
**Prepared:** 2026-10-07 UTC · **Plan item:** `f2de1957-fddd-4f12-a1c4-ba854d623c30`.

Full evidence brief and machine-readable map: Magister Brand Files
`resources/2026-10-07-local-query-on-page-brief.md` and
`resources/2026-10-07-local-query-page-map.json`. This document is the condensed
implementation companion.

## Keyword-to-page map (audited 2026-10-01 baseline, preserved)

| Phrase | Volume | Audited rank | Verified page |
|---|---:|---|---|
| thrift store pearl ms | 390 | Not ranking | `pearl-thrift-store.html` |
| thrift stores pearl ms | 390 | Position 52 | `pearl-thrift-store.html` |
| thrift store byram ms | 70 | Not ranking | `byram-thrift-store.html` |
| thrift stores byram ms | 70 | Position 6 | `byram-thrift-store.html` |

Ranks/volumes come from the October 1 audit and were not remeasured; they are
baselines, not targets or current positions. A mapping is an intent match, not
identification of the URL that ranked. No new URL is created; the sitemap keeps
its four existing entries. Singular/plural pairs stay on one city page each;
do not sum their volumes or force exact-string repetition.

## Change summary (exact diffs in this PR)

1. Both city pages: replace the opening paragraph with an address-first direct
   answer (exact posted addresses retained), keep the existing mission sentence
   as a separate paragraph, and shorten the meta descriptions.
2. Both city pages: revise the visit H2 to `Where is SuperThrift in <City>, MS?`
   while keeping its existing ID, address, hours and help cards.
3. Both city footers: descriptive cross-city link label; same file target.
4. Homepage location cards only: descriptive city link labels; same targets.

Titles, H1s, canonical tags, directions/map links, phone links, donation
guidance, pickup-request qualification, form, scripts, sitemap, robots and the
privacy policy are intentionally unchanged. The GEO/FAQ, CTA-clarity (PR #11)
and tracking (PR #10) workstreams remain separate; resolve any merge conflict
without discarding either reviewed intent.

## Verification

`python3 tests/test_local_query_map.py` — structural offline checks covering
single H1 per page, retained titles/canonicals/addresses/hours, revised copy
present, existing link targets intact, and untouched form/scripts/privacy/
sitemap/workflow files. `git diff --check` — whitespace. These are static
checks, not a rendered-browser, indexing or ranking measurement. No form
submission, no live-site change, no deploy attempt.
