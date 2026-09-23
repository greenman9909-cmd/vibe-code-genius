from __future__ import annotations

import json
import uuid
from dataclasses import dataclass, asdict
from pathlib import Path
from datetime import datetime, timezone


@dataclass
class Project:
    name: str
    path: str
    id: str


class GodTreeCore:
    """Small local runtime foundation for GodTree OS."""

    def __init__(self, workspace: str):
        self.workspace = Path(workspace).resolve()
        self.store = self.workspace / '.godtree'
        self.store.mkdir(exist_ok=True)

    def register_project(self):
        project = Project(
            name=self.workspace.name,
            path=str(self.workspace),
            id=uuid.uuid4().hex[:12],
        )
        self._write('project.json', asdict(project))
        return project

    def create_mission(self, objective: str):
        mission = {
            'id': uuid.uuid4().hex[:12],
            'objective': objective,
            'created': datetime.now(timezone.utc).isoformat(),
            'stages': [
                'inspect', 'plan', 'execute',
                'verify', 'review', 'commit'
            ],
            'receipts': []
        }
        self._write(f'missions/{mission["id"]}.json', mission)
        return mission

    def _write(self, name, value):
        path = self.store / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(value, indent=2), encoding='utf-8')
