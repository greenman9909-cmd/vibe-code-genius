from __future__ import annotations
import json, uuid
from datetime import datetime, timezone
from pathlib import Path

STAGES=("inspect","plan","execute","verify","review","commit")
def _now():return datetime.now(timezone.utc).isoformat()

def create_mission(objective:str,workspace:Path,out:Path)->Path:
 if not objective.strip():raise ValueError("objective required")
 mid=uuid.uuid4().hex[:12]
 payload={"version":"1.0.0","id":mid,"objective":objective,"workspace":str(workspace.resolve()),"status":"pending",
 "created_at":_now(),"stages":[{"id":x,"status":"pending","receipts":[]} for x in STAGES]}
 out.mkdir(parents=True,exist_ok=True);path=out/f"{mid}.json"
 path.write_text(json.dumps(payload,indent=2)+"\n",encoding="utf-8");return path

def record_receipt(path:Path,stage:str,kind:str,status:str,evidence:dict)->dict:
 data=json.loads(path.read_text(encoding="utf-8"))
 if stage not in STAGES:raise ValueError("unknown stage")
 item=next(x for x in data["stages"] if x["id"]==stage)
 receipt={"at":_now(),"kind":kind,"status":status,"evidence":evidence}
 item["receipts"].append(receipt);item["status"]=status
 order=[x["status"] for x in data["stages"]]
 data["status"]="failed" if "failed" in order else ("complete" if all(x=="passed" for x in order) else "running")
 path.write_text(json.dumps(data,indent=2)+"\n",encoding="utf-8");return receipt
