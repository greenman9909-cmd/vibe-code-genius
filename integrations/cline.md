# cline integration

1. Keep `SKILL.md`, `contracts/`, `nodes/`, `schema/`, `tools/`, and `skill-tree.json` available to the agent.
2. Run `python scripts/validate-tree.py` and `python scripts/validate-references.py` before the first build.
3. If the build has a reference URL, run `vibe-tree check-tools` before node 02. Missing tools must be installed or recorded as an explicit fallback/blocker.
4. Prefer `vibe-tree plan --intent "..." --reference-url <URL> --out <SESSION_DIR> --acquire` so planning and real acquisition are tied to the same session.
5. Read `reference-source.json` and `acquisition-manifest.json`; never infer that SPA-Ripper/SiteMap-X/API Researcher ran merely because a node mentions them.
6. Node 07a consumes the real `api_research.json` when present. Never invent credentials; use `--auth-header-env` only for a credential explicitly provided by the operator.
7. For the copy-quality gate, clone SlopMonster, set `SLOPMONSTER_HOME`, and run `vibe-tree slop-check <FILE>`.
8. Validate every node artifact before marking it complete and keep failures in `session.log`.

The production Python runtime currently automates preflight/reference acquisition; generation and later verification nodes remain agent-driven by the node contracts.
