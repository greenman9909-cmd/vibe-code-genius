import { NextResponse } from "next/server";
import { z } from "zod";

/**
 * RFC 7807 compliant Problem Details error representation.
 */
export interface ProblemDetails {
  type: string;
  title: string;
  status: number;
  detail: string;
  instance?: string;
  errors?: Record<string, string[]>;
}

/**
 * Standardized API error handler for Next.js route handlers.
 * Maps Zod validation errors, syntax errors, and unexpected exceptions
 * into structured RFC 7807 Problem Details payloads.
 */
export function handleApiError(err: unknown, instancePath?: string): NextResponse<ProblemDetails> {
  console.error(`[API Error] ${instancePath || "unknown route"}:`, err);

  if (err instanceof z.ZodError) {
    const formattedErrors: Record<string, string[]> = {};
    for (const issue of err.issues) {
      const key = issue.path.join(".") || "body";
      if (!formattedErrors[key]) formattedErrors[key] = [];
      formattedErrors[key].push(issue.message);
    }

    return NextResponse.json(
      {
        type: "https://vibe-code-genius.dev/errors/validation-error",
        title: "Unprocessable Entity",
        status: 422,
        detail: "The submitted request failed schema validation.",
        instance: instancePath,
        errors: formattedErrors,
      },
      { status: 422 }
    );
  }

  if (err instanceof SyntaxError) {
    return NextResponse.json(
      {
        type: "https://vibe-code-genius.dev/errors/malformed-json",
        title: "Bad Request",
        status: 400,
        detail: "The request body contains invalid JSON.",
        instance: instancePath,
      },
      { status: 400 }
    );
  }

  return NextResponse.json(
    {
      type: "https://vibe-code-genius.dev/errors/internal-server-error",
      title: "Internal Server Error",
      status: 500,
      detail: "An unexpected server error occurred while processing the request.",
      instance: instancePath,
    },
    { status: 500 }
  );
}
