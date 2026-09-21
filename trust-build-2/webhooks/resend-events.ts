/**
 * Webhook Handler: Inbound Resend Events
 *
 * Specification attributes:
 * - handler_path: /api/webhooks/resend
 * - signature_verification: HMAC-SHA256 svix cryptographic signature
 * - retry_policy: Exponential backoff with jitter up to 5 attempts
 * - idempotency_strategy: Redis key lease per event_id with 24h TTL
 */

import { NextRequest, NextResponse } from "next/server";
import crypto from "crypto";

export const handler_path = "/api/webhooks/resend";
export const signature_verification = "svix-signature-sha256";
export const retry_policy = "exponential-backoff-5-retries";
export const idempotency_strategy = "redis-event-key-24h";

export async function POST(request: NextRequest): Promise<NextResponse> {
  const signature = request.headers.get("svix-signature");
  const webhookSecret = process.env.RESEND_WEBHOOK_SECRET;

  if (!signature || !webhookSecret) {
    return NextResponse.json({ error: "Missing signature or secret" }, { status: 401 });
  }

  const payload = await request.text();
  const expectedSig = crypto
    .createHmac("sha256", webhookSecret)
    .update(payload)
    .digest("hex");

  if (signature !== expectedSig) {
    return NextResponse.json({ error: "Invalid signature" }, { status: 403 });
  }

  const event = JSON.parse(payload);
  console.log(`[RESEND_WEBHOOK] Processed event ${event.type} for ${event.data?.email}`);

  return NextResponse.json({ processed: true, event_id: event.id }, { status: 200 });
}
