# Donate and shop actions — review specification

**Status:** Proposed production copy; UNMERGED and not approved for publication.  
**Prepared:** 2026-10-05 UTC.  
**Plan item:** `cf2cd252-efb6-40bc-b455-d4f0eae49e3a`.  
**Audience:** Pearl and Byram residents donating usable household goods or shopping affordable secondhand items.  
**Full evidence/approval specification:** Magister Brand Files, `resources/2026-10-05-donate-shop-action-path-spec.md`. This repository document is its condensed implementation companion. No SEO keyword, paid campaign, tracking change or signup promise is added.

## Baseline, predecessors and conflict

The October 1 audit counts four paths and flags no obvious CTA, but its saved homepage excerpt already contains pickup, location and accepted-items links. October 5 rendered reads confirm them. PR #7 was merged September 25; its two-path hero is already live and retained. This change is a clarity/destination-match revision, not a second installation of that hero or proof of mobile prominence.

Predecessors: `resources/2026-09-22-donation-shopping-cta-landing-path-draft.md` and the September 29 CRO rewrite at `resources/workflow-results/cro-audit-142287b8-0978-4787-87e2-85199d67925d/step-4-copy-rewrites.md`. This adopts only focused request/navigation clarification, not the broader hero or testimonial rewrite. Their historical missing-city-page statements are superseded by current live reads.

## Page and destination evidence

The audit supplies a count, not its exact historical URL list. The current sitemap identifies four paths consistent with that count; all were read through rendered-page scraping and returned HTTP 200 on October 5:

| Source page | Live read UTC | Proposed donor next step | Proposed shopper next step |
|---|---|---|---|
| `/` | 02:55:42 | Request a Donation Pickup → `#schedule-pickup` | Find a Store to Shop → `#locations`; keep hero Find a SuperThrift Location |
| `/pearl-thrift-store.html` | 02:56:05 | Request a Donation Pickup → `index.html#schedule-pickup`; manually choose Pearl Area | Get Pearl Store Directions → exact existing Pearl map href |
| `/byram-thrift-store.html` | 02:56:04 | Request a Donation Pickup → `index.html#schedule-pickup`; manually choose Byram Area | Get Byram Store Directions → exact existing Byram map href |
| `/privacy-policy.html` | 02:56:05 | Header/footer Request a Donation Pickup → `index.html#schedule-pickup` | Header/footer Find a Store to Shop → `index.html#locations` |

City and privacy `.html` paths redirect to extensionless URLs and still return 200; retain existing published paths. The homepage `index.html` alias was reread at 02:56:47 UTC and resolves to `/` with the same pickup form. Do not invent `/donate`, `/shop`, a preselected city form, or a signup URL.

**Verified destination register:**
- `https://superthriftdeals.org/#schedule-pickup`: live rendered HTML contains `id="schedule-pickup"` next to `form#donation-form`. `index.html#schedule-pickup` is the published cross-page alias. Form posts to `https://formspree.io/f/xzdekbzd`; no submission was made.
- `https://superthriftdeals.org/#what-we-accept`: live `section#what-we-accept` lists categories with a call-before-transport qualification. City pages already link to `index.html#what-we-accept`.
- `https://superthriftdeals.org/#locations`: live `section#locations` has both location cards, posted hours, phone and map links. Published cross-page alias is `index.html#locations`.
- Pearl directions: `https://maps.google.com/?q=434+N+Bierdeman+Rd+Pearl+MS+39208`, copied exactly from live homepage/Pearl page; posted address is 434 N Bierdeman Rd, Pearl, MS 39208.
- Byram directions: `https://maps.google.com/?q=6787+S+Siwell+Rd+STE+D+Byram+MS+39272`, copied exactly from live homepage/Byram page; posted address is 6787 S Siwell Rd STE D, Byram, MS 39272.
- `tel:6017683532`: shared published `(601) 768-3532` phone. No call or map journey tested.
- `https://superthriftdeals.org/privacy-policy.html`: live policy documents pickup/contact data use. The new adjacent link uses the existing file path; no consent assertion is added.
- Existing Pearl and Byram detail pages remain linked; both were verified above.

## Exact implementation summary

### Homepage

Keep the live H1, supporting copy, two hero CTAs and accepted-items helper unchanged.

- How It Works step: “Check accepted items, request a pickup, or shop in-store.”
- Replace “Schedule a Pickup” and “Schedule Donation Pickup” links and pickup section heading with “Request a Donation Pickup.” Existing pickup target remains.
- Shopping section: replace two differently labelled links to the same location target with one “Find a Store to Shop.” Add “Shop in-store in Pearl or Byram. Find posted hours and directions below.”
- Form button: “Send Pickup Request.” Preserve all fields, required status, options, transport, hidden routing fields and scripts.
- Beside submit: “Sending this form requests a pickup; it does not confirm an appointment. SuperThrift must confirm the items, address, and timing. Read our Privacy Policy.” Policy link uses `privacy-policy.html`.
- Final actions: “Request a Donation Pickup” → `#schedule-pickup`, replacing “Donate Now” → `#contact`; “Find a Store to Shop” → existing `#locations`.

