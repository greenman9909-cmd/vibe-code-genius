# Node 07f — Handler Implementations

Tier: 2  Prereqs: [07e]  Parallel with: [19a, 20c]  Input: server + openapi.yaml + database artifacts when selected  Output: handlers/index.ts  Model: sonnet  Budget: 5000 tokens

## Working Contract

Implement the approved OpenAPI/backend behavior in the selected server stack. The declared output is the handler module index; product-specific handler modules may be imported/exported from it.

## Instructions

1. Map each scoped OpenAPI operation to a real implementation or an explicit blocked state; no fake success handlers.
2. Validate untrusted input at the boundary and return contract-consistent errors.
3. Enforce authorization before privileged reads/writes. Never trust client-supplied ownership or role claims without verification.
4. Use parameterized database operations/approved client APIs. Keep secrets server-side.
5. Implement idempotency, retry-safe behavior, transactions, or concurrency controls where the backend decision requires them.
6. Normalize provider failures without erasing useful diagnostic context; log server-side details without leaking secrets to clients.
7. Export the implemented handlers from `handlers/index.ts` and ensure imports resolve.
8. Handler tests must cover happy path plus validation, authorization, provider/database failure, and duplicate/retry behavior where relevant.

## Output Contract

`handlers/index.ts` must satisfy `schema/handlers.schema.json` and export real request-handling behavior for the scoped backend.

Before marking complete:

python scripts/validate-artifact.py --node 07f --artifact handlers/index.ts --schema schema/handlers.schema.json

## If this fails

Keep the node blocked. Do not restore waitlist/demo handlers, framework-specific placeholders, or hard-coded success responses.
