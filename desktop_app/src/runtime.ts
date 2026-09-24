export type NodeState = "blocked" | "ready" | "running" | "succeeded" | "failed";

export interface TreeNode {
  id: string;
  name: string;
  tier: number;
  prereqs: string[];
  parallel_with?: string[];
  expected_artifact_path?: string;
  artifact_schema?: string;
}

export interface TreeContract { version: string; node_count: number; nodes: TreeNode[]; }

export interface RuntimeNode extends TreeNode { state: NodeState; }

export function buildRuntime(contract: TreeContract, completed = new Set<string>()): RuntimeNode[] {
  return contract.nodes.map((node) => ({
    ...node,
    state: completed.has(node.id)
      ? "succeeded"
      : node.prereqs.every((id) => completed.has(id))
        ? "ready"
        : "blocked",
  }));
}

export function runnable(nodes: RuntimeNode[]): RuntimeNode[] {
  return nodes.filter((node) => node.state === "ready");
}

export function validateContract(contract: TreeContract): string[] {
  const ids = new Set(contract.nodes.map((n) => n.id));
  const errors: string[] = [];
  if (ids.size !== contract.nodes.length) errors.push("duplicate node ids");
  for (const node of contract.nodes) {
    for (const prereq of node.prereqs) if (!ids.has(prereq)) errors.push(`${node.id}: missing prereq ${prereq}`);
  }
  return errors;
}
