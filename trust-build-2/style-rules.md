# Code Style and Design Rules

## Stack & Runtime
- **Framework**: Next.js 14.2 App Router using React Server Components by default.
- **Client Boundaries**: Mark interactive UI elements (`use client`) strictly when requiring state, drag-and-drop gestures, or event listeners (e.g. `CanvasViewport.tsx`, `WaitlistForm.tsx`).
- **Language**: TypeScript 5.4 in strict mode (`"strict": true`, no `any` types).
- **Styling**: Tailwind CSS with semantic design tokens defined in `tailwind.config.js`.

## Aesthetic & Color Tokens
- **Background**: High-contrast obsidian canvas (`#0b0c0e`).
- **Cards & Surfaces**: Dark elevated panel (`#131418`) with subtle border separation (`#22242a`).
- **Primary Accent**: Electric Neon Violet (`#a855f7`) for primary call-to-actions and active state indicators.
- **Secondary Accent**: Telemetry Emerald (`#22c55e`) for health probes, live status pills, and positive confirmations.
- **Typography**: Geist Sans for interface layout, Geist Mono for code snippets, telemetry streams, and CLI logs.

## Contract Guarantees
- **Working Contract**: Zero orphaned files; all imported modules must resolve cleanly during compile.
- **Wiring Contract**: All network requests must target declared route handlers matching the OpenAPI specification.
- **Integrity Contract**: Strictly avoid hallucinated metrics, unverified testimonials, or placeholder lorem ipsum copy.
- **Hardening Contract**: Strict input sanitation using Zod schemas; default-deny CORS and Content Security Policy headers.
