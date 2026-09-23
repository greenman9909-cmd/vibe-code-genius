from __future__ import annotations

import json
from dataclasses import dataclass, asdict
from pathlib import Path

IGNORED = {'.git', 'node_modules', '.next', 'dist', 'build', '.godtree'}

@dataclass
class GraphNode:
    path: str
    kind: str
    label: str


def scan_project(root: Path) -> dict:
    root = root.resolve()
    nodes = []
    for item in root.rglob('*'):
        if item.is_file() and not any(part in IGNORED for part in item.parts):
            rel = str(item.relative_to(root))
            nodes.append(asdict(GraphNode(rel, 'file', item.name)))
    return {
        'version': '1.0.0',
        'project': root.name,
        'nodes': nodes,
        'node_count': len(nodes)
    }


def save_graph(root: Path, output: Path) -> Path:
    data = scan_project(root)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(data, indent=2), encoding='utf-8')
    return output
