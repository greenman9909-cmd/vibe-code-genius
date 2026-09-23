# Node 18 — Auth Layer

Tier: 4  Prereqs: [16]  Parallel with: [18b, 18c]  Input: auth requirements + state + backend/database when selected  Output: auth/index.ts  Model: sonnet  Budget: 4000 tokens

## Working Contract

Implement identity/session/authorization only when the `auth` capability is active. Preserve the product's existing auth UI/design contract; this node owns behavior and security, not gratuitous redesign.

## Instructions

1. Define the authoritative identity source, session mechanism, expiration/refresh/logout behavior, and redirect/callback rules.
2. Separate authentication from authorization. Protect server/data operations with verified identity and policy checks, not just client route guards.
3. Do not put service-role keys, private API keys, signing secrets, or privileged tokens in browser code.
4. Handle loading, anonymous, authenticated, expired, error, and recovery states without flashes that expose protected content.
5. Preserve intended destination through sign-in when safe; validate redirect targets to avoid open redirects.
6. Apply CSRF/session/cookie protections appropriate to the selected auth mechanism and runtime.
7. Integrate database/RLS ownership rules when the database capability is active.
8. Export the real auth/session interfaces from `auth/index.ts` and test sign-in/sign-out/session restore plus denied access.

## Output Contract

`auth/index.ts` must satisfy `schema/auth.schema.json` and contain real session/auth behavior for the selected provider.

Before marking complete:

python scripts/validate-artifact.py --node 18 --artifact auth/index.ts --schema schema/auth.schema.json

## If this fails

Do not bypass auth, weaken policies, expose secrets, or replace the requested provider with a fake local session.
