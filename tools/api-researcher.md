# api-researcher

Repository: `github.com/greenman9909-cmd/api-researcher`. Package CLI: `apiresearch`.

Install:

```bash
git clone https://github.com/greenman9909-cmd/api-researcher.git
cd api-researcher
python -m pip install -e .
```

Run:

```bash
apiresearch --endpoints ./endpoints.txt --out ./api_research
```

It writes `api_research.json` and `api_research.md`. Safe mode is GET-only/no-body by default and never guesses credentials.

Runtime integration: after SiteMap-X (or another acquisition rung) produces `endpoints.txt`, `vibe-tree acquire` invokes `apiresearch` automatically unless `--no-api` is supplied. If an explicit Authorization header is needed, place it in an environment variable and pass `--auth-header-env NAME`; the recorded manifest redacts its value.

## Contract

Only explicitly supplied credentials may be used. Preserve the tool's observed/inferred distinction and validate `api_research.json` before node 07a is complete.
