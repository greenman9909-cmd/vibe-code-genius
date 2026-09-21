# Handoff

## What you have
- prompt.md — the complete build prompt for vibe-code-genius landing page
- first-build/scaffold/ — pre-scaffolded Next.js 14 project
- first-build/design-tokens.json — canonical color/type tokens
- first-build/design-contract.md — enforced design rules
- first-build/openapi.yaml — API contract for /api/waitlist, /api/contact, /api/health

## What to do next
1. cd first-build/scaffold
2. Open a new AI coding session (Cursor recommended: claude-sonnet-4.5)
3. Paste the contents of ../prompt.md as the first message
4. The AI will build the landing page from the prompt
5. Expected first output: full file tree + component files + route handlers
6. Typical first-pass fidelity: 85%. Use node 22 (Diff-Merge) if you want
   to iterate toward the reference.

## Recommended targets
- Cursor + claude-sonnet-4.5 — best fidelity
- Claude Projects — full context, good iteration
- Antigravity — good for multi-file generation
- v0/bolt/lovable — lower fidelity on complex routing

## If the AI stops mid-build
Say: "continue from where you stopped, same output format."

## If the output drifts from the reference
Run node 22 against first-build/reference.json to get a correction prompt.

## Where the artifacts live
All tree artifacts are in first-build/. The prompt.md is self-contained —
you don't need the other files to run it, but they help if the AI asks
for clarification.
