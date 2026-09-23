from pathlib import Path
import subprocess
import re

class WorktreeManager:
    """Creates isolated mission workspaces so agents never mutate the main checkout."""

    def __init__(self, repo: Path, root: Path):
        self.repo = repo.resolve()
        self.root = root.resolve()

    def create(self, mission_id: str):
        safe = re.sub(r'[^a-zA-Z0-9_-]', '-', mission_id)
        branch = f'godtree/{safe}'
        target = self.root / safe
        subprocess.run([
            'git','-C',str(self.repo),'worktree','add',
            '-b',branch,str(target),'HEAD'
        ], check=True, capture_output=True, text=True)
        return {
            'branch': branch,
            'workspace': str(target),
            'isolated': True
        }

    def remove(self, workspace: Path):
        subprocess.run([
            'git','-C',str(self.repo),'worktree','remove',str(workspace)
        ], check=True, capture_output=True, text=True)
