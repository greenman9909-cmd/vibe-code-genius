# Node 18e — Security Verify

Tier: 4  Prereqs: [18d]  Parallel with: [23b]  Input: harden report + preview  Output: security-verify.json  Model: sonnet  Budget: 2500 tokens

## Working Contract

Independently verify the post-hardening application. This node validates outcomes; it does not trust the hardening report's claims.

## Instructions

1. Re-run every blocking/high-risk check from the review against the repaired build.
2. Re-test negative authorization cases, auth/session boundaries, database/RLS restrictions, browser security controls, external input handling and secrets exposure relevant to the app.
3. Verify security regressions with the actual test/runtime path whenever tools permit; source inspection alone is insufficient for behavior claims.
4. Record accepted risks explicitly with owner/rationale when the product allows them. Accepted risk is not the same as fixed.
5. Produce `security-verify.json` with `stage: verification`, evidence per check, remaining findings and final pass state.

## Output Contract

`security-verify.json` must satisfy `schema/security_report.schema.json`; a passing report has zero blocking findings.

Before marking complete:

python scripts/validate-artifact.py --node 18e --artifact security-verify.json --schema schema/security_report.schema.json

## If this fails

Block the final ship gate and return the issue to hardening with a minimal reproduction.
