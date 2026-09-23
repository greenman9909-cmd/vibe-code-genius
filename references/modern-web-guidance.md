# Modern Web Guidance — current primary-source reference

Last reviewed: 2026-09-23

Primary sources:
- Chrome for Developers — Modern Web Guidance: https://developer.chrome.com/docs/modern-web-guidance
- Get started: https://developer.chrome.com/docs/modern-web-guidance/get-started
- Disciplines: https://developer.chrome.com/docs/modern-web-guidance/disciplines
- Use cases: https://developer.chrome.com/docs/modern-web-guidance/use-cases
- Chrome I/O 2026 web UI update: https://developer.chrome.com/blog/new-in-web-ui-io26
- web.dev accessibility: https://web.dev/accessibility
- Chrome accessibility course/video index: https://developer.chrome.com/docs/accessibility

## Reusable lessons

1. Set a browser/Baseline target before adopting a new platform feature. Newer is not automatically better.
2. Prefer native HTML/CSS primitives over custom JavaScript reimplementations when the target browsers support them and semantics/accessibility remain correct.
3. Accessibility is part of component behavior: focus management, error announcements, labels, keyboard interaction, contrast, document structure, and user preferences must be tested.
4. Use modern layout and interaction primitives (container queries, subgrid, dialog/popover/anchor positioning, view transitions, native validation states) when they simplify the implementation. Provide fallbacks where the chosen Baseline requires them.
5. Performance must be observed in the browser. Diagnose LCP, INP/long tasks, duplicated JavaScript, render-blocking work, image/font loading, and SPA navigations instead of guessing.
6. Natural motion should communicate state or hierarchy, respect reduced-motion preferences, and avoid blocking interactivity.
7. Keep real DOM semantics when building visually rich interfaces; visual novelty is not permission to discard searchability, accessibility, translation, or browser behavior.

## Promotion rule

These are reference-level heuristics. A project-specific reference, compatibility target, framework constraint, or measured result may override them. Experimental APIs must never be introduced merely because they are new.
