# Completeness Contract

The tree builds a complete product within the declared scope, not a collection of convincing pages. `system.json` enumerates actors, journeys, routes, states, entities, and integrations before code. `manifest.json` is the checklist. Every node updates it.

Completion is binary for declared scope: complete or explicitly blocked. The ship gate fails while any required artifact, route, interaction, state, integration, responsive surface, or acceptance criterion remains pending, stubbed, dead, substituted with a generic fallback, or unverified. TODOs, placeholder implementations, knowingly broken buttons, and "finish later" paths cannot be relabeled as complete.

Architecture must support the declared auth, layouts, routes, fetching, tokens, components, persistence, error states, and responsive behavior without avoidable rework. When extracted design evidence exists, completion also requires consistency with `contracts/extracted-design-learning-contract.md`.

If an external blocker prevents completion, record it precisely and ship only with a blocked status; never hide unfinished work behind a success claim.
