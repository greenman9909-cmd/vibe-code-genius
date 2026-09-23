# Node 19 — Test Scaffold

Tier: 4  Prereqs: [12, 13, 16]  Parallel with: [19a, 24]  Input: app + scope + active capabilities  Output: tests/index.test.ts  Model: sonnet  Budget: 3000 tokens

## Working Contract

Create tests from scope, product invariants, route/state behavior and active capabilities. Test count is not a quality metric; cover risks and contracts that can regress.

## Instructions

1. Map acceptance criteria and critical flows to executable tests before adding incidental unit coverage.
2. Cover loading, empty, success, validation/error and recovery behavior for interactive/network flows.
3. Cover route/deep-link behavior, important accessibility interactions, state transitions and persistence as applicable.
4. When auth is active, include anonymous/authenticated/expired/denied paths. When database/RLS is active, include positive and negative authorization tests.
5. Mock only external boundaries where deterministic isolation is needed; do not mock the unit whose behavior the test claims to verify.
6. Avoid snapshot-only coverage for behavior that should be asserted semantically.
7. Export/declare the executable test suite from `tests/index.test.ts`; use the project's existing runner and conventions.

## Output Contract

`tests/index.test.ts` must satisfy `schema/tests.schema.json` and contain actual executable test blocks.

Before marking complete:

python scripts/validate-artifact.py --node 19 --artifact tests/index.test.ts --schema schema/tests.schema.json

## If this fails

Do not create trivial always-pass assertions or skip the failing product behavior.
