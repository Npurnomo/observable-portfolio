"""Check the bundled offline fixtures without models, keys, or dependencies."""

from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path

from routeval import Harness

ROOT = Path(__file__).parent


def main() -> None:
    for folder in sorted((ROOT / "examples").iterdir()):
        config = json.loads((folder / "routeval.json").read_text())
        name = "trial_" + folder.name.replace("-", "_")
        spec = importlib.util.spec_from_file_location(name, folder / "pipeline.py")
        if spec is None or spec.loader is None:
            raise RuntimeError(f"Cannot load {folder.name}")
        module = importlib.util.module_from_spec(spec)
        sys.modules[name] = module
        spec.loader.exec_module(module)
        kwargs = {
            "auto_routes": config["auto_routes"],
            "escalation_routes": config["escalation_routes"],
            "cost_basis": config["cost_basis"],
            "runs_dir": folder / "runs",
        }
        baseline = Harness(module.evaluate, **kwargs).run(folder / "golden.jsonl")
        regressed = Harness(module.missed_escalation, **kwargs).run(
            folder / "golden.jsonl", baseline=baseline
        )
        assert baseline["aggregates"]["accuracy_attempted"] == 1
        assert baseline["aggregates"]["routing"]["escalation_recall"] == 1
        assert regressed["aggregates"]["accuracy_attempted"] == 1
        assert regressed["aggregates"]["routing"]["escalation_recall"] == 0.5
        assert regressed["baseline"]["exit_code"] == 1
        print(f"PASS {folder.name}: five correct answers; missed escalation fails comparison")
    print("All bundled fixtures passed. External-user trials remain to be conducted.")


if __name__ == "__main__":
    main()
