# Motion patterns

Motion is a product token system. Use 100–150ms ease-out for hover, 200–250ms ease-in-out for toggles, 300–400ms spring-like reveals, and 400–600ms modal transitions only when the product needs spatial context. Default spring profile: snappy 400/28; smooth 200/25.

Every pattern requires a static state, visible focus, cancellation behavior, and `prefers-reduced-motion` coverage. Animate transform and opacity before layout. Avoid perpetual loops, bounce defaults, scroll-jacking, cursor trails, and motion that delays task completion.

## Customization contract

Product teams may set a profile, a 0–1 intensity multiplier, a reduced-motion mode, and scoped component overrides. Components consume classes or CSS custom properties from the motion contract; they do not invent local durations.
