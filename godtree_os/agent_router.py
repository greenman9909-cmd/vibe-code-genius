from __future__ import annotations

from dataclasses import dataclass, asdict
import shutil

@dataclass
class Agent:
    name: str
    available: bool
    mode: str


def discover_agents():
    candidates = ['claude', 'gemini', 'codex', 'aider']
    return [asdict(Agent(x, shutil.which(x) is not None, 'local-cli')) for x in candidates]


def route(task_type: str):
    deterministic = {'scan', 'graph', 'test', 'git'}
    if task_type in deterministic:
        return {'executor': 'godtree-core', 'reason': 'deterministic operation'}
    for agent in discover_agents():
        if agent['available']:
            return {'executor': agent['name'], 'reason': 'available local agent'}
    return {'executor': 'human-bridge', 'reason': 'no callable local agent'}
