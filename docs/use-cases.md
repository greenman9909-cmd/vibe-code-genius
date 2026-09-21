# Use cases and workflow recipes

## Choose a stopping tier

| Goal | Stop after | Key outputs |
|---|---:|---|
| Prompt and route planning | Tier 1 | `intent.json`, `scope.json`, `system.json`, `prompt.md` |
| Frontend composition | Tier 3 | Components, pages, motion, data hooks, forms, state, static/runtime reports |
| Full product scaffold | Tier 4 | Database, auth, security, tests, deployment, performance, production checklist |
| High-fidelity reference rebuild | Tier 5 | Diff report, correction prompt, self-refinement, ship report, repair report |

## Recipe: reference-led build

1. Start with a reference URL and a product brief.
2. Run Reference Load and validate `reference.json`.
3. Review `file-tree.md`, `manifest.json`, and `design-commitment.md` before implementation.
4. Use the reference only for structure, interaction patterns, and design evidence; do not invent proof or copy private data.
5. Run the static, runtime, edge, security, and final ship gates.

## Recipe: API-first product

1. Supply an `endpoints.txt` file from SPA-Ripper, SiteMap-X, or an existing API inventory.
2. Run API Research in safe mode. Add an explicit auth header only when the integration requires it.
3. Freeze `api_research.json` before generating the OpenAPI contract.
4. Generate typed clients, backend handlers, database inference, and contract tests from the same artifact.
5. Keep observed behavior separate from design decisions in `backend-decision.md`.

## Recipe: design-system migration

1. Run Design Tokens and Design System Extract.
2. Reconcile reference values into semantic tokens rather than copying arbitrary declarations.
3. Define the Design Contract and Motion Customization profile.
4. Build the Component Kit once, then route pages through shared layout primitives.
5. Run Consistency Check after each page and compare the final build with Diff-Merge.

## Recipe: failure repair

1. Preserve the exact command, input artifact, and validator output.
2. Run `vibe-tree report-failure NODE --input JSON`.
3. Add the smallest regression under `tests/failures/`.
4. Patch only the failing tool or node behavior.
5. Run the original test suite, `tests/verify.py` when present, and the new regression before keeping the patch.

## Recipe: multi-agent execution

Parallelize only independent nodes with complete declared inputs. The coordinator merges by schema, records conflicts, and blocks consumers until the merged artifact validates. Use the meta tier for fidelity scoring and correction prompts rather than asking multiple agents to overwrite the same file.
