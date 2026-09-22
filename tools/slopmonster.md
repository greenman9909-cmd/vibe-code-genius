# SlopMonster

Repository: `github.com/ItsssssJack/SlopMonster`.

SlopMonster is not a pip console package. Clone it and point Vibe Code Genius at the repository:

```bash
git clone https://github.com/ItsssssJack/SlopMonster.git
export SLOPMONSTER_HOME=/path/to/SlopMonster
python "$SLOPMONSTER_HOME/tools/deslop.py" page.html
```

Windows PowerShell:

```powershell
$env:SLOPMONSTER_HOME='C:\path\to\SlopMonster'
python "$env:SLOPMONSTER_HOME\tools\deslop.py" page.html
```

Vibe Code Genius exposes the same gate as:

```bash
vibe-tree check-tools --all
vibe-tree slop-check page.html
```

The scorer checks AI vocabulary/constructions, punctuation cadence, rule-of-three rhythm, and unsupported proof. It exits non-zero below 5/5. `--allow-proof` is available only when the numbers/claims are actually evidenced.

The rival-model cleanse remains SlopMonster's own workflow (`tools/cleanse.sh`); Vibe Code Genius does not pretend to have run that cleanse unless the command actually executed.

## Contract

Lint results are evidence. Rewrites remain subject to the tree's integrity and no-invented-proof rules.
