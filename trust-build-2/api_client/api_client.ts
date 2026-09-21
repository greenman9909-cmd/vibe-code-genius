/**
 * API Client Implementation for Vibe Code Genius
 */

export interface ApiResponse<T = any> {
  data?: T;
  error?: string;
  status: number;
}

export interface WaitlistPayload {
  email: string;
}

export interface WaitlistResponse {
  position: number;
  token: string;
}

export interface ContactPayload {
  name: string;
  email: string;
  message: string;
}

export interface ContactResponse {
  received: boolean;
}

export class ApiClient {
  private baseUrl: string;

  constructor(baseUrl: string = "") {
    this.baseUrl = baseUrl;
  }

  public async joinWaitlist(payload: WaitlistPayload): Promise<ApiResponse<WaitlistResponse>> {
    try {
      const res = await fetch(`${this.baseUrl}/api/waitlist`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(payload)
      });
      const data = await res.json();
      return { data, status: res.status };
    } catch (err: any) {
      return { error: err.message || "Network error", status: 500 };
    }
  }

  public async submitContact(payload: ContactPayload): Promise<ApiResponse<ContactResponse>> {
    try {
      const res = await fetch(`${this.baseUrl}/api/contact`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(payload)
      });
      const data = await res.json();
      return { data, status: res.status };
    } catch (err: any) {
      return { error: err.message || "Network error", status: 500 };
    }
  }

  public async checkHealth(): Promise<ApiResponse<{ status: string; uptime: number }>> {
    try {
      const res = await fetch(`${this.baseUrl}/api/health`);
      const data = await res.json();
      return { data, status: res.status };
    } catch (err: any) {
      return { error: err.message || "Health check failed", status: 500 };
    }
  }
}

export const api = new ApiClient();
