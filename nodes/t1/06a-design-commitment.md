# Node 06a — Design Commitment

Tier: 1  Prereqs: [06]  Parallel with: []  Input: prompt.md + intent.json + reference.json + design-tokens.json (optional) + references/aesthetic-directions.md  Output: design-commitment.md  Model: sonnet  Budget: 2500 tokens

## Working Contract

Read `contracts/working-contract.md`, `contracts/human-quality-contract.md`, and only the declared inputs. This node makes explicit design decisions before implementation; it does not browse for a fashionable style.

## Instructions

1. Read the product intent and prompt first. Identify the users, repeated tasks, information density, trust requirements, content type, and interaction model.
2. Read `reference.json`. If it is no-reference mode, treat that as absence of visual evidence rather than permission to invent reference facts.
3. Use `design-tokens.json` only when it already exists. If it does not exist, do not block or fabricate tokens.
4. Read `references/aesthetic-directions.md` as vocabulary, not a category-to-style lookup table. Choose or combine a direction only when it fits the product and available evidence.
5. When reference evidence exists, separate what is observed from what is a product decision. Preserve the useful hierarchy, density, spacing, typography attitude, motion attitude, and interaction grammar when the project calls for fidelity.
6. Define concrete rules for typography, color, grid, spacing, motion, iconography, elevation, radius, imagery, and copy. Avoid default generated-UI patterns unless the product/reference actually supports them.
7. Include accessibility commitments: readable contrast, keyboard/focus behavior, reduced motion, semantic hierarchy, and responsive behavior.
8. Include explicit anti-patterns that are specific to this product. Do not ban gradients, cards, glass, dark mode, or centered content merely because a detector flags them.
9. Produce `design-commitment.md` and validate it. Downstream Design Contract must consume this artifact.

## Output Contract

The document must satisfy `schema/design-commitment.schema.json` and contain the required commitment sections. Decisions must be specific enough that two independent implementers would converge on the same visual system.

Before marking complete:

python scripts/validate-artifact.py --node 06a --artifact design-commitment.md --schema schema/design-commitment.schema.json

## If this fails

If reference evidence is absent, base the commitment on the product intent and human-quality contract and record that explicitly. If evidence conflicts, document the conflict and chosen product decision. Do not invent typefaces, metrics, screenshots, brand rules, or reference behavior.
