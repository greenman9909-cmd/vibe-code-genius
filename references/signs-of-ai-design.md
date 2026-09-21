# Signs of AI Design — sourced anti-pattern registry

> This registry is generated from fetched public source registries. It preserves source attribution and does not claim the sources have the same rule count.

## Provenance and count reconciliation

| Source | Fetched source | Extracted rules | Requested count | Result |
|---|---|---:|---:|---|
| Impeccable — Skill 3.5.0 detector registry | https://raw.githubusercontent.com/pbakaus/impeccable/skill-v3.5.0/cli/engine/registry/antipatterns.mjs | 41 | 41 | matches |
| Design On anti-patterns | https://github.com/linkonai2026-kr/design-on/blob/main/vendor/impeccable/scripts/detector/registry/antipatterns.mjs | 60 | 59 | current source differs; all fetched rules retained |
| slop-detect | https://github.com/ravidsrk/slop-detect | 27 | 16 | current source differs; all fetched rules retained |
| deep-slop Next.js rules | https://github.com/DemumuMind/deep-slopDM/blob/149fcb04be8af79b75ba9e60ac074fc83f00c8b0/src/engines/framework-lint/rules.ts | 8 | 8 | matches |

The historical 41-rule Impeccable Skill 3.5.0 tag was used for the Impeccable source. The current Design On executable registry contains 60 rules although its documentation describes 59. The current slop-detect design catalogue contains 27 rules although the requested historical baseline is 16. Deep-slop contains 8 Next.js rules. These discrepancies are recorded rather than silently deleting source rules.

## Categorization

Rules are grouped into the requested categories: **colors**, **typography**, **layout**, **motion**, **copy**, and **imagery**. The category is an editorial index over the source rule; the source title, source path, and remediation wording remain visible below.

## Colors

### C001 — AI color palette
- **Source:** Impeccable — Skill 3.5.0 detector registry — `cli/engine/registry/antipatterns.mjs#ANTIPATTERNS — AI slop (ai-color-palette)`
- **Rule:** AI color palette
- **Fix:** Choose a distinctive, intentional palette.

### C002 — Cream / beige palette
- **Source:** Impeccable — Skill 3.5.0 detector registry — `cli/engine/registry/antipatterns.mjs#ANTIPATTERNS — AI slop (cream-palette)`
- **Rule:** Cream / beige palette
- **Fix:** Choose a background that comes from a deliberate palette, not the safe warm off-white.

### C003 — Dark mode with glowing accents
- **Source:** Impeccable — Skill 3.5.0 detector registry — `cli/engine/registry/antipatterns.mjs#ANTIPATTERNS — AI slop (dark-glow)`
- **Rule:** Dark mode with glowing accents
- **Fix:** Use subtle, purposeful lighting instead, or skip the dark theme entirely.

### C004 — Cramped padding
- **Source:** Impeccable — Skill 3.5.0 detector registry — `cli/engine/registry/antipatterns.mjs#ANTIPATTERNS — Quality (cramped-padding)`
- **Rule:** Cramped padding
- **Fix:** Add at least 8px, ideally 12–16px, of padding inside bordered, outlined, or colored containers.

### C005 — Hairline border with wide shadow
- **Source:** Impeccable — Skill 3.5.0 detector registry — `cli/engine/registry/antipatterns.mjs#ANTIPATTERNS — Provider tells (gpt-thin-border-wide-shadow)`
- **Rule:** Hairline border with wide shadow
- **Fix:** Commit to one: a defined edge or a soft elevation, rather than both at once.

### C006 — AI color palette
- **Source:** Design On anti-patterns — `vendor/impeccable/scripts/detector/registry/antipatterns.mjs — AI slop: tells that something was AI-generated`
- **Rule:** AI color palette
- **Fix:** Choose a distinctive, intentional palette.

### C007 — Cream / beige palette
- **Source:** Design On anti-patterns — `vendor/impeccable/scripts/detector/registry/antipatterns.mjs — AI slop: tells that something was AI-generated`
- **Rule:** Cream / beige palette
- **Fix:** Choose a background from a deliberate palette rather than a safe warm off-white.

### C008 — Glowing shadow accents
- **Source:** Design On anti-patterns — `vendor/impeccable/scripts/detector/registry/antipatterns.mjs — AI slop: tells that something was AI-generated`
- **Rule:** Glowing shadow accents
- **Fix:** Use neutral elevation shadows and subtle, purposeful lighting.

### C009 — Radial-gradient background halo
- **Source:** Design On anti-patterns — `vendor/impeccable/scripts/detector/registry/antipatterns.mjs — AI slop: tells that something was AI-generated`
- **Rule:** Radial-gradient background halo
- **Fix:** Ground the surface with a solid or subtly shifted background.

### C010 — Decorative radial spotlight glow
- **Source:** Design On anti-patterns — `vendor/impeccable/scripts/detector/registry/antipatterns.mjs — AI slop: tells that something was AI-generated`
- **Rule:** Decorative radial spotlight glow
- **Fix:** Let the surface stand on its own, or use a deliberate material accent rather than a floating colored haze.

### C011 — Cramped padding
- **Source:** Design On anti-patterns — `vendor/impeccable/scripts/detector/registry/antipatterns.mjs — Quality: general design and accessibility issues`
- **Rule:** Cramped padding
- **Fix:** Add at least 8px, ideally 12–16px, inside bordered, outlined, or colored containers.

### C012 — Color outside DESIGN.md
- **Source:** Design On anti-patterns — `vendor/impeccable/scripts/detector/registry/antipatterns.mjs — Quality: general design and accessibility issues`
- **Rule:** Color outside DESIGN.md
- **Fix:** Make the color an intentional design-system addition rather than accidental drift.

### C013 — Hairline border with wide shadow
- **Source:** Design On anti-patterns — `vendor/impeccable/scripts/detector/registry/antipatterns.mjs — Common generated-UI tells`
- **Rule:** Hairline border with wide shadow
- **Fix:** Commit to one: a defined edge or a soft elevation.

