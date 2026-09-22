# Field Report — Resend-inspired God Tree Explainer

Date: 2026-09-22  
Agent: ChatGPT (GPT-5.6 Sol)  
Repository: `greenman9909-cmd/vibe-code-genius`  
Working branch: `site/resend-inspired-god-tree`  
Pull request: #1  
Target reference: `https://resend.com`

## 1. User intent

The request was not merely to explain Vibe Code Genius. The user wanted the **God Tree itself used as the build process** for a Resend-inspired website whose content explains the God Tree.

The first interpretation drifted toward "make a site about the tree." The user corrected this to "use the god tier skill tree to make the website" and explicitly asked to use the supporting tools in repository order.

### Reusable lesson

Node 01 must capture **process intent as well as deliverable intent** when the user specifies a required methodology.

For this request, the methodology was part of the product requirement:

`God Tree execution order + tool usage + Resend-style reference + God Tree explanatory content`.

Treating the methodology as optional would have produced the wrong build even if the final page looked acceptable.

## 2. Repository conventions discovered

Before adding new structure, repository inspection found:

- `first-build/` — a prior artifact run including `session.log` and a handoff;
- `trust-build-2/` — a second artifact run with its own session log and handoff;
- `walkthroughs/` — four placeholder files explicitly intended to record intent, scope, reference loading, artifacts, verification, and repair decisions;
- Node 25 and `repair-contract.md` — the existing failure-to-regression mechanism;
- `MAINTAINING.md` — requires golden coverage for node behavior changes and periodic failure-stat review.

### Reusable lesson

When adding "memory" or "experience" to the God Tree, prefer the existing `walkthroughs/` convention. Do not create a parallel `experience/` system unless the existing convention becomes insufficient.

## 3. Reference acquisition

Node 02 was read before using reference data. Its policy is strict:

1. SPA-Ripper for public-page/route acquisition;
2. SiteMap-X for sitemap/route reconciliation;
3. HAR/browser network when API behavior is needed;
4. manual URL/screenshot evidence only when automated acquisition is unavailable.

It also explicitly forbids treating authored fixtures as scraped evidence.

### Existing evidence found

A repository named `greenman9909-cmd/resend-test-sitemap-x` already contained a SiteMap-X run for Resend. Its README reported:

- 25 total URLs discovered;
- 5 navigable pages;
- 13 static assets;
- 266 mapped endpoints;
- 7 technology fingerprints;
- 6 detected forms.

The recorded stack signals included Next.js and Vercel, plus Stripe and other third-party services.

### Fixture handling

`references/fixtures/resend.json` exists, but Node 02 says fixture entries cannot satisfy reference acquisition. It was therefore treated as a schema/example asset, not as live evidence.

### Reusable lesson

Search for prior **provenance-bearing acquisition artifacts** before doing duplicate work. A previous crawl can be useful cached/reference input when the contract allows it, but its age and acquisition method must stay visible.

Do not promote a curated or authored fixture to "scraped evidence" because it happens to mention the same site.

## 4. Toolchain inspected

The build inspected the actual repositories/instructions for:

### SPA-Ripper

Useful for:

- recursive SPA asset recovery;
- Vite/Webpack dynamic chunks;
- CSS-referenced fonts/assets;
- manifests and service workers;
- SPA route fallback;
- optional API proxying.

Operational lesson: it is best viewed as frontend acquisition, not as proof of backend behavior.

### SiteMap-X

Useful for:

- route reconciliation;
- endpoint discovery;
- technology fingerprinting;
- runtime/headless capture;
- reports and resumable crawl state.

Operational lesson: its endpoint inventory may include noisy literals/escaped variants. Treat discovery source and confidence as data, not every string as an authoritative API contract.

### api-researcher

Useful after endpoint discovery for:

- auth requirements;
- pagination;
- versioning;
- rate-limit signals;
- error format;
- CORS;
- response shape.

Operational lesson: endpoint discovery and endpoint behavior are separate jobs. Do not infer the second from the first.

### SlopMonster

The initial visible copy failed the scorer at **3/5** because of repeated rule-of-three cadence and compound-heavy phrasing. The copy was revised without weakening the checker and then reached **5/5**.

Operational lesson: a deterministic copy gate is more useful when the agent edits the copy rather than editing the gate.

## 5. Design execution

The requested visual target was Resend-like, not a literal clone.

The resulting design used:

- dark-first monochrome surfaces;
- large, sparse developer-oriented typography;
- terminal/code panels as explanatory visuals;
- thin borders and restrained radii;
- dense technical information presented with high whitespace;
- no borrowed Resend logo, claims, or email-product copy.

Node 11d was important because its design contract bans common AI-design shortcuts such as decorative gradient utilities and gradient text. A gradient-like violation in an early local draft was removed.

### Reusable lesson

"Reference-inspired" should mean **design grammar**, not brand copying.

Translate the reference into tokens, density, hierarchy, component behavior, and motion rules. Keep the new product's identity and factual content separate.

## 6. Scope discipline

The site explains all five God Tree tiers and all 61 nodes, but the website itself is a static technical explainer.

It did not need:

- authentication;
- a database;
- transactional email;
- a production API;
- invented forms or user accounts.

