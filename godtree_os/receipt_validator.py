from __future__ import annotations

import json
import subprocess
import time
from pathlib import Path


def run_validator(workspace: Path, command: list[str], output: Path):
    start = time.time()
    result = subprocess.run(command, cwd=workspace, capture_output=True, text=True)
    receipt = {
        "command": command,
        "status": "passed" if result.returncode == 0 else "failed",
        "exit_code": result.returncode,
        "duration_ms": int((time.time() - start) * 1000),
        "stdout": result.stdout[-5000:],
        "stderr": result.stderr[-5000:]
    }
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(receipt, indent=2))
    return receipt