### C014 — Decorative grid-line background
- **Source:** Design On anti-patterns — `vendor/impeccable/scripts/detector/registry/antipatterns.mjs — Common generated-UI tells`
- **Rule:** Decorative grid-line background
- **Fix:** Reserve grid overlays for actual canvas, map, blueprint, or measurement surfaces; otherwise use product structure or a plain surface.

### C015 — VibeCode Purple — filled indigo/violet CTAs
- **Source:** slop-detect — `spec/patterns.md — ### purple_accent; packages/core/src/fixes.ts — purple_accent`
- **Rule:** VibeCode Purple — filled indigo/violet CTAs
- **Fix:** No #6366f1, #8b5cf6, or any HSL hue in 240–295° on filled CTAs.

### C016 — Gradient-heavy backgrounds (5+ elements)
- **Source:** slop-detect — `spec/patterns.md — ### gradient_backgrounds; packages/core/src/fixes.ts — gradient_backgrounds`
- **Rule:** Gradient-heavy backgrounds (5+ elements)
- **Fix:** ≤1 gradient element total on the page.

### C017 — Colored top/left card borders (the AI em-dash)
- **Source:** slop-detect — `spec/patterns.md — ### accent_stripe; packages/core/src/fixes.ts — accent_stripe`
- **Rule:** Colored top/left card borders (the AI em-dash)
- **Fix:** No `border-top: 4px solid <color>` or `border-left: 4px solid <color>` on cards.

### C018 — Big colored box-shadow glows (purple/blue/pink)
- **Source:** slop-detect — `spec/patterns.md — ### colored_glows; packages/core/src/fixes.ts — colored_glows`
- **Rule:** Big colored box-shadow glows (purple/blue/pink)
- **Fix:** No box-shadow with a saturated color (red/orange/yellow/green/blue/purple/pink). Greys only, ≤8% opacity.

### C019 — Aurora / mesh gradient blobs (blurred glowing backdrop)
- **Source:** slop-detect — `spec/patterns.md — ### aurora_mesh_gradient; packages/core/src/fixes.ts — aurora_mesh_gradient`
- **Rule:** Aurora / mesh gradient blobs (blurred glowing backdrop)
- **Fix:** No blurred radial/conic gradient blobs as decorative hero backdrop.

### C020 — Cream / beige default page background
- **Source:** slop-detect — `spec/patterns.md — ### cream_default_bg; packages/core/src/fixes.ts — cream_default_bg`
- **Rule:** Cream / beige default page background
- **Fix:** No unexamined warm off-white. If the background is cream, it must be a deliberate palette choice with a matching system.

## Typography

### T001 — Overused font
- **Source:** Impeccable — Skill 3.5.0 detector registry — `cli/engine/registry/antipatterns.mjs#ANTIPATTERNS — AI slop (overused-font)`
- **Rule:** Overused font
- **Fix:** Choose a face that gives your interface personality.

### T002 — Single font for everything
- **Source:** Impeccable — Skill 3.5.0 detector registry — `cli/engine/registry/antipatterns.mjs#ANTIPATTERNS — AI slop (single-font)`
- **Rule:** Single font for everything
- **Fix:** Pair a distinctive display font with a refined body font to create typographic hierarchy.

### T003 — Flat type hierarchy
- **Source:** Impeccable — Skill 3.5.0 detector registry — `cli/engine/registry/antipatterns.mjs#ANTIPATTERNS — AI slop (flat-type-hierarchy)`
- **Rule:** Flat type hierarchy
- **Fix:** Use fewer sizes with more contrast (aim for at least a 1.25 ratio between steps).

### T004 — Icon tile stacked above heading
- **Source:** Impeccable — Skill 3.5.0 detector registry — `cli/engine/registry/antipatterns.mjs#ANTIPATTERNS — AI slop (icon-tile-stack)`
- **Rule:** Icon tile stacked above heading
- **Fix:** Try a side-by-side icon and heading, or let the icon sit in flow without its own container.

### T005 — Hero eyebrow / pill chip
- **Source:** Impeccable — Skill 3.5.0 detector registry — `cli/engine/registry/antipatterns.mjs#ANTIPATTERNS — AI slop (hero-eyebrow-chip)`
- **Rule:** Hero eyebrow / pill chip
- **Fix:** Drop the eyebrow, integrate the kicker into the headline, or run it as a navigation breadcrumb instead.

### T006 — Crushed letter spacing
- **Source:** Impeccable — Skill 3.5.0 detector registry — `cli/engine/registry/antipatterns.mjs#ANTIPATTERNS — AI slop (extreme-negative-tracking)`
- **Rule:** Crushed letter spacing
- **Fix:** Tighten display type optically, not destructively.

### T007 — Skipped heading level
- **Source:** Impeccable — Skill 3.5.0 detector registry — `cli/engine/registry/antipatterns.mjs#ANTIPATTERNS — Quality (skipped-heading)`
- **Rule:** Skipped heading level
- **Fix:** Do not skip heading levels; preserve the document outline.

### T008 — Overused font
- **Source:** Design On anti-patterns — `vendor/impeccable/scripts/detector/registry/antipatterns.mjs — AI slop: tells that something was AI-generated`
- **Rule:** Overused font
- **Fix:** Choose a face that gives the interface personality.

### T009 — Single font without hierarchy
- **Source:** Design On anti-patterns — `vendor/impeccable/scripts/detector/registry/antipatterns.mjs — AI slop: tells that something was AI-generated`
- **Rule:** Single font without hierarchy
- **Fix:** Use weight and size contrast, or pair a distinctive display face with a refined body face.

### T010 — Flat type hierarchy
- **Source:** Design On anti-patterns — `vendor/impeccable/scripts/detector/registry/antipatterns.mjs — AI slop: tells that something was AI-generated`
- **Rule:** Flat type hierarchy
- **Fix:** Use fewer sizes with more contrast; aim for at least a 1.25 ratio between steps.

