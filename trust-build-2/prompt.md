# Vibe Code Genius Build Prompt

## REFERENCE STACK
- Framework: Next.js 14.2 App Router (React Server Components)
- Language: TypeScript 5.4 in strict mode
- Styling: Tailwind CSS v3.4 with custom obsidian color tokens
- Icons: Lucide React
- Motion: Framer Motion 11.0 for interactive canvas pan/zoom and node wires

## ROUTE MAP
The implementation must build the following 5 public marketing routes:
- `/`: Landing page with interactive contract execution canvas hero, live build log dock, and waitlist registration form.
- `/pricing`: Transparent tier breakdown and resource slider calculator for orchestration runs.
- `/about`: Architecture narrative and deterministic contract verification principles.
- `/blog`: Engineering deep-dives on zero-drift orchestration patterns and telemetry pipelines.
- `/contact`: Enterprise inquiries and dedicated pilot request form with honeypot validation.

## HOMEPAGE SECTIONS
1. Navbar: Sticky frosted container with branding, route links, and primary violet CTA.
2. CanvasHero: Interactive infinite 2D canvas featuring connected build orchestration tree nodes and contract gates.
3. TerminalDock: Real-time autonomous tree execution log stream demonstrating sub-second contract validations.
4. ContractBento: Grid detailing the 9 foundational contracts governing zero-drift builds.
5. WaitlistSection: Zod-validated early access email registration for indie builders.
6. Footer: Navigation columns, open-source repo links, and legal notices.

## KEY COMPONENTS
- `CanvasViewport`: Infinite canvas pan/zoom viewport rendering reactive build orchestration nodes.
- `ServiceNodeCard`: Interactive contract node card displaying live validation status pills.
- `WireConnection`: Dynamic SVG cubic bezier line connecting orchestration steps.
- `TerminalDock`: Monospace typewriter stream simulating autonomous build stdout/stderr.
- `ResourceCalculator`: Dual-slider resource estimator for build pipelines.
- `WaitlistForm`: Client form submitting to `/api/waitlist` with optimistic status UI.
- `ContactForm`: Enterprise inquiry form with CSRF validation and spam mitigation.

## DESIGN TOKENS
- Canvas Background: `#0b0c0e`
- Surface / Cards: `#131418`
- Border Subtle: `#22242a`
- Border Active: `#353842`
- Accent Primary: Electric Violet (`#a855f7`)
- Accent Secondary: Telemetry Emerald (`#22c55e`)
- Text Primary: `#f8fafc`
- Text Secondary: `#94a3b8`
- Text Muted: `#64748b`
- Fonts: Geist Sans (primary UI), Geist Mono (code and terminals)

## API SURFACE
- `POST /api/waitlist`: Accepts `{ "email": string }`, returns `{ "position": number, "token": string }`.
- `POST /api/contact`: Accepts `{ "name": string, "email": string, "message": string }`, returns `{ "received": true }`.
- `GET /api/health`: Returns `{ "status": "ok", "uptime": number }`.

## MY PRODUCT
vibe-code-genius — a contract-driven AI build orchestration tree that turns a reference website into a complete, verified, hardened app. Target user: indie developers and small teams who use AI to build web products. The platform orchestrates 61 topological nodes across 5 tiers to ensure zero-drift execution, normative contract gates, and automated code generation.

## BANNED PATTERNS
- Purple gradient CTAs: bg-gradient-to-r from-purple-500 to-indigo-600 filled buttons: Use solid brand token colors or neutral high-contrast buttons
- Gradient text: text-transparent bg-clip-text on headlines: Use solid high-contrast text
- Arbitrary color utilities: bg-[#...] or text-[#...]: Use defined tokens from design-tokens.json
- Decorative emoji in UI: Sparkles or emoji in JSX headings and buttons: Replace with semantic SVG icons or remove
- Arbitrary border-radius: rounded-[...] outside token scale: Use token radii (sm: 4px, md: 8px, lg: 12px, full: 9999px)
- Hero eyebrow pill: 'Now in Beta' / 'New' pill badge above H1: Integrate version directly or remove decorative badge
- Monotonous icon card grid: 3+ cards with centered icon tile stacked over heading: Use asymmetric bento hierarchy or code/terminal artifact previews
- Fake stat banners: 99.9% uptime or 10k+ users without verifiable data: Show verifiable live metrics or omit claims

## BUILD INSTRUCTIONS
1. Initialize project dependencies defined in `scaffold/package.json`.
2. Configure Tailwind CSS color tokens matching `design-tokens.json`.
3. Implement route handlers under `app/api/` matching the OpenAPI contract.
4. Build UI components under `components/` ensuring React Server Component purity where possible.
5. Verify zero build warnings or lint errors under strict TypeScript checks.

## OUTPUT FORMAT
Provide the complete source code files with full implementations. Do not use placeholders, truncated blocks, or omitted methods.
