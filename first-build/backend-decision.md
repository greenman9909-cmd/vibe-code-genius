# Backend Architecture Specification

# Decisions
1. **Runtime Platform**:
   - Next.js 14+ App Router Route Handlers (`app/api/*/route.ts`) executing on Edge / Node.js Serverless runtime.
   - Low latency execution close to global users with automatic TLS termination.
2. **State & Persistence Architecture**:
   - Zero persistent relational database requirement for landing page scope.
   - Lead captures and waitlist submissions are dispatched directly to third-party APIs (Resend Audience & webhook endpoints) with idempotent retry logic.
   - Ephemeral in-memory key-value cache for token bucket rate limiting.

# Validation Protocols
- Strict inbound request validation using Zod 3.x schemas before touching any external services.
- Invalid requests are immediately rejected with RFC 7807 Problem Details for HTTP APIs (Status 422 Unprocessable Entity).
- Sanitization of all string fields to eliminate script injection, HTML entities, and SQL injection vectors.
- Strict header enforcement requiring `Content-Type: application/json` on all mutating HTTP methods.

# Abuse Prevention & Security Hardening
- **Sliding Window IP Rate Limiting**: Maximum 5 registration requests per IP per 60 seconds.
- **Honeypot Decoy Trap**: Hidden input field (`_gotcha`) embedded in forms; submissions containing values are silently dropped with simulated 200 OK responses to neutralize spam bots.
- **Payload Size Caps**: Maximum request body size capped at 16KB to prevent denial of service via memory exhaustion.
- **CORS Policy**: Default-deny posture; only identical origin requests permitted on public mutative endpoints.
