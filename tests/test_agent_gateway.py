import json, os, tempfile, unittest
from pathlib import Path
from unittest.mock import patch
from vibe_code_genius.agent_gateway import discover_agents, create_task_packet

class AgentGatewayTests(unittest.TestCase):
    def test_human_bridge_always_available(self):
        agents={a.id:a for a in discover_agents()}
        self.assertTrue(agents["chatgpt-bridge"].available)
        self.assertEqual(agents["chatgpt-bridge"].mode,"human-bridge")

    def test_antigravity_is_not_fabricated(self):
        with patch.dict(os.environ,{},clear=True):
            agents={a.id:a for a in discover_agents()}
            self.assertFalse(agents["antigravity"].available)
            self.assertEqual(agents["antigravity"].mode,"manual")

    def test_task_packet_is_bounded(self):
        with tempfile.TemporaryDirectory() as d:
            repo=Path(d)/"repo"; repo.mkdir()
            out=Path(d)/"task.json"
            create_task_packet("Fix auth",repo,out,allowed=["src/auth/**"],
                               forbidden=["src/ui/**"],acceptance=["tests pass"])
            data=json.loads(out.read_text())
            self.assertEqual(data["policy"]["cost"],"zero-cost-first")
            self.assertEqual(data["allowed_paths"],["src/auth/**"])
            self.assertEqual(data["forbidden_paths"],["src/ui/**"])
            self.assertEqual(data["acceptance"],["tests pass"])

if __name__=="__main__":
    unittest.main()
