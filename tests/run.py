#!/usr/bin/env python3
from pathlib import Path
import subprocess, sys, tempfile
root=Path(__file__).resolve().parents[1]
with tempfile.TemporaryDirectory() as d:
    out=Path(d)/'prompt.md'; subprocess.run([sys.executable,str(root/'scripts/build-prompt.py'),str(root/'tests/inputs/structure.json'),str(root/'tests/inputs/product.json'),str(out)],check=True,cwd=root)
    expected=(root/'tests/expected/.prompt.md').read_text(); actual=out.read_text()
    if expected != actual: print('golden prompt mismatch'); sys.exit(1)
print('prompt golden test passed')
