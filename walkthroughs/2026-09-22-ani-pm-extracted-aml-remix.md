# Field Report — ani.pm extracted frontend remixed to AML

Date: 2026-09-22  
Reference repository: `greenman9909-cmd/ani-pm-frontend`  
Working branch: `remix/aml-extracted-frontend`  
Pull request: `#2`

## Correction

The first attempt treated the cached SPA-Ripper capture as design/reference evidence and generated a new mock interface.

That was the wrong interpretation.

The user wanted the **extracted ani.pm frontend itself** to remain the frontend, with its real lazy chunks, CSS, components, routes and interaction structure preserved, while its branding and data layer were modified for mock testing.

## Correct Node 11f interpretation for this case

Node 11f — Clone Extract provides a real clone under `mirror_path`.

When the user explicitly asks to "use the extracted code and edit/remix it", do not reduce the clone to a visual reference and regenerate the UI.

Instead:

1. preserve the extracted frontend tree;
2. identify the data/runtime boundary;
3. patch branding and local integration points;
4. replace backend/API state with synthetic fixtures;
5. disable unwanted production network behavior;
6. verify that the original extracted chunks still load and consume the mock responses.

This is distinct from Node 12's normal "study structure, do not copy code" path because the user's requested artifact here is specifically a remix of the already-extracted working copy they control.

## Existing architecture used

The repository already paired the SPA-Ripper output with:

- `ani.pm_frontend/` — captured Vite/React production SPA;
- `server.js` — local Node gateway emulating the frontend's API surface;
- `serve.py` — Python alternative gateway;
- `local-bridge.js` — playback/resume integration bridge.

The corrected approach reused those boundaries instead of creating a parallel frontend.

## AML patch

A new branch, `remix/aml-extracted-frontend`, was created from `main`.

Changes:

- kept the original hashed React/Vite chunks and CSS;
- added `aml-brand.js` before the application entrypoint;
- changed visible branding to AML at runtime;
- changed the PWA shell/manifest branding;
- replaced catalogue/search/title data with synthetic AML fixtures;
- replaced profile/community/leaderboard state with synthetic users;
- added mock watchlist/progress/settings/collections state;
- disabled live AniList fallback;
- disabled live Yoru/MegaPlay/Settlar playback;
- routed watch/preview flows to a local mock player;
- blocked external `fetch()` from the browser-side AML shim.

## Important implementation lesson

The existing gateway already reproduced many response shapes used by the captured SPA.

The highest-fidelity approach was therefore to **change the gateway state**, not to rewrite Home, Search, Profile, Library, Settings or AnimeDetails components.

This preserved the original UI behavior automatically.

## Regression caught during patching

A stream-resolver cleanup accidentally removed the AML fixture block because the fixtures had been inserted immediately before the server marker that was also used as the replacement boundary.

A source-order verification found:

- `AML_ITEMS` missing;
- high-priority mock routes referring to an undefined symbol.

The repair:

1. restored the fixture block in a stable location;
2. checked symbol positions explicitly;
3. moved mock route overrides until after `sendJson` and `sendFile` were defined;
4. intercepted `/embed/preview` locally;
5. re-ran runtime CI.

Reusable lesson: after large string-based code transformations, verify both **symbol existence** and **declaration/use ordering**, not just syntax.

## Design is code in extracted-SPA remix work

A later clarification exposed another important distinction: the design was not a screenshot or a hand-recreated visual target.

In this build, the design itself lives in the extracted frontend code:

- React/Vite component markup and composition;
- CSS files and design tokens;
- responsive breakpoints and mobile layout rules;
- glass/overlay treatments;
- card and hero structure;
- motion/transition logic;
- route-level page composition;
- interaction states such as tabs, menus, filters, watch controls and settings.

Static assets such as banners, logos, posters, icons and fonts support that design, but they are not the design system by themselves.

### Reusable lesson

When remixing an extracted SPA, preserve the **design code path** whenever fidelity matters. Replacing it with screenshots, hand-authored lookalikes, or newly invented component trees discards the highest-value part of the extraction.

For this class of task, "use the design" should usually mean "keep and run the extracted layout/style/component code", not "visually imitate the screenshot".

## Hero artwork key failure and repair

The first AML mock fixture pass used synthetic AniList IDs such as `91001`.

The extracted Home bundle did not render the hero banner even though the spotlight API returned valid items. Investigation showed that the original Home/glass-list code contains an artwork allowlist keyed by specific original AniList IDs:

- `189046`
- `135865`
- `178789`
- `196187`
- `16498`
- `113415`
- `185874`
- `187538`

Those IDs map to already-extracted local banner/logo assets.

The repair kept the AML mock records but mapped their `anilistId` fields onto those original artwork keys. This preserved the original hero selection and artwork pipeline instead of bypassing or rewriting it.

A second metadata mismatch was found at the same time:

- mock data provided `episodeCount` and `synopsis`;
- `HeroCarousel` expected `episodes` and `description`.

The Home metadata adapter was patched to carry both shapes through.

### Verification improvement

The CI gate was strengthened from API/static checks to a real headless-browser assertion. It now boots the extracted SPA and verifies that the homepage DOM contains the original hero structure, title and episode metadata.

### Reusable lesson

When an extracted UI silently omits a component:

1. inspect component-side allowlists and key maps;
2. preserve original external identifiers when they are structural keys;
3. distinguish record identity from artwork/metadata identity;
4. adapt response-field names at the boundary instead of rewriting the component;
5. verify the actual browser DOM, not only the API response.

## Runtime verification

Workflow: `aml-extracted-runtime`

The CI job successfully:

- syntax-checked `server.js`;
- syntax-checked `aml-brand.js`;
- asserted production-network markers were absent from the mock gateway;
- booted the Node gateway;
- served the real extracted SPA shell;
- served the captured Home lazy chunk;
- returned AML search results;
- returned AML title details;
- returned a synthetic profile;
- returned mock auth state;
- returned mock watchlist state;
- returned settings fixtures;
- served the local mock player;
- served the local preview path.

The first completed workflow run passed all steps.

## Superseded run

The earlier branch `mock/yoru-full-surface` and PR #1 generated a new UI. PR #1 was closed after the user clarified the requirement.

## Reusable lessons

### Clone Extract has two valid downstream modes

**Reference mode:** inspect the clone and independently implement equivalent product components.

**Remix mode:** when explicitly requested and appropriate for the supplied/extracted code, preserve the clone and modify its data/runtime/branding layers.

The user's requested artifact decides which mode applies.

### Preserve the highest-value layer

When a captured frontend is already complete, route-rich and componentized, replacing its data layer usually preserves more fidelity than reimplementing its pages.

### Network isolation must be tested

Mock data is not enough if old fallbacks can still contact production services. Disable dynamic fallback functions and scan for known production URL markers.

### Verification should hit both code and behavior

Static syntax checks would not have found the missing fixture block. Starting the gateway and requesting search/profile/auth/watch routes did.

## Outcome

The corrected branch now runs the actual SPA-Ripper-extracted ani.pm frontend as an AML mock build with synthetic data and local playback fixtures, with runtime CI passing.
