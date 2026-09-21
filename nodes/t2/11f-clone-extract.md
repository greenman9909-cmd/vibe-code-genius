# Node 11f — Clone Extract

Tier: 2  Prereqs: 02  Parallel with: 07, 08, 09, 10, 11  Input: reference_url + output_dir  Output: clone/ + clone-manifest.json + clone-motion.json + clone-components.json  Model: sonnet  Budget: 3500

## Working Contract

Read `contracts/working-contract.md` and the declared input only. Emit the exact declared artifacts, validate them against their schemas when schemas exist, and update the manifest. Keep evidence separate from inference.

## Instructions

1. Invoke SPA-Ripper against the reference URL:

   ```text
   spa-ripper clone <reference_url> -o <output_dir>/clone -t 20
   ```

2. After the clone completes, inventory it:
   - HTML pages: every `*.html` file
   - CSS files: every `*.css` file
   - JS chunks: every `*.js` / `*.mjs` file
   - Assets: images, fonts, SVGs

   Write `clone-manifest.json`:

   ```json
   {
     "reference_url": "...",
     "acquired_at": "...",
     "pages": ["index.html", "anime/[id].html"],
     "stylesheets": ["assets/index-abc.css"],
     "chunks": ["assets/AnimeCard-7vp7TjMF.js"],
     "assets": {"images": 0, "fonts": 0, "svgs": 0},
     "total_bytes": 0
   }
   ```

3. Extract motion from every CSS file:
   - `@keyframes` definitions: name, timing, and iteration
   - `transition-property` declarations with durations
   - `cubic-bezier` timing functions
   - Animation shorthand usage

   Write `clone-motion.json`:

   ```json
   {
     "keyframes": [{"name": "...", "timing": "...", "props": []}],
     "transitions": [{"property": "...", "duration": "...", "easing": "..."}],
     "easings": []
   }
   ```

4. Infer the component inventory from chunk filenames. For `<ComponentName>-<hash>.js` or `<ComponentName>.<hash>.js`, extract the name before the hash and deduplicate it. Cross-reference names with DOM structure in HTML pages. Write `clone-components.json`:

   ```json
   {
     "components": [{
       "name": "AnimeCard",
       "source": "assets/AnimeCard-7vp7TjMF.js",
       "inferred_props": [],
       "used_on_pages": ["index.html"]
     }]
   }
   ```

5. Mark complete. Announce unlocked: 11a, 12.

## Output Contract

All four artifacts must exist: `clone/`, `clone-manifest.json`, `clone-motion.json`, and `clone-components.json`. `clone/` must be greater than 0 bytes.

## If this fails

- SPA-Ripper is not installed → halt and print installation instructions.
- The target is bot-protected → log it as blocked and continue with what was fetched.
- The clone is empty → halt with a specific error.

## Do not

Do not attempt to re-fetch assets SPA-Ripper missed. Do not modify the clone. Do not parse JavaScript beyond chunk filename extraction in this node.
