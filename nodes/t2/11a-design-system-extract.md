# Node 11a — Design System Extract

Tier: 2  Prereqs: [02, 01d]  Parallel with: [11, 12]  Input: reference.json + system.json + rendered pages when available  Output: design_system.json  Model: sonnet  Budget: 3000 tokens

## Working Contract

Read `contracts/working-contract.md`, `contracts/human-quality-contract.md`, and `contracts/extracted-design-learning-contract.md`. Extract only what the available evidence supports. Clone artifacts are optional evidence, never a mandatory prerequisite.

## Instructions

1. Start with `reference.json` and `system.json`. Distinguish observed reference facts from product requirements.
2. If rendered pages, screenshots, DOM/CSS evidence, or a cached clone are available, inspect them. If `clone-manifest.json`, `clone-motion.json`, or `clone-components.json` exist, use them as additional evidence; do not require or fabricate them.
3. Record observed:
   - composition, grid, alignment, whitespace, density, and responsive changes;
   - typography hierarchy and text treatment;
   - color/surface/overlay/border/radius/shadow behavior;
   - repeated components, variants, states, and navigation patterns;
   - form, auth, settings, profile, loading, empty, error, and dialog treatment when evidence exists;
   - motion timing/easing/sequencing and reduced-motion implications.
4. Explain why each major pattern supports the product task or reference composition. Separate rationale from observation.
5. When there is no visual reference, derive a minimal product design system from `system.json` and the Human Quality Contract, mark the source as `product-derived`, and do not claim it was extracted.
6. When clone/reference evidence exists, mark the source accordingly and preserve provenance.
7. Do not force arbitrary counts of components, tokens, or keyframes. Static products may have zero keyframes; small products may have a small component vocabulary.
8. Produce `design_system.json` with evidence, source mode, tokens, components, motion/keyframes, and a non-empty `design_analysis` containing observed patterns, rationale, remix rules, and anti-patterns appropriate to the product.
9. Validate before completion.

## Output Contract

`design_system.json` must satisfy `schema/design_system.schema.json`. Every extracted claim must be traceable to current evidence; every product-derived rule must be labelled as a decision.

## If this fails

Record the missing evidence precisely. Fall back from clone/rendered evidence to normalized reference evidence, then to product-derived design guidance. Never invent CSS values, components, screenshots, or motion to satisfy the schema.
