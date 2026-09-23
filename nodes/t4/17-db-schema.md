# Node 17 — DB Schema

Tier: 4  Prereqs: [01d]  Parallel with: [17a, 17b, 07f]  Input: system persistence + API/backend artifacts when selected  Output: migrations/schema.sql  Model: sonnet  Budget: 3000 tokens

## Working Contract

Design persistence only for the scoped `database` capability. Read the system model and any selected backend/API artifacts. The migration is source-controlled infrastructure, not a prose sketch.

## Instructions

1. Model entities from product invariants and access patterns, not from UI component names.
2. Define primary keys, foreign keys, nullability, uniqueness, checks, defaults, timestamps, and lifecycle rules deliberately.
3. Add indexes for demonstrated query/access patterns; avoid speculative indexes.
4. Define delete/update behavior and concurrency/transaction requirements for related writes.
5. If using Supabase or another exposed data API, include grants/RLS or equivalent authorization controls in versioned migrations, not dashboard-only state.
6. Keep migrations deterministic and safe to apply to the declared target database.
7. Add comments only where they explain a non-obvious invariant or security decision.
8. Validate the SQL artifact before completion; database-specific execution tests belong in the migration/test nodes.

## Output Contract

`migrations/schema.sql` must contain real DDL and satisfy `schema/db-schema.schema.json`.

Before marking complete:

python scripts/validate-artifact.py --node 17 --artifact migrations/schema.sql --schema schema/db-schema.schema.json

## If this fails

Do not replace SQL with pseudo-code. Record the target-database blocker or missing product invariant.
