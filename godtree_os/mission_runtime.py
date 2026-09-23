from __future__ import annotations

import json
import uuid
from dataclasses import dataclass, asdict
from datetime import datetime, timezone
from pathlib import Path

STAGES = ["inspect", "plan", "execute", "verify", "review", "commit"]


def now():
    return datetime.now(timezone.utc).isoformat()


@dataclass
class Mission:
    id: str
    objective: str
    workspace: str
    status: str = "created"

    def save(self, root: Path):
        root.mkdir(parents=True, exist_ok=True)
        (root / f"{self.id}.json").write_text(json.dumps({**asdict(self), "stages": [{"name": s, "status": "pending", "receipts": []} for s in STAGES]}, indent=2))


def create_mission(objective: str, workspace: Path, root: Path):
    mission = Mission(uuid.uuid4().hex[:12], objective, str(workspace.resolve()))
    mission.save(root)
    return mission


def add_receipt(file: Path, stage: str, result: str, evidence: dict):
    data = json.loads(file.read_text())
    for item in data["stages"]:
        if item["name"] == stage:
            item["status"] = result
            item["receipts"].append({"time": now(), "evidence": evidence})
    file.write_text(json.dumps(data, indent=2))
