# Production Engineering Reference — 2026

Last reviewed: 2026-09-23

Primary sources:
- Vercel production checklist: https://vercel.com/docs/production-checklist
- Vercel Deployment Checks: https://vercel.com/docs/deployment-checks
- Supabase production checklist: https://supabase.com/docs/guides/deployment/going-into-prod
- Supabase database testing: https://supabase.com/docs/guides/local-development/testing/overview
- Supabase Row Level Security: https://supabase.com/docs/guides/database/postgres/row-level-security
- OWASP ASVS: https://owasp.org/projects/asvs

## Reusable production gates

### Database and RLS
- Database migrations are versioned artifacts, not dashboard-only state.
- For exposed Supabase tables, RLS and grants belong in reproducible migrations.
- RLS tests must include both allow and deny behavior, covering relevant CRUD operations and roles.
- Test policy bypass/edge cases, not only the happy path.
- Database tests belong in CI before production deployment.

### Application security
- Use OWASP ASVS 5.0 as a requirements vocabulary for security verification where relevant.
- Verify authentication, authorization, input handling, secrets, transport, browser security, data protection, and abuse controls against the product's real threat surface.
- Agent-generated code receives the same security scrutiny as human-authored code.
- Security findings need evidence and a reproducible verification after remediation.

### Deployment
- A successful build is not the same as a production-ready release.
- Production readiness includes rollback/recovery, deployment protection where appropriate, CSP/security headers, rate limiting/abuse controls, lockfile/dependency pinning, SSL/domain configuration, and observable runtime behavior.
- Deployment checks should evaluate the exact build intended for release.
- Preview/staging evidence must not be silently substituted for production verification.

### Reliability and observability
- Important production paths need logs/metrics/traces or an explicitly scoped alternative.
- Record how to detect and recover from failure.
- Verify origin/database/function region alignment where latency matters.
- Load or capacity testing should be proportional to expected traffic and risk.

### Performance
- Use measured browser/runtime evidence rather than speculative optimization.
- Evaluate Core Web Vitals and application-specific latency, long tasks, payload/bundle behavior, image/font loading, cache behavior, and backend query performance.
- Performance regressions that exceed the project's budget block release or require an explicit accepted exception.

## Promotion rule

These are reference-level gates. Apply only the items relevant to the current platform, architecture, plan, and threat model. Do not fabricate evidence for enterprise-only controls or services that are not available to the project.
