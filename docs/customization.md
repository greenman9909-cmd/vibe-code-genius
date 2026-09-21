# Customization guide

The tree is intentionally configurable without changing node logic. Customize contracts, schemas, profiles, and integration adapters; keep orchestration behavior model-agnostic.

## Product defaults

Set the default deliverable, tier stop, route inclusion/exclusion, evidence policy, and budget in the session scope. The default scope is an MVP stopping at tier 3.

## Design tokens

Use `design-tokens.json` and `design-contract.md` as the only source for colors, type scale, spacing, radii, shadows, and approved animation. Components consume semantic names such as `color.surface.canvas` and `motion.duration.reveal`, not arbitrary hex values or one-off utility values.

## Motion

Use `motion-config.json` to set:

- `profile`: `instant`, `restrained`, `precise`, `energetic`, or `editorial`
- `intensity`: a number from `0` to `1`
- `reduced_motion.mode`: `replace`, `minimize`, or `off`
- duration, easing, distance, scale, opacity, spring stiffness, and damping tokens
- scoped component overrides that inherit the global profile

The motion system must preserve semantic state changes when motion is reduced. See `docs/animation-customization.md` for recipes and QA cases.

## Integration adapters

Add a new platform in `integrations/` without editing nodes. The adapter must explain installation, entry-file placement, artifact handoff, session persistence, and platform-specific constraints. Keep platform behavior out of model-agnostic node files.

## Tool replacement

Replace a tool when another tool produces the same contract artifact. Update the relevant `tools/{name}.md` file with invocation, input, output schema, fallback, and verification behavior. Do not couple consumers to an executable name.

## Schema extensions

Add a new versioned schema instead of silently changing a frozen contract. Include `$id`, `$defs`, strict properties, required fields, one fixture, and a validator test. Update `compatibility.json` when producers or consumers change.

## Debugging

Use `vibe-tree debug on` to write the state toggle, `scripts/stats.py` for failure trends, and `vibe-tree report-failure` for a reproducible case. Keep debug output out of production artifacts and do not log secrets, tokens, cookies, or PII.
