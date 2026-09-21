# Project File Tree Structure

## Project File Tree Overview
This document specifies the canonical directory layout for `vibe-code-genius` landing page implementation, adhering to Next.js 14 App Router standards.

## app/ Directory
The root routing folder contains server components and API route handlers:
- `app/layout.tsx`: Root HTML layout injecting Geist font family variables and global CSS.
- `app/page.tsx`: Root landing page showcasing interactive canvas hero and waitlist registration.
- `app/pricing/page.tsx`: Usage-based pricing calculator page with CPU/RAM estimation sliders.
- `app/about/page.tsx`: Architecture narrative and deterministic contract verification principles.
- `app/blog/page.tsx`: Technical engineering blog index with search and newsletter subscription.
- `app/contact/page.tsx`: Direct sales and enterprise support inquiry form with honeypot security.
- `app/api/waitlist/route.ts`: POST endpoint persisting early-access developer registrations.
- `app/api/contact/route.ts`: POST endpoint forwarding enterprise inquiries.
- `app/api/health/route.ts`: GET endpoint returning system health and uptime metrics.
- `app/globals.css`: Tailwind directives and custom CSS variables for obsidian surfaces.

## components/ Directory
Component primitives organized by domain:
- `components/navbar/Navbar.tsx`: Sticky frosted navbar with navigation links and waitlist CTA.
- `components/canvas/CanvasViewport.tsx`: Client-side infinite pan/zoom canvas container.
- `components/canvas/ServiceNodeCard.tsx`: Draggable microservice card with telemetry status badge.
- `components/canvas/WireConnection.tsx`: SVG cubic bezier line connecting services.
- `components/pricing/ResourceCalculator.tsx`: Interactive dual-slider calculating compute costs.
- `components/marketing/TerminalDock.tsx`: Monospace terminal dock streaming live build events.
- `components/marketing/ContractBento.tsx`: Bento grid explaining the 9 foundational contracts.
- `components/marketing/WaitlistForm.tsx`: Zod-validated waitlist email input form.
- `components/marketing/ContactForm.tsx`: Enterprise inquiry form with CSRF validation.
- `components/footer/Footer.tsx`: Semantic footer with multi-column links and copyright notice.
