# Aesthetic Directions Registry

This registry gives Node 06a an explicit visual point of view. Exemplars are real public sites used as directional references, not claims of endorsement or permission to copy their content.

## 1. Terminal / Brutalist

- **Name:** Terminal / Brutalist
- **Summary:** Dense, confident, systems-oriented interfaces with visible structure and very little decoration.
- **Real exemplars:** [linear.app](https://linear.app), [vercel.com](https://vercel.com), [railway.app](https://railway.app)
- **Typography:** Monospace accents such as JetBrains Mono or IBM Plex Mono, paired with tight sans headings such as Inter Tight or Geist; no serif.
- **Color strategy:** Monochrome base with one accent, often neutral or single-saturated.
- **Layout grid:** 12-column grid, dense composition, high information per screen, explicit alignment.
- **Motion attitude:** Minimal and functional; transitions confirm state or explain hierarchy.
- **Icon policy:** Line-only icons, used only when they carry meaning.
- **When it works:** Developer tools, infrastructure, APIs, agents, DevOps, observability, and technical workflows.
- **When it fails:** Consumer products, publications, hospitality, and anything that needs warmth or emotional softness.
- **What wrong looks like:** Gradient text on headings, decorative icons, loose sans headings, oversized hero images, vague marketing copy, or fake terminal decoration.

## 2. Editorial / Magazine

- **Name:** Editorial / Magazine
- **Summary:** Typographic hierarchy, deliberate pacing, and generous whitespace that make reading feel authored.
- **Real exemplars:** [Stripe press](https://stripe.com/newsroom), [anthropic.com](https://www.anthropic.com), [resend.com](https://resend.com)
- **Typography:** Serif display faces such as Tiempos, GT Sectra, or Freight Display paired with a clean sans body face.
- **Color strategy:** Warm neutrals, one strong ink color, and restrained accents.
- **Layout grid:** Editorial columns, generous whitespace, strong measure control, and visible typographic hierarchy.
- **Motion attitude:** None or one elegant reveal; motion must not interrupt reading.
- **Icon policy:** Avoid icons; typography and image selection carry the design.
- **When it works:** Publications, long-form products, research, cultural work, premium positioning, and narrative brands.
- **When it fails:** Dashboards, dense tools, operations consoles, and workflows where scanning speed matters.
- **What wrong looks like:** Fake serifs, columns broken without reason, ornament without purpose, generic sans-only typography, or decorative pull quotes that do not add meaning.

## 3. Warm Humanist

- **Name:** Warm Humanist
- **Summary:** Approachable, calm product surfaces that use softness and rhythm to make collaboration feel easy.
- **Real exemplars:** [notion.so](https://www.notion.so), [cal.com](https://cal.com), [cron.com](https://cron.com)
- **Typography:** Humanist sans such as Söhne, Inter, or Untitled Sans, with an occasional handwritten accent used sparingly for flavor.
- **Color strategy:** Soft neutrals, warm grays, and one soft accent such as peach, sage, or dust.
- **Layout grid:** Rounded cards, breathing room, generous line-height, and clear grouping.
- **Motion attitude:** Gentle transitions, spring-based, low velocity, and never attention-seeking.
- **Icon policy:** Rounded line icons and playful illustrations where they clarify a task.
- **When it works:** Consumer SaaS, productivity, community, collaboration, education, and personal organization.
- **When it fails:** Hardcore developer tools, infrastructure products, security consoles, and latency-sensitive operations.
- **What wrong looks like:** Purple gradients, glassmorphism, techy language, harsh shadows, brutalist corners, or a fake warmth created only by beige backgrounds.

## 4. Playful / Bold

- **Name:** Playful / Bold
- **Summary:** High-energy visual systems that use contrast, collision, and personality to make the brand memorable.
- **Real exemplars:** [figma.com](https://www.figma.com), [posthog.com](https://posthog.com), [framer.com](https://www.framer.com)
- **Typography:** Display sans with personality such as Tobias, Migra, or Diatype, or a chunky geometric family with deliberate contrast.
- **Color strategy:** Saturated, multi-hue, high-energy palette with controlled contrast and an intentional dominant color.
- **Layout grid:** Asymmetric grids, oversized elements, deliberate collisions, and strong visual anchors.
- **Motion attitude:** Expressive, with page-cycling, anticipation, follow-through, and clear timing.
- **Icon policy:** Illustrative, custom, and full-color icons are allowed when they are part of the brand system.
- **When it works:** Creative tools, social products, communities, brand-forward marketing, events, and playful onboarding.
- **When it fails:** Enterprise, finance, security, compliance, healthcare, and anything trust-critical.
- **What wrong looks like:** Aggression without humor, clashing palettes, motion without purpose, random stickers, or illustration used as filler.

## 5. Minimal Utility

- **Name:** Minimal Utility
- **Summary:** Quiet, functional interfaces where hierarchy and content do the work and decoration is removed.
- **Real exemplars:** [tailwindcss.com](https://tailwindcss.com), [ui.shadcn.com](https://ui.shadcn.com), [supabase.com/docs](https://supabase.com/docs)
- **Typography:** One sans family throughout with a tight, explicit hierarchy.
- **Color strategy:** Near-monochrome, with accents reserved for links, states, and actionable feedback.
- **Layout grid:** Utility grid, functional density, clear alignment, and no decoration without purpose.
- **Motion attitude:** None by default; use only short state confirmation where it improves comprehension.
- **Icon policy:** Small line icons only, and only when functional.
- **When it works:** Documentation, component libraries, utilities, CLIs, developer references, and technical education.
- **When it fails:** Marketing-forward products, brand-conscious SaaS, entertainment, and experiences where emotional expression is the product.
- **What wrong looks like:** Unnecessary color, decorative borders, code blocks used as ornament, filler illustrations, or a visual system so neutral that hierarchy disappears.

## Selection rule

Choose one primary direction before implementation. A product may borrow one secondary trait, but it must not become an unreviewed blend of all five. Record the chosen direction, evidence, tradeoffs, and banned direction-specific patterns in `design-commitment.md`.
