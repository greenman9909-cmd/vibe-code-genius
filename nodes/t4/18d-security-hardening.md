# Node 18d — Security Hardening

Tier: 4  Prereqs: [18b, 18c]  Parallel with: [18e, 20d]  Input: security report + app  Output: harden_report.json  Model: sonnet  Budget: 3000 tokens

## Working Contract

Repair verified security findings without broad rewrites. Read the review report, edge/runtime evidence, current source, and `references/production-engineering-2026.md`.

## Instructions

1. Prioritize blocking/high-confidence findings by exploitability and product impact; do not churn code for theoretical low-value issues.
2. Apply the smallest fix that restores the intended security invariant while preserving product behavior.
3. Strengthen authorization at the authoritative boundary, not only in UI code.
4. Correct RLS/grants, secret exposure, input validation, CSP/headers, CORS/CSRF/session handling, unsafe external fetches, webhook verification, dependency issues, or rate controls only where the evidence requires them.
5. Add a regression test or reproducible verification for each material fix.
6. Re-run the affected security checks after each repair batch.
7. Produce `harden_report.json` using the shared security schema with `stage: hardening`, listing patches and any remaining blocking findings.

## Output Contract

`harden_report.json` must satisfy `schema/security_report.schema.json`; `pass: true` means the blocking findings from the review were actually remediated and rechecked.

Before marking complete:

python scripts/validate-artifact.py --node 18d --artifact harden_report.json --schema schema/security_report.schema.json

## If this fails

Leave unresolved findings explicit. Do not downgrade severity, suppress tests, or weaken a policy merely to make the report pass.
