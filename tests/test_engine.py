import tempfile
import unittest
from pathlib import Path

from vibe_code_genius.engine import load_tree, plan, topo_order


class EngineTests(unittest.TestCase):
    def test_tree_order(self):
        root = Path(__file__).resolve().parents[1]
        tree = load_tree(root)
        order = topo_order(tree)
        self.assertEqual(len(order), 62)
        self.assertIn("11f", order)
        self.assertLess(order.index("01"), order.index("01a"))
        self.assertLess(order.index("02"), order.index("02b"))
        self.assertLess(order.index("02"), order.index("11f"))

    def test_plan_defaults_to_required_nodes_only(self):
        root = Path(__file__).resolve().parents[1]
        with tempfile.TemporaryDirectory() as d:
            result = plan(
                "Build a dashboard",
                Path(d),
                root,
                reference_url="https://example.com",
            )
            self.assertEqual(result["nodes"], 60)
            self.assertTrue((Path(d) / "plan.md").exists())
            self.assertTrue((Path(d) / "request.json").exists())
            self.assertTrue((Path(d) / "session.json").exists())
            self.assertFalse((Path(d) / "intent.json").exists())
            self.assertEqual(result["reference_url"], "https://example.com")

    def test_plan_can_activate_optional_reference_nodes(self):
        root = Path(__file__).resolve().parents[1]
        with tempfile.TemporaryDirectory() as d:
            result = plan(
                "Build a reference-led site",
                Path(d),
                root,
                reference_url="https://example.com",
                features=["deep_reference", "clone_extract"],
            )
            self.assertEqual(result["nodes"], 62)
            self.assertIn("02b", result["order"])
            self.assertIn("11f", result["order"])


if __name__ == "__main__":
    unittest.main()