### T011 — Icon tile stacked above heading
- **Source:** Design On anti-patterns — `vendor/impeccable/scripts/detector/registry/antipatterns.mjs — AI slop: tells that something was AI-generated`
- **Rule:** Icon tile stacked above heading
- **Fix:** Place the icon and heading side by side, or leave the icon in flow without its own container.

### T012 — Hero eyebrow / pill chip
- **Source:** Design On anti-patterns — `vendor/impeccable/scripts/detector/registry/antipatterns.mjs — AI slop: tells that something was AI-generated`
- **Rule:** Hero eyebrow / pill chip
- **Fix:** Drop the eyebrow, integrate its content into the headline, or use it as a navigation breadcrumb.

### T013 — Crushed letter spacing
- **Source:** Design On anti-patterns — `vendor/impeccable/scripts/detector/registry/antipatterns.mjs — AI slop: tells that something was AI-generated`
- **Rule:** Crushed letter spacing
- **Fix:** Tighten display type optically, not destructively.

### T014 — Skipped heading level
- **Source:** Design On anti-patterns — `vendor/impeccable/scripts/detector/registry/antipatterns.mjs — Quality: general design and accessibility issues`
- **Rule:** Skipped heading level
- **Fix:** Do not skip heading levels in the document outline.

### T015 — Heading crowded against the previous block
- **Source:** Design On anti-patterns — `vendor/impeccable/scripts/detector/registry/antipatterns.mjs — Quality: general design and accessibility issues`
- **Rule:** Heading crowded against the previous block
- **Fix:** Open up the space above each heading so it exceeds the space below it.

### T016 — Font outside DESIGN.md
- **Source:** Design On anti-patterns — `vendor/impeccable/scripts/detector/registry/antipatterns.mjs — Quality: general design and accessibility issues`
- **Rule:** Font outside DESIGN.md
- **Fix:** Use the documented type system or update DESIGN.md for an intentional brand addition.

### T017 — Font size outside DESIGN.md
- **Source:** Design On anti-patterns — `vendor/impeccable/scripts/detector/registry/antipatterns.mjs — Quality: general design and accessibility issues`
- **Rule:** Font size outside DESIGN.md
- **Fix:** Use a documented size step or update the design system for an intentional new step.

### T018 — AI-default font stack (Inter / Geist / Space Grotesk)
- **Source:** slop-detect — `spec/patterns.md — ### slop_fonts; packages/core/src/fixes.ts — slop_fonts`
- **Rule:** AI-default font stack (Inter / Geist / Space Grotesk)
- **Fix:** If you can't name the foundry, don't ship the font. Inter/Geist/Space Grotesk are banned for this site.

### T019 — Eyebrow pill above hero ("Now in beta" / "New")
- **Source:** slop-detect — `spec/patterns.md — ### hero_eyebrow_pill; packages/core/src/fixes.ts — hero_eyebrow_pill`
- **Rule:** Eyebrow pill above hero ("Now in beta" / "New")
- **Fix:** No rounded pill (border-radius ≥ 999px) above the H1 unless it announces real, specific, dated news.

### T020 — Crushed letter-spacing on display type
- **Source:** slop-detect — `spec/patterns.md — ### crushed_tracking; packages/core/src/fixes.ts — crushed_tracking`
- **Rule:** Crushed letter-spacing on display type
- **Fix:** No letter-spacing tighter than -0.03em on display type. Characters must keep their own shapes.

### T021 — Oversized hero headline (long sentence at display size)
- **Source:** slop-detect — `spec/patterns.md — ### oversized_hero_h1; packages/core/src/fixes.ts — oversized_hero_h1`
- **Rule:** Oversized hero headline (long sentence at display size)
- **Fix:** A headline at ≥72px must be short. Long sentences (≥40 chars) get set at ≤60px.

### T022 — Flat type hierarchy (sizes too close together)
- **Source:** slop-detect — `spec/patterns.md — ### flat_type_hierarchy; packages/core/src/fixes.ts — flat_type_hierarchy`
- **Rule:** Flat type hierarchy (sizes too close together)
- **Fix:** Display-to-body size ratio must be ≥2×. No flat ladders of near-identical sizes.

## Layout

### L001 — Side-tab accent border
- **Source:** Impeccable — Skill 3.5.0 detector registry — `cli/engine/registry/antipatterns.mjs#ANTIPATTERNS — AI slop (side-tab)`
- **Rule:** Side-tab accent border
- **Fix:** Use a subtler accent or remove it entirely.

### L002 — Border accent on rounded element
- **Source:** Impeccable — Skill 3.5.0 detector registry — `cli/engine/registry/antipatterns.mjs#ANTIPATTERNS — AI slop (border-accent-on-rounded)`
- **Rule:** Border accent on rounded element
- **Fix:** Remove the border or the border-radius.

### L003 — Nested cards
- **Source:** Impeccable — Skill 3.5.0 detector registry — `cli/engine/registry/antipatterns.mjs#ANTIPATTERNS — AI slop (nested-cards)`
- **Rule:** Nested cards
- **Fix:** Flatten the hierarchy; use spacing, typography, and dividers instead of nesting containers.

### L004 — Monotonous spacing
- **Source:** Impeccable — Skill 3.5.0 detector registry — `cli/engine/registry/antipatterns.mjs#ANTIPATTERNS — AI slop (monotonous-spacing)`
- **Rule:** Monotonous spacing
- **Fix:** Use tight groupings for related items and generous separations between sections.

### L005 — Numbered section markers (01 / 02 / 03)
- **Source:** Impeccable — Skill 3.5.0 detector registry — `cli/engine/registry/antipatterns.mjs#ANTIPATTERNS — AI slop (numbered-section-markers)`
- **Rule:** Numbered section markers (01 / 02 / 03)
- **Fix:** Choose a different section cadence.

