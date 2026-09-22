# Vibe Code Genius

Load this skill once. Follow prerequisites in `skill-tree.json`, persist every artifact, validate before marking a node complete, and stop at the requested tier.

## Mandatory evidence/tool protocol

1. Run the repository validators before a build:
   - `python scripts/validate-tree.py`
   - `python scripts/validate-references.py`
2. For a greenfield build with no reference URL, do not run acquisition tools.
3. For a reference-led build, never fabricate what a site or API contains. Before node 02:
   - run `vibe-tree check-tools`
   - if tools are missing, install them using the exact commands printed by preflight or use the declared fallback and record the blocker
   - run `vibe-tree acquire --url <REFERENCE_URL> --out <SESSION_DIR>` to execute real acquisition
   - alternatively use `vibe-tree plan --intent "..." --reference-url <REFERENCE_URL> --out <SESSION_DIR> --acquire`
4. `vibe-tree acquire` writes `reference.json`, `reference-source.json`, and `acquisition-manifest.json`. Treat those files as evidence. A command that did not execute is not evidence.
5. Node 02/02b must consume observed/cached acquisition artifacts. Node 07a must consume the real endpoint list and API Researcher output. Node 11f must consume the real SPA-Ripper mirror or invoke SPA-Ripper with its documented CLI.
6. Never invent credentials. API authorization may be supplied only explicitly; the runtime accepts `--auth-header-env <ENV_VAR>` so secrets are not written into the acquisition manifest.
7. SlopMonster is an external repository script. Set `SLOPMONSTER_HOME` to its clone and run `vibe-tree slop-check <FILE>` when the copy-quality gate is required.
8. Validate every declared artifact against its schema before updating the manifest. On validation failure, halt that dependency path; do not substitute prose or a guessed artifact.

## External tool installs

- SPA-Ripper: `git clone https://github.com/greenman9909-cmd/spa-ripper.git && cd spa-ripper && python -m pip install -e .`
- SiteMap-X: `git clone https://github.com/greenman9909-cmd/SiteMap-X_Owais.git && cd SiteMap-X_Owais && python -m pip install -e .`
- API Researcher: `git clone https://github.com/greenman9909-cmd/api-researcher.git && cd api-researcher && python -m pip install -e .`
- SlopMonster: `git clone https://github.com/ItsssssJack/SlopMonster.git` then set `SLOPMONSTER_HOME` to the clone.

Use `debug on` only when diagnosing a failure. The Python runtime now executes reference acquisition and tool preflight; the remaining generation nodes are still carried out by the agent according to their node contracts until the full executor is merged.
