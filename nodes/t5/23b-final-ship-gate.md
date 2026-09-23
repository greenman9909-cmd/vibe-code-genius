# Node 23b — Final Ship Gate

Tier: 5  Prereqs: [18e, 20a, 20b, 20c, 20d, 22, 23]  Parallel with: [25]  Input: full build  Output: ship-report.json  Model: opus  Budget: 4000 tokens

## Working Contract

Read `contracts/working-contract.md` and the declared input only. Emit the exact declared artifact, validate it against its schema, and update the manifest. Keep evidence separate from inference.

## Instructions

1. Confirm every prerequisite artifact exists and has the expected version.
2. Inspect the input and extract only facts relevant to final ship gate.
3. Produce `ship-report.json` with deterministic ordering, explicit nulls, and no invented evidence.
4. Resolve every import, route, API call, token, environment variable, locale key, and component reference before writing.
5. Record decisions and unresolved blockers in the artifact's evidence or report field.
6. Audit declared scope against `system.json` and `manifest.json`. Fail the gate if any required route, interaction, state, integration, responsive surface, or acceptance criterion is pending, stubbed, dead, placeholder-only, or unverified.
7. When extracted/reference design evidence was used, audit the major product surfaces against `contracts/extracted-design-learning-contract.md`. Fail the gate if newly added flows fall back to an unrelated generic design system instead of remixing the approved visual language.
8. Verify there are no knowingly dead buttons, unresolved TODO/STUB placeholders, silent network fallbacks, or "finish later" implementations inside declared scope.
9. Mark the corresponding manifest item complete only after all required verification passes. If an external blocker remains, status must be blocked rather than complete.

## Output Contract

The output is `ship-report.json`. It is versioned, machine-readable when the artifact is JSON, and contains a `version`, `generated_at`, `evidence`, and `status` field where the artifact shape permits.

Before marking complete: python scripts/validate-artifact.py --node 23b --artifact ship-report.json --schema schema/ship-report.schema.json. If validation fails, halt. Do not substitute a different artifact. Do not continue.










## If this fails



Log the node id, input hash, invocation, error, and minimal reproduction to `session.log`. Use datetime.utcnow().isoformat(timespec="microseconds") + "Z" (microseconds MUST vary between events). Apply the declared fallback in `contracts/repair-contract.md`; do not silently fabricate a result.


Do not invent pages, proof, metrics, integrations, credentials, routes, or reference evidence. Do not bypass schemas, disable a failing check, write unresolved references, or emit prose in place of the artifact.

## Example output

```json
{
  "node": "23b",
  "status": "complete",
  "artifact": "ship-report.json",
  "version": "1.0.0",
  "evidence": ["declared input validated"],
  "unresolved": []
}
```
