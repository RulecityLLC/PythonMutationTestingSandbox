#!/usr/bin/env python3
"""Exit 0 when mutation score >= threshold.

Usage:
  python mutation_score_check.py /path/to/file.json 80
"""
import argparse
import json
import sys
from pathlib import Path


def compute_score(data: dict) -> float:
    killed = data.get("killed")
    total = data.get("total")
    if killed is None or total is None:
        raise ValueError("JSON must contain 'killed' and 'total' fields")
    if total == 0:
        raise ZeroDivisionError("'total' is zero; cannot compute mutation score")
    return float(killed) * 100.0 / float(total)


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="Check mutation score against threshold")
    parser.add_argument("json_file", help="Path to mutation JSON file")
    parser.add_argument("threshold", help="Mutation score threshold (numeric)")
    args = parser.parse_args(argv)

    path = Path(args.json_file)
    if not path.exists():
        print(f"Error: file not found: {path}", file=sys.stderr)
        return 2

    try:
        with path.open("r", encoding="utf-8") as fh:
            data = json.load(fh)
    except Exception as e:
        print(f"Error reading JSON: {e}", file=sys.stderr)
        return 2

    try:
        score = compute_score(data)
    except Exception as e:
        print(f"Error computing score: {e}", file=sys.stderr)
        return 2

    try:
        threshold = float(args.threshold)
    except ValueError:
        print(f"Error: threshold must be numeric: {args.threshold}", file=sys.stderr)
        return 2

    if score >= threshold:
        print(f"Mutation score {score:.4f} meets threshold {threshold:.4f}")
        return 0
    else:
        print(f"Mutation score {score:.4f} is below threshold {threshold:.4f}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
