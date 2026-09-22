#!/usr/bin/env bash
set -euo pipefail
target="${2:-}"
if [[ "${1:-}" != "--target" || -z "$target" ]]; then
  echo "Usage: ./install.sh --target {cursor|claude|claude-project|claude-skill|custom-gpt|gemini|antigravity|aider|continue|generic}" >&2
  exit 2
fi

copy_skill_bundle() {
  local dest="$1"
  mkdir -p "$dest"
  cp SKILL.md "$dest/SKILL.md"
  cp -R contracts nodes schema tools skill-tree.json "$dest/"
}

case "$target" in
  cursor)
    mkdir -p .cursor/commands .cursor/vibe-code-genius
    cp SKILL.md .cursorrules
    cp integrations/cursor.md .cursor/commands/build-frontend.md
    cp -R contracts nodes schema tools skill-tree.json .cursor/vibe-code-genius/
    ;;
  claude|claude-project|claude-skill)
    copy_skill_bundle .claude/skills/vibe-code-genius
    ;;
  gemini)
    cp SKILL.md GEMINI.md
    mkdir -p .vibe-code-genius
    cp -R contracts nodes schema tools skill-tree.json .vibe-code-genius/
    ;;
  antigravity)
    mkdir -p hooks custom-agents .vibe-code-genius
    cp integrations/antigravity.md hooks/vibe-code-genius.md
    cp -R contracts nodes schema tools skill-tree.json .vibe-code-genius/
    printf '{"name":"Research Agent","skill":"vibe-code-genius","scope":"research"}\n' > custom-agents/research-agent.json
    ;;
  custom-gpt|aider|continue|generic)
    copy_skill_bundle .vibe-code-genius
    ;;
  *)
    echo "Unsupported target: $target" >&2
    exit 2
    ;;
esac

echo "Installed vibe-code-genius for $target."
echo "Run python scripts/validate-tree.py before starting a session."
echo "For reference-led builds, run vibe-tree check-tools and use vibe-tree ... --acquire."
