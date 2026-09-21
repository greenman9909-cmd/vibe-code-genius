# BUILD PROMPT: VIBE CODE GENIUS LANDING PAGE

# REFERENCE STACK
- Next.js 14+ App Router, React 18 Server Components.
- Tailwind CSS with dark theme variables.
- Framer Motion spring physics.
- Vercel Edge runtime deployment.

# ROUTE MAP
- / : Homepage with live terminal and 9-contract bento grid.
- /pricing : Transparent tier comparisons (Hobby, Indie, Scale).
- /about : Mission, philosophy, and contract-driven determinism.
- /blog : Technical breakdowns, release notes, and tree guides.
- /contact : Support inquiry and enterprise lead capture form.
- /privacy : Default-deny data handling and telemetry policy.
- /terms : Terms of service, code ownership, and warranties.

# HOMEPAGE SECTIONS
1. Navbar with brand wordmark, route links, and primary CTA.
2. Hero section with bold heading and dual action buttons.
3. Terminal showcase with interactive contract execution emulator.
4. Contract bento grid detailing the 9 foundational invariants.
5. Tree visualizer displaying the 61-node topological graph.
6. Pricing teaser previewing developer tiers.
7. Waitlist signup form with real-time feedback.
8. Footer with ecosystem links, legal notices, and status badge.

# KEY COMPONENTS
- Navbar: Sticky dark backdrop blur with mobile drawer.
- TerminalShowcase: Simulated interactive CLI showing live node execution.
- ContractBento: Grid of 9 glassmorphic cards with subtle hover glow.
- TreeVisualizer: Hierarchical visualizer mapping Tiers 1 through 5.
- WaitlistForm: Validated client form dispatching to /api/waitlist.
- PricingMatrix: Feature comparison table with monthly/annual toggle.

# DESIGN TOKENS
- Canvas Background: #000000
- Card Background: #09090b
- Border Subtle: #27272a
- Border Highlight: #3f3f46
- Text Primary: #ffffff
- Text Muted: #a1a1aa

# API SURFACE
- POST /api/waitlist : Register early access lead.
- POST /api/contact : Submit developer inquiries.
- GET /api/health : System status probe.

# MY PRODUCT
- Vibe Code Genius: The contract-driven AI build orchestration tree that turns reference websites into hardened, verified applications.

# BUILD INSTRUCTIONS
- Scaffold app structure from ./first-build/scaffold/.
- Adhere strictly to design-tokens.json and design-contract.md.
- Validate incoming POST payloads with Zod schemas matching openapi.yaml.

# OUTPUT FORMAT
- Deliver complete, executable React Server Components and Route Handlers in strict TypeScript.
