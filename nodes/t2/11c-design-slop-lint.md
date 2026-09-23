# Node 11c — Design Slop Lint

Tier: 2  Prereqs: [11]  Parallel with: [11d, 12]  Input: design tokens + references  Output: slop-lint.json  Model: haiku  Budget: 1500 tokens

## Working Contract

Read `contracts/working-contract.md`, `contracts/human-quality-contract.md`, and `references/signs-of-ai-design.md`. Emit only the declared artifact and keep evidence separate from judgment.

## Instructions

1. Audit only patterns that are actually present in the current design evidence or declared design direction.
2. Use the anti-pattern registry as a detector catalogue, not as a universal ban list. A dark theme, glass, cards, gradients, pills, centered copy, or motion can be valid when the product/reference clearly calls for it.
3. Record every source/registry actually consulted. `rules_checked` is the number genuinely evaluated, not a target quota.
4. For each violation record the surface, observable evidence, concrete fix, and any context exception. If a flagged pattern is intentional and well-supported, keep it and explain the exception.
5. Prioritize structural generated-UI tells: card soup, identical feature tiles, arbitrary rounded containers, decorative glow/gradient defaults, repeated eyebrow labels, weak hierarchy, random spacing, gratuitous animation, placeholder imagery, and design-system drift.
6. Check accessibility and product behavior together with aesthetics: focus, contrast, text scale, overflow, labels, reduced motion, responsive density, and meaningful states.
7. Do not mutate `prompt.md` or write a hidden companion file. Downstream nodes consume `slop-lint.json` and the design contract directly.
8. Validate `slop-lint.json` before completion.

## Output Contract

Before marking complete:

python scripts/validate-artifact.py --node 11c --artifact slop-lint.json --schema schema/slop-lint.schema.json

## If this fails

Record the exact detector/source failure and continue only through the declared fallback. Never invent violations, rule counts, screenshots, or tool output.