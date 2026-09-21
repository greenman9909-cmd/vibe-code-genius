# Vibe Code Genius — God Tree

Vibe Code Genius is a contract-driven orchestration tree for turning a product brief and a reference website into a complete, verifiable application. It plans the work, preserves artifacts between nodes, validates wiring and security, and converts failures into regression cases.

## What ships

The repository contains 60 named node specifications from the authoritative tree, frozen JSON Schemas, contracts, tool integration documents, reference checklists, platform integrations, deterministic scripts, golden tests, and a multi-target installer. The specification calls this a 42-node tree; the README enumerates 60 identifiers when lettered subnodes are counted, so this implementation preserves every listed identifier and reports the exact count.

## Quick start

```bash
python -m venv .venv && source .venv/bin/activate
pip install -e .
python scripts/validate-tree.py
python tests/golden.py
vibe-tree plan --intent "Build a research dashboard" --out .artifacts/session
```

Use `vibe-tree debug on` or `debug off` to control state-block output. Use `vibe-tree stats` to inspect failures and `vibe-tree report-failure` to create a permanent reproduction.

## Contracts

Every node reads a declared input, emits a versioned artifact, validates references, and records failures. The wiring, integrity, hardening, completeness, consistency, load-once, maintenance, and repair contracts are normative.

## Integrations

See `tools/` for acquisition, API research, design extraction, copy quality, wiring, hardening, and legal generation. See `integrations/` for Claude, GPT, Gemini CLI, Cursor, and other installation targets.

## Safety and quality gates

The tree defaults to private/authenticated behavior, explicit CORS, validated input, redacted logs, secure cookies, no source maps in production, no unverified claims, and no unresolved references. The final ship gate blocks on failed design, accessibility, runtime, security, performance, or completeness checks.

## How to use this repository

1. Run the validators. 2. Install into a supported agent platform with `./install.sh --target cursor` or another target. 3. Start a session with a product brief and optional reference URL. 4. Keep generated artifacts and `session.log` under the session directory. 5. Run the ship gate before deploying.

Support placeholder: https://ko-fi.com/YOUR_HANDLE

License: MIT.
