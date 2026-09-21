# Assets and attribution

## Source profile

The documentation direction uses the public profile of [Debasish Ray](https://github.com/debasishray16) as an inspiration source for a developer-tool aesthetic: terminal output, Ubuntu/Debian workflows, backend engineering, IoT, ML/DL, DevOps, Docker, Kubernetes, AWS, React, and Tailwind CSS.

The profile metadata was reviewed on 2026-09-22. Public profile page: `https://github.com/debasishray16/debasishray16`. Public avatar endpoint observed in GitHub metadata: `https://avatars.githubusercontent.com/u/83941421?v=4`.

## Usage policy

This repository does not bundle the profile avatar, personal photographs, logos, or copied profile text. It does include two explicitly marked anime reference assets under `assets/anime/`: `Beta.jpg` and `Solo-Leveling-PNG.png`, copied from the source repository at the user’s request. The source repository does not state a license for these images; attribution and SHA-256 checksums are recorded, and permission or a verified license is required before commercial redistribution. A public URL is not automatically a license to redistribute an image. If a product-specific build wants to use another external asset, record its URL, license or permission, attribution, checksum, and intended use in an asset manifest before shipping.

## Asset manifest shape

```json
{
  "source_url": "https://example.com/asset.svg",
  "asset_type": "illustration | logo | avatar | screenshot | font",
  "license": "verified license or permission reference",
  "attribution": "required credit text or null",
  "checksum": "sha256:...",
  "usage": "where the asset appears",
  "verified_at": "2026-09-22"
}
```

## Preferred sources

Prefer repository-owned SVG/CSS assets, permissively licensed open-source assets, generated assets with recorded prompts, or explicit user-provided files. Avoid scraping and republishing third-party images by default. Keep remote assets out of critical runtime paths unless their availability, licensing, dimensions, and cache behavior are verified.
