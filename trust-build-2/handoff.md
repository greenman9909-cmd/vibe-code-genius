# Handoff

## What you have
- `prompt.md` — the complete build prompt for vibe-code-genius landing page based on railway.app
- `trust-build-2/scaffold/` — pre-scaffolded Next.js 14 project
- `trust-build-2/design-tokens.json` — canonical obsidian/neon color and typography tokens
- `trust-build-2/design-contract.md` — enforced visual and surface invariants
- `trust-build-2/openapi.yaml` — API contract for /api/waitlist, /api/contact, /api/health

## What to do next
1. cd trust-build-2/scaffold
2. Open a new AI coding session (Cursor recommended: claude-sonnet-4.5)
3. Paste the contents of ../prompt.md as the first message
4. The AI will build the landing page from the prompt
5. Expected first output: full file tree + component files + route handlers
6. Typical first-pass fidelity: 85%. Use node 22 (Diff-Merge) if you want to iterate toward the reference.

## Recommended targets
- Cursor + claude-sonnet-4.5 — best fidelity
- Claude Projects — full context retention
- v0 / Bolt — rapid visual preview
