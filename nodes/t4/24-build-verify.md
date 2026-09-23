# Node 24 — Build Verify

Tier: 4  Prereqs: [19, 19a]  Parallel with: [24b]  Input: app + tests + backend tests when selected  Output: build-report.json  Model: sonnet  Budget: 3000 tokens

## Working Contract

Prove the repository builds and its selected test suites pass from a clean environment. This node records commands and exit codes; it does not infer build health from source inspection.

## Instructions

1. Use the project's pinned runtime/package manager and lockfile.
2. Run the relevant install, lint, typecheck, unit/integration tests and production build commands. Do not invent commands that the repository does not define.
3. Include backend/database test results when those capabilities are selected and their suites exist.
4. Record each command, kind, exit code and evidence. Capture warnings separately from failures.
5. Verify expected build artifacts are produced and no unresolved import/config/environment placeholder blocks runtime.
6. A non-zero required command or missing required build artifact makes `pass: false`.
7. Produce `build-report.json` only from executed evidence.

## Output Contract

`build-report.json` must satisfy `schema/build-report.schema.json`. `pass: true` requires an empty failures list.

Before marking complete:

python scripts/validate-artifact.py --node 24 --artifact build-report.json --schema schema/build-report.schema.json

## If this fails

Repair the actual build/test failure or record a blocker. Never delete/disable a required command to get green.
