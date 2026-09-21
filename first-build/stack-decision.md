# Stack Fingerprint & Architecture Alignment

# Reference Profile (https://resend.com)
- **Framework & Rendering**: Next.js 14+ with App Router, React 18 Server Components (RSC) for zero-JS static marketing pages.
- **Styling Paradigm**: Tailwind CSS utilizing strict dark mode tokens, high-contrast monochrome `#000000` pitch black background, and zinc neutral borders.
- **Iconography & Visual Assets**: Lucide React iconography, custom SVG bento illustrations, and high-fidelity terminal code blocks.
- **Motion & Interactions**: Framer Motion spring physics with subtle hover translations and interactive live terminal emulator.
- **Edge Deployment**: Vercel Serverless / Edge runtime for high availability and sub-millisecond edge routing.

# Target Architecture Decisions
1. **Complete Parity with Reference**:
   - Replicate the exact typography hierarchy (Geist Sans / Inter paired with Geist Mono).
   - Enforce pure pitch black surfaces (`#000000`) without milky dark grays.
   - Implement border highlight glows with 1px subtle gradients (`#27272a`).
2. **Type Safety & Build Invariants**:
   - Strict TypeScript configuration (`strict: true`, `noImplicitAny: true`).
   - Zero external client-side state managers; React Server Components handle all marketing data rendering.
   - Form state managed with native React actions and Zod schema validations.
