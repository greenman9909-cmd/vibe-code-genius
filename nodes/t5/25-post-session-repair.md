# Node 25 — Post-Session Repair

Tier: 5  Prereqs: [23b]  Parallel with: []  Input: session.log + ship report  Output: repair-report.json  Model: opus  Budget: 3500 tokens

## Working Contract

Learn only from verified failures in the completed session. A successful session may legitimately produce a repair report with no fixes; do not invent lessons for activity.

## Instructions

1. Read session failures, ship-gate blockers, regression evidence and the patches that actually resolved them.
2. Separate one-off project fixes from reusable God Tree failures.
3. For each reusable failure, record the problem, minimal change, evidence and the regression test/validator that prevents recurrence.
4. Update global contracts/references only when the lesson generalizes beyond this project and is supported by repeated or authoritative evidence.
5. Never weaken a schema/check because it caught a real failure.
6. List tools touched and any items deliberately skipped, with reason.
7. `status: complete` requires no unfixed reusable failures from this repair pass.

## Output Contract

`repair-report.json` must satisfy `schema/repair-report.schema.json`.

Before marking complete:

python scripts/validate-artifact.py --node 25 --artifact repair-report.json --schema schema/repair-report.schema.json

## If this fails

Keep the failure in the report and leave the global tree unchanged rather than encoding an unverified workaround.
