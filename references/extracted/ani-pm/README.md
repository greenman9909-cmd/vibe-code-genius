# ani.pm extracted frontend — code reference

This directory attaches the **actual SPA-Ripper-extracted ani.pm frontend** to the God Tree as a version-pinned external code reference.

The code is intentionally kept in its existing repository instead of duplicating roughly 17.5 MB of hashed SPA output inside the God Tree repository.

## Pinned source

- Repository: `greenman9909-cmd/ani-pm-frontend`
- Commit: `2f734e7334a9a9e2db6a43c876fe88613687827f`
- Extracted frontend path: `ani.pm_frontend/`
- Acquisition tool: SPA-Ripper
- Reference target: `https://ani.pm`

To materialize the exact reference:

```bash
git clone https://github.com/greenman9909-cmd/ani-pm-frontend.git
cd ani-pm-frontend
git checkout 2f734e7334a9a9e2db6a43c876fe88613687827f
cd ani.pm_frontend
```

Agents with GitHub connector access should fetch the pinned commit directly and inspect files there rather than assuming `main` is unchanged.

## Why this reference matters

For streaming/media products, this capture provides a concrete implementation reference for the design language the God Tree should prioritize when no stronger product-specific reference exists:

- cinematic hero/spotlight composition;
- title/logo, score, year, episode/duration, genres and synopsis metadata;
- Play/Resume and Library actions;
- horizontal media shelves;
- detail/title pages;
- search and browse flows;
- library and history surfaces;
- profiles and settings;
- community/leaderboard/schedule;
- dedicated watch/player layout;
- responsive mobile navigation;
- dark media-first surfaces, glass overlays and motion.

The design is not a screenshot. It is implemented in the extracted React/Vite chunks, CSS, responsive rules, component composition and motion code.

## Important files/chunks

Representative extracted chunks include:

- `assets/Home-CGFASR0W.js`
- `assets/HeroCarousel-BDv_ijSP.js` / related hashed HeroCarousel chunk
- `assets/Search-2nEGoI9L.js`
- `assets/AnimeDetails-Cbtev-sg.js`
- `assets/Library-ZYaQLPnI.js`
- `assets/Profile-CMoU59Rx.js`
- `assets/Settings-CkAqqnh3.js`
- `assets/Community-DH7hDm6p.js`
- `assets/Leaderboard-BUOuY75J.js`
- `assets/ReleaseSchedule-Bgz-d3sW.js`
- `assets/WatchRoom-CG3SvFCv.js`

Hash names may differ in later captures. Use the pinned commit for the exact filenames above.

## Evidence boundary

This is a **historical pinned code reference**. It may influence architecture, design strategy and known failure modes.

It does **not** prove that the current public ani.pm site still has the same routes, APIs, assets or behavior. For current-state evidence, run the required Node 02 / Node 11f acquisition flow again.

## Artwork and external assets

The extracted repository contains banners, logos, fonts and other captured assets. Their presence in the reference does not establish redistribution rights. Use them for analysis/testing only unless licensing or permission is verified.

See:

- `docs/use-cases.md#recipe-streamingmedia-app`
- `walkthroughs/2026-09-22-ani-pm-extracted-aml-remix.md`
