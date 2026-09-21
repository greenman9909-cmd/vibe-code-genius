# Third-Party Integrations Specification

## Resend Email Dispatch Integration
The platform uses the official Resend Node.js SDK to handle transactional communications and marketing notifications.

### Authentication & Secrets
- `RESEND_API_KEY`: Secret API token provisioned with restricted send capabilities.
- `RESEND_FROM_EMAIL`: Authorized sender domain address (`notifications@vibe-code-genius.dev`).
- `RESEND_AUDIENCE_ID`: Target audience identifier for waitlist broadcast subscriptions.

### Inbound Webhook Handling
Inbound email events (deliveries, bounces, complaints) are processed via `/api/webhooks/resend`. Each webhook payload is verified using HMAC-SHA256 signature verification via the `svix-signature` header before payload parsing.

## Analytics & Observability Integration
The marketing website enforces a strict zero-cookie, zero-PII analytics policy to comply with GDPR and privacy by design principles.

### Provider Details
- **Plausible Analytics**: Embedded lightweight script (~1KB) measuring aggregate route pageviews, referrer channels, and conversion completions.
- **Environment Configuration**: `NEXT_PUBLIC_PLAUSIBLE_DOMAIN` controls the target metrics domain.
- **Privacy Guarantees**: Zero fingerprinting, zero cross-site tracking, and zero personal data stored in persistent cookies.