### L006 — Em-dash overuse
- **Source:** Impeccable — Skill 3.5.0 detector registry — `cli/engine/registry/antipatterns.mjs#ANTIPATTERNS — AI slop (em-dash-overuse)`
- **Rule:** Em-dash overuse
- **Fix:** Use commas, colons, periods, or parentheses instead.

### L007 — Marketing buzzword
- **Source:** Impeccable — Skill 3.5.0 detector registry — `cli/engine/registry/antipatterns.mjs#ANTIPATTERNS — AI slop (marketing-buzzword)`
- **Rule:** Marketing buzzword
- **Fix:** Pick a specific verb and noun that says what the product literally does.

### L008 — Positioned child clipped by overflow container
- **Source:** Impeccable — Skill 3.5.0 detector registry — `cli/engine/registry/antipatterns.mjs#ANTIPATTERNS — Quality (clipped-overflow-container)`
- **Rule:** Positioned child clipped by overflow container
- **Fix:** Let the overflow be visible, or move the positioned layer out of the clip.

### L009 — Side-tab accent border
- **Source:** Design On anti-patterns — `vendor/impeccable/scripts/detector/registry/antipatterns.mjs — AI slop: tells that something was AI-generated`
- **Rule:** Side-tab accent border
- **Fix:** Use a subtler accent or remove it entirely.

### L010 — Border accent on rounded element
- **Source:** Design On anti-patterns — `vendor/impeccable/scripts/detector/registry/antipatterns.mjs — AI slop: tells that something was AI-generated`
- **Rule:** Border accent on rounded element
- **Fix:** Remove the accent border or the border-radius.

### L011 — Nested cards
- **Source:** Design On anti-patterns — `vendor/impeccable/scripts/detector/registry/antipatterns.mjs — AI slop: tells that something was AI-generated`
- **Rule:** Nested cards
- **Fix:** Flatten the hierarchy with spacing, typography, and dividers rather than nested containers.

### L012 — Monotonous spacing
- **Source:** Design On anti-patterns — `vendor/impeccable/scripts/detector/registry/antipatterns.mjs — AI slop: tells that something was AI-generated`
- **Rule:** Monotonous spacing
- **Fix:** Use tight groupings for related items and generous separation between sections.

### L013 — Em-dash overuse
- **Source:** Design On anti-patterns — `vendor/impeccable/scripts/detector/registry/antipatterns.mjs — AI slop: tells that something was AI-generated`
- **Rule:** Em-dash overuse
- **Fix:** Prefer commas, colons, periods, or parentheses.

### L014 — Marketing buzzword
- **Source:** Design On anti-patterns — `vendor/impeccable/scripts/detector/registry/antipatterns.mjs — AI slop: tells that something was AI-generated`
- **Rule:** Marketing buzzword
- **Fix:** Use a specific verb and noun that literally describe what the product does.

### L015 — Uncaught script error on load
- **Source:** Design On anti-patterns — `vendor/impeccable/scripts/detector/registry/antipatterns.mjs — Quality: general design and accessibility issues`
- **Rule:** Uncaught script error on load
- **Fix:** Fix the error before judging anything else.

### L016 — Content invisible at rest
- **Source:** Design On anti-patterns — `vendor/impeccable/scripts/detector/registry/antipatterns.mjs — Quality: general design and accessibility issues`
- **Rule:** Content invisible at rest
- **Fix:** Make content visible by default and let JavaScript enhance its entrance rather than gate its existence.

### L017 — Cards flush against the scroller edge
- **Source:** Design On anti-patterns — `vendor/impeccable/scripts/detector/registry/antipatterns.mjs — Quality: general design and accessibility issues`
- **Rule:** Cards flush against the scroller edge
- **Fix:** Keep a consistent inset on both sides of the scroller or panel.

### L018 — One column stretches the first viewport
- **Source:** Design On anti-patterns — `vendor/impeccable/scripts/detector/registry/antipatterns.mjs — Quality: general design and accessibility issues`
- **Rule:** One column stretches the first viewport
- **Fix:** Balance the columns, cap the tall one, or flow long content below the opening row.

### L019 — Positioned child clipped by overflow container
- **Source:** Design On anti-patterns — `vendor/impeccable/scripts/detector/registry/antipatterns.mjs — Quality: general design and accessibility issues`
- **Rule:** Positioned child clipped by overflow container
- **Fix:** Let overflow be visible, or move the positioned layer out of the clipping container.

### L020 — Radius outside DESIGN.md
- **Source:** Design On anti-patterns — `vendor/impeccable/scripts/detector/registry/antipatterns.mjs — Quality: general design and accessibility issues`
- **Rule:** Radius outside DESIGN.md
- **Fix:** Use a documented radius token or update the design system for an intentional new shape.

### L021 — Glassmorphism (backdrop-filter blur on translucent layers)
- **Source:** slop-detect — `spec/patterns.md — ### glassmorphism; packages/core/src/fixes.ts — glassmorphism`
- **Rule:** Glassmorphism (backdrop-filter blur on translucent layers)
- **Fix:** No `backdrop-filter: blur()` anywhere on the page.

### L022 — Numbered "1 · 2 · 3" step sequences
- **Source:** slop-detect — `spec/patterns.md — ### numbered_steps; packages/core/src/fixes.ts — numbered_steps`
- **Rule:** Numbered "1 · 2 · 3" step sequences
- **Fix:** No numbered steps section with generic verbs like 'Sign up / Connect / Get started'. If you keep numbered steps, each must include a real product screenshot.

### L023 — Big-number stat banner ("10k+", "99.9%", "$2M+")
- **Source:** slop-detect — `spec/patterns.md — ### stat_banner; packages/core/src/fixes.ts — stat_banner`
- **Rule:** Big-number stat banner ("10k+", "99.9%", "$2M+")
- **Fix:** No big-number stat banner unless every stat is backed by a verifiable source on the page or one click away.

