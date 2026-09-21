#!/usr/bin/env python3
import shutil, sys
from pathlib import Path
src=Path(sys.argv[1]); dst=Path(sys.argv[2]) if len(sys.argv)>2 else Path('.artifacts/rollback')
if not src.exists(): raise SystemExit(f'missing checkpoint: {src}')
if dst.exists(): shutil.rmtree(dst)
shutil.copytree(src,dst); print(dst)
