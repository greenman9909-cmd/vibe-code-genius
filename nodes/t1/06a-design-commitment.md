# Node 06a — Design Commitment

Tier: 1  Prereqs: [06]  Parallel with: —  Input: intent.json + reference.json + design-tokens.json (if present) + references/aesthetic-directions.md  Output: design-commitment.md  Model: sonnet  Budget: 2500

## Working Contract

Read `contracts/working-contract.md` and the declared input only. Emit the exact declared artifact, validate it against its schema, and update the manifest. Keep evidence separate from inference.

**No-explore rule:** Do not browse for additional references, invent exemplars, or inspect unrelated files. Read only `intent.json`, `reference.json`, `design-tokens.json` when present, and `references/aesthetic-directions.md`.

## Instructions

1. Read `references/aesthetic-directions.md`. It defines five aesthetic families.
2. Match product category to a primary direction:
   - developer tools / infra / APIs / agents → Terminal
   - content platforms / publications / long-form → Editorial
   - consumer SaaS / productivity / community → Warm Humanist
   - creative tools / social / brand-forward → Playful
   - docs / utilities / libraries / CLIs → Minimal Utility
3. Cross-check against the reference's actual aesthetic using `design-tokens.json`. Determine which direction the reference sits in.
4. If product direction matches reference direction, stay in that direction. If they differ, decide explicitly: either borrow the reference's visual language or diverge to the product's natural direction. State the choice and the reason.
4b. EVIDENCE FROM CLONE. If `clone-motion.json` and `clone-components.json` exist, read them.
   - Note the reference's actual motion attitude:
     - no transitions at all → reference is "static"
     - < 200ms transitions → "snappy"
     - 200–400ms → "considered"
     - > 400ms or spring-based → "expressive"
   - Note the component density (components per page).
   - Note the type scale (how many distinct font sizes are used).
   These are EVIDENCE for your direction choice, not inputs. They confirm or challenge the category-based match from step 2. Record them in the `Reference Used` section of `design-commitment.md`.
5. Emit `design-commitment.md` with the exact six required sections below.
6. Do not invent typefaces. Real faces only. If unsure, use one of: Geist, Inter Tight, JetBrains Mono, Söhne, Untitled Sans, Tiempos, GT Sectra, Diatype, Tobias, Migra.
7. Mark complete and announce unlocked: 07.

## Output Contract

design-commitment.md must contain all six sections. No section may be empty.

## Chosen Direction <name> — <one-line summary>

Why: <reasoning — product category + reference evidence>

## Visual Rules

- Typeface: <specific face, real, named>
- Color strategy: <single-accent | dual-accent | monochrome | editorial>
- Grid: <12-col | asymmetric | editorial-columns | utility>
- Spacing rhythm: <tight | medium | editorial>
- Motion attitude: <none | subtle | expressive> + timing values
- Icon policy: <line | solid | none | illustrated>
- Shadow policy: <none | subtle | elevated>
- Border radius scale: <e.g. 4/8/12/none>

## Copy Tone

Write 2–3 sentences explaining how copy reads and what it must never sound like.

## Per-Section Rendering

Provide one concrete instruction each for hero, features, pricing, and footer.

## Banned For This Direction

List 5–8 anti-patterns specific to the chosen direction. These are direction-specific traps, not the global registry from node 11c.

## Reference Used

State what came from the reference—tokens, layout, and structure—and what was decided for the product—typography face, tone, and direction.

Before marking complete: python scripts/validate-artifact.py --node 06a --artifact design-commitment.md --schema schema/design-commitment.schema.json. If validation fails, halt. Do not substitute a different artifact. Do not continue.

## If this fails

- Reference tokens missing → infer direction from `intent.json.product_type`.
- Product category ambiguous → default to Terminal for dev tools, else Warm Humanist.
- Log the node id, input hash, invocation, and minimal reproduction to `session.log`. Use datetime.utcnow().isoformat(timespec="microseconds") + "Z" (microseconds MUST vary between events). Apply the declared fallback in `contracts/repair-contract.md`; do not silently fabricate a result.

## Do not

Do not invent typefaces. Do not copy the reference's copy tone if it mismatches the product. Do not produce a commitment that is just a restatement of `design-tokens.json`. Do not browse beyond the declared inputs or write unresolved references.

## Example output

```md
## Chosen Direction Terminal / Brutalist — dense, functional, systems-oriented
Why: The product is an API operations console and the reference uses a monochrome token set with tight sans headings.

## Visual Rules
- Typeface: Geist with JetBrains Mono accents
- Color strategy: single-accent
- Grid: 12-col
- Spacing rhythm: tight
- Motion attitude: subtle; 120ms hover and 180ms state transitions
- Icon policy: line
- Shadow policy: none
- Border radius scale: 4/8/12

## Copy Tone
Direct and operational. Never sound like vague launch marketing or fictional proof.

## Per-Section Rendering
- hero: Keep the heading under 12 words and align it to the first grid column.
- features: Use dense two-column capability rows with evidence labels.
- pricing: Use a plain comparison table with no decorative card nesting.
- footer: Keep links compact and grouped by task.

## Banned For This Direction
- Gradient hero text
- Decorative icon tiles
- Oversized lifestyle imagery
- Bounce easing
- Warm editorial serif display

## Reference Used
Reference tokens supplied the monochrome palette and dense grid; the product decision adds Geist and JetBrains Mono for API tooling.
```