### L024 — FAQ accordion in the lower half
- **Source:** slop-detect — `spec/patterns.md — ### faq_accordion; packages/core/src/fixes.ts — faq_accordion`
- **Rule:** FAQ accordion in the lower half
- **Fix:** FAQ section may exist only if every question is one a real user has actually asked, and the section has ≤5 entries.

### L025 — Bento-grid wall — mixed-span rounded card grid
- **Source:** slop-detect — `spec/patterns.md — ### bento_grid; packages/core/src/fixes.ts — bento_grid`
- **Rule:** Bento-grid wall — mixed-span rounded card grid
- **Fix:** No mixed-span rounded-card 'bento' wall unless each span maps to real content priority.

### L026 — Cards nested inside cards
- **Source:** slop-detect — `spec/patterns.md — ### nested_cards; packages/core/src/fixes.ts — nested_cards`
- **Rule:** Cards nested inside cards
- **Fix:** No card-like container inside another card-like container. One level of elevation, max.

### L027 — Misplaced 'use client' directive
- **Source:** deep-slop Next.js rules — `src/engines/framework-lint/rules.ts:7-24 (§ Next.js Rules; nextjs/misplaced-use-client)`
- **Rule:** Misplaced 'use client' directive
- **Fix:** Remove 'use client' when the file contains only server-safe code.

### L028 — Missing 'use client' directive
- **Source:** deep-slop Next.js rules — `src/engines/framework-lint/rules.ts:26-52 (§ Next.js Rules; nextjs/missing-use-client)`
- **Rule:** Missing 'use client' directive
- **Fix:** Add 'use client' at the top of the file when it uses React hooks or event handlers.

### L029 — Pages Router function in an App Router project
- **Source:** deep-slop Next.js rules — `src/engines/framework-lint/rules.ts:54-73 (§ Next.js Rules; nextjs/pages-router-in-app)`
- **Rule:** Pages Router function in an App Router project
- **Fix:** Replace getServerSideProps/getStaticProps/getStaticPaths with fetch in Server Components or 'use server' actions.

### L030 — next/router import in an App Router project
- **Source:** deep-slop Next.js rules — `src/engines/framework-lint/rules.ts:75-85 (§ Next.js Rules; nextjs/next-router-vs-navigation)`
- **Rule:** next/router import in an App Router project
- **Fix:** Use next/navigation hooks—useRouter, usePathname, or useSearchParams—instead of next/router.

### L031 — Metadata export in a client component
- **Source:** deep-slop Next.js rules — `src/engines/framework-lint/rules.ts:108-125 (§ Next.js Rules; nextjs/metadata-in-client)`
- **Rule:** Metadata export in a client component
- **Fix:** Move metadata or generateMetadata to a separate Server Component file without 'use client'.

### L032 — Hardcoded environment URL
- **Source:** deep-slop Next.js rules — `src/engines/framework-lint/rules.ts:127-144 (§ Next.js Rules; nextjs/hardcoded-env)`
- **Rule:** Hardcoded environment URL
- **Fix:** Replace the hardcoded URL with process.env.NEXT_PUBLIC_API_URL or similar; use a non-NEXT_PUBLIC variable for server-only URLs.

## Motion

### M001 — Bounce or elastic easing
- **Source:** Impeccable — Skill 3.5.0 detector registry — `cli/engine/registry/antipatterns.mjs#ANTIPATTERNS — AI slop (bounce-easing)`
- **Rule:** Bounce or elastic easing
- **Fix:** Use exponential easing (ease-out-quart/quint/expo) instead.

### M002 — Layout property animation
- **Source:** Impeccable — Skill 3.5.0 detector registry — `cli/engine/registry/antipatterns.mjs#ANTIPATTERNS — Quality (layout-transition)`
- **Rule:** Layout property animation
- **Fix:** Use transform and opacity instead, or grid-template-rows for height animations.

### M003 — Bounce or elastic easing
- **Source:** Design On anti-patterns — `vendor/impeccable/scripts/detector/registry/antipatterns.mjs — AI slop: tells that something was AI-generated`
- **Rule:** Bounce or elastic easing
- **Fix:** Use exponential easing such as ease-out-quart, ease-out-quint, or ease-out-expo.

### M004 — Decorative blinking cursor
- **Source:** Design On anti-patterns — `vendor/impeccable/scripts/detector/registry/antipatterns.mjs — AI slop: tells that something was AI-generated`
- **Rule:** Decorative blinking cursor
- **Fix:** Limit carets to real editable fields; elsewhere let the composition hold attention without a fake prompt.

### M005 — Auto-scrolling marquee
- **Source:** Design On anti-patterns — `vendor/impeccable/scripts/detector/registry/antipatterns.mjs — AI slop: tells that something was AI-generated`
- **Rule:** Auto-scrolling marquee
- **Fix:** Reserve motion for changing content and let readers move at their own pace.

### M006 — Layout property animation
- **Source:** Design On anti-patterns — `vendor/impeccable/scripts/detector/registry/antipatterns.mjs — Quality: general design and accessibility issues`
- **Rule:** Layout property animation
- **Fix:** Use transform and opacity instead, or grid-template-rows for height animation.

## Copy

### C001 — Gradient text
- **Source:** Impeccable — Skill 3.5.0 detector registry — `cli/engine/registry/antipatterns.mjs#ANTIPATTERNS — AI slop (gradient-text)`
- **Rule:** Gradient text
- **Fix:** Use solid colors for text.

### C002 — Italic serif display headline
- **Source:** Impeccable — Skill 3.5.0 detector registry — `cli/engine/registry/antipatterns.mjs#ANTIPATTERNS — AI slop (italic-serif-display)`
- **Rule:** Italic serif display headline
- **Fix:** Set roman, or move to a non-serif display face; judge editorial or magazine contexts by context.

