# Product-first build order

The promotional website is deliberately downstream of the product.

1. Project Engine — register/inspect durable local workspaces.
2. Git Engine — status, diff, branch, explicit staging, commit; push remains confirmation-gated.
3. Mission Engine — DAG, receipts, pause/resume/retry/checkpoints.
4. Local Daemon — authenticated localhost API for filesystem/process/Git capabilities.
5. Validator Engine — build/test/lint/browser receipts; agents cannot self-certify.
6. Agent Router — deterministic local tools first, then supported agents/human bridge.
7. GitHub Adapter — repo/PR/checks/issues with explicit external-action policy.
8. Browser Lab — launch app, exercise flows, screenshots/network/console evidence.
9. Desktop UI — premium project/mission/Git/agent surfaces.
10. Windows packaging — Windows 10/11 installer and release pipeline.
11. Promotional website — generated from real product capabilities and real captured demos.

No marketing surface may advertise a capability that lacks a verified product receipt.