### Pearl and Byram

Hero: named city store directions plus direct “Request a Donation Pickup” button. Preserve phone access in navigation and add the same nearby qualification:

> Pickup requests require confirmation of the items, address, and timing. Questions about an item or drop-off? Call (601) 768-3532.

Donation sections retain accepted-items links and use “Request a Donation Pickup.” Final donor cards describe their actual form destination:

> Request a Donation Pickup  
> Choose Pearl Area [or Byram Area] in the form. Item eligibility, address coverage, and timing require confirmation.

The form is not prefilled; existing city shopping cards and other-city links stay intact. No new inventory, hours, pickup guarantees, operational policies or service boundaries.

### Privacy policy

Header/footer action labels and targets only. Policy body, dates and privacy/consent statements remain unchanged. No promotional hero is added to the legal page.

## Unresolved details — not invented

1. **Signup path/event:** No verified account, membership or newsletter signup was identified across these four pages. The policy mentions consent-based marketing, not a signup destination. Owner must define signup, consent, fields, destination and confirmed event before any “Sign up” CTA.
2. **Conversions:** Source contains a Google Ads conversion call following a successful Formspree response; this is not verified receipt, deduplication, or proof that audited conversions are signups. Open PR #10 concerns tracking; coordinate any index.html conflict without adopting its behavior silently. Tracking remains outside this PR.
3. **End-to-end form delivery:** Form destination and published fields are verified, not staff receipt or fulfillment. No request was submitted. `/thank-you` is an existing 200 completion page (read 02:57:08 UTC), but a direct visit cannot prove receipt or a working redirect. No CTA points there and it is not changed here.
4. **Drop-off:** Store hours are not confirmed donation drop-off hours. Loading/access and large-item instructions are missing. Use the published phone until operations confirms them; no “Drop off today” guarantee.
5. **Pickup scope:** Pearl Area/Byram Area options are published; exact boundaries, exclusions and acceptance are unresolved. Every request remains subject to confirmation.
6. **Monetary donation/online checkout:** No verified monetary payment or store cart/catalog/checkout in this inspected scope. Do not add financial-donation, “Buy now,” stock or price promises.
7. **Privacy/marketing consent:** Policy promises direction to the policy and agreement, but a visible checkbox or marketing opt-in was not found in the form. Add only policy access and request clarification; reconcile legally/operationally before a consent or signup change.
8. **Mobile/UI:** Link/HTML verification does not prove visibility, wrapping, browser hash scrolling or map/call behavior. Preview before production approval.
9. **Deployment:** Repo root files match live site and Cloudflare deployment workflow runs on main and PR events. No current successful custom-domain deployment was verified in this task. Keep branch unmerged and inspect deploy after separate approval. Do not label a preview/GitHub Pages URL as the live site.

## Review and shipping gate

Review the exact HTML diff and destination register; request revisions or approve this limited draft. Draft approval is not production merge approval. Connected GitHub is sufficient for Magister to request an exact approved merge; no new CMS connection is needed.

Before shipping, preview at phone/desktop widths, check every fragment landing, city map address, phone and privacy link; no live form submission needed for copy review. Resolve overlap with tracking PR #10. Separately approve production merge, then check deployment receipt and reread all four canonical-domain pages. If unsuitable, prepare an approved revert of this copy-only commit. Never claim publication merely because a branch or PR exists.

Separate performance task: audited mobile Lighthouse 88/100 and estimated unused-JavaScript saving of ~300 ms are lab evidence only. No performance, CSS, JavaScript, tracking, assets or deployment workflow change is made here; no signup or real-user lift is claimed.

Follow-up at review: validate mobile/desktop action behavior. Only after separately approved publication and event validation, compare pickup requests and matching eligible sessions in a closed 14-day window; direction taps are intent, not store visits/signups. No recurring workflow or numerical lift target is created.

## Verification

- Live reads verified four current sitemap paths, anchors and literal published map/phone links.
- `python3 tests/test_action_paths.py` checks local files/fragments, unique IDs, labels, map queries, request qualifiers, unchanged form field requirements and policy navigation.
- Baseline diff gate checks scripts, IDs, hero, form transport/controls and privacy legal body unchanged.
- `git diff --check` checks patch whitespace.
- Executed 2026-10-05: `python3 tests/test_action_paths.py` — exit 0, six tests passed. Offline baseline-comparison command — exit 0, scripts, IDs, form routing/controls, live hero and policy legal body unchanged. `git diff --check` — exit 0.
- Dependency installer was attempted but failed with sandbox file-size limit EFBIG/SIGXFSZ. This static site has no working npm test/build script. Offline structural checks passed; browser/deployment validation is outstanding and not represented as passed.
