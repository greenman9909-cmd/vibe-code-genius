# Technology Stack Decision Record

## Stack Fingerprint
- **Core Framework**: Next.js 14.2 with App Router architecture and React Server Components.
- **Client Hydration Strategy**: Islands architecture — static SSR for marketing narratives and selective client hydration for the interactive infrastructure canvas.
- **Language**: TypeScript 5.4 configured with `"strict": true` and `"noUncheckedIndexedAccess": true`.
- **CSS Architecture**: Tailwind CSS 3.4 with theme extensions for obsidian canvas backgrounds, card borders, and neon accent colors.
- **Vector Graphics & Motion**: Framer Motion 11.0 handling smooth panning, zooming, and dynamic cubic bezier connections.
- **Form Handling & State**: Zod v3 client-side and server-side validation schemas with native fetch submissions.

## Reference Profile
- **Target Reference**: https://railway.app
- **Architectural Parity**: Replicates the developer-first cloud infrastructure aesthetic featuring an infinite interactive canvas, dark surface cards, and monospace telemetry streams.
- **Performance Budget**: Target First Contentful Paint (FCP) < 0.8s, Cumulative Layout Shift (CLS) < 0.02, and zero uncompressed visual assets.
- **Deployment Target**: Edge-ready container execution on Railway with continuous delivery from GitHub.
