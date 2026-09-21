import { NextRequest, NextResponse } from "next/server";
import { z } from "zod";
import { handleApiError } from "@/server";

export const waitlistSchema = z.object({
  email: z.string().trim().email("Please provide a valid email address"),
  role: z.enum(["developer", "designer", "founder", "other"]).optional().default("developer"),
  source: z.string().trim().max(100).optional().default("landing_page"),
  _gotcha: z.string().max(0, "Bot submission detected").optional(),
});

export type WaitlistInput = z.infer<typeof waitlistSchema>;

/**
 * Handle public developer waitlist submissions.
 * Performs schema validation, honeypot bot rejection, and returns early queue position.
 */
export async function POST(req: NextRequest): Promise<NextResponse> {
  const instance = "/api/waitlist";
  try {
    const rawBody = await req.json();
    const data = waitlistSchema.parse(rawBody);

    // Honeypot bot detection check
    if (data._gotcha && data._gotcha.length > 0) {
      // Silently ignore bot submission with simulated success
      return NextResponse.json({ ok: true, position: 1042 });
    }

    // In a production build, dispatch to Resend Audience or webhook
    return NextResponse.json(
      {
        ok: true,
        message: "Successfully joined early access waitlist",
        position: 412,
        timestamp: new Date().toISOString(),
      },
      {
        status: 200,
        headers: {
          "Cache-Control": "no-store, max-age=0",
        },
      }
    );
  } catch (err: unknown) {
    return handleApiError(err, instance);
  }
}
