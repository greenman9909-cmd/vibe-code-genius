from __future__ import annotations
from dataclasses import asdict,dataclass
from .agent_gateway import discover_agents
@dataclass(frozen=True)
class Route:
 executor:str; mode:str; reason:str; paid:bool=False
def route(capability:str,prefer:str|None=None)->dict:
 deterministic={"git","graph","inspect","test","build","lint","browser"}
 if capability in deterministic:return asdict(Route("godtree-local","deterministic","local capability owns this operation"))
 agents=discover_agents()
 if prefer:
  hit=next((x for x in agents if x.id==prefer and x.available),None)
  if hit:return asdict(Route(hit.id,hit.mode,"explicit available preference"))
 for x in agents:
  if x.available and x.mode not in {"human-bridge","manual"}:return asdict(Route(x.id,x.mode,"first available callable zero-cost/subscription agent"))
 bridge=next(x for x in agents if x.id=="chatgpt-bridge")
 return asdict(Route(bridge.id,bridge.mode,"no callable agent; export bounded task packet"))
