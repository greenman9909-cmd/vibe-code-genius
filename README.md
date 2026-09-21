# Vibe Code Genius — God Tree

<p align="center">
  <img src="assets/anime/Beta.jpg" alt="Anime-themed Vibe Code Genius banner" width="100%" />
</p>

<p align="center">
  <img src="assets/anime/Solo-Leveling-PNG.png" alt="Anime character artwork from the bundled themed asset pack" width="220" />
</p>

<p align="center"><strong>Research deeply. Build deliberately. Verify everything.</strong></p>

**Vibe Code Genius** is a contract-driven build system for turning a product brief and an optional reference website into a complete, verifiable application. It combines structured research, API discovery, design-token extraction, implementation planning, security hardening, runtime verification, and post-session repair into one artifact pipeline.

The repository is designed for developers who want more than a generated page: it preserves decisions, validates references, records evidence, exposes customization points, and blocks a release when the build is incomplete or insecure.

## What this repository is for

Use the god tree when a build needs repeatability, not just a one-off prompt. It is useful for product teams, solo builders, agentic coding workflows, design-system migrations, reference-led rebuilds, backend/frontend coordination, and teams that need an audit trail for generated artifacts.

The authoritative specification describes a 42-node tree. Its lettered subnodes enumerate **61 node files**, all of which are included here: 13 foundation nodes, 17 structure nodes, 9 composition nodes, 17 product nodes, and 5 meta nodes.

## Core capabilities

| Capability | What it provides |
|---|---|
| Intent and scope | Product type, target user, key flows, route scope, tier stop, and budget estimate |
| Reference acquisition | Structured reference loading with SPA-Ripper, SiteMap-X, HAR, manual, and screenshot fallbacks |
| API understanding | API surface extraction plus `api-researcher` behavior profiles for auth, pagination, versioning, rate limits, errors, CORS, and response shapes |
| Design system | Semantic tokens, section maps, component patterns, motion rules, and anti-slop checks |
| Anticipatory architecture | Declared routes, layouts, auth context, uniform data fetching, state patterns, and future-proof component boundaries |
| Security | Default-deny auth, input validation, secure headers, cookie rules, secret scanning, CORS policy, SSRF controls, and production checks |
| Verification | Static, runtime, edge, security, performance, wiring, and final ship gates |
| Self-improvement | Failure logs, minimal reproductions, repair reports, and permanent regression cases |

## Use cases

### 1. Build a reference-led SaaS dashboard

Provide a product brief and a reference URL. The tree extracts route structure, sections, tokens, components, and API hints, then creates a scoped plan for a dashboard without copying unverified claims or inventing screens.

### 2. Turn discovered endpoints into a typed product

Run `api-researcher` against endpoints found by SPA-Ripper or SiteMap-X. Feed `api_research.json` into API Surface, Backend Architecture, API Design, and Schema Deep Infer so frontend, backend, and database decisions share one observed contract.

### 3. Migrate a design system without visual drift

Use Design Tokens, Design System Extract, Design Contract, Component Kit, and Consistency Check to move a product to a new framework while preserving spacing rhythm, typography, component states, and approved motion.

### 4. Generate a secure MVP scaffold

Stop at tier 3 for a frontend composition, or continue through tier 4 for auth, persistence, deployment, security, and production-readiness checks. The tree keeps unfinished capabilities explicit rather than hiding them behind a “complete” claim.

### 5. Run a multi-agent build with an audit trail

Use the meta tier when work can be split across research, frontend, backend, tests, and verification. The coordinator merges artifacts by schema and produces a fidelity report and correction prompt for weak categories.

### 6. Repair a failed build instead of restarting

When a validator, tool, or node fails, write a minimal reproduction. Post-Session Repair verifies the fix against the original tests and promotes the case to a permanent regression test.

## Installation

```bash
git clone https://github.com/greenman9909-cmd/vibe-code-genius
cd vibe-code-genius
python -m venv .venv
source .venv/bin/activate
pip install -e .
```

Install into an agent platform:

```bash
./install.sh --target cursor
# targets: claude, claude-project, claude-skill, custom-gpt,
#          gemini, antigravity, aider, continue, generic
```

The installer copies only the tree, contracts, schemas, and platform-specific entry files required by the selected target. It does not transmit credentials or create external accounts.

## First run

```bash
python scripts/validate-tree.py
python scripts/validate-structure.py
python tests/golden.py
python -m unittest discover -s tests -v

vibe-tree plan \
  --intent "Build a research dashboard for API teams" \
  --out .artifacts/session
```

Useful commands:

```bash
vibe-tree tree
vibe-tree debug on
vibe-tree debug off
vibe-tree stats
vibe-tree report-failure 13a --input '{"route":"/settings"}'
```

