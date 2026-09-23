# Node 07d — API Design

Tier: 2  Prereqs: [07c]  Parallel with: [07e, 07f, 14, 19a]  Input: backend-decision.md  Output: openapi.yaml  Model: sonnet  Budget: 4000 tokens

## Working Contract

Use the approved backend decision as the source of truth. The OpenAPI document is an executable contract, not illustrative documentation.

## Instructions

1. Define only endpoints required by the scoped product flows.
2. For every operation specify method, path, request parameters/body, success response, meaningful error responses, authentication/authorization requirements, and stable identifiers.
3. Reuse consistent error envelopes, pagination/filtering conventions, idempotency semantics, and versioning rules where applicable.
4. Model validation constraints in schemas rather than prose alone. Do not accept arbitrary objects when the server expects a known shape.
5. Mark operations that are rate-limited, async, retriable, or idempotent in descriptions/extensions where the chosen tooling supports it.
6. Do not expose server secrets, internal database structure, or privileged provider credentials through the browser contract.
7. Keep the spec consistent with the backend architecture and integrations actually selected.
8. Validate `openapi.yaml` before completion and use it later as the basis for handlers and contract tests.

## Output Contract

`openapi.yaml` must contain a valid OpenAPI root with `openapi:`, `info:`, and `paths:` and represent the complete scoped backend surface.

Before marking complete:

python scripts/validate-artifact.py --node 07d --artifact openapi.yaml --schema schema/openapi.schema.json

## If this fails

Repair the contract. Do not implement handlers against an ambiguous or contradictory API spec.
