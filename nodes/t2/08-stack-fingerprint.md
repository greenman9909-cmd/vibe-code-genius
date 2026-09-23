# Node 08 — Stack Fingerprint

Tier: 2  Prereqs: [02, 01d]  Parallel with: [11, 05]  Input: reference.json.stack + system.json.stack  Output: stack-decision.md  Model: haiku  Budget: 1200 tokens

## Working Contract

Read `contracts/working-contract.md` and the declared input only. Emit the exact declared artifact, validate it against its schema, and update the manifest. Keep evidence separate from inference.

## Instructions

1. Confirm every prerequisite artifact exists and has the expected version.
2. Inspect the input and extract only facts relevant to stack fingerprint.
3. Produce `stack-decision.md` with deterministic ordering, explicit nulls, and no invented evidence.
4. Resolve every import, route, API call, token, environment variable, locale key, and component reference before writing.
5. Record decisions and unresolved blockers in the artifact's evidence or report field.
6. Mark the corresponding manifest item complete only after validation passes.

## Output Contract

The output is `stack-decision.md`. It is versioned, machine-readable when the artifact is JSON, and contains a `version`, `generated_at`, `evidence`, and `status` field where the artifact shape permits.

Before marking complete: python scripts/validate-artifact.py --node 08 --artifact stack-decision.md --schema schema/stack-decision.schema.json. If validation fails, halt. Do not substitute a different artifact. Do not continue.










## If this fails



Log the node id, input hash, invocation, error, and minimal reproduction to `session.log`. Use datetime.utcnow().isoformat(timespec="microseconds") + "Z" (microseconds MUST vary between events). Apply the declared fallback in `contracts/repair-contract.md`; do not silently fabricate a result.


Do not invent pages, proof, metrics, integrations, credentials, routes, or reference evidence. Do not bypass schemas, disable a failing check, write unresolved references, or emit prose in place of the artifact.

## Example output

```json
{
  "node": "08",
  "status": "complete",
  "artifact": "stack-decision.md",
  "version": "1.0.0",
  "evidence": ["declared input validated"],
  "unresolved": []
}
```
