# Agent Engineering Research — 2026 guardrails

Last reviewed: 2026-09-23

Sources:
- GitHub — Agentic Workflows: https://github.blog/ai-and-ml/automate-repository-tasks-with-github-agentic-workflows/
- GitHub — security validation for third-party coding agents: https://github.blog/changelog/2026-06-09-security-validation-for-third-party-coding-agents/
- GitHub video — Introducing GitHub Agentic Workflows: https://www.youtube.com/watch?v=3_i03fGXs9U
- Microsoft Research video — GitHub Agentic Workflows: https://www.youtube.com/watch?v=W4oAJgZx7-U

The available public video pages supplied descriptions; no transcript-derived claim is promoted here unless separately verified.

## Reusable lessons

- Agent work should be inspectable: intent, inputs, outputs, provenance, validation result, and failure state must be visible.
- Automation needs bounded permissions and safe outputs. Agents should not overwrite shared artifacts concurrently.
- Agent-generated changes should receive the same security treatment as human changes: secret scanning, dependency review, static analysis where available, and ordinary CI.
- A failed check is not a reason to weaken the check. Repair the artifact/code or record a blocker.
- Repository automation should produce reviewable changes and evidence, not invisible "background intelligence".
- Parallelism is useful only when workstreams are independent and merge conflicts are explicitly handled.
