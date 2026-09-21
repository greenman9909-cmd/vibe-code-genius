#!/usr/bin/env python3
import subprocess, sys
from pathlib import Path
root=Path(__file__).resolve().parents[1]
checks=[[sys.executable,str(root/'scripts/validate-tree.py')],[sys.executable,str(root/'scripts/validate-structure.py')],[sys.executable,str(root/'tests/run.py')]]
for cmd in checks: subprocess.run(cmd,check=True,cwd=root)
print('3 golden checks passed')
