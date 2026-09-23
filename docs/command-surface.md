# Command Surface

The GUI and CLI should converge on the same operations.

| Command | Purpose |
|---|---|
| project add | register a local workspace/repository |
| project inspect | map stack, scripts, routes and health |
| mission new | create an execution graph from a goal |
| mission resume | continue a paused mission from receipts |
| agents | inspect available executors |
| task | export a bounded agent task |
| git status | inspect branch and working tree |
| git diff | inspect changes before mutation |
| git branch | create an isolated feature branch |
| git commit | commit selected verified changes |
| git push | push after policy/confirmation gate |
| pr create | create a pull request from the mission branch |
| verify | run declared validators and attach receipts |
| browser verify | exercise web flows and capture evidence |
| deploy | deploy through an explicit provider adapter |
| rollback | restore a mission checkpoint |

The implementation rule is simple: UI buttons call typed operations; typed operations produce receipts; the activity feed renders receipts. The UI must never invent execution state.