### C003 — Repeated section kicker labels
- **Source:** Impeccable — Skill 3.5.0 detector registry — `cli/engine/registry/antipatterns.mjs#ANTIPATTERNS — AI slop (repeated-section-kickers)`
- **Rule:** Repeated section kicker labels
- **Fix:** Replace them with stronger structure, artifacts, imagery, or a deliberate brand system.

### C004 — Aphoristic-cadence copy
- **Source:** Impeccable — Skill 3.5.0 detector registry — `cli/engine/registry/antipatterns.mjs#ANTIPATTERNS — AI slop (aphoristic-cadence)`
- **Rule:** Aphoristic-cadence copy
- **Fix:** Avoid repeated manufactured-contrast or short rebuttal-sentence patterns; once is fine.

### C005 — Oversized hero headline
- **Source:** Impeccable — Skill 3.5.0 detector registry — `cli/engine/registry/antipatterns.mjs#ANTIPATTERNS — AI slop (oversized-h1)`
- **Rule:** Oversized hero headline
- **Fix:** Set long headlines smaller, or tighten the copy.

### C006 — Gray text on colored background
- **Source:** Impeccable — Skill 3.5.0 detector registry — `cli/engine/registry/antipatterns.mjs#ANTIPATTERNS — Quality (gray-on-color)`
- **Rule:** Gray text on colored background
- **Fix:** Use a darker shade of the background color instead, or white/near-white for contrast.

### C007 — Low contrast text
- **Source:** Impeccable — Skill 3.5.0 detector registry — `cli/engine/registry/antipatterns.mjs#ANTIPATTERNS — Quality (low-contrast)`
- **Rule:** Low contrast text
- **Fix:** Increase the contrast between text and background.

### C008 — Line length too long
- **Source:** Impeccable — Skill 3.5.0 detector registry — `cli/engine/registry/antipatterns.mjs#ANTIPATTERNS — Quality (line-length)`
- **Rule:** Line length too long
- **Fix:** Add a max-width (65ch to 75ch) to text containers.

### C009 — Body text touching viewport edge
- **Source:** Impeccable — Skill 3.5.0 detector registry — `cli/engine/registry/antipatterns.mjs#ANTIPATTERNS — Quality (body-text-viewport-edge)`
- **Rule:** Body text touching viewport edge
- **Fix:** Wrap content in a container with at least 16px, ideally 24–32px, of horizontal padding, or apply max-width with mx-auto.

### C010 — Tight line height
- **Source:** Impeccable — Skill 3.5.0 detector registry — `cli/engine/registry/antipatterns.mjs#ANTIPATTERNS — Quality (tight-leading)`
- **Rule:** Tight line height
- **Fix:** Use 1.5 to 1.7 for body text so lines have room to breathe.

### C011 — Justified text
- **Source:** Impeccable — Skill 3.5.0 detector registry — `cli/engine/registry/antipatterns.mjs#ANTIPATTERNS — Quality (justified-text)`
- **Rule:** Justified text
- **Fix:** Use text-align: left for body text, or enable hyphens: auto if you must justify.

### C012 — Tiny body text
- **Source:** Impeccable — Skill 3.5.0 detector registry — `cli/engine/registry/antipatterns.mjs#ANTIPATTERNS — Quality (tiny-text)`
- **Rule:** Tiny body text
- **Fix:** Use at least 14px for body content; 16px is ideal.

### C013 — All-caps body text
- **Source:** Impeccable — Skill 3.5.0 detector registry — `cli/engine/registry/antipatterns.mjs#ANTIPATTERNS — Quality (all-caps-body)`
- **Rule:** All-caps body text
- **Fix:** Reserve uppercase for short labels and headings.

### C014 — Wide letter spacing on body text
- **Source:** Impeccable — Skill 3.5.0 detector registry — `cli/engine/registry/antipatterns.mjs#ANTIPATTERNS — Quality (wide-tracking)`
- **Rule:** Wide letter spacing on body text
- **Fix:** Reserve wide tracking for short uppercase labels only.

### C015 — Content overflowing its container
- **Source:** Impeccable — Skill 3.5.0 detector registry — `cli/engine/registry/antipatterns.mjs#ANTIPATTERNS — Quality (text-overflow)`
- **Rule:** Content overflowing its container
- **Fix:** Let text wrap, constrain widths, or give the region a deliberate scroll affordance.

### C016 — Repeating-gradient stripes
- **Source:** Impeccable — Skill 3.5.0 detector registry — `cli/engine/registry/antipatterns.mjs#ANTIPATTERNS — Provider tells (repeating-stripes-gradient)`
- **Rule:** Repeating-gradient stripes
- **Fix:** Reach for a deliberate texture or leave the surface plain.

### C017 — Theater framing copy
- **Source:** Impeccable — Skill 3.5.0 detector registry — `cli/engine/registry/antipatterns.mjs#ANTIPATTERNS — Provider tells (theater-slop-phrase)`
- **Rule:** Theater framing copy
- **Fix:** Say plainly what the thing does or does not do.

### C018 — Gradient text
- **Source:** Design On anti-patterns — `vendor/impeccable/scripts/detector/registry/antipatterns.mjs — AI slop: tells that something was AI-generated`
- **Rule:** Gradient text
- **Fix:** Use solid colors for text.

### C019 — Pulsing status dot
- **Source:** Design On anti-patterns — `vendor/impeccable/scripts/detector/registry/antipatterns.mjs — AI slop: tells that something was AI-generated`
- **Rule:** Pulsing status dot
- **Fix:** Reserve pulse for genuinely live data; use a static, clearly labelled indicator otherwise.

### C020 — Italic serif display headline
- **Source:** Design On anti-patterns — `vendor/impeccable/scripts/detector/registry/antipatterns.mjs — AI slop: tells that something was AI-generated`
- **Rule:** Italic serif display headline
- **Fix:** Set the headline in roman or move to a non-serif display face; judge editorial contexts by context.

