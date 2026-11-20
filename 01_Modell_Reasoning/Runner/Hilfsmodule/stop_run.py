#!/usr/bin/env python3
"""Ask a running batch to finish active trials without starting new ones."""
import argparse
from datetime import datetime, timezone
import json
from pathlib import Path
import re

LAB = Path(__file__).resolve().parent


def request_stop(experiment, batch, *, lab=LAB):
    if not re.fullmatch(r'experiment-[A-Za-z0-9][A-Za-z0-9_-]*', experiment):
        raise ValueError('Invalid experiment')
    if not re.fullmatch(r'batch-[A-Za-z0-9][A-Za-z0-9_-]*', batch):
        raise ValueError('Invalid batch')
    root = Path(lab) / experiment / batch
    if root.resolve() != root.absolute():
        raise ValueError('Symlink targets are not allowed')
    manifest = json.loads((root / 'manifest.json').read_text())
    if manifest['status'] != 'running':
        raise ValueError('Batch is not running; no stop request written')
    path = root / 'STOP_AFTER_ACTIVE.json'
    if path.exists():
        return path
    temporary = root / 'STOP_AFTER_ACTIVE.tmp'
    temporary.write_text(json.dumps({'at': datetime.now(timezone.utc).isoformat(),
        'reason': 'Explicit user request: finish active trials, start no further tasks',
        'active_trials_when_requested': manifest.get('active_trials', [])}, indent=2) + '\n')
    temporary.replace(path)
    return path


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--experiment', required=True)
    parser.add_argument('--batch', required=True)
    args = parser.parse_args()
    print(request_stop(args.experiment, args.batch))
