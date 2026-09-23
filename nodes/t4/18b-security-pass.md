# Node 18b — Security Pass

Tier: 4  Prereqs: [16a]  Parallel with: [18d, 18e]  Input: application + auth/backend when selected  Output: security-report.json  Model: sonnet  Budget: 3500 tokens

## Working Contract

Perform a threat-surface review of the actual application after runtime verification. Use `references/production-engineering-2026.md` and relevant current primary docs. OWASP ASVS 5.0 is a requirements vocabulary, not a box-ticking score.

## Instructions

1. Enumerate exposed surfaces: browser routes, APIs, auth/session, database/storage, uploads, webhooks, external fetches, secrets/config, deployment headers and privileged operations.
2. Test authorization and negative cases, not only successful access. Verify tenant/user isolation where applicable.
3. Check input/output handling for injection/XSS/HTML injection, unsafe command/process use, path traversal, SSRF, open redirects, insecure deserialization and untrusted URLs as relevant.
4. Review CORS, CSRF/session/cookie behavior, CSP/security headers, transport, caching of sensitive responses, secrets, dependency risk, rate limiting and abuse controls.
5. For Supabase/exposed databases, verify RLS/grants and require allow/deny CRUD tests for relevant roles.
6. For every finding record proof, severity, current status and a concrete fix. Do not report theoretical vulnerabilities unsupported by the architecture.
7. Produce `security-report.json` with `stage: review`, baseline references, checks, findings, blocking findings and evidence.

## Output Contract

`security-report.json` must satisfy `schema/security_report.schema.json`. `pass: true` requires no blocking findings.

Before marking complete:

python scripts/validate-artifact.py --node 18b --artifact security-report.json --schema schema/security_report.schema.json

## If this fails

Keep the security gate failed. Never remove a failing check to obtain a green report.
