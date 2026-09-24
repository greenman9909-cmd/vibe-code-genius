import React, { useMemo, useState } from "react";
import { invoke } from "@tauri-apps/api/core";
import tree from "../../skill-tree.json";
import { buildRuntime, runnable, validateContract, type TreeContract } from "./runtime";
import "./app.css";

type Snapshot = { workspace:string; name:string; branch?:string; dirty:boolean; changed_files:string[]; godtree_store:boolean };
const nav = ["Command", "Projects", "Missions", "Agents", "Evidence", "Git", "Tools"];

export default function App() {
  const contract = tree as TreeContract;
  const [completed, setCompleted] = useState<Set<string>>(new Set());
  const [workspace,setWorkspace]=useState("");
  const [snapshot,setSnapshot]=useState<Snapshot|null>(null);
  const [nativeError,setNativeError]=useState("");
  const nodes = useMemo(() => buildRuntime(contract, completed), [contract, completed]);
  const ready = runnable(nodes);
  const errors = validateContract(contract);

  async function connectRepo(){ setNativeError(""); try { setSnapshot(await invoke<Snapshot>("inspect_project",{workspace})); } catch(e){ setNativeError(String(e)); } }

  function complete(id: string) {
    setCompleted((current) => new Set([...current, id]));
  }

  return <div className="shell">
    <aside>
      <div className="brand"><span>GT</span><strong>GodTree</strong></div>
      <nav>{nav.map((item, i) => <button className={i === 0 ? "active" : ""} key={item}>{item}</button>)}</nav>
      <div className="health"><i /> Runtime contract<br/><small>{errors.length ? errors.join(", ") : "verified locally"}</small></div>
    </aside>
    <main>
      <header><div><p className="eyebrow">AGENTIC DEVELOPMENT OS</p><h1>Command Center</h1></div><div className="connect"><input value={workspace} onChange={e=>setWorkspace(e.target.value)} placeholder="C:\\path\\to\\repository"/><button className="primary" onClick={connectRepo}>Connect repo</button></div></header>{nativeError&&<div className="error">{nativeError}</div>}
      <section className="hero">
        <div><span className="status">TREE ONLINE</span><h2>{contract.node_count} contract nodes.<br/>One execution graph.</h2><p>GodTree exposes the repository's real dependency graph instead of inventing activity. Nodes unlock only when their declared prerequisites are satisfied.</p></div>
        <div className="orb"><b>{ready.length}</b><span>READY</span></div>
      </section>
      <section className="grid">
        <article className="panel span2"><div className="panelHead"><div><p className="eyebrow">LIVE TREE</p><h3>Execution surface</h3></div><span>{completed.size}/{contract.nodes.length}</span></div>
          <div className="nodes">{nodes.slice(0,18).map(node => <button key={node.id} className={"node "+node.state} disabled={node.state!=="ready"} onClick={()=>complete(node.id)}><span>{node.id}</span><strong>{node.name}</strong><small>{node.state}</small></button>)}</div>
        </article>
        <article className="panel"><p className="eyebrow">RUNNABLE NOW</p><h3>Scheduler queue</h3><div className="queue">{ready.slice(0,8).map(n=><div key={n.id}><span>{n.id}</span><b>{n.name}</b><em>T{n.tier}</em></div>)}</div></article>
        <article className="panel"><p className="eyebrow">TRUST MODEL</p><h3>Validator-owned success</h3><p className="muted">Agents propose work. Contracts, artifacts and validators decide whether it advances.</p><div className="metric"><b>{errors.length}</b><span>contract errors</span></div></article>
        <article className="panel"><p className="eyebrow">PROJECT</p><h3>vibe-code-genius</h3><p className="muted">Branch-aware control plane for missions, Git operations, evidence and build receipts.</p><div className="tags"><span>Git</span><span>Evidence</span><span>Agents</span><span>Windows</span></div></article>
      </section>
    </main>
  </div>;
}
