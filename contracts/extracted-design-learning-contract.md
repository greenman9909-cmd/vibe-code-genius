# Extracted Design Learning Contract

Extracted code is design evidence and a learning source, not a shortcut to ship copied application code. When an approved acquisition path produces frontend code, styles, markup, motion, or component structure, the tree must study how the design works before implementation continues.

## Mandatory analysis

For every extracted frontend, analyze and record:

- layout composition, grid, alignment, whitespace, and information density;
- typography hierarchy, scale, weight, line-height, and text treatment;
- color roles, surfaces, borders, shadows, radii, glass/overlay behavior, and contrast;
- component boundaries, repetition, variants, states, and composition patterns;
- navigation, hierarchy, CTA placement, content ordering, and interaction affordances;
- responsive behavior across mobile, tablet, and desktop;
- motion timing, easing, sequencing, transitions, hover/focus behavior, and reduced-motion behavior;
- asset placement, image cropping, backdrop treatment, icons, and visual emphasis;
- loading, empty, error, auth, settings, profile, modal, and other utility states when present.

The analysis must explain not only what exists, but why the observed pattern works and how it should be adapted into the current product.

## Remix rule

When adding new features to a reference-led build, preserve and remix the extracted visual language. Authentication, profile, settings, library, admin, forms, dialogs, and new routes must look native to the existing product rather than like generic AI-generated UI.

Reuse or adapt existing primitives, spacing rhythm, typography hierarchy, surface treatment, responsive rules, and motion language. Do not introduce an unrelated dashboard shell, generic auth card, arbitrary gradients/glows, excessive rounded containers, or a second design system unless the product brief explicitly requires a redesign.

## Learning rule

Feed reusable design observations into the current run's design artifacts and walkthrough. A useful pattern may influence future strategy, but old extractions remain operational experience rather than current evidence. Reacquire evidence for each new target.

Repeated, verified design lessons may be promoted into references, validators, schemas, or contracts only with the repository's normal versioning and regression requirements.

## Shipping rule

A reference-led build cannot pass the ship gate while a declared route, state, interaction, integration, responsive surface, or design-critical flow is unfinished, replaced by a lazy generic fallback, or inconsistent with the approved design contract.

If a blocker prevents completion, report the blocker explicitly. Never relabel partial work as complete.
