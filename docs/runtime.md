# GodTree runtime

The current runtime is local-first.

- project graph: persistent/shared repository structure
- missions: inspect → plan → execute → verify → review → commit
- worktrees: isolated branch/workspace per mission
- validators: deterministic commands produce durable receipts
- router: deterministic operations stay local; callable agents are selected only for model work; ChatGPT bridge is the fallback
- local API: loopback-only read surface for the desktop UI

Start the local API with the CLI daemon command. It binds to 127.0.0.1 by default. Mutation endpoints are intentionally not exposed until per-session authentication and confirmation receipts are implemented.
