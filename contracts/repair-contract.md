# Repair Contract

Node 25 is reactive. Trigger it after tool failures, schema mismatches, timeouts, fallbacks, or repeated node failures. Read `session.log`, extract a minimal reproduction, add a regression, patch only the failed tool, run its existing tests plus the new case, keep or revert, and write `repair-report.json`. Never silently change public contracts or touch a tool that did not fail.
