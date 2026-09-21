# generic integration

1. Copy the repository into the platform's project context.
2. Keep `contracts/`, `nodes/`, `schema/`, and `skill-tree.json` together.
3. Configure the platform to load `SKILL.md` or the equivalent entry file once.
4. Run `python scripts/validate-tree.py` before the first build.
5. Store artifacts and `session.log` in the session directory.

Platform-specific behavior belongs here, not in node files.
