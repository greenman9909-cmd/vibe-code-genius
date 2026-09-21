/**
 * Next.js Server Runtime & Error Infrastructure
 */

import { NextResponse } from "next/server";
import { ZodError } from "zod";

export interface StandardErrorResponse {
  error: string;
  details?: any;
  status: number;
}

export function handleApiError(error: unknown): NextResponse<StandardErrorResponse> {
  console.error("[API_ERROR]", error);

  if (error instanceof ZodError) {
    return NextResponse.json(
      {
        error: "Validation error: invalid request payload",
        details: error.flatten(),
        status: 400
      },
      { status: 400 }
    );
  }

  if (error instanceof Error) {
    if (error.message.includes("Rate limit")) {
      return NextResponse.json(
        {
          error: "Rate limit exceeded. Please retry shortly.",
          status: 429
        },
        { status: 429 }
      );
    }

    return NextResponse.json(
      {
        error: error.message || "Internal server disruption",
        status: 500
      },
      { status: 500 }
    );
  }

  return NextResponse.json(
    {
      error: "An unknown infrastructure failure occurred",
      status: 500
    },
    { status: 500 }
  );
}