The implementation was therefore kept dependency-light: one static HTML document plus deployment metadata and build evidence.

### Reusable lesson

Do not instantiate Tier-4 product features merely because the tree contains them. The tree is a capability graph, not a command to add unnecessary infrastructure.

Completeness means completing the **declared scope**, not maximizing feature count.

## 7. Verification results

The branch contained the exact 61-node inventory and correct tier split:

- Tier 1: 13
- Tier 2: 17
- Tier 3: 9
- Tier 4: 17
- Tier 5: 5

Repository CI on the branch passed:

- `python scripts/validate-tree.py`;
- `python scripts/validate-structure.py`;
- `python tests/golden.py`;
- full unittest discovery.

GitHub Actions workflows `validate` and `golden-tests` completed successfully for the site commit.

### Runtime constraint

A local browser/Playwright-style verification attempt was blocked by the execution environment with an administrator navigation restriction. This was recorded as unresolved rather than converted into a pass.

A plain local HTTP server later returned HTTP 200 for the generated page, proving that the static document could be served, but this is weaker than a full browser interaction/visual test.

### Reusable lesson

Differentiate:

- **static validation**;
- **HTTP serving**;
- **browser runtime verification**;
- **visual/fidelity verification**.

Passing one does not imply the others.

## 8. Deployment attempt

A GitHub Pages workflow was added to obtain a real hosted preview.

The workflow failed at `actions/configure-pages` with a clear infrastructure error: Pages was not enabled/configured for the repository. Checkout itself succeeded.

The failed workflow was then removed so the PR did not carry a permanently red, unusable deployment experiment.

### Reusable lesson

A deployment failure caused by repository/platform configuration is not evidence that the built site is broken.

Record the exact failing layer:

`source -> build -> artifact -> deployment configuration -> runtime`.

Do not collapse all failures into "deploy failed."

## 9. Connector/tooling lesson

The GitHub code-search action returned no matches for several terms that were known to exist in the repository. Listing repository directories through the GitHub contents API revealed the relevant structure reliably.

### Reusable lesson

When semantic/code search unexpectedly returns nothing:

1. do not conclude the concept/file is absent;
2. list likely directories;
3. fetch known files directly;
4. use search as discovery assistance, not as proof of absence.

This is especially important when looking for repository conventions.

## 10. What worked well in the God Tree

### Evidence separation

The strongest behavior was refusing to treat fixtures or assumptions as observed reference data.

### Explicit prerequisites

The node graph made it easy to explain why API behavior research belongs after endpoint discovery and why design-contract work belongs before component composition.

### Failure honesty

The system's repair/verification philosophy encouraged recording the browser and Pages failures precisely rather than claiming an end-to-end pass.

### Copy/design gates

SlopMonster and the design-slop rules caught issues that a generic "looks good" review would likely have allowed through.

### Existing artifact history

`first-build/`, `trust-build-2/`, session logs, and handoffs provide useful operational context even though they are not substitutes for new evidence.

## 11. What should improve

### Walkthroughs were placeholders

The repository already anticipated build walkthroughs but had no substantial real report in that directory. Future meaningful runs should append field reports here.

### Experience discovery was not wired into SKILL.md

An agent could load the skill and never discover prior operational lessons. The skill should tell agents to scan relevant walkthroughs before Node 01 while explicitly warning that walkthroughs are not evidence.

### Experience should not become prompt bloat

Do not load every walkthrough into every run. Read the index, then open only reports relevant to the target, toolchain, or observed failure.

### Failure statistics can become structured later

If enough walkthroughs accumulate, extract repeated failure categories into machine-readable statistics. Do not create that machinery before there is enough real data.

## 12. Anti-lessons

Future agents must **not** infer any of the following from this run:

- that Resend still has the exact same routes/endpoints;
- that SiteMap-X will always outperform a fresh SPA-Ripper acquisition;
- that static HTML is the right stack for every explainer;
- that GitHub Pages is unavailable in general;
- that browser verification may be skipped because CI is green;
- that a previous 5/5 SlopMonster score applies after copy changes;
- that this walkthrough can satisfy any node's evidence requirement.

## 13. Compact checklist for a similar future run

1. Parse the user's required process, not only the desired output.
2. Read the relevant node contracts before using cached evidence.
3. Look for prior provenance-bearing artifacts.
4. Reacquire anything that must be current.
5. Separate endpoint discovery from API behavior research.
6. Convert reference design into tokens/rules rather than cloned branding.
7. Run copy/design gates before declaring visual completion.
8. Keep scope minimal and explicit.
9. Record static, runtime, visual, and deployment results separately.
10. Add a walkthrough when the run produces a lesson another agent can reuse.

## 14. Outcome

The run produced:

- a Resend-inspired God Tree explainer;
- an interactive presentation of all 61 nodes;
- documented toolchain behavior;
- passing repository validation/golden CI;
- a copy-lint correction from 3/5 to 5/5;
- one browser-runtime environment blocker;
- one GitHub Pages configuration failure;
- this operational field report.

The most important lesson is that the God Tree is strongest when it is used as a **discipline for evidence and failure handling**, not merely as a long checklist of generation steps.
