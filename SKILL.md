# Vibe Code Genius

Load this skill once. Before Node 01 on a substantial build, scan `walkthroughs/README.md` and open only prior field reports relevant to the target, toolchain, or failure mode. Treat walkthroughs as operational experience, never as current evidence.

Read `contracts/working-contract.md`, `contracts/completeness-contract.md`, and `contracts/human-quality-contract.md` before implementation. Use `references/modern-web-guidance.md` when browser/platform decisions matter and `references/agent-engineering-2026.md` when coordinating automated or multi-agent work.

Start at node 01, follow prerequisites in `skill-tree.json`, persist every artifact, and stop at the requested tier. Prefer the executable runtime:
- `vibe-tree plan` creates the resumable session.
- `vibe-tree next` emits task packets only for nodes whose prerequisites validate.
- `vibe-tree status` derives workflow state from real artifacts.
- `vibe-tree run --executor <wrapper>` executes one validated node at a time through a provider-neutral agent wrapper.

Run validators after each write. Never mark a node complete because prose says it is done; artifact validation is the source of truth.

When a non-trivial run produces a reusable lesson, add a walkthrough. Do not promote a one-off lesson into a contract or global rule without repeated evidence and the required tests/versioning.

## Extracted design learning rule

When an approved acquisition path produces frontend code, CSS, markup, motion, or component structure, read `contracts/extracted-design-learning-contract.md` before design implementation. Analyze how the extracted design is built, record reusable patterns in the current run's design artifacts, and remix new functionality into that visual language instead of falling back to generic AI-generated UI.

A build is complete only when the declared scope is implemented and the final ship gate passes. Partial routes, dead interactions, generic fallback surfaces, unresolved placeholders, unverified integrations, inaccessible states, or evidence-free claims must remain explicitly incomplete or blocked.