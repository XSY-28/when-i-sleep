"""Check the example's fixed acceptance contract in a disposable copy.

This script writes controlled candidate implementations; it does not run an
agent, create a scheduler, or establish overnight reliability.
"""

from pathlib import Path
import os
import shutil
import subprocess
import sys
import tempfile


ROOT = Path(__file__).resolve().parents[1]


def main():
    results = []
    with tempfile.TemporaryDirectory(prefix="when-i-sleep-example-") as directory:
        project = Path(directory) / "cart"
        shutil.copytree(ROOT / "examples/cart", project)
        acceptance_before = (project / "acceptance.py").read_bytes()

        def check(stage, expected_ok, label):
            env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1")
            result = subprocess.run(
                [sys.executable, "acceptance.py", stage], cwd=project,
                capture_output=True, text=True, timeout=15, env=env,
            )
            assert (result.returncode == 0) == expected_ok, (
                label, result.returncode, result.stdout, result.stderr,
            )
            results.append(label)

        check("totals", False, "reject broken subtotal")
        (project / "cart.py").write_text("def subtotal(prices):\n    return sum(prices)\n", encoding="utf-8")
        check("totals", True, "accept corrected subtotal")
        check("receipt", False, "reject missing receipt")
        (project / "cart.py").write_text(
            "def subtotal(prices):\n    return sum(prices)\n\n"
            "def receipt(prices):\n"
            "    return {'items': len(prices), 'subtotal': subtotal(prices)}\n",
            encoding="utf-8",
        )
        check("receipt", True, "accept receipt and subtotal regression")
        assert (project / "acceptance.py").read_bytes() == acceptance_before
    print(f"Example passed: {len(results)} acceptance cases; fixed checks unchanged")


if __name__ == "__main__":
    main()
