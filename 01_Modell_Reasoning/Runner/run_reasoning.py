#!/usr/bin/env python3
"""Reasoning experiments: delegate unchanged to the subscription runner.

One model/effort combination per experiment; always the standard architecture.
Preparation, controls, prompts, isolation, trials and grading live in run.py.
"""
import argparse
import os
from pathlib import Path
import sys

from control_reuse import seed_from_argv


LAB = Path(__file__).resolve().parent
MODELS = {"luna": "gpt-6-luna", "sol": "gpt-6-sol", "sol61": "gpt-6.1-sol", "terra": "gpt-5.6-terra"}
NAMESPACES = {"gpt-6-luna": "luna", "gpt-6-sol": "sol6",
              "gpt-6.1-sol": "sol", "gpt-5.6-terra": "terra"}
EFFORTS = ("low", "medium", "high", "xhigh", "max")


def command(argv, *, python=None):
    parser = argparse.ArgumentParser(
        description="Compare Luna/Sol/Terra reasoning with the unchanged standard benchmark architecture.",
        epilog="Other options go to run.py: --batch, --tasks/--next, --run, --parallel, "
               "--model-workers, --parallel-controls, --control-workers, --resume-from, "
               "--exclude-invalid-controls and --selection. Without --run: controls only.")
    parser.add_argument("--model", required=True, choices=tuple(MODELS) + tuple(MODELS.values()))
    parser.add_argument("--reasoning", required=True, choices=EFFORTS)
    parser.add_argument("--experiment", help="Optional experiment name; default: experiment-reasoning-MODEL-EFFORT")
    parser.add_argument("--setup", choices=("standard",), default="standard", help="Fixed standard architecture")
    args, remaining = parser.parse_known_args(argv)
    model = MODELS.get(args.model, args.model)
    namespace = NAMESPACES[model]
    experiment = args.experiment or f"experiment-reasoning-{namespace}-{args.reasoning}"
    # No automatic sweep, no shared model context or variant-specific prompts.
    # run.py freezes model/effort, tasks, sources and controls in each manifest.
    result = [python or sys.executable, str(LAB / "run.py"),
              "--experiment", experiment, "--model", model,
              "--reasoning", args.reasoning, "--setup", "standard"]
    if not any(x == "--selection" or x.startswith("--selection=") for x in remaining):
        result.extend(["--selection", "selection-extended.json"])
    return result + remaining


def main(argv=None):
    args = command(sys.argv[1:] if argv is None else argv)
    imported = seed_from_argv(args[2:])
    approved = sorted(p['task'] for p in imported if p.get('approved_exclusion'))
    if approved and not any(x == '--exclude-invalid-controls' or x.startswith('--exclude-invalid-controls=') for x in args):
        args.extend(['--exclude-invalid-controls', ','.join(map(str, approved))])
        print(f"Reusing previously approved control exclusions: {approved}", flush=True)
    print("Reasoning experiment: unchanged run.py, standard architecture; "
          "subscription auth and existing benchmark protocol", flush=True)
    # Replace this process: Ctrl+C and the existing coordinator lock behave
    # exactly as in run.py, without an extra subprocess coordinator.
    os.execv(args[0], args)


if __name__ == "__main__":
    main()
