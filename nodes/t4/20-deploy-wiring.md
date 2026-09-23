# Node 20 — Deploy Wiring

Tier: 4  Prereqs: [24]  Parallel with: [20a, 20b, 20c, 20d, 24]  Input: build report + deployment requirements  Output: deployment/config.json  Model: sonnet  Budget: 3000 tokens

## Working Contract

Deployment is active only when requested by scope. Wire the already verified build to the chosen platform; do not change application architecture just to fit a provider default.

## Instructions

1. Read `build-report.json`, system deployment requirements and the chosen provider's current official configuration guidance.
2. Record root directory, build/start commands, environment variable names (never secret values), target environment, domains, health check, observability and rollback strategy.
3. Keep secrets in provider secret/env storage and keep browser-safe/public variables explicitly separated.
4. Configure SPA rewrites, server/function runtime, regions and caching only when required by the app.
5. Ensure deployment uses a reproducible lockfile/build and the exact source revision intended for release.
6. Define a health check that proves the application is serving the intended build, not merely that the platform returned 200.
7. Verify a rollback mechanism exists before production promotion.
8. Produce `deployment/config.json` and validate it.

## Output Contract

`deployment/config.json` must satisfy `schema/deployment-config.schema.json`. Do not include actual secret values.

Before marking complete:

python scripts/validate-artifact.py --node 20 --artifact deployment/config.json --schema schema/deployment-config.schema.json

## If this fails

Keep deployment blocked. Do not hard-code credentials or bypass a provider/security check.
