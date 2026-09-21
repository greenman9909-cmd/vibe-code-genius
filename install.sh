#!/usr/bin/env bash
set -euo pipefail
target="${2:-}"
if [[ "${1:-}" != "--target" || -z "$target" ]]; then echo "Usage: ./install.sh --target {cursor|claude|claude-project|claude-skill|custom-gpt|gemini|antigravity|aider|continue|generic}" >&2; exit 2; fi
case "$target" in
  cursor) mkdir -p .cursor/commands; cp SKILL.md .cursorrules; cp integrations/cursor.md .cursor/commands/build-frontend.md;;
  claude|claude-project|claude-skill) mkdir -p .claude/skills/vibe-code-genius; cp SKILL.md .claude/skills/vibe-code-genius/SKILL.md; cp -R contracts nodes schema skill-tree.json .claude/skills/vibe-code-genius/;;
  gemini) cp SKILL.md GEMINI.md;;
  antigravity) mkdir -p hooks custom-agents; cp integrations/antigravity.md hooks/vibe-code-genius.md; printf '{"name":"Research Agent","skill":"vibe-code-genius","scope":"research"}\n' > custom-agents/research-agent.json;;
  custom-gpt|aider|continue|generic) mkdir -p .vibe-code-genius; cp SKILL.md .vibe-code-genius/SKILL.md;;
  *) echo "Unsupported target: $target" >&2; exit 2;;
esac
echo "Installed vibe-code-genius for $target. Run python scripts/validate-tree.py before starting a session."