### C021 — Kicker / eyebrow label above heading
- **Source:** Design On anti-patterns — `vendor/impeccable/scripts/detector/registry/antipatterns.mjs — AI slop: tells that something was AI-generated`
- **Rule:** Kicker / eyebrow label above heading
- **Fix:** Delete the label; put meaningful words in the heading or body copy.

### C022 — Tiny numbered section labels
- **Source:** Design On anti-patterns — `vendor/impeccable/scripts/detector/registry/antipatterns.mjs — AI slop: tells that something was AI-generated`
- **Rule:** Tiny numbered section labels
- **Fix:** Let hierarchy, content, and rhythm carry the sequence.

### C023 — Aphoristic-cadence copy
- **Source:** Design On anti-patterns — `vendor/impeccable/scripts/detector/registry/antipatterns.mjs — AI slop: tells that something was AI-generated`
- **Rule:** Aphoristic-cadence copy
- **Fix:** Avoid repeating manufactured-contrast or short-rebuttal copy patterns across sections.

### C024 — Oversized hero headline
- **Source:** Design On anti-patterns — `vendor/impeccable/scripts/detector/registry/antipatterns.mjs — AI slop: tells that something was AI-generated`
- **Rule:** Oversized hero headline
- **Fix:** Set long headlines smaller or tighten the copy.

### C025 — Text occluded by an overlapping element
- **Source:** Design On anti-patterns — `vendor/impeccable/scripts/detector/registry/antipatterns.mjs — Quality: general design and accessibility issues`
- **Rule:** Text occluded by an overlapping element
- **Fix:** Give overlapping layers room, or move the text out from beneath the upper layer.

### C026 — Gray text on colored background
- **Source:** Design On anti-patterns — `vendor/impeccable/scripts/detector/registry/antipatterns.mjs — Quality: general design and accessibility issues`
- **Rule:** Gray text on colored background
- **Fix:** Use a darker shade of the background color, or white or near-white for contrast.

### C027 — Low contrast text
- **Source:** Design On anti-patterns — `vendor/impeccable/scripts/detector/registry/antipatterns.mjs — Quality: general design and accessibility issues`
- **Rule:** Low contrast text
- **Fix:** Increase contrast between text and background to meet WCAG AA: 4.5:1 for body and 3:1 for large text.

### C028 — Line length too long
- **Source:** Design On anti-patterns — `vendor/impeccable/scripts/detector/registry/antipatterns.mjs — Quality: general design and accessibility issues`
- **Rule:** Line length too long
- **Fix:** Constrain text containers with a max-width of 65ch to 75ch.

### C029 — Body text touching viewport edge
- **Source:** Design On anti-patterns — `vendor/impeccable/scripts/detector/registry/antipatterns.mjs — Quality: general design and accessibility issues`
- **Rule:** Body text touching viewport edge
- **Fix:** Wrap content with at least 16px, ideally 24–32px, of horizontal padding.

### C030 — Tight line height
- **Source:** Design On anti-patterns — `vendor/impeccable/scripts/detector/registry/antipatterns.mjs — Quality: general design and accessibility issues`
- **Rule:** Tight line height
- **Fix:** Use line-height of 1.5 to 1.7 for body text.

### C031 — Justified text
- **Source:** Design On anti-patterns — `vendor/impeccable/scripts/detector/registry/antipatterns.mjs — Quality: general design and accessibility issues`
- **Rule:** Justified text
- **Fix:** Use left-aligned body text, or enable hyphens: auto when justification is necessary.

### C032 — Tiny body text
- **Source:** Design On anti-patterns — `vendor/impeccable/scripts/detector/registry/antipatterns.mjs — Quality: general design and accessibility issues`
- **Rule:** Tiny body text
- **Fix:** Use at least 14px for body content; 16px is ideal.

### C033 — Undersized functional text
- **Source:** Design On anti-patterns — `vendor/impeccable/scripts/detector/registry/antipatterns.mjs — Quality: general design and accessibility issues`
- **Rule:** Undersized functional text
- **Fix:** Keep interactive and content-bearing UI text at 11px or above; only non-interactive legal smallprint may use the softer 10px floor.

### C034 — All-caps body text
- **Source:** Design On anti-patterns — `vendor/impeccable/scripts/detector/registry/antipatterns.mjs — Quality: general design and accessibility issues`
- **Rule:** All-caps body text
- **Fix:** Reserve uppercase for short labels and headings.

### C035 — Wide letter spacing on body text
- **Source:** Design On anti-patterns — `vendor/impeccable/scripts/detector/registry/antipatterns.mjs — Quality: general design and accessibility issues`
- **Rule:** Wide letter spacing on body text
- **Fix:** Reserve wide tracking for short uppercase labels only.

### C036 — Content overflowing its container
- **Source:** Design On anti-patterns — `vendor/impeccable/scripts/detector/registry/antipatterns.mjs — Quality: general design and accessibility issues`
- **Rule:** Content overflowing its container
- **Fix:** Let text wrap, constrain widths, or provide a deliberate scroll affordance.

### C037 — Same text repeated inside one container
- **Source:** Design On anti-patterns — `vendor/impeccable/scripts/detector/registry/antipatterns.mjs — Quality: general design and accessibility issues`
- **Rule:** Same text repeated inside one container
- **Fix:** Say the text once, in the slot where it matters most.

### C038 — Repeating-gradient stripes
- **Source:** Design On anti-patterns — `vendor/impeccable/scripts/detector/registry/antipatterns.mjs — Common generated-UI tells`
- **Rule:** Repeating-gradient stripes
- **Fix:** Use a deliberate texture or leave the surface plain.

### C039 — Theater framing copy
- **Source:** Design On anti-patterns — `vendor/impeccable/scripts/detector/registry/antipatterns.mjs — Common generated-UI tells`
- **Rule:** Theater framing copy
- **Fix:** Say plainly what the thing does or does not do.

