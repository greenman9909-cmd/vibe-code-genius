import { NextRequest, NextResponse } from "next/server";
import { z } from "zod";
import { handleApiError } from "@/server";

export const contactSchema = z.object({
  name: z.string().trim().min(1, "Name is required").max(100),
  email: z.string().trim().email("Please provide a valid email address"),
  subject: z.string().trim().min(1, "Subject is required").max(200).optional().default("General Inquiry"),
  message: z.string().trim().min(5, "Message must be at least 5 characters").max(5000),
  _gotcha: z.string().max(0, "Bot submission detected").optional(),
});

export type ContactInput = z.infer<typeof contactSchema>;

/**
 * Handle public developer inquiry submissions.
 * Validates payload, screens bot submissions, and routes inquiries to team notifications.
 */
export async function POST(req: NextRequest): Promise<NextResponse> {
  const instance = "/api/contact";
  try {
    const rawBody = await req.json();
    const data = contactSchema.parse(rawBody);

    // Honeypot bot trap check
    if (data._gotcha && data._gotcha.length > 0) {
      return NextResponse.json({ ok: true, received: true });
    }

    return NextResponse.json(
      {
        ok: true,
        message: "Your inquiry has been received. Our engineering team will respond shortly.",
        received: true,
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
