# Interaction architecture

## Project

Opening a project lands on its current work state, not analytics.

Header:
project / branch / sync / command palette / run action.

Canvas states:
1. clean repo → recent work + suggested deterministic inspections
2. dirty repo → diff-first workspace
3. active mission → mission execution workspace
4. failed validation → failure/evidence workspace
5. PR ready → review/commit/PR workspace

## Command palette

Ctrl+K is the fastest path to every command. Commands are capability-aware; unavailable actions explain why instead of disappearing.

Examples:
Open project
Inspect repository
Create mission
Run tests
Show diff
Create branch
Stage selected files
Commit staged changes
Prepare push
Create pull request
Open browser verification
Export task for ChatGPT
Use available local agent

## Git workspace

Three-pane optional layout:
changed files | diff | commit/PR inspector.

No AI-generated commit happens invisibly. Generated messages are suggestions. The exact staged diff remains visible before commit.

## Mission workspace

The mission graph is a compact horizontal/vertical execution trace, not a decorative flowchart. Selecting a node opens:
objective, inputs, executor, files, commands, evidence, output, validation and retry history.

## AI handoff

When no callable agent exists, the same mission node becomes a Human Bridge:
Copy task packet → use ChatGPT/other app → paste patch/result → GodTree validates locally.

The mission does not pretend the external app was automatically invoked.

## Empty states

Empty states teach one action, not five. Example:
“No project open.” → Open folder.
“No changes.” → Inspect project.
“Validation failed.” → Open first failure.

## Native feel

Window chrome, resize behavior, keyboard shortcuts, file dialogs, notifications and update flow should feel Windows-native even if the view layer is web technology.
