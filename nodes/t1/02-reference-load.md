# Node 02 — Reference Load

Tier: 1  Prereqs: [01]  Parallel with: [03, 04, 06, 07, 08, 09, 10, 11]  Input: intent.json  Output: reference.json  Model: sonnet  Budget: 3000 tokens

## Working Contract

Read `contracts/working-contract.md` and the declared input only. Emit the exact declared artifact, validate it against its schema, and update the manifest. Keep evidence separate from inference.

## Acquisition policy

The bundled reference vault is not a substitute for evidence. Load a local entry from `references/index.json` only when all of the following are true:

```json
{
  "type": "scraped",
  "acquirer": "spa-ripper"
}
```

Entries with `type: fixture`, `acquirer: fixture`, `acquirer: curated-reference-index`, missing provenance, or any other combination are schema examples only. They must never be presented as a scraped reference and must not satisfy the reference-load step.

If no qualifying SPA-Ripper entry exists, fall through to the live acquisition chain in this order:

1. SPA-Ripper for public pages and route discovery.
2. SiteMap-X for sitemap and route reconciliation.
3. HAR or browser-network capture when API behavior is required.
4. Manual URL and screenshot evidence when automated acquisition is unavailable.

Record the selected acquirer, invocation, timestamp, source URL, route count, section count, design-token count, and any fallback or unresolved blocker in `reference.json`. A failed scrape is a failed acquisition, not permission to use an authored fixture as evidence.

## Instructions

1. Confirm every prerequisite artifact exists and has the expected version.
2. Inspect the input and extract only facts relevant to reference load.
3. Evaluate local index entries against the explicit `{type: scraped, acquirer: spa-ripper}` gate.
4. Produce `reference.json` with deterministic ordering, explicit nulls, and no invented evidence.
5. Resolve every import, route, API call, token, environment variable, locale key, and component reference before writing.
6. Record decisions and unresolved blockers in the artifact's evidence or report field.
7. Mark the corresponding manifest item complete only after validation passes.

## Output Contract

The output is `reference.json`. It is versioned, machine-readable when the artifact is JSON, and contains a `version`, `generated_at`, `evidence`, `status`, `acquirer`, `acquired_at`, and `source_url` field where the artifact shape permits.

Before marking complete: python scripts/validate-artifact.py --node 02 --artifact reference.json --schema schema/reference.schema.json. If validation fails, halt. Do not substitute a different artifact. Do not continue.










## If this fails



Log the node id, input hash, invocation, error, and minimal reproduction to `session.log`. Use datetime.utcnow().isoformat(timespec="microseconds") + "Z" (microseconds MUST vary between events). Apply the declared fallback in `contracts/repair-contract.md`; do not silently fabricate a result.


Do not load authored fixtures as scraped evidence. Do not invent pages, proof, metrics, integrations, credentials, routes, or reference evidence. Do not bypass schemas, disable a failing check, write unresolved references, or emit prose in place of the artifact.

## Example output

```json
{
  "node": "02",
  "status": "complete",
  "artifact": "reference.json",
  "version": "1.0.0",
  "source_url": "https://example.com",
  "acquirer": "spa-ripper",
  "acquired_at": "2026-09-22T00:00:00Z",
  "evidence": ["SPA-Ripper command and output hash recorded"],
  "unresolved": []
}
```
