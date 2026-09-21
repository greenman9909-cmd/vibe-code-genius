# Node 06 — Prompt Composer

Tier: 1  Prereqs: [02, 03, 04, 05]  Parallel with: [06a, 07, 12, 13, 14]  Input: reference.json + style-rules.md + file-tree.md  Output: prompt.md  Model: sonnet  Budget: 5000 tokens

## Working Contract

Read `contracts/working-contract.md` and the declared input only. Emit the exact declared artifact, validate it against its schema, and update the manifest. Keep evidence separate from inference.

## Instructions

CONTENT ORIGIN RULE:
- REFERENCE STACK — tech choices from the reference (Next.js, Tailwind, etc.)
- ROUTE MAP — URL paths from the reference OR system.json (whichever is broader)
- HOMEPAGE SECTIONS — layout order and section types from the reference
- KEY COMPONENTS — component patterns and props from the reference
- DESIGN TOKENS — colors/fonts/spacing from the reference
- MY PRODUCT — copy, headline, subhead, feature descriptions, value
  proposition, CTAs — ALL from MY PRODUCT, NEVER from the reference

The reference provides STRUCTURE and AESTHETIC.
The product provides CONTENT and IDENTITY.

If MY PRODUCT is an AI build orchestrator, the copy says
'AI build orchestrator.' If the reference is railway.app and talks about
cloud infrastructure, that language does NOT appear in the output unless
the product IS cloud infrastructure.

Add a validation step: after composing prompt.md, verify that no section
of the copy contains phrases from the reference's marketing copy. If it
does, rewrite that section using MY PRODUCT's description only.

1. Confirm every prerequisite artifact exists and has the expected version.
2. Inspect the input and extract only facts relevant to prompt composer.
3. Produce `prompt.md + handoff.md` with deterministic ordering, explicit nulls, and no invented evidence.
4. Resolve every import, route, API call, token, environment variable, locale key, and component reference before writing.
5. Record decisions and unresolved blockers in the artifact's evidence or report field.
6. Mark the corresponding manifest item complete only after validation passes.

## Output Contract

The output is `prompt.md`.md + handoff.md`. It is versioned, machine-readable when the artifact is JSON, and contains a `version`, `generated_at`, `evidence`, and `status` field where the artifact shape permits.

Before marking complete: python scripts/validate-artifact.py --node 06 --artifact prompt.md --schema schema/prompt.schema.json. If validation fails, halt. Do not substitute a different artifact. Do not continue.










## If this fails



Log the node id, input hash, invocation, error, and minimal reproduction to `session.log`. Use datetime.utcnow().isoformat(timespec="microseconds") + "Z" (microseconds MUST vary between events). Apply the declared fallback in `contracts/repair-contract.md`; do not silently fabricate a result.


Do not invent pages, proof, metrics, integrations, credentials, routes, or reference evidence. Do not bypass schemas, disable a failing check, write unresolved references, or emit prose in place of the artifact.

## Example output

```json
{
  "node": "06",
  "status": "complete",
  "artifact": "prompt.md + handoff.md",
  "version": "1.0.0",
  "evidence": ["declared input validated"],
  "unresolved": []
}
```
