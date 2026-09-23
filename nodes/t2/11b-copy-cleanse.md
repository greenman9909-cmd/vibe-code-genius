# Node 11b — Copy Cleanse

Tier: 2  Prereqs: [11]  Parallel with: [12, 13]  Input: copy + design tokens  Output: slop-report.json  Model: haiku  Budget: 1800 tokens

## Working Contract

Read `contracts/working-contract.md` and `contracts/human-quality-contract.md`. Emit only the declared artifact, validate it, and keep evidence separate from judgment.

## Instructions

1. Inventory the actual user-facing copy available in the declared inputs. If there is no copy to audit, record that explicitly; do not invent sample phrases just to satisfy the node.
2. Use `references/signs-of-ai-writing.md` as a risk checklist, not as a word blacklist.
3. Flag copy only when context supports the finding. Look for generic claims, filler transitions, manufactured contrast, repetitive three-part slogans, fake precision, unsupported proof, needless section kickers, and wording that could belong to any product.
4. Preserve domain language, user terminology, legal text, reference copy intentionally locked by the project, and concise functional labels unless there is a concrete quality/accessibility problem.
5. For each finding choose one action: keep, rewrite, or remove. Explain why. A clean audit may legitimately contain zero eliminated phrases.
6. Errors, empty states, loading states, confirmations, destructive actions, and recovery messages must tell the user what happened and what they can do next.
7. Never manufacture metrics, testimonials, customer counts, awards, urgency, guarantees, or social proof.
8. Produce `slop-report.json` with evidence pointing to the inspected source/artifact and validate it before completion.

## Output Contract

`slop-report.json` must conform to `schema/slop-report.schema.json`. The score may be null when a meaningful numeric score is not justified; findings and evidence are authoritative.

Before marking complete:

python scripts/validate-artifact.py --node 11b --artifact slop-report.json --schema schema/slop-report.schema.json

## If this fails

Record the node id, input hash, invocation, error, and minimal reproduction in `session.log`. Do not weaken the schema or fabricate audit findings to make the node pass.

Do not invent pages, proof, metrics, integrations, credentials, routes, or reference evidence.