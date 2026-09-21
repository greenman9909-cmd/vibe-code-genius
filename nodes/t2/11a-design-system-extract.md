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
6. Emit `design_system.json`:

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

7. Mark complete. Announce unlocked: 11b, 11c, 11d.

## Output Contract

The output is `design_system.json`. It must contain the extracted `tokens`, the complete contents of `clone-motion.json` under `motion`, the complete contents of `clone-components.json` under `components`, and `source: "clone-extracted"`. Validate it against `schema/design_system.schema.json` when present before marking complete.

## If this fails

Log the node id, input hash, invocation, error, and minimal reproduction to `session.log`. Apply the declared fallback in `contracts/repair-contract.md`; do not silently fabricate a result.

## Do not

Do not invent design evidence, modify the clone, or substitute category-based assumptions for values that can be extracted from the clone.
