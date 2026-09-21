# Resend SDK Integration Specification

## Resend Overview and Implementation
- Deliverable transactional email dispatch service for waitlist confirmation, notification delivery, and contact form forwarding.
- SDK: `resend` official npm package (`import { Resend } from "resend"`).
- Client Initialization:
  ```typescript
  export const resend = new Resend(process.env.RESEND_API_KEY);
  ```
- Environment Variables:
  - `RESEND_API_KEY`: Server-side secret key with restricted send permissions.
  - `RESEND_FROM_EMAIL`: Authorized verified domain sending address (e.g., `notifications@vibe-code-genius.dev`).
  - `RESEND_AUDIENCE_ID`: Target audience identifier for waitlist subscribers.

## Operational Workflows
1. **Waitlist Onboarding**:
   - Triggers automated double opt-in confirmation email to user.
   - Appends contact record to Resend Audience with custom tags `{ tier: "indie", source: "landing-page" }`.
2. **Contact Inquiry Relay**:
   - Validates user payload via Zod schema.
   - Dispatches structured Markdown email to internal routing inbox.

# Analytics Integration Strategy

## Cookieless Privacy-First Telemetry
- Client-side event forwarding via PostHog or Plausible cookieless edge proxy.
- Minimal payload tracking pageviews, scroll depth, and terminal interaction conversions without third-party cookies or fingerprinting.
- Respects `Do-Not-Track` header and global privacy controls by default.
- Custom events:
  - `waitlist_submitted`: Captured upon 200 OK response from `/api/waitlist`.
  - `contract_expanded`: Triggered when developer inspects contract specifications.
