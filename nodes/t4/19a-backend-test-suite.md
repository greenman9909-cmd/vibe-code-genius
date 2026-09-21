# Node 19a — Backend Test Suite

Tier: 4  Prereqs: [07e, 07f, 07g, 19]  Parallel with: [24]  Input: backend + contracts  Output: backend-test-report.json  Model: sonnet  Budget: 3000 tokens

## Working Contract

Read `contracts/working-contract.md` and the declared input only. Emit the exact declared artifact, validate it against its schema, and update the manifest. Keep evidence separate from inference.

## Instructions

1. Confirm every prerequisite artifact exists and has the expected version.
2. Inspect the input and extract only facts relevant to backend test suite.
3. Produce `backend-test-report.json` with deterministic ordering, explicit nulls, and no invented evidence.
4. Resolve every import, route, API call, token, environment variable, locale key, and component reference before writing.
5. Record decisions and unresolved blockers in the artifact's evidence or report field.
6. Mark the corresponding manifest item complete only after validation passes.

## Output Contract

The output is `backend-test-report.json`. It is versioned, machine-readable when the artifact is JSON, and contains a `version`, `generated_at`, `evidence`, and `status` field where the artifact shape permits.

## If this fails

Log the node id, input hash, invocation, error, and minimal reproduction to `session.log`. Apply the declared fallback in `contracts/repair-contract.md`; do not silently fabricate a result.

## Do not

Do not invent pages, proof, metrics, integrations, credentials, routes, or reference evidence. Do not bypass schemas, disable a failing check, write unresolved references, or emit prose in place of the artifact.

## Example output

```json
{
  "node": "19a",
  "status": "complete",
  "artifact": "backend-test-report.json",
  "version": "1.0.0",
  "evidence": ["declared input validated"],
  "unresolved": []
}
```
