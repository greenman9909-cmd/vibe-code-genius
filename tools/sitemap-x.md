# SiteMap-X

Repository: `github.com/greenman9909-cmd/SiteMap-X_Owais`. Package/CLI name: `sitemapx`.

Install:

```bash
git clone https://github.com/greenman9909-cmd/SiteMap-X_Owais.git
cd SiteMap-X_Owais
python -m pip install -e .
# optional browser rendering:
python -m playwright install chromium
```

Basic run:

```bash
sitemapx https://example.com --out ./out
```

SiteMap-X is the deep crawler/reconciliation specialist. It can emit `mirror/`, `crawl.sqlite3`, `report.html`, `report.json`, `report.md`, `endpoints.txt`, `endpoints.json`, external hosts, optional OpenAPI/GraphQL artifacts, and screenshots depending on flags and discovery.

Runtime integration: `vibe-tree acquire` invokes SiteMap-X with bounded depth and machine-readable report formats, then uses its real `endpoints.txt` as API Researcher input when present.

## Contract

Input and output are validated before downstream nodes consume them. Missing optional artifacts stay missing; do not synthesize them.
