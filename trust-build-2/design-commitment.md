# Design Commitments

## Visual Integrity Commitments
- **Palette Fidelity**: Maintain strict adherence to Railway-inspired obsidian surfaces (`#0b0c0e`), card backgrounds (`#131418`), and subtle boundary borders (`#22242a`).
- **Accent Precision**: Reserve Electric Violet (`#a855f7`) solely for primary interactive triggers, and Telemetry Emerald (`#22c55e`) for verified runtime states.
- **Canvas Spatial Hierarchy**: Ensure microservice cards maintain minimum 24px grid alignment with clear cubic bezier connection curves.
- **Typography Calibration**: Enforce Geist Sans for marketing narratives and Geist Mono for code blocks and logs without typeface mixing.

## Accessibility Commitments
- **WCAG 2.2 Level AA Compliance**: Maintain minimum 4.5:1 contrast ratios on all text elements against obsidian surfaces.
- **Keyboard Traversal**: Full focus outline indicators and logical tab index traversal across all canvas nodes, sliders, and form inputs.
- **Screen Reader Announcements**: Provide descriptive `aria-label` tags for interactive canvas wires, slider thumbs, and status indicators.
- **Reduced Motion Support**: Honor `prefers-reduced-motion` media queries by dampening canvas background transforms and particle animations.
