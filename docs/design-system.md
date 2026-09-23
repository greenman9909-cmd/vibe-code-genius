# GodTree OS — Interface System v0.1

The product should borrow SlopMonster's strongest product lesson, not its visual identity: one obvious loop, deterministic gates around model work, evidence instead of claims, and graceful fallback when an AI is unavailable.

## Information architecture

Primary navigation is intentionally small:
- Projects
- Work
- Git
- Activity

Everything else is contextual:
- Agents live inside Work.
- Browser verification lives inside a mission or project.
- Deployments live inside a project.
- Knowledge is searchable from the command palette and project inspector.
- Settings and integrations live in the account/system menu.

The sidebar must never become a catalogue of implementation subsystems.

## Shell

Desktop shell:
- 52px title/command rail
- 224px collapsible project rail
- flexible work canvas
- optional 320px inspector panel
- bottom status strip only when a process is active

Default project screen is not a dashboard. It is a workspace:
project name / branch / sync state → primary work surface → contextual inspector.

## Icons

One icon grammar only. Use Lucide-style 1.75px outline geometry as the reference grammar; final assets are vendored SVGs so the desktop product has no icon-CDN dependency.

Rules:
- 16px navigation/action icons
- 14px dense metadata icons
- 20px empty-state icons
- no emoji
- no filled/outline mixing
- no decorative sparkle/brain/robot icons
- color never carries meaning without shape/text
- destructive actions use the same icon weight, not louder artwork
- logos for external providers are visually separated from product icons

Core semantic map:
Projects=folder; Work=workflow/play; Git=git-branch; Activity=activity; search=search; command=terminal-square; inspect=scan-search; diff=git-compare; commit=git-commit-horizontal; pull request=git-pull-request; tests=check-circle; browser=panel-top; deploy=rocket; rollback=history; settings=settings-2.

## Typography

Use a neutral grotesk for UI and a true monospace for code/diffs. No display font inside the product. Hierarchy comes from size, weight, spacing and contrast.

Scale:
11 metadata
12 dense controls
13 default UI
15 emphasized UI
20 project/mission title
28 exceptional empty/onboarding title

## Color

Base surfaces are near-black neutrals, not blue-black sci-fi panels.
Accent is one cool spectral hue used sparingly for focus, selected state and progress.
Green = verified pass only.
Amber = waiting/attention.
Red = destructive/failure.
Purple/blue gradients are prohibited as generic decoration.

## Components

Every primitive needs hover, focus-visible, active, disabled, loading, success and error states where applicable:
Button, IconButton, Input, CommandPalette, Tabs, Tree, DataTable, Diff, Drawer, Dialog, Toast, Tooltip, Progress, ProcessLog, StatusPill, EmptyState, SplitPane, ContextMenu.

Cards are not a default layout primitive. Use sections, lists, split panes and tables first.

## Motion

120–180ms for direct manipulation.
180–240ms for panel transitions.
Spring only for drag/reorder.
No continuous ambient animation in the app.
Progress animation must correspond to real execution.
Respect prefers-reduced-motion.

## The core loop

Every project makes the operating loop obvious:

INSPECT → PLAN → EXECUTE → VERIFY → REVIEW → COMMIT

An AI can help at PLAN/EXECUTE/REVIEW, but deterministic gates own INSPECT facts, VERIFY results and Git receipts.

## Design acceptance gate

A screen fails review if:
- more than four primary navigation destinations are visible;
- icon families or stroke weights are mixed;
- a card can be replaced by spacing/divider/list semantics;
- status is conveyed by color alone;
- a fake activity/progress state exists;
- decorative gradients/glows compete with code/diff/work content;
- an autonomous mutation cannot be traced to a receipt;
- a frequent action requires more than two navigational hops;
- keyboard focus is unclear;
- the layout breaks at 1280×720.
