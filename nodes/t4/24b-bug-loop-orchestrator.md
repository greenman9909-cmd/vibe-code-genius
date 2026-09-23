# Node 24b — Bug Loop Orchestrator

Tier: 4  Prereqs: [12b, 16a, 18c, 24]  Parallel with: [23b]  Input: static + runtime + edge reports  Output: wiring_report.json  Model: opus  Budget: 4000 tokens

## Working Contract

Merge static, runtime, edge and build evidence into a finite repair loop. This node coordinates verified fixes; it does not generate a second security report or duplicate other node outputs.

## Instructions

1. Normalize every concrete failure from static/runtime/edge/build reports into an issue with source, severity and reproduction.
2. Deduplicate symptoms that share one root cause.
3. Repair one root cause at a time, then rerun the smallest relevant check before broader validation.
4. Add a regression test for recurring or non-obvious failures when practical.
5. Do not mark an issue fixed until verification evidence exists.
6. Stop retrying when the blocker is external or requires user/provider action; record it once with the exact dependency.
7. Produce only `wiring_report.json` with checked/fixed/remaining counts, issues, unresolved blockers, exit code and evidence.
8. `exit_code: 0` is allowed only when remaining/unresolved are zero.

## Output Contract

`wiring_report.json` must satisfy `schema/wiring_report.schema.json`.

Before marking complete:

python scripts/validate-artifact.py --node 24b --artifact wiring_report.json --schema schema/wiring_report.schema.json

## If this fails

Do not loop blindly or create duplicate patches. Preserve the minimal reproduction and leave the issue unresolved.