A plan creates `intent.json`, `scope.json`, `session.json`, and `plan.md`. A real agent integration then consumes the plan and writes the node artifacts in prerequisite order.

## How the tree works

1. **Foundation** defines intent, suitability, scope, budget, system model, reference inputs, coding style, file tree, manifest, and scaffold.
2. **Structure** defines API behavior, backend contracts, route maps, sections, design tokens, copy quality, design anti-patterns, and the design contract.
3. **Composition** creates reusable components, motion, pages, data fetching, forms, state, and static/runtime consistency checks.
4. **Product** adds database design, auth, security, edge states, hardening, tests, deployment, performance, and production readiness.
5. **Meta** coordinates parallel work, compares output to the reference, refines weak areas, runs the final ship gate, and repairs failed tools.

Every node has prerequisites, declared inputs and outputs, a model/budget hint, a schema, failure behavior, banned behaviors, and an example artifact. See `skill-tree.json` and `nodes/`.

## Contracts and quality gates

The contracts are normative, not advisory:

- `wiring-contract.md` rejects unresolved imports, routes, API calls, tokens, environment variables, i18n keys, and components.
- `integrity-contract.md` covers types, state, assets, promises, listeners, leaks, and accessibility.
- `hardening-contract.md` covers secrets, headers, auth, CSRF, input/output, CORS, dependencies, infrastructure, runtime, logging, cookies, external services, and build-time security.
- `completeness-contract.md` makes `system.json` and `manifest.json` the source of truth for scope.
- `consistency-contract.md` keeps pages on the same layout, token, component, and spacing system.
- `repair-contract.md` turns a verified failure into a regression case instead of silently changing behavior.

## Animation and motion customization

Motion is a first-class design contract, not a pile of local CSS values. Node `11e` emits `motion-customization.md` and `motion-config.json`, while node `12a` applies the motion layer.

Supported profiles:

| Profile | Behavior | Typical use |
|---|---|---|
| `instant` | Removes decorative travel and keeps state changes immediate | Dense tools and accessibility-first workflows |
| `restrained` | Short, quiet confirmation motion | Research, finance, and technical products |
| `precise` | Directional transitions explain hierarchy | Navigation-heavy applications |
| `energetic` | More visible reveals and gesture feedback | Consumer products and onboarding |
| `editorial` | Slower, intentional entrance rhythm | Storytelling and portfolio surfaces |

Customize `profile`, `intensity` from `0` to `1`, `reduced_motion.mode`, token durations, easing, spring stiffness/damping, and scoped component overrides. Every effect must have a stable state, cancellation behavior, keyboard behavior, and `prefers-reduced-motion` fallback.

See [`docs/animation-customization.md`](docs/animation-customization.md), [`references/motion-patterns.md`](references/motion-patterns.md), and [`schema/motion-config.schema.json`](schema/motion-config.schema.json).

## Reference library and asset sourcing

The repository includes 20 schema-valid, explicitly labeled **non-scraped fixtures** under `references/fixtures/{site}.json`, indexed in `references/index.json`, plus API, security, design, writing, motion, and trust references. Run `python scripts/validate-references.py` to validate the fixtures and any future scraped entries. Fixtures are examples and validation inputs; they are not claims that the referenced companies endorse this project and are never loaded as scraped evidence.

The visual direction of the documentation and examples takes inspiration from the public profile of [Debasish Ray](https://github.com/debasishray16): a terminal-oriented developer identity spanning Ubuntu/Debian, backend development, IoT, ML/DL, DevOps, Docker, Kubernetes, AWS, React, and Tailwind CSS. The profile is used as a source of aesthetic and topic cues, not as a copied brand identity. No profile image or personal asset is bundled without an explicit license or permission. See [`docs/assets-and-attribution.md`](docs/assets-and-attribution.md).

The optional anime pack in [`assets/anime/`](assets/anime/) contains `Beta.jpg` and `Solo-Leveling-PNG.png` sourced from the shared profile repository. They are preserved with attribution and checksums for themed demos and reference-led customization. Their source repository does not declare an image license, so obtain permission or verify a license before commercial redistribution.

## Testing and validation

```bash
python scripts/validate-tree.py
python scripts/validate-references.py
python scripts/validate-structure.py
python tests/golden.py
python -m unittest discover -s tests -v
grep -r "TODO\|STUB\|placeholder\|implement here" nodes/ vibe_code_genius/
```

The expected result is an acyclic tree, valid structure fixture, 3/3 golden checks, passing unit tests, and no forbidden stub markers in node or runtime code.

## Support and contribution

Open an issue with the smallest reproducible artifact and the exact validator output. Keep schema changes versioned, add golden coverage for behavior changes, and preserve evidence rather than replacing it with a confident guess.

Ko-fi placeholder: **https://ko-fi.com/YOUR_HANDLE**

## License

MIT. See [`LICENSE`](LICENSE).
