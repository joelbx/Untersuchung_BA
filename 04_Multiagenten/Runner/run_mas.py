#!/usr/bin/env python3
"""Fresh Standard / Roles B / bounded self-organizing comparison on a fixed task pool.

Delegates to the shared subscription runner. Controls and models are separate
explicit invocations. This entry point never launches an automatic sweep.
"""
import argparse
import json
import os
import re
from pathlib import Path
import sys

from control_reuse import seed_from_argv
from stop_run import request_stop

LAB = Path(__file__).resolve().parent
EXPERIMENT = 'experiment-mas-sol6-medium'
EXCLUSIONS = (40, 65, 127, 184, 186)
EXTENDED_EXCLUSIONS = EXCLUSIONS + (217, 218, 258, 261, 285)


def exclusions_for(pool):
    if pool not in (200, 300):
        raise ValueError('MAS task pool must be 200 or 300')
    return EXCLUSIONS if pool == 200 else EXTENDED_EXCLUSIONS


def command(argv, *, python=None, lab=LAB):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--experiment', default=EXPERIMENT)
    parser.add_argument('--batch', default='batch-01')
    parser.add_argument('--setup', choices=('standard', 'roles-b', 'self-organizing', 'all'), default='all')
    parser.add_argument('--tasks', default='1-200')
    parser.add_argument('--pool', type=int, choices=(200, 300), default=200,
                        help='Immutable task-pool prefix; extending an existing experiment requires a new directory')
    parser.add_argument('--stop', action='store_true', help='Only request stop-after-active; no models started')
    parser.add_argument('--model', choices=('sol', 'gpt-6-sol'), default='sol')
    parser.add_argument('--reasoning', choices=('medium',), default='medium')
    args, remaining = parser.parse_known_args(argv)
    if not re.fullmatch(r'experiment-[A-Za-z0-9][A-Za-z0-9_-]*', args.experiment) or not re.fullmatch(r'batch-[A-Za-z0-9][A-Za-z0-9_-]*', args.batch):
        parser.error('Use an experiment-* directory and batch-* name within the laboratory')
    if args.stop:
        if remaining:
            parser.error('--stop cannot be combined with runner options')
        return args, None
    if any(x in ('--selection', '--next') or x.startswith(('--selection=', '--next=')) for x in remaining):
        parser.error('MAS v1 uses a fixed task pool and explicit --tasks')
    base = [python or sys.executable, str(Path(lab) / 'run.py'), '--experiment', args.experiment,
            '--batch', args.batch, '--tasks', args.tasks, '--selection', f'selection-mas-{args.pool}.json',
            '--model', 'gpt-6-sol', '--reasoning', 'medium', '--setup', args.setup]
    is_model_run = '--run' in remaining
    has_exclusions = any(x == '--exclude-invalid-controls' or x.startswith('--exclude-invalid-controls=') for x in remaining)
    # Exclusions still need failed local/imported control evidence. A brand-new
    # control run must establish that evidence before requesting the exclusions.
    from control_reuse import numbers
    selected = numbers(args.tasks, args.pool)
    root = Path(lab) / args.experiment / args.batch
    excluded = [n for n in exclusions_for(args.pool) if n in selected]
    evidence = all((root / f'task-{n:02d}/controls.json').exists() and
                   not json.loads((root / f'task-{n:02d}/controls.json').read_text()).get('passed')
                   for n in excluded)
    if excluded and not has_exclusions and (is_model_run or evidence):
        base.extend(['--exclude-invalid-controls', ','.join(map(str, excluded))])
    if not is_model_run and '--parallel-controls' not in remaining:
        base.extend(['--parallel-controls', '--control-workers', '2'])
    if is_model_run and '--parallel' not in remaining:
        base.extend(['--parallel', '--model-workers', '1'])
    return args, base + remaining


def ensure_selection(lab=LAB, pool=200):
    exclusions_for(pool)
    destination = Path(lab) / f'selection-mas-{pool}.json'
    master = json.loads((Path(lab) / 'selection-extended.json').read_text())
    if len(master['scored_tasks']) < pool:
        raise ValueError('Master selection does not contain the requested task pool')
    prior = Path(lab) / 'selection-mas-200.json'
    if pool == 300 and prior.exists() and json.loads(prior.read_text())['scored_tasks'] != master['scored_tasks'][:200]:
        raise ValueError('First 200 task identities differ; do not extend this pool')
    selection = {**master, 'scored_tasks': master['scored_tasks'][:pool],
                 'architecture_protocol': f'mas-v1; fixed first {pool} tasks; model and effort fixed before fresh architecture runs'}
    if destination.exists():
        if json.loads(destination.read_text()) != selection:
            raise ValueError('Fixed MAS selection changed; do not overwrite an existing pool')
    else:
        destination.write_text(json.dumps(selection, indent=2) + '\n')


def ensure_experiment(experiment=EXPERIMENT, lab=LAB, pool=200):
    if not re.fullmatch(r'experiment-[A-Za-z0-9][A-Za-z0-9_-]*', experiment):
        raise ValueError('Use a fresh experiment-* directory within the laboratory')
    directory = Path(lab) / experiment
    if directory.is_symlink():
        raise ValueError('Symlink experiment directories are not allowed')
    expected = {'model': 'gpt-6-sol', 'reasoning': 'medium', 'protocol': 'mas-v1',
                'storage_reserve_gib': 25, 'scored_task_prefix': pool,
                'architectures': ['standard', 'roles-b', 'self-organizing'],
                'approved_control_exclusions': list(exclusions_for(pool))}
    config = directory / 'experiment.json'
    if config.exists():
        if json.loads(config.read_text()) != expected:
            raise ValueError('Experiment configuration differs; use a fresh MAS directory')
    else:
        if any(directory.glob('batch-*/manifest.json')):
            raise ValueError('Existing historical batches must not be converted into a MAS experiment')
        directory.mkdir(exist_ok=True, mode=0o700)
        config.write_text(json.dumps(expected, indent=2) + '\n')


if __name__ == '__main__':
    args, argv = command(sys.argv[1:])
    if args.stop:
        print(request_stop(args.experiment, args.batch))
        raise SystemExit(0)
    ensure_selection(pool=args.pool)
    ensure_experiment(args.experiment, pool=args.pool)
    seed_from_argv(argv[2:])
    print('MAS v1: fresh standard / fixed roles / free-role bounded orchestration; Sol 6 / medium; subscription', flush=True)
    os.execv(argv[0], argv)
