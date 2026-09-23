# God Tree evidence cycle — 2026-09-23

Status: research-only promotion candidate. Fresh evidence reacquired this run; no claim below implies SPA-Ripper, SiteMap-X, api-researcher, browser automation, or a separate autonomous agent was executed when it was not.

## Workstream 1 — target scout
Targets selected to rotate categories rather than overfit to one product:
- Vercel dashboard/navigation (developer SaaS/dashboard): current 2026 redesign prioritizes common workflows, consistent team/project navigation, resizable sidebar, project-as-filter, and a mobile one-handed bottom bar.
- Supabase docs/product surface (developer SaaS/backend): current security and Postgres guidance gives primary-source evidence for RLS, grants, indexing, keys, Auth, Storage, Realtime, Edge Functions, Cron and Queues.
- AniList API ecosystem (anime metadata): metadata-oriented GraphQL is treated separately from playback.
- hls.js / browser media platform (media/player): use only legal/public/user-owned streams as playback evidence.

## Workstream 2 — video/transcript researcher
Fresh public video search was attempted, but no video/transcript result was promoted because this run did not obtain a transcript/caption plus an independent primary-source cross-check. This is intentional evidence hygiene: creator claims do not become rules without primary support.

## Workstream 3 — website acquisition
No SPA-Ripper, SiteMap-X, or api-researcher invocation was available/executed in this runtime, so no acquisition claim is made. Public web/docs and GitHub repository evidence remain separate from extracted-site evidence.

## Workstream 4 — frontend/design analyst
Evidence-backed observations:
- Vercel's 2026 dashboard redesign moves frequent workflows into a consistent navigation model and explicitly adapts mobile navigation for one-handed use. Treat navigation hierarchy as task-priority architecture, not decoration.
- A responsive remix should preserve information architecture while changing the navigation mechanism at narrow widths; do not merely shrink desktop chrome.
- This is a category-specific dashboard lesson, not a universal rule for editorial, ecommerce, or media products.

Candidate remix rule: when generating dashboard/SaaS UIs, derive navigation order from workflow frequency and supply an explicit narrow-screen navigation mode. Do not promote this globally until repeated across additional targets.

## Workstream 5 — backend/infra analyst
Primary-source Supabase findings:
- Every exposed table needs RLS plus intentionally scoped grants; policies and grants are complementary.
- Prefer operation-specific SELECT/INSERT/UPDATE/DELETE policies over a broad FOR ALL policy because intent and testing are clearer.
- RLS tests should assert allow and deny behavior for anonymous/authenticated cases before acceptance.
- Index columns used by RLS predicates (commonly user_id). Wrapping stable helper calls such as `(select auth.uid())` can avoid per-row function evaluation.
- Frontends may expose a publishable key only when authorization is enforced with RLS/least privilege. Secret/service-role keys bypass RLS and must stay server-side.
- Security-definer functions need a pinned empty search_path and schema-qualified names; keep privileged helpers out of exposed schemas.
- Postgres index advice is evidence, not an automatic mandate: the planner can rationally prefer sequential scans on small tables.

Candidate fortification: backend generation involving Supabase should generate RLS/grants and an authorization test matrix together, and validators should reject browser-shipped secret/service-role keys.

## Workstream 6 — synthesis/comparison
Repeated/strong evidence:
- Security belongs in the generated backend contract and tests, not as a post-generation checklist.
- Responsive behavior is structural: desktop navigation cannot simply be scaled down.

One-off/category evidence:
- Vercel's project-as-filter pattern is useful for multi-scope developer dashboards but should not become a global UI rule.
- Index Advisor recommendations require planner/context verification; avoid blindly adding indexes.

Contradictions resolved:
- "Add indexes" is not "index everything". Promote a rule to index authorization/filter predicates when query shape and scale justify it, then validate with plans/advisor where available.

## Workstream 7 — tree fortifier proposal
This run persists evidence first instead of immediately changing behavior contracts. Proposed next promotion, only after another independent source/run confirms it:
1. Supabase generator contract: RLS + least-privilege grants + per-operation policies + RLS tests are one atomic completeness unit.
2. Secret validator: reject service-role/secret keys in client bundles/env prefixes intended for browsers.
3. Dashboard remix guidance: task-frequency navigation hierarchy plus explicit mobile navigation transformation.

No global rule was changed in this run because the repository should prefer minimal evidence-backed improvements over rule bloat.

## Workstream 8 — validator/red team
Review outcome:
- ACCEPT research artifact: provenance is explicit and claims are scoped.
- REJECT immediate universalization of Vercel navigation patterns: one current product is insufficient evidence.
- REJECT any claim that website extraction tools ran: they did not.
- REJECT any video-derived promotion: transcript evidence was not acquired.
- ACCEPT Supabase security findings as strong primary-source guidance, but behavior-changing generator changes remain gated on repository-level tests and a later patch.

## Workstream 9 — anime/API researcher
Safe architecture lessons retained:
- Keep metadata identity separate from playback identity. An AniList-style media ID is not a playable episode ID.
- Normalize provider-specific season/episode identifiers behind an adapter before player code sees them.
- A playback candidate must pass HTTPS, CORS/browser fetch/media compatibility, response-schema validation, hostname allow-list/ownership review, and licensing/terms signals before recommendation.
- HLS/MP4/player adapters, subtitle/audio selection, progress persistence, and explicit unavailable/fallback states are reusable architecture. Unauthorized stream resolvers, scraped cookies/credentials, anti-bot bypasses, DRM circumvention, and private endpoints are excluded.
- WebVTT/subtitle handling and HLS playback should be tested with legal public test media or user-owned media.

## Coordinator decision
Promoted this run: research/provenance artifact only.
Blocked from downstream contract promotion: dashboard-specific navigation rule, video lessons without transcripts, any unverified playback source, and any claim of extraction-tool output.

## Fresh sources
- Supabase RLS: https://supabase.com/docs/guides/database/postgres/row-level-security
- Supabase secure data: https://supabase.com/docs/guides/database/secure-data
- Supabase API keys: https://supabase.com/docs/guides/getting-started/api-keys
- Supabase indexes: https://supabase.com/docs/guides/database/postgres/indexes
- Supabase security configuration: https://supabase.com/docs/guides/security/product-security
- Vercel dashboard redesign (2026-02-26): https://vercel.com/changelog/dashboard-navigation-redesign-rollout

## Validation checklist
- Evidence provenance present: PASS
- Unsupported tool/agent claims: PASS (none)
- One-off vs repeated evidence separated: PASS
- Security-sensitive claims backed by primary docs: PASS
- Unauthorized anime playback sources promoted: PASS (none)
- Behavior-changing contract/schema changes: N/A (none in this patch)
- Regression tests required: N/A (research-only patch)
