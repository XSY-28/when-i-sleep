"""Fixed acceptance checks. Run from this directory with Python 3."""

import argparse
import cart


def check_totals():
    assert cart.subtotal([2, 3]) == 5
    assert cart.subtotal([]) == 0
    assert cart.subtotal([1.5, 2.5, 1]) == 5


def check_receipt():
    check_totals()
    assert cart.receipt([2, 3]) == {"items": 2, "subtotal": 5}
    assert cart.receipt([]) == {"items": 0, "subtotal": 0}


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("stage", choices=["totals", "receipt"])
    args = parser.parse_args()
    {"totals": check_totals, "receipt": check_receipt}[args.stage]()
    print(f"{args.stage}: passed")
