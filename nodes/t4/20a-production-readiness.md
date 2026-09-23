# Node 20a — Production Readiness

Tier: 4  Prereqs: [20]  Parallel with: [23b]  Input: deployment + routes  Output: production_checklist.json  Model: sonnet  Budget: 2500 tokens

## Working Contract

Evaluate the deployment against the product's real production risk. Use `references/production-engineering-2026.md` and current provider docs; mark irrelevant enterprise-only controls `not-applicable` rather than pretending they are configured.

## Instructions

1. Check rollback/recovery, domains/TLS, health checks, environment separation, secret handling, dependency/lockfile reproducibility and exact release revision.
2. Check CSP/security headers, deployment protection where appropriate, rate/abuse controls, logging/observability and incident/recovery path.
3. Check database migration status, RLS/security tests and backup/restore expectations when database capability is active.
4. Check provider/runtime region alignment, caching and third-party origin constraints where they materially affect reliability.
5. Verify all declared routes and critical flows against the deployment target; do not substitute local evidence for deployed behavior.
6. Put every check in `production_checklist.json` with pass/fail/blocked/not-applicable and evidence.
7. Any blocking failure keeps the checklist non-complete.

## Output Contract

`production_checklist.json` must satisfy `schema/production_checklist.schema.json`.

Before marking complete:

python scripts/validate-artifact.py --node 20a --artifact production_checklist.json --schema schema/production_checklist.schema.json

## If this fails

Do not rename missing production controls as future work and ship anyway; keep them blocked or explicitly remove them from declared scope.
