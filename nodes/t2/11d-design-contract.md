# Node 11d — Design Contract

Tier: 2  Prereqs: [06a, 11, 11a, 11c]  Parallel with: [12, 13, 12b]  Input: design commitment + design system + design tokens + slop lint  Output: design-contract.md  Model: sonnet  Budget: 2200 tokens

## Working Contract

Read `contracts/working-contract.md` and `contracts/human-quality-contract.md`. Reconcile the declared design commitment, extracted/product-derived system, tokens, and contextual slop findings into one implementation contract.

## Instructions

1. Verify all prerequisite artifacts and identify conflicts between commitment, observed reference evidence, tokens, and lint findings.
2. Resolve conflicts explicitly: reference fidelity and product usability outrank generic detector preferences; accessibility and declared user requirements may override visual mimicry.
3. Specify implementation rules for layout, typography, spacing, color, surfaces, states, responsive behavior, imagery, motion, focus, and reduced motion.
4. Turn only relevant lint findings into banned patterns. A detector rule is not automatically a global prohibition.
5. Define allowed exceptions with evidence. For example, gradients, glass, pills, dark mode, or rounded containers may remain when they are part of the reference/product language and pass accessibility checks.
6. Define how new routes and utility surfaces inherit the same design language so they do not collapse into generic dashboard/auth-card UI.
7. Do not require a second undeclared output. If a project wants executable lint rules, a later tooling step may compile this contract into project-specific lint configuration.
8. Produce and validate `design-contract.md`.

## Output Contract

The declared output is only `design-contract.md`; it must satisfy `schema/design-contract.schema.json` and be concrete enough to review implementation drift.

Before marking complete:

python scripts/validate-artifact.py --node 11d --artifact design-contract.md --schema schema/design-contract.schema.json

## If this fails

Record the conflicting evidence or missing prerequisite. Do not resolve ambiguity by banning whole classes of visual patterns or by inventing a second design system.
