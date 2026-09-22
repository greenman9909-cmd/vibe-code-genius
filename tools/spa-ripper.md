# SPA-Ripper

Repository: `github.com/greenman9909-cmd/spa-ripper`.

SPA-Ripper is the lightweight frontend-clone specialist. The current CLI is:

```bash
git clone https://github.com/greenman9909-cmd/spa-ripper.git
cd spa-ripper
python -m pip install -e .
spa-ripper clone https://example.com -o ./clone -t 20
```

`python run.py clone <URL> -o <DIR>` is also supported from the cloned repository.

Important: the live SPA-Ripper tool primarily produces the cloned frontend tree. Do not claim it directly emitted `structure.json`, `design_tokens.json`, or other Vibe Code Genius artifacts unless those files actually exist. Node 11f inventories the real clone into `clone-manifest.json`, `clone-motion.json`, and `clone-components.json`.

Runtime integration: `vibe-tree acquire --url <URL> --out <SESSION_DIR>` invokes `spa-ripper clone` when available and records the exact command and result in `acquisition-manifest.json`.

Fallback: SiteMap-X → HAR/browser capture → manual evidence → screenshots, as defined in `tools/acquisition-fallback.md`.

## Contract

Input and output are validated before downstream nodes consume them. Never present an authored fixture as a live scrape.
