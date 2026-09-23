# Use cases and workflow recipes

## Choose a stopping tier

| Goal | Stop after | Key outputs |
|---|---:|---|
| Prompt and route planning | Tier 1 | `intent.json`, `scope.json`, `system.json`, `prompt.md` |
| Frontend composition | Tier 3 | Components, pages, motion, data hooks, forms, state, static/runtime reports |
| Full product scaffold | Tier 4 | Database, auth, security, tests, deployment, performance, production checklist |
| High-fidelity reference rebuild | Tier 5 | Diff report, correction prompt, self-refinement, ship report, repair report |

## Recipe: reference-led build

1. Start with a reference URL and a product brief.
2. Run Reference Load and validate `reference.json`.
3. Review `file-tree.md`, `manifest.json`, and `design-commitment.md` before implementation.
4. When extracted code is available, run Design System Extract and analyze how the real layout, components, typography, responsive rules, interaction states, and motion are composed. Record why the patterns work and how new features should remix them.
5. Preserve/remix the extracted visual language for new surfaces such as login, signup, profile, settings, library, forms, dialogs, and admin instead of introducing generic AI-generated UI.
6. Use the reference only for structure, interaction patterns, and design evidence; do not invent proof or copy private data.
7. Finish the complete declared scope. Do not call the project done with dead flows, placeholders, missing responsive states, or unverified integrations.
8. Run the static, runtime, edge, security, design-consistency, completeness, and final ship gates.

## Recipe: API-first product

1. Supply an `endpoints.txt` file from SPA-Ripper, SiteMap-X, or an existing API inventory.
2. Run API Research in safe mode. Add an explicit auth header only when the integration requires it.
3. Freeze `api_research.json` before generating the OpenAPI contract.
4. Generate typed clients, backend handlers, database inference, and contract tests from the same artifact.
5. Keep observed behavior separate from design decisions in `backend-decision.md`.

## Recipe: design-system migration

1. Run Design Tokens and Design System Extract.
2. Reconcile reference values into semantic tokens rather than copying arbitrary declarations.
3. Define the Design Contract and Motion Customization profile.
4. Build the Component Kit once, then route pages through shared layout primitives.
5. Run Consistency Check after each page and compare the final build with Diff-Merge.

## Recipe: streaming/media app

For anime, video, movie, TV, music, or other streaming products, prioritize a **media-first layout** before falling back to a generic SaaS/dashboard shell.

Default design priorities:

1. Start with a full-width cinematic hero/spotlight area using real design code from the reference when available: backdrop, title/logo, score/year/episode or duration metadata, genres/tags, synopsis, primary Play/Resume action, library/save action, and secondary details action.
2. Follow the hero with horizontal media shelves rather than dashboard cards: Continue Watching, Trending, Latest, Popular, Recommended, genres/collections, and schedule/release rows as appropriate.
3. Treat title/detail pages as a primary surface: large artwork, metadata, synopsis, episode/season lists, cast/details, related titles, comments/community, library state, and playback entry points.
4. Preserve a dedicated player/watch layout with playlist/episode navigation, progress, subtitles/audio controls, fullscreen/theater states, and responsive mobile behavior.
5. Give Library, Search/Browse, Profile, Settings, Community, Schedule/Leaderboard and Watch-Together flows the same design-system treatment as Home; do not make them generic utility pages.
6. Prefer dark, immersive media surfaces, restrained glass/overlay treatments, strong artwork hierarchy, dense but readable metadata, and motion that supports browsing without competing with the content.
7. On extracted-SPA remix work, preserve the original component/CSS/responsive/motion code path whenever possible. The design is code; do not replace it with screenshots or a hand-built lookalike unless the task explicitly calls for a redesign.
8. Keep record identity separate from artwork/metadata identity. If the extracted design keys hero assets by external IDs such as AniList IDs, preserve or adapt those keys at the data boundary instead of rewriting the hero component.
9. Verify the actual browser DOM and responsive layout for the hero, shelves, title page, and player. API success alone does not prove the streaming design rendered correctly.

This is a default heuristic, not a universal contract. An explicit product brief, accessibility requirement, or stronger reference should override it. For a concrete code reference, load `references/extracted/ani-pm/reference-source.json` and `references/extracted/ani-pm/README.md`. See `walkthroughs/2026-09-22-ani-pm-extracted-aml-remix.md` for the field report that motivated this recipe.

## Recipe: failure repair

1. Preserve the exact command, input artifact, and validator output.
2. Run `vibe-tree report-failure NODE --input JSON`.
3. Add the smallest regression under `tests/failures/`.
4. Patch only the failing tool or node behavior.
5. Run the original test suite, `tests/verify.py` when present, and the new regression before keeping the patch.

## Recipe: multi-agent execution

Parallelize only independent nodes with complete declared inputs. The coordinator merges by schema, records conflicts, and blocks consumers until the merged artifact validates. Use the meta tier for fidelity scoring and correction prompts rather than asking multiple agents to overwrite the same file.
