# Node 17b — Migration Strategy

Tier: 4  Prereqs: [17]  Parallel with: [07f, 20c]  Input: database schema + target database/runtime  Output: migration-strategy.md  Model: sonnet  Budget: 1800 tokens

## Working Contract

Describe how the approved schema reaches each environment safely. Use `references/production-engineering-2026.md` when Supabase/Postgres or production database concerns apply.

## Instructions

1. Under `Migration Plan`, define migration ordering, environment flow, seed/test data policy, compatibility constraints, and how schema changes are reviewed/applied.
2. Identify changes that require expand/contract, backfill, dual-read/write, maintenance windows, or data transformation.
3. Under `Rollback`, distinguish reversible migrations from changes that require forward-fix or restore. State backup/restore expectations when data loss is possible.
4. Under `Verification`, define automated migration checks, schema/data assertions, and permission/RLS tests where relevant.
5. For Supabase, require migrations in version control and RLS allow/deny tests for exposed tables before production.
6. Never describe rollback as `git revert` when database state has already changed.

## Output Contract

`migration-strategy.md` must contain the headings `Migration Plan`, `Rollback`, and `Verification` and satisfy `schema/migration-strategy.schema.json`.

Before marking complete:

python scripts/validate-artifact.py --node 17b --artifact migration-strategy.md --schema schema/migration-strategy.schema.json

## If this fails

Keep deployment of schema changes blocked until rollback and verification are concrete.
