import { NextRequest, NextResponse } from "next/server";
import { z } from "zod";
import { handleApiError } from "../server";

const WaitlistSchema = z.object({
  email: z.string().email("Invalid email address format"),
  intended_use: z.string().optional()
});

export async function POST(request: NextRequest): Promise<NextResponse> {
  try {
    const rawBody = await request.json();
    const validatedData = WaitlistSchema.parse(rawBody);

    // Mock sequence assignment and queue persistence
    const assignedPosition = Math.floor(Math.random() * 50) + 1420;
    const registrationToken = `tok_${Math.random().toString(36).substring(2, 10)}`;

    return NextResponse.json(
      {
        success: true,
        email: validatedData.email,
        position: assignedPosition,
        token: registrationToken,
        message: "Developer priority waitlist registration confirmed."
      },
      { status: 200 }
    );
  } catch (error) {
    return handleApiError(error);
  }
}
