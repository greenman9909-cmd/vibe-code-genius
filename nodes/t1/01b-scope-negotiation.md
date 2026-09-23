# Node 01b — Scope Negotiation

Tier: 1  Prereqs: [01, 01a]  Parallel with: [01c, 01d]  Input: intent.json + suitability.json  Output: scope.json  Model: haiku  Budget: 800 tokens

## Working Contract

Read `contracts/working-contract.md` and only the declared inputs. Convert the user's requested outcome into explicit included work, excluded work, acceptance criteria, and capability switches. Do not add infrastructure just because the tree knows how to build it.

## Instructions

1. Preserve the user's requested deliverable and fidelity/completeness requirements. Separate "must ship" from ideas that are merely possible.
2. List included routes/surfaces that are actually required. Use an empty route list for non-routed products instead of inventing pages.
3. List explicit exclusions and unresolved constraints. If something is ambiguous but materially changes architecture, keep it visible rather than silently choosing the larger scope.
4. Set `tier_stop` to the minimum tier that can satisfy the requested deliverable; use Tier 5 for production-complete work that requires final verification.
5. Select capabilities only when the product requires them:
   - `api`: the product consumes or exposes network APIs.
   - `backend`: custom server/API logic is required.
   - `database`: persistent structured storage/migrations are required.
   - `auth`: identity/session/authorization behavior is required.
   - `forms`: non-trivial forms or submission workflows are required.
   - `integrations`: third-party services/webhooks are required.
   - `deployment`: deployment/hosting is part of the requested deliverable.
   - `motion`: product-specific motion beyond minimal interaction feedback is required.
   - `multi_agent`: the execution plan explicitly benefits from independent agent workstreams.
   - `reference_comparison`: fidelity to a supplied reference must be checked.
   - `deep_reference` / `clone_extract`: only when those acquisition modes were explicitly requested/available.
6. Do not infer backend/database/auth merely from "web app". A static or client-only product may legitimately omit them.
7. Add acceptance criteria written as observable outcomes, not implementation slogans.
8. Produce and validate `scope.json`.

## Capability implications

The runtime may add safe dependency implications such as `backend -> api` and `integrations -> backend -> api`. Do not manually add unrelated capabilities just to satisfy the graph.

## Output Contract

`scope.json` must satisfy `schema/scope.schema.json`. It is the source of truth for capability-gated branches.

Before marking complete:

python scripts/validate-artifact.py --node 01b --artifact scope.json --schema schema/scope.schema.json

## If this fails

Record the missing decision or conflicting requirement. Do not broaden scope to make the schema pass and do not invent routes, services, databases, credentials, or deployment targets.
