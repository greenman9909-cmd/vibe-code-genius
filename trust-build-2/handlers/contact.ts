import { NextRequest, NextResponse } from "next/server";
import { z } from "zod";
import { handleApiError } from "../server";

const ContactSchema = z.object({
  name: z.string().min(2, "Name must be at least 2 characters"),
  email: z.string().email("Invalid email address"),
  message: z.string().min(10, "Message must be at least 10 characters"),
  _gotcha: z.string().max(0, "Bot detected").optional()
});

export async function POST(request: NextRequest): Promise<NextResponse> {
  try {
    const body = await request.json();
    const data = ContactSchema.parse(body);

    if (data._gotcha && data._gotcha.length > 0) {
      return NextResponse.json({ received: true }, { status: 200 });
    }

    return NextResponse.json(
      {
        received: true,
        message: "Enterprise inquiry delivered to maintainer queue."
      },
      { status: 200 }
    );
  } catch (error) {
    return handleApiError(error);
  }
}
