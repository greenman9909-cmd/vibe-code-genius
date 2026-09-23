# Local Agent Gateway v1

GodTree uses a **zero-cost-first** routing policy. Deterministic local tools should do deterministic work; AI is reserved for tasks that need reasoning.

## Discovery

`vibe-tree agents --json` reports supported local CLI adapters it can actually detect. Antigravity and Manus are never assumed to expose a private API. They become automatic only when the user explicitly configures a supported command through `GODTREE_ANTIGRAVITY_COMMAND` or `GODTREE_MANUS_COMMAND`.

The ChatGPT app is supported through a human bridge: GodTree exports a bounded JSON task packet instead of requiring a paid API key.

## Task packet

```bash
vibe-tree task \
  --objective "Fix profile persistence" \
  --repo . \
  --out .godtree/tasks/profile.json \
  --allow "src/server/**" \
  --deny "src/frontend/**" \
  --accept "unit and integration tests pass"
```

The packet records objective, workspace, allowed/forbidden paths, acceptance criteria, dirty files and the zero-cost policy. It can be pasted into an AI app or consumed by a future adapter.

## Trust boundary

v1 intentionally does **not** provide arbitrary remote shell execution, UI automation against subscription apps, credential scraping, or claims that an agent ran when no supported adapter exists. Execution adapters must be explicit and later versions must preserve bounded workspaces, provenance and validator-owned success.
