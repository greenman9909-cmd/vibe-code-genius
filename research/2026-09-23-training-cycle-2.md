# God Tree evidence cycle — 2026-09-23 (cycle 2)

## Scope and provenance

This batch records fresh public evidence without promoting one-off observations into global behavior rules. It deliberately does not modify the frozen ani.pm frontend.

### Primary evidence reacquired

1. GitHub Docs — Artifact attestations / build provenance (crawled 2026-09-23): https://docs.github.com/en/actions/how-tos/secure-your-work/use-artifact-attestations/use-artifact-attestations
2. GitHub Docs — Artifact attestations concepts (crawled 2026-09-23): https://docs.github.com/en/actions/concepts/security/artifact-attestations

## Independent workstream findings

### Target scout / product rotation

For subsequent visual acquisition, rotate across categories rather than treating the anime lab as canonical evidence: developer tools, SaaS/dashboard, editorial/content, ecommerce-like interfaces, and streaming/media. The frozen ani.pm lab remains a proving ground only.

No SPA-Ripper, SiteMap-X, or api-researcher execution is claimed in this cycle: those tools were not available in the automation runtime. No extracted proprietary bundles or private endpoints were used.

### Frontend/design

No new global visual rule is justified by the evidence acquired in this cycle. Existing anti-overfitting policy stands: one target is an observation, repeated independent evidence is needed for a reusable design rule.

### Backend / infra / supply chain

GitHub's current documentation states that artifact attestations create cryptographically signed provenance tying a build artifact to workflow/repository/commit/trigger information. For a binary, the documented workflow requires `id-token: write`, `contents: read`, and `attestations: write`, followed by `actions/attest@v4` with the binary as `subject-path`.

Important limitation from the same primary source: attestation is provenance, not a claim that the artifact is secure. Consumers still need verification policy and security validation.

### Validator / red-team conclusion

This is strong primary evidence and directly relevant to GodTree's Windows executable pipeline. It justifies a narrow release-hardening rule:

> Release binaries SHOULD carry verifiable build provenance after tests/build succeed; provenance MUST NOT substitute for tests, code review, malware/security checks, or runtime validation.

This is intentionally a release/build recommendation, not a global agent behavior rule.

## Anime/API workstream

No playback source is promoted in this cycle. The legal/safety contract remains unchanged: metadata and playback are separate concerns; candidate playback must be authorized and checked for HTTPS, browser compatibility/CORS, schema stability, hostname allow-list suitability, and licensing/terms signals. No stream URLs, pirate resolvers, private endpoints, cookies, DRM bypasses, or anti-bot bypasses were collected.

## Coordinator decision

Accepted into research memory:
- Build provenance for downloadable GodTree binaries is worth adding to the Windows release pipeline.
- Attestation is evidence of origin/integrity, not evidence of software safety.

Not promoted:
- No new visual/design global rule.
- No new anime playback provider.
- No claims about SPA-Ripper/SiteMap-X/api-researcher output.
- No frontend mutation to ani.pm.

## Proposed follow-up patch

When the Windows EXE workflow is present on the target branch, add GitHub artifact attestation only after unit tests and the executable build succeed, and keep SHA-256 generation. Verify the resulting attestation before calling a release artifact trusted.
