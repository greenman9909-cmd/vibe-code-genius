# Support, sponsorship, and contribution

## Support channels

Use GitHub Issues for reproducible bugs, GitHub Discussions for design questions, and pull requests for schema, node, tool, or documentation improvements. Include the exact command, input artifact, output artifact, validator result, and environment when reporting a failure.

## Ko-fi configuration

The repository intentionally uses this editable placeholder:

`https://ko-fi.com/YOUR_HANDLE`

A maintainer can replace it in `README.md`, `docs/support.md`, and tool integration pages after verifying the destination. Do not invent a handle, use a redirect with unknown ownership, or present a placeholder as an active sponsorship link.

## Contribution checklist

- Run `python scripts/validate-tree.py`.
- Run `python tests/golden.py` and the unit suite.
- Add a golden case for behavior changes.
- Version any frozen schema change.
- Preserve evidence and attribution for external sources.
- Keep secrets, tokens, PII, generated caches, and local session artifacts out of commits.
