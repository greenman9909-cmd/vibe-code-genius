# Node 20b — Performance Pass

Tier: 4  Prereqs: [20]  Parallel with: [23b]  Input: preview build  Output: performance-report.json  Model: sonnet  Budget: 2200 tokens

## Working Contract

Measure the deployed/preview product before optimizing. Use current browser/platform guidance and project-specific budgets; do not invent Lighthouse/Core Web Vitals numbers.

## Instructions

1. Identify relevant user journeys and measure the deployed target or a production-equivalent preview.
2. Collect available evidence for loading/rendering responsiveness, long tasks/INP, LCP where meaningful, bundle/payload behavior, images/fonts, caching and network waterfalls.
3. Inspect server/API/database latency when those capabilities are active, including expensive queries/RLS impact where relevant.
4. Compare measurements to explicit project budgets or accepted baselines. If no numeric budget exists, mark observations as observed rather than fabricating thresholds.
5. Fix high-impact regressions first: duplicate work, render-blocking resources, unnecessary JS, oversized media, uncached repeated calls, slow queries or region mismatch.
6. Re-measure after fixes and record before/after evidence.
7. Produce `performance-report.json`; passing requires no blocking regressions.

## Output Contract

`performance-report.json` must satisfy `schema/performance-report.schema.json`.

Before marking complete:

python scripts/validate-artifact.py --node 20b --artifact performance-report.json --schema schema/performance-report.schema.json

## If this fails

Keep measurements unavailable/blocked rather than fabricating performance data.
