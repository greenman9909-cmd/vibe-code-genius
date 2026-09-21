// Typed API client for Vibe Code Genius public endpoints

export interface ApiResponse<T = unknown> {
  ok: boolean;
  data?: T;
  error?: string;
}

export interface WaitlistPayload {
  email: string;
  role?: string;
  source?: string;
}

export interface ContactPayload {
  name: string;
  email: string;
  subject: string;
  message: string;
}

export class ApiClient {
  private baseUrl: string;

  constructor(baseUrl: string = "") {
    this.baseUrl = baseUrl;
  }

  async request<T>(path: string, init?: RequestInit): Promise<ApiResponse<T>> {
    try {
      const res = await fetch(`${this.baseUrl}${path}`, {
        headers: { "Content-Type": "application/json" },
        ...init,
      });
      const data = await res.json();
      if (!res.ok) return { ok: false, error: data.error || "Request failed" };
      return { ok: true, data };
    } catch (err: any) {
      return { ok: false, error: err.message || "Network error" };
    }
  }

  async joinWaitlist(payload: WaitlistPayload): Promise<ApiResponse<{ position: number }>> {
    return this.request<{ position: number }>("/api/waitlist", {
      method: "POST",
      body: JSON.stringify(payload),
    });
  }

  async submitContact(payload: ContactPayload): Promise<ApiResponse<{ received: boolean }>> {
    return this.request<{ received: boolean }>("/api/contact", {
      method: "POST",
      body: JSON.stringify(payload),
    });
  }

  async checkHealth(): Promise<ApiResponse<{ status: string; timestamp: string }>> {
    return this.request<{ status: string; timestamp: string }>("/api/health");
  }
}

export const api = new ApiClient();
