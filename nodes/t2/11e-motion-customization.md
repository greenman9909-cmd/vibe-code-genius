# Node 11e — Motion Customization

Tier: 2  Prereqs: [11d]  Parallel with: [12a, 12b]  Input: design-contract.md + motion requirements  Output: motion-customization.md + motion-config.json  Model: haiku  Budget: 2200 tokens

## Working Contract

Read `contracts/working-contract.md`, `contracts/consistency-contract.md`, and the declared design contract. Motion is a tokenized system, not a collection of ad-hoc effects. Every animation must have a purpose, a trigger, a duration, an easing curve, a reduced-motion behavior, and a verification state.

## Instructions

1. Establish the motion personality from the product intent: calm, precise, energetic, playful, editorial, or restrained.
2. Define motion tokens for duration, delay, easing, distance, scale, opacity, blur, spring stiffness, and damping.
3. Map tokens to interaction classes: hover, focus, press, toggle, reveal, route transition, modal, toast, skeleton, drag, and validation feedback.
4. Prefer transform and opacity; never animate layout-affecting properties when a composited alternative exists.
5. Define `prefers-reduced-motion: reduce` behavior for every token and every component. Replace non-essential movement with instant state changes or a short opacity transition.
6. Define interruption rules: a new state cancels or reverses the previous transition; repeated triggers do not accumulate timers or listeners.
7. Document customization knobs that a product team can change without editing components: `motion.profile`, `motion.intensity`, `motion.reduced`, and per-component overrides.
8. Specify visual QA cases at 375px, keyboard focus, touch, dark mode, slow device, and reduced motion.
9. Emit deterministic artifacts and validate `motion-config.json` against `schema/motion-config.schema.json`.

## Output Contract

`motion-customization.md` must include: motion personality, token table, interaction matrix, reduced-motion policy, interruption policy, customization API, implementation examples, and QA checklist. `motion-config.json` must have this shape:

```json
{
  "version": "1.0.0",
  "profile": "restrained",
  "intensity": 0.7,
  "reduced_motion": {"mode": "replace", "opacity_only": true},
  "tokens": {
    "hover_ms": 140,
    "reveal_ms": 360,
    "modal_ms": 460,
    "ease_standard": "cubic-bezier(0.2, 0.8, 0.2, 1)",
    "spring": {"stiffness": 400, "damping": 28}
  },
  "overrides": {},
  "evidence": []
}
```

Before marking complete: python scripts/validate-artifact.py motion-customization.md + motion-config.json schema/motion-config.schema.json. If validation fails, halt. Do not mark complete.










## If this fails



Log the node id, input hash, invocation, error, and minimal reproduction to `session.log`. Use datetime.utcnow().isoformat(timespec="microseconds") + "Z" (microseconds MUST vary between events). Apply the declared fallback in `contracts/repair-contract.md`; do not silently fabricate a result.


Do not use infinite decorative loops, cursor-following effects, bounce or elastic easing by default, layout animation for content changes, motion that blocks keyboard input, animation without reduced-motion behavior, or component-local magic numbers. Do not add a library solely for one effect.

## Example output

```md
## Motion personality
Restrained and precise: movement confirms state, exposes hierarchy, and never competes with content.

## Customization
- `motion.profile`: restrained | expressive | instant
- `motion.intensity`: 0..1 multiplier
- `motion.reduced`: replace | minimize | off
- Per-component overrides inherit tokens and remain schema-validated.

## QA
- Keyboard focus remains visible during transitions.
- Reduced motion removes travel and spring behavior.
- Repeated toast triggers clear the prior timer.
```
