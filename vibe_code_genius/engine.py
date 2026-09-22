from __future__ import annotations
import json, hashlib
from pathlib import Path
from datetime import datetime, timezone

def load_tree(root: Path):
    return json.loads((root / "skill-tree.json").read_text())

def topo_order(tree):
    items={n["id"]:n for n in tree["nodes"]}; remaining=set(items); order=[]
    while remaining:
        ready=sorted(n for n in remaining if all(p not in remaining for p in items[n]["prereqs"]))
        if not ready: raise ValueError("cycle or missing prerequisite: " + ",".join(sorted(remaining)))
        order.extend(ready); remaining.difference_update(ready)
    return order

def artifact_hash(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True).encode()).hexdigest()[:12]

def now(): return datetime.now(timezone.utc).isoformat().replace("+00:00","Z")

def plan(intent: str, out: Path, root: Path, reference_url: str | None = None):
    out.mkdir(parents=True, exist_ok=True)
    tree=load_tree(root); order=topo_order(tree)
    data={"product_type":"custom","target_user":"unspecified","key_flows":[intent],"reference_url":reference_url,"vibe":"technical"}
    scope={"deliverable":"mvp","tier_stop":3,"routes_include":[],"routes_exclude":[],"time_budget_minutes":30}
    session={"session_id":artifact_hash({"intent":intent,"at":str(out)}),"started_at":now(),"intent":intent,"scope":"mvp","active_skills":["vibe-code-genius"],"artifacts":[],"checkpoints":[],"budget":{"nodes_count":len(order)},"why_log":[]}
    for name,value in (("intent.json",data),("scope.json",scope),("session.json",session)):
        (out/name).write_text(json.dumps(value, indent=2)+"\n")
    (out/"plan.md").write_text("# Build Plan\n\n"+"\n".join(f"{i+1}. Node {n}" for i,n in enumerate(order))+"\n")
    return {"out":str(out),"nodes":len(order),"order":order,"reference_url":reference_url}
