# Design Commitment Contract

# Visual Integrity Commitments
- **Surface Invariance**: Pitch black surface `#000000` must remain invariant across all routes, cards, dialogs, and navigation menus.
- **Elevation Layers**: Elevated card containers and bento sections strictly use `#09090b` (`bg-zinc-950`) with `#27272a` (`border-zinc-800`) borders.
- **Spacing Grid**: Spacing rhythm must strictly adhere to 4px and 8px increments (`p-4`, `p-6`, `p-8`, `gap-4`, `gap-6`).
- **Typography Scale**: High-contrast typography hierarchy utilizing tracking `-0.02em` on headings and monospace font for terminal commands and API payloads.
- **Token Discipline**: Zero arbitrary utility values or unapproved hex color codes in markup. Every style must link directly to the design tokens catalog.

# Accessibility Commitments
- **Contrast Ratios**: Body text contrast ratio exceeds 7:1 against the `#000000` black canvas, fully satisfying WCAG AAA standards. Secondary muted text exceeds 4.5:1 (WCAG AA).
- **Interactive Focus Indicators**: Visible, high-contrast focus rings on all interactive links, buttons, and form inputs (2px solid `#ffffff` with 2px offset).
- **Assistive Technology Support**: All buttons and form inputs include explicit `aria-label` or visible label bindings.
- **Motion Safety**: Full compliance with the `prefers-reduced-motion` media query; all Framer Motion springs and CSS transitions are eliminated when reduced motion is requested.
