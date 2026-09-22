# Walkthroughs — Operational Experience

This directory is the God Tree's **experience memory**.

A walkthrough records what actually happened during a non-trivial build: the request, scope, tools used, artifacts produced, validation results, failures, corrections, and reusable lessons. The goal is to let future agents benefit from prior runs without turning old observations into new evidence.

## Rule: experience is not evidence

Past experience may influence **strategy**:

- which acquisition tool to try first after the required policy checks;
- which failure modes to watch for;
- where a tool is likely to produce noisy output;
- which validators caught useful problems before;
- when a simpler implementation is sufficient.

Past experience must never be used as **current factual evidence** for a new build.

A previous crawl does not prove a current route still exists. A previous API profile does not prove current authentication behavior. A previous screenshot does not prove the current design system. Node 02 provenance rules, schemas, validators, and contracts remain authoritative.

## Agent startup behavior

Before Node 01 on a substantial build:

1. Read `skill-tree.json`, the relevant contracts, and the requested tier.
2. Scan this index for a walkthrough with a similar target, toolchain, or failure mode.
3. Use relevant lessons as hypotheses or risk flags only.
4. Re-run the required acquisition and validation steps for the current session.
5. Record new findings in a new walkthrough when the run teaches something reusable.

## Promotion rule

A lesson becomes part of the core system only when it deserves to:

- **One run:** keep it in a walkthrough.
- **Repeated runs:** consider adding a reference note, validator, or test.
- **Behavior-changing rule:** version the contract/schema and add golden coverage.
- **Verified failure:** use Node 25 and promote the minimal reproduction to a regression test.

Do not silently convert one agent's preference into a global contract.

## Field reports

- [2026-09-22 — Resend-inspired God Tree explainer](2026-09-22-resend-god-tree-explainer.md) — real build using the repo's own tree, Resend reference evidence, SiteMap-X data, SlopMonster, GitHub CI, and deployment attempts.
- `walkthrough-1.md` through `walkthrough-4.md` are legacy placeholders and should be replaced with real runs rather than copied forward.

## Recommended walkthrough format

Each report should contain:

- context and user intent;
- requested tier/actual scope;
- reference acquisition path and provenance;
- tools used and why;
- artifacts/checks completed;
- failures and environment constraints;
- corrections made;
- reusable lessons;
- anti-lessons (what future agents should not infer);
- commit/PR/run identifiers when available.

Prefer concrete observations over opinions.
