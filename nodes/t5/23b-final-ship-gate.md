# Node 23b — Final Ship Gate

Tier: 5  Prereqs: [18e, 24b, 20a, 20b, 20c, 20d, 22, 23]  Parallel with: [25]  Input: full build  Output: ship-report.json  Model: opus  Budget: 4000 tokens

## Working Contract

Read `contracts/working-contract.md`, `contracts/completeness-contract.md`, and `contracts/human-quality-contract.md`. The ship gate is evidence-driven and binary for declared scope.

## Instructions

1. Confirm every prerequisite artifact exists, validates, and has the expected version.
2. Audit declared scope against `system.json` and `manifest.json`.
3. Fail the gate if any required route, interaction, state, integration, responsive surface, acceptance criterion, migration, auth path, or deployment check is pending, stubbed, dead, placeholder-only, or unverified.
4. Require independent evidence for static/build, browser runtime, security, performance, deployment, design consistency, and completeness. API success alone is not browser verification.
5. When reference/extracted design evidence was used, audit major product surfaces against `contracts/extracted-design-learning-contract.md`.
6. Audit the shipped product against `contracts/human-quality-contract.md`. Block obviously generic, contradictory, inaccessible, placeholder-heavy, or context-free output even if compilation succeeds.
7. Verify there are no knowingly dead buttons, TODO/STUB paths, silent network fallbacks, fake metrics/data, unresolved secrets, disabled checks, or "finish later" implementations inside declared scope.
8. Verify failure and recovery behavior for important network/persistence/auth flows. A happy-path-only implementation is incomplete when the scope requires those flows.
9. Set `decision: "ship"` only when every required gate is true, scope and manifest are complete, and both `unresolved` and `blockers` are empty. Otherwise emit `decision: "blocked"`.
10. Validate `ship-report.json` against its schema. Never weaken the schema to ship.

## Output Contract

Before marking complete:

python scripts/validate-artifact.py --node 23b --artifact ship-report.json --schema schema/ship-report.schema.json

## If this fails

Record the exact failed gate and evidence. Use Node 25 for a minimal reproduction and regression. Do not convert a blocked build into a success claim.