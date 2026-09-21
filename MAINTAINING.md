# Maintaining vibe-code-genius

Schemas are versioned contracts. Run `python scripts/validate-tree.py`, `python tests/golden.py`, and `python tests/run.py` before every release. Add a golden case for every node behavior change. Preserve retired nodes and schemas. Refresh reference metadata weekly and review failure statistics quarterly.
