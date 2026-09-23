import json
import tempfile
import unittest
from pathlib import Path

from vibe_code_genius.engine import load_tree, plan
from vibe_code_genius.runtime import ready_nodes, refresh_status, validate_artifact, write_task_packet


class RuntimeTests(unittest.TestCase):
    def setUp(self):
        self.root = Path(__file__).resolve().parents[1]
        self.tree = load_tree(self.root)

    def test_fresh_session_exposes_only_node_01(self):
        with tempfile.TemporaryDirectory() as d:
            out = Path(d)
            plan("Build a product", out, self.root)
            ready = ready_nodes(self.root, out, self.tree)
            self.assertEqual([n["id"] for n in ready], ["01"])

    def test_task_packet_contains_real_skill_and_schema(self):
        with tempfile.TemporaryDirectory() as d:
            out = Path(d)
            plan("Build a product", out, self.root)
            node = ready_nodes(self.root, out, self.tree)[0]
            task = write_task_packet(self.root, out, node)
            data = json.loads(task.read_text())
            self.assertEqual(data["node"], "01")
            self.assertEqual(data["artifact_schema"], "schema/intent.schema.json")
            self.assertIn("Intent Parse", data["instructions"])
            self.assertIn("Do not invent evidence", " ".join(data["rules"]))

    def test_invalid_existing_artifact_fails_session(self):
        with tempfile.TemporaryDirectory() as d:
            out = Path(d)
            plan("Build a product", out, self.root)
            (out / "intent.json").write_text("{}\n")
            session = refresh_status(self.root, out, self.tree)
            self.assertEqual(session["status"], "failed")
            self.assertEqual(session["nodes"]["01"]["status"], "failed")

    def test_validate_artifact_accepts_schema_valid_intent(self):
        with tempfile.TemporaryDirectory() as d:
            out = Path(d)
            node = next(n for n in self.tree["nodes"] if n["id"] == "01")
            artifact = {
                "status": "complete",
                "version": "1.0.0",
                "product_name": "Example",
                "product_type": "web app",
                "target_user": "developers",
                "key_flows": ["create a project", "review output"],
                "evidence": ["user request"],
            }
            (out / "intent.json").write_text(json.dumps(artifact))
            ok, errors = validate_artifact(self.root, out, node)
            self.assertTrue(ok, errors)


if __name__ == "__main__":
    unittest.main()
