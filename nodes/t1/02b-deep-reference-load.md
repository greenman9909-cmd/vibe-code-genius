# Node 02b — Deep Reference Load

Tier: 1  Prereqs: [01]  Parallel with: [03, 04, 06, 07, 08, 09, 10, 11]  Input: intent.json  Output: reference.json  Model: sonnet  Budget: 3000 tokens

## Working Contract

Read `contracts/working-contract.md` and the declared input only. Emit the exact declared artifact, validate it against its schema, and update the manifest. Keep evidence separate from inference.

## Instructions

### Runtime wiring

`vibe-tree acquire` invokes SiteMap-X when installed and records its real endpoint/report paths in `reference-source.json`. In cached mode, use `endpoints_path` and do not invoke SiteMap-X a second time.

0. Check for `./reference-source.json` in the output directory. If it exists AND `mode == "cached"` and `endpoints_path` exists, use `endpoints_path` as the endpoint input and skip SiteMap-X. Otherwise, proceed with the standard SiteMap-X acquisition chain in steps 1+.

1. Confirm every prerequisite artifact exists and has the expected version.
2. Inspect the input and extract only facts relevant to deep reference load.
3. Produce `reference.json` with deterministic ordering, explicit nulls, and no invented evidence.
4. Resolve every import, route, API call, token, environment variable, locale key, and component reference before writing.
5. Record decisions and unresolved blockers in the artifact's evidence or report field.
6. Mark the corresponding manifest item complete only after validation passes.

## Output Contract

The output is `reference.json`. It is versioned, machine-readable when the artifact is JSON, and contains a `version`, `generated_at`, `evidence`, and `status` field where the artifact shape permits.

Before marking complete: python scripts/validate-artifact.py --node 02b --artifact reference.json --schema schema/reference.schema.json. If validation fails, halt. Do not substitute a different artifact. Do not continue.










## If this fails



Log the node id, input hash, invocation, error, and minimal reproduction to `session.log`. Use datetime.utcnow().isoformat(timespec="microseconds") + "Z" (microseconds MUST vary between events). Apply the declared fallback in `contracts/repair-contract.md`; do not silently fabricate a result.


Do not invent pages, proof, metrics, integrations, credentials, routes, or reference evidence. Do not bypass schemas, disable a failing check, write unresolved references, or emit prose in place of the artifact.

## Example output

```json
{
  "node": "02b",
  "status": "complete",
  "artifact": "reference.json",
  "version": "1.0.0",
  "evidence": ["declared input validated"],
  "unresolved": []
}
```
