# SuperThrift mobile performance recommendation

**Status:** Unpublished website recommendation; ready for review, not implementation approval.  
**Prepared:** 2026-10-05 UTC.  
**Audience:** SuperThrift decision-makers reviewing the Pearl/Byram discovery-to-action experience.  
**Plan item:** `381cecf2-12ce-432d-8833-efa0f7592120` · Activation · Website & content.  
**Decision requested:** Approve this recommendation only. Approval does not authorize code, tracking, configuration, deployment, production merge or spend.

## Recommendation

Keep the verified donate/shop action-path work first. Then validate Lighthouse's unused-JavaScript finding before selecting a small, separately approved optimization. Do not remove scripts merely because they are not exercised during an initial page-load test: donation forms, contact options and measurement may depend on them.

**Task outcome:** A documented baseline and validation sequence—not a faster live site or signup lift.

## Evidence preserved from the October 1 audit

Source: audit ID `9f4a84d6-720f-40ce-b58a-01c67820fea6`; `audits/2026-10-01-050641-full-audit.md` and the linked plan's evidence references. These are historical lab findings, not fresh October 5 measurements.

- **Mobile Lighthouse performance: 88/100; SEO: 100/100.**
- **Desktop Lighthouse performance: 98/100; SEO: 100/100.** Desktop is a separate test context, not a before/after result.
- **Reduce unused JavaScript: approximately 300 ms.** This is Lighthouse's estimated opportunity under the audited conditions—not a measured saving, guarantee, or amount to subtract from an unreported load time.
- `channel.google_search.web_vitals` supplies these lab results and opportunity. `website_and_content.checklist.6` marks page speed **fail**, citing **88/100 (lab; no real-user field data for this site yet)**. This checklist label does not establish a failed real-user Core Web Vitals assessment.

**Real-user field data is unavailable in the supplied audit.** No field LCP, INP or CLS result, performance gain, conversion lift or signup lift is established. No new Lighthouse or CrUX run was performed for this recommendation; current field availability remains unverified. Missing field data is neither a pass nor a fail.

## Technical assumptions to validate

1. **Recover resource-level evidence.** The summary does not identify the responsible script, tested/final URL, test settings, Lighthouse version or affected metric. Recover the original report, or rerun a comparable mobile test, before attributing the approximately 300 ms estimate to a dependency.
2. **Distinguish candidates from proven waste.** Read-only inspection of `verticalconsulting/superthrift`, `main` commit `d9859a388c7961d18b5a83b37a2b6532c323d4d6`, found a Google tag, inline pickup-form submission/conversion logic and a deferred Formspree Quick Contact widget in `index.html`. None is proven responsible or safely removable. The widget already uses `defer`; adding that attribute is not a supported remedy. Source presence does not establish current deployment parity or runtime cost.
3. **Test the whole journey, not only initial load.** In a controlled preview, inspect runtime coverage while using navigation, donate/shop links and contact controls. Preserve form behavior and measurement. Do not submit a live request or transmit personal data without separate permission.
4. **Make the remedy conditional.** Only if diagnostics identify nonessential code, propose removing that exact dependency or loading it when needed. Supply the exact diff, affected paths, regression tests and rollback in a separate PR. No specific script removal or framework rewrite is recommended now.

## Action-path priority and review decision

The donate/shop draft was prepared first in [PR #11](https://github.com/verticalconsulting/superthrift/pull/11). October 5 GitHub readback confirms it is open and unmerged; the plan records its drafting task as completed, not deployed. This recommendation does not replace or change that work.

The audit's “no obvious CTA links” claim conflicts with links in its own saved homepage excerpt and the prior verified action-path specification. Review wording, destinations and mobile tap behavior rather than asserting that no links exist. Mobile visual/tap validation remains outstanding.

**Approve now:** Accept this evidence-qualified recommendation as the completed drafting deliverable. Nothing needs to go live; keep its documentation-only PR unmerged during review. This is not authorization to implement an optimization.

**Next step, only on a separate request:** A bounded read-only diagnostic review using the original report or repeat mobile Lighthouse runs and a current CrUX availability check. Use matching settings, multiple runs and reported variability; keep new results separate from the October 1 baseline. Built-in PageSpeed/CrUX need no new connection. No paid work or recurring monitoring is scheduled.

**To ship a future remedy:** Review its exact code-change PR and regression evidence, then give separate production approval. Connected GitHub supports the PR and an approved merge; no CMS connection is needed. Verify a working deployment path first: the prior CTA review recorded a failed deployment action, and recovery is not verified here. A merge alone is not proof of publication.

Before deployment, check mobile navigation, donation/shop anchors, pickup-form validation and success/error handling, Quick Contact, phone/directions/privacy links and measurement in a preview. After a separately approved deployment, report only observed like-for-like lab deltas. Claim real-user outcomes only when field data exists over a stated comparable window. Signups require a defined, validated event; audited ad conversions are not signups by default.

## Verification and deliverables

- Mobile **88/100** and **approximately 300 ms** checked against supplied audit/plan evidence; desktop **98/100** and SEO **100/100** retained as context.
- Field-data absence, uncertain resource attribution and separate implementation approval stated explicitly.
- No technical or public-site change, merge, campaign change or spend made. No performance or signup gain invented.
- Workspace: `resources/2026-10-05-mobile-performance-recommendation.md`.
- Repository review copy: `docs/2026-10-05-mobile-performance-recommendation.md` on a separate unmerged recommendation PR. This is not a live site update or rendered preview. Repository/PR visibility follows the existing public repository; “unpublished” means not deployed to the website.
