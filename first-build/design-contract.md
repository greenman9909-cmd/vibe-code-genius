# Normative Design Contract

# Surface Invariance
- The root canvas background is invariant at pure `#000000`.
- Card components, terminal wrappers, and dialog panels are invariant at `#09090b`.
- Dividers and structural borders strictly evaluate to 1px solid `#27272a`.
- Gradient fills are strictly banned across all layouts; subtle gradients are permitted exclusively for 1px border highlight pseudo-elements and terminal glow effects.

## Typography Laws
- Primary sans-serif font family: Geist Sans or Inter.
- Monospace font family: Geist Mono or JetBrains Mono, strictly reserved for code blocks, terminal emulator, cryptographic hashes, and HTTP endpoints.
- Heading letter tracking locked to `-0.02em` to `-0.03em` for crisp modern developer aesthetic.
- Text sizes bound to modular typographic scale: 12px (caption), 14px (body-sm), 16px (body), 20px (h4), 24px (h3), 32px (h2), 48px (h1).

## Motion Restraint
- Maximum transition duration capped at 250ms for micro-interactions.
- Spring animations calibrated to `cubic-bezier(0.16, 1, 0.3, 1)` to eliminate bounce slop.
- Animated elements must unconditionally respect `prefers-reduced-motion: reduce`.
