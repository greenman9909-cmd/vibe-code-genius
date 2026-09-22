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
