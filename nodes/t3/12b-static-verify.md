# Node 12b — Static Verify

Tier: 3  Prereqs: [12, 11d]  Parallel with: [13, 24b]  Input: source tree  Output: static-report.json  Model: sonnet  Budget: 2500 tokens

## Working Contract

Read `contracts/working-contract.md` and the declared input only. Emit the exact declared artifact, validate it against its schema, and update the manifest. Keep evidence separate from inference.

## Instructions

1. Confirm every prerequisite artifact exists and has the expected version.
2. Inspect the input and extract only facts relevant to static verify.
3. Produce `static-report.json` with deterministic ordering, explicit nulls, and no invented evidence.
4. Resolve every import, route, API call, token, environment variable, locale key, and component reference before writing.
5. Record decisions and unresolved blockers in the artifact's evidence or report field.
6. Mark the corresponding manifest item complete only after validation passes.

## Output Contract

The output is `static-report.json`. It is versioned, machine-readable when the artifact is JSON, and contains a `version`, `generated_at`, `evidence`, and `status` field where the artifact shape permits.

Before marking complete: python scripts/validate-artifact.py static-report.json schema/node.schema.json. If validation fails, halt. Do not mark complete.







## If this fails

Log the node id, input hash, invocation, error, and minimal reproduction to `session.log`. Append with datetime.utcnow().isoformat() + 'Z' — real timestamps only. Apply the declared fallback in `contracts/repair-contract.md`; do not silently fabricate a result.


## Do not

Do not invent pages, proof, metrics, integrations, credentials, routes, or reference evidence. Do not bypass schemas, disable a failing check, write unresolved references, or emit prose in place of the artifact.

## Example output

```json
{
  "node": "12b",
  "status": "complete",
  "artifact": "static-report.json",
  "version": "1.0.0",
  "evidence": ["declared input validated"],
  "unresolved": []
}
```
