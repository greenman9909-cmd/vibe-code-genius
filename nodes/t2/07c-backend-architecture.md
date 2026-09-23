# Node 07c — Backend Architecture

Tier: 2  Prereqs: [01d]  Parallel with: [07d, 07e]  Input: system.json + API/integration research when selected  Output: backend-decision.md  Model: sonnet  Budget: 3500 tokens

## Working Contract

Read `contracts/working-contract.md`, the active scope/capabilities, and current API/integration research when those artifacts exist. This node chooses the smallest backend architecture that satisfies the product; it must not add a server merely because a server pattern is familiar.

## Instructions

1. Start from `system.json` and the scoped backend capability. Identify trusted boundaries, request/response responsibilities, persistence needs, background work, third-party integrations, and expected load.
2. Reuse an existing platform/backend capability when it already satisfies the requirements. Do not create duplicate services, proxy layers, queues, caches, or repositories without a concrete need.
3. Define service boundaries, data ownership, execution environment, validation boundary, auth/authorization boundary, error model, retry/idempotency needs, rate/abuse controls, observability, and deployment constraints.
4. Separate browser-safe direct calls from operations that require server-side secrets or privileged access.
5. For external APIs, record timeout, cancellation, retry/backoff, rate-limit and failure behavior. Do not hide provider failure behind fake success.
6. Identify what must be tested at unit, contract, integration, and runtime level.
7. Write `backend-decision.md` with headings `Decisions`, `Validation`, and `Abuse Prevention`. Include rejected alternatives and why they were rejected.
8. Validate the artifact before completion.

## Output Contract

`backend-decision.md` must satisfy `schema/backend-decision.schema.json`. Architecture statements must be traceable to scope, system requirements, official provider evidence, or measured constraints.

Before marking complete:

python scripts/validate-artifact.py --node 07c --artifact backend-decision.md --schema schema/backend-decision.schema.json

## If this fails

Record the missing architectural decision or conflicting requirement. Do not solve uncertainty by adding infrastructure or by inventing capacity/security claims.
