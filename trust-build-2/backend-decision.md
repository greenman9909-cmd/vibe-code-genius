# Backend Architecture Decision Record

## Architectural Decisions
- **Runtime Choice**: Next.js Route Handlers running on Edge / Node.js runtime to co-locate API endpoints with marketing server components.
- **Data Persistence**: Postgres database hosted on Railway with Prisma ORM for structured queries and schema migrations.
- **Stateless Handlers**: Endpoints remain fully stateless, relying on cryptographic signature checks and Redis rate-limiting tokens.

## Input Validation Framework
- **Schema Engine**: Zod v3 is chosen as the standard runtime typing and validation engine across all client and server boundaries.
- **Request Coercion**: All incoming JSON payloads are stripped of undeclared properties (`.strict()`) to prevent prototype pollution or parameter injection attacks.
- **Strict Typing**: TypeScript contracts are inferred directly from Zod schemas (`z.infer<typeof Schema>`) to eliminate manual type drift.

## Abuse Prevention & Security Hardening
- **Sliding-Window Rate Limiting**: Upstash Redis tracks request counts per IP address, enforcing a hard limit of 5 requests per 60 seconds on public forms.
- **Honeypot Traps**: Form submissions contain a visually hidden `_gotcha` field; any submission with a non-empty value is immediately discarded without database persistence.
- **Security Headers**: Standard defense-in-depth headers applied globally via `next.config.js` including `X-Frame-Options: DENY`, `X-Content-Type-Options: nosniff`, and strict `Content-Security-Policy`.