### C040 — Hero gradient text (background-clip:text)
- **Source:** slop-detect — `spec/patterns.md — ### gradient_text; packages/core/src/fixes.ts — gradient_text`
- **Rule:** Hero gradient text (background-clip:text)
- **Fix:** No `background-clip: text` on H1. The headline either earns attention through copy or it doesn't.

### C041 — Centered hero in generic sans (Inter-style)
- **Source:** slop-detect — `spec/patterns.md — ### centered_hero; packages/core/src/fixes.ts — centered_hero`
- **Rule:** Centered hero in generic sans (Inter-style)
- **Fix:** No `text-align: center` on the H1 + subhead + CTA stack.

### C042 — All-caps section labels (text-transform:uppercase)
- **Source:** slop-detect — `spec/patterns.md — ### all_caps_labels; packages/core/src/fixes.ts — all_caps_labels`
- **Rule:** All-caps section labels (text-transform:uppercase)
- **Fix:** No `text-transform: uppercase` with `letter-spacing` > 0 on section labels.

### C043 — Perma dark mode + medium-grey body text
- **Source:** slop-detect — `spec/patterns.md — ### perma_dark_mode; packages/core/src/fixes.ts — perma_dark_mode`
- **Rule:** Perma dark mode + medium-grey body text
- **Fix:** Body text on dark backgrounds must have L ≥ 0.85. No defaulting to dark — the user's system preference is the default.

### C044 — AI-sparkle badges (✨ / Sparkles "magic" tells)
- **Source:** slop-detect — `spec/patterns.md — ### ai_sparkle_badges; packages/core/src/fixes.ts — ai_sparkle_badges`
- **Rule:** AI-sparkle badges (✨ / Sparkles "magic" tells)
- **Fix:** No ✨/Sparkles glyph as an 'AI magic' label. Name the capability instead.

### C045 — Washed-out grey body text (below WCAG AA on a light background)
- **Source:** slop-detect — `spec/patterns.md — ### low_contrast_text; packages/core/src/fixes.ts — low_contrast_text`
- **Rule:** Washed-out grey body text (below WCAG AA on a light background)
- **Fix:** Every block of reading text must clear 4.5:1 (body) or 3:1 (large) against its real background. No exceptions for 'aesthetic' grey.

### C046 — Gray text on a colored background
- **Source:** slop-detect — `spec/patterns.md — ### gray_on_color; packages/core/src/fixes.ts — gray_on_color`
- **Rule:** Gray text on a colored background
- **Fix:** No neutral grey text on a chromatic background. Match the hue or use white.

### C047 — Wide letter-spacing on body text
- **Source:** slop-detect — `spec/patterns.md — ### wide_body_tracking; packages/core/src/fixes.ts — wide_body_tracking`
- **Rule:** Wide letter-spacing on body text
- **Fix:** No letter-spacing above 0.05em on body text. Tracking is for labels, not paragraphs.

### C048 — Link without descriptive text or aria-label
- **Source:** deep-slop Next.js rules — `src/engines/framework-lint/rules.ts:146-165 (§ Next.js Rules; nextjs/link-without-aria)`
- **Rule:** Link without descriptive text or aria-label
- **Fix:** Add descriptive text inside Link or add an aria-label prop.

## Imagery

### I001 — Broken or placeholder image
- **Source:** Impeccable — Skill 3.5.0 detector registry — `cli/engine/registry/antipatterns.mjs#ANTIPATTERNS — Quality (broken-image)`
- **Rule:** Broken or placeholder image
- **Fix:** Use real images, generated assets, or remove the tag.

### I002 — Image hover transform
- **Source:** Impeccable — Skill 3.5.0 detector registry — `cli/engine/registry/antipatterns.mjs#ANTIPATTERNS — Provider tells (image-hover-transform)`
- **Rule:** Image hover transform
- **Fix:** Let imagery sit still, or use a subtler, purposeful interaction.

### I003 — Shape-assembled illustration
- **Source:** Design On anti-patterns — `vendor/impeccable/scripts/detector/registry/antipatterns.mjs — AI slop: tells that something was AI-generated`
- **Rule:** Shape-assembled illustration
- **Fix:** Use real artwork, a photograph, or a deliberately drawn graphic for a hero-sized visual.

### I004 — Broken or placeholder image
- **Source:** Design On anti-patterns — `vendor/impeccable/scripts/detector/registry/antipatterns.mjs — AI slop: tells that something was AI-generated`
- **Rule:** Broken or placeholder image
- **Fix:** Use real images or generated assets, or remove the image tag.

### I005 — Image hover transform
- **Source:** Design On anti-patterns — `vendor/impeccable/scripts/detector/registry/antipatterns.mjs — Common generated-UI tells`
- **Rule:** Image hover transform
- **Fix:** Let imagery sit still, or use a subtler, purposeful interaction.

### I006 — Identical feature cards with icon on top
- **Source:** slop-detect — `spec/patterns.md — ### icon_card_grid; packages/core/src/fixes.ts — icon_card_grid`
- **Rule:** Identical feature cards with icon on top
- **Fix:** No grid of ≥3 sibling cards each with a top-aligned icon. If you have a feature grid, ≥1 card must contain a real product screenshot, not a generic icon.

### I007 — Gradient-letter avatars (testimonial slop)
- **Source:** slop-detect — `spec/patterns.md — ### gradient_letter_avatars; packages/core/src/fixes.ts — gradient_letter_avatars`
- **Rule:** Gradient-letter avatars (testimonial slop)
- **Fix:** No avatars showing initials on a gradient or solid colored background. Either real photos or no avatars.

### I008 — Image missing explicit dimensions
- **Source:** deep-slop Next.js rules — `src/engines/framework-lint/rules.ts:87-106 (§ Next.js Rules; nextjs/image-missing-dimensions)`
- **Rule:** Image missing explicit dimensions
- **Fix:** Add the missing width and/or height props, or use fill with a sized container for a responsive image.
