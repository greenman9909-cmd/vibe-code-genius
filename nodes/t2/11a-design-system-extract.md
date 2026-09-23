# Node 11a — Design System Extract

Tier: 2  Prereqs: 11f  Parallel with: —  Input: clone/  Output: design_system.json  Model: sonnet  Budget: 3000

## Working Contract

Read `contracts/working-contract.md` and the declared input only. Emit the exact declared artifact, validate it against its schema, and update the manifest. Keep evidence separate from inference.

## Instructions

1. Read `clone-manifest.json` for the file list.
2. Parse every `*.css` file for:
   - CSS custom properties in `:root` declarations
   - Color values: hex, rgb, hsl, and oklch
   - `font-family` declarations
   - `border-radius` values
   - `box-shadow` values
   - Spacing patterns in margin and padding
3. Read `clone-motion.json` for animation and transition data.
4. Read `clone-components.json` for the component inventory.
5. For each component in the inventory, note:
   - Its source file path in the clone
   - The count of occurrences in CSS, representing how many classes it likely has
6. Read `contracts/extracted-design-learning-contract.md`. Analyze the extracted frontend as a design system, not just a token dump. Record:
   - composition, grid, alignment, whitespace, and information density;
   - typography hierarchy and text treatment;
   - surface, border, radius, shadow, overlay, and contrast patterns;
   - component composition, variants, states, and repeated interaction patterns;
   - navigation hierarchy, CTA placement, and content ordering;
   - responsive behavior and density changes across breakpoints;
   - motion timing, easing, sequencing, hover/focus behavior, and reduced-motion implications;
   - how utility surfaces such as auth, settings, profile, forms, dialogs, loading, empty, and error states inherit the same language when evidence exists.
   For each major pattern, explain why it works and how new product features should remix it without introducing a second, generic design system.
7. Emit `design_system.json` with the extracted evidence plus a `design_analysis` object containing `patterns`, `rationale`, `remix_rules`, and `anti_patterns`:

   ```json
   {
     "tokens": {
       "colors": {},
       "fonts": {},
       "spacing": [],
       "radii": [],
       "shadows": []
     },
     "motion": "<contents of clone-motion.json>",
     "components": "<contents of clone-components.json>",
     "source": "clone-extracted"
   }
   ```

8. Mark complete. Announce unlocked: 11b, 11c, 11d.

## Output Contract

The output is `design_system.json`. It must contain the extracted design evidence and a non-empty `design_analysis` section that explains the observed patterns, why they work, how they should be remixed, and which generic fallback patterns would violate the reference language. Preserve `source: "clone-extracted"`. Validate it against `schema/design_system.schema.json` when present before marking complete.

## If this fails

Log the node id, input hash, invocation, error, and minimal reproduction to `session.log`. Apply the declared fallback in `contracts/repair-contract.md`; do not silently fabricate a result.

## Do not

Do not invent design evidence, modify the clone, or substitute category-based assumptions for values that can be extracted from the clone. Do not stop at colors and tokens when real component/layout code is available. Do not design new auth, profile, settings, library, admin, form, or utility surfaces as generic AI UI when the extracted system provides patterns that can be remixed.
