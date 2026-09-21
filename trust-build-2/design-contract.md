# Design Contract Specification

## Normative Design Contract
This contract enforces absolute design consistency across all landing page routes and component implementations.

1. **Token Exclusivity**: No arbitrary CSS hex codes or pixel dimensions may be written in component markup. All values must resolve to semantic keys in `design-tokens.json`.
2. **Component Integrity**: Every visual card, form, and button must inherit base interactive states (default, hover, active, focus, disabled) defined in `design_system.json`.
3. **Contrast Verification**: All foreground text must achieve at least 4.5:1 contrast against its immediate parent surface background.
4. **Motion Discipline**: Animations must remain under 300ms duration with physical spring damping curves.

## Surface Invariance
The visual hierarchy consists of exactly three invariant elevation tiers:
- **Canvas Base Layer (`#0b0c0e`)**: Deep obsidian foundation hosting the interactive 2D graph and background grid lines.
- **Card Surface Layer (`#131418`)**: Elevated dark container surface with 1px border (`#22242a`) framing content blocks.
- **Active / Accent Highlights**:
  - **Electric Violet (`#a855f7`)**: Applied strictly to user-triggered interactive states, focus rings, and primary action buttons.
  - **Telemetry Emerald (`#22c55e`)**: Applied strictly to healthy service indicators, successful test passes, and deployment badges.
