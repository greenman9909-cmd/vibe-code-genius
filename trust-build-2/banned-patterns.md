## BANNED PATTERNS
- Purple gradient CTAs: bg-gradient-to-r from-purple-500 to-indigo-600 filled buttons: Use solid brand token colors or neutral high-contrast buttons
- Gradient text: text-transparent bg-clip-text on headlines: Use solid high-contrast text
- Arbitrary color utilities: bg-[#...] or text-[#...]: Use defined tokens from design-tokens.json
- Decorative emoji in UI: Sparkles or emoji in JSX headings and buttons: Replace with semantic SVG icons or remove
- Arbitrary border-radius: rounded-[...] outside token scale: Use token radii (sm: 4px, md: 8px, lg: 12px, full: 9999px)
- Hero eyebrow pill: 'Now in Beta' / 'New' pill badge above H1: Integrate version directly or remove decorative badge
- Monotonous icon card grid: 3+ cards with centered icon tile stacked over heading: Use asymmetric bento hierarchy or code/terminal artifact previews
- Fake stat banners: 99.9% uptime or 10k+ users without verifiable data: Show verifiable live metrics or omit claims
