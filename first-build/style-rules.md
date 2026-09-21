# Stack & Runtime Rules

## 1. Stack & Runtime
- **Framework**: Next.js 14+ with App Router (RSC by default, client components only when required).
- **TypeScript**: Version 5.4+ in strict mode with noImplicitAny, strictNullChecks.
- **Styling**: Tailwind CSS with CSS variables mapped to design tokens.

# Aesthetic & Color Tokens
- Canvas Surface: Pitch Black `#000000` (`bg-black`).
- Elevated Containers: Dark Zinc `#09090b` (`bg-zinc-950`).
- Subtle Borders: 1px Solid `#27272a` (`border-zinc-800`), hover `#3f3f46`.
- Typography Scale: Geist Sans / Inter for body, Geist Mono / JetBrains Mono for code.

# Contract Guarantees
- Zero arbitrary utility classes or unapproved hex values in markup.
- WCAG AAA contrast ratio compliance (>= 7:1) across body copy.
- Unconditional fallback for prefers-reduced-motion media query.
