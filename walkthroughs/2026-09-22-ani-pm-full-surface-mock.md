> Superseded for this user's actual target. The run below rebuilt the ani.pm surface from extracted evidence, but the user clarified that the desired operation was to **edit/remix the SPA-Ripper-extracted frontend itself**. See `2026-09-22-ani-pm-extracted-aml-remix.md` for the corrected workflow.

# Field Report — ani.pm full-surface mock rebuild

Date: 2026-09-22  
Agent: ChatGPT (GPT-5.6 Sol)  
Reference: `https://ani.pm`  
Reference repository: `greenman9909-cmd/ani-pm-frontend`  
Mock branch: `mock/yoru-full-surface`

## Goal

Recreate the major ani.pm product surfaces under a renamed product for testing, while replacing real catalogue data, profiles, search results, playback, authentication, and community content with synthetic fixtures.

## Patch discovered

The God Tree now contains **62 node files**. The new node is:

- `11f Clone Extract`

Node 11f consumes a reference URL plus output directory and emits:

- `clone/`
- `clone-manifest.json`
- `clone-motion.json`
- `clone-components.json`

It also supports cached mode through `reference-source.json.mirror_path`.

## Cached reference path

A prior SPA-Ripper capture already existed in:

`greenman9909-cmd/ani-pm-frontend/ani.pm_frontend`

The capture was therefore treated as the cached mirror for Node 11f rather than running a duplicate scrape.

Inventory observed from the cached clone:

- 227 files
- 17,479,101 bytes
- 1 SPA HTML shell
- 120 JavaScript chunks
- 26 stylesheets
- 64 images
- 12 font files
- 1 SVG
- 66 named component-style chunks inferred from filenames

## Route surface inferred

The captured application exposed or referenced these major surfaces:

- home
- browse/catalog
- search
- anime details
- watch/player
- library
- profile/public user profile
- settings
- community/forum/chat
- leaderboard
- release schedule
- watch together
- genres
- latest/recent
- collections
- downloads
- about/privacy/terms

The mock rebuild implemented equivalent test surfaces without reusing production API behavior.

## Component evidence

Chunk filenames exposed useful product structure including:

- Home
- HeroCarousel
- AnimeCard
- AnimeDetails
- AnimeTitle
- Search
- Library
- Profile
- Settings
- Community
- Leaderboard
- ReleaseSchedule
- WatchRoom
- WatchTogether
- AuthModal
- player overlays and controls

Node 12's patched instruction was followed conceptually: component structure informed the rebuild, but source code was not copied.

## Motion evidence

Representative cached CSS contained route fades, card entrances, menu transitions, chat entrances, detail-page rises/fades, loading spinners, and several spring-like cubic-bezier curves.

The mock build retained only restrained interaction motion and a `prefers-reduced-motion` fallback.

## Mock-data boundary

The rebuild deliberately contains:

- no ani.pm API requests;
- no external streaming resolver;
- no real authentication;
- no real user profiles;
- no production comments or activity;
- no copied anime artwork;
- no external video embeds.

Synthetic titles, people, comments, schedules, progress, scores, badges, folders, settings, and player states provide the test surface.

## Verification

A dedicated GitHub Actions workflow checks:

1. required page renderers exist;
2. God Tree clone/reference artifacts parse as JSON;
3. no known real network/stream markers exist in the mock app;
4. inline JavaScript passes `node --check`;
5. a local static HTTP server returns the Yoru HTML document.

The first workflow run completed successfully.

## Reusable lessons

### 1. Node 11f materially improves reference-led rebuilds

A cached SPA clone can now be treated as a first-class structural artifact instead of an informal folder an agent happens to inspect.

### 2. One HTML file does not imply one page

Modern Vite/React SPAs may expose one HTML shell while lazy chunks encode the real route/component surface. Inventory route chunks before judging page count.

### 3. Component names are useful evidence, implementation is not permission to copy

Hashed filenames such as `AnimeCard-*.js`, `Profile-*.js`, and `Settings-*.js` reveal product architecture. Use that to plan equivalent components, then implement them independently.

### 4. Full-surface mocks should preserve states, not production data

For realistic testing, reproduce navigation, filters, tabs, empty/loading states, progress, settings toggles, profile statistics, discussion layouts, and player controls with fixtures.

### 5. Network isolation deserves its own gate

A mock clone can accidentally retain production endpoints even when the visible data looks fake. Scan for known API/stream markers and fail CI if any appear.

## Anti-lessons

Do not infer that:

- the cached clone proves ani.pm's current backend behavior;
- every lazy chunk is reachable today;
- a synthetic player validates real playback;
- copied source is needed for visual fidelity;
- the cached artwork is safe to redistribute;
- one successful mock verification replaces browser visual comparison.

## Outcome

The run produced a renamed full-surface mock app on `greenman9909-cmd/ani-pm-frontend`, branch `mock/yoru-full-surface`, with synthetic data, Node 11f-style artifacts, and a passing CI verification gate.
