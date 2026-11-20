#!/usr/bin/env python3
"""Import compatible host-only controls before a new batch; never call a model.

run.py remains unchanged. No existing batch or task directory is overwritten.
Source choice uses control validity only, never candidate model outcomes.
"""
import argparse
from datetime import datetime, timezone
import fcntl
import hashlib
import json
from pathlib import Path
import re
import shutil
import subprocess
import tempfile

LAB = Path(__file__).resolve().parent
# Exact source matching is deliberately conservative. Model-specific config and
# selection paths differ across experiments; their task identities are checked.
CORE = ('run.py', 'runner_helpers.py', 'report.py', 'egress_proxy.py', 'requirements.toml',
        'patch_export.py', 'mas_orchestrator.py', 'delegate_agent.py',
        'AgentCompass/src/agentcompass/benchmarks/swebench_pro_verified/swebench_pro_verified.py',
        'AgentCompass/src/agentcompass/harnesses/codex.py',
        'AgentCompass/src/agentcompass/harnesses/codex_roles_b.py',
        'AgentCompass/src/agentcompass/environments/docker.py',
        'AgentCompass/src/agentcompass/environments/docker_egress_proxy.py')
DATASET = 'data/swe_bench_pro_verified/swebench_pro_verified.jsonl'
OVERRIDES = 'data/swe_bench_pro_verified/dependency-cache-overrides.json'
ALLOWED_FAILED = {40, 65, 127, 184, 186, 217, 218, 258, 261, 285}  # Documented study exclusions; still require explicit CLI approval.
FILES = ('preparation', 'controls-original', 'controls-reference', 'controls.json')


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read(path):
    return json.loads(path.read_text())


def save(path, value):
    temp = path.with_suffix(path.suffix + '.tmp')
    temp.write_text(json.dumps(value, indent=2) + '\n')
    temp.replace(path)


def numbers(spec, limit):
    answer = []
    for part in spec.split(','):
        if re.fullmatch(r'\d+-\d+', part):
            first, last = map(int, part.split('-'))
            if first > last:
                raise ValueError('Descending task range')
            answer.extend(range(first, last + 1))
        elif part.isdigit():
            answer.append(int(part))
        else:
            raise ValueError('Invalid task range')
    if not answer or len(set(answer)) != len(answer) or min(answer) < 1 or max(answer) > limit:
        raise ValueError('Invalid or duplicate tasks')
    return answer


def image_exists(image):
    if not re.fullmatch(r'sha256:[0-9a-f]{64}', image):
        return False
    return subprocess.run(['docker', 'image', 'inspect', image], stdout=subprocess.DEVNULL,
                          stderr=subprocess.DEVNULL, check=False).returncode == 0


def source_batches(lab, current):
    fingerprints = {key: sha(lab/key) for key in CORE}
    if (lab/OVERRIDES).exists():
        fingerprints[OVERRIDES] = sha(lab/OVERRIDES)
    sources = []
    for path in sorted(lab.glob('experiment-*/batch-*/manifest.json')):
        try:
            manifest_bytes = path.read_bytes()
            m = json.loads(manifest_bytes)
        except (OSError, json.JSONDecodeError):
            continue
        frozen = m.get('source_hashes', {})
        if any(frozen.get(k) != v for k, v in fingerprints.items()):
            continue
        if not (lab/OVERRIDES).exists() and OVERRIDES in frozen:
            continue
        selection_path = lab/m.get('selection_file', '')
        if not selection_path.is_file() or frozen.get(str(selection_path.relative_to(lab))) != sha(selection_path):
            continue
        selection = read(selection_path)
        if selection.get('dataset_sha256') != current['dataset_sha256']:
            continue
        sources.append((path.parent, m, selection, manifest_bytes))
    return sources


def import_controls(lab, experiment, batch, tasks, selection_name='selection-extended.json', *, dry_run=False):
    lab = Path(lab)
    if not re.fullmatch(r'experiment-[A-Za-z0-9][A-Za-z0-9_-]*', experiment):
        raise ValueError('Invalid experiment name')
    if not re.fullmatch(r'batch-[A-Za-z0-9][A-Za-z0-9_-]*', batch):
        raise ValueError('Invalid batch name')
    directory = lab/experiment; root = directory/batch
    if directory.is_symlink() or root.is_symlink():
        raise ValueError('Symlink targets are not allowed')
    if (root/'manifest.json').exists():
        return []  # Existing batches, including currently running ones, are immutable here.
    local_selection = directory/'selection.json'
    if not re.fullmatch(r'selection(?:-[A-Za-z0-9_-]+)?\.json', selection_name):
        raise ValueError('Invalid selection filename')
    selected_path = local_selection if local_selection.exists() else lab/selection_name
    selection = read(selected_path)
    if sha(lab/DATASET) != selection['dataset_sha256']:
        raise ValueError('Dataset hash mismatch')
    selected = numbers(tasks, len(selection['scored_tasks']))
    sources = source_batches(lab, selection)
    candidates = []; images = {}
    for n in selected:
        if (root/f'task-{n:02d}').exists():
            continue
        case = selection['scored_tasks'][n - 1]
        for source, manifest, source_selection, manifest_bytes in sources:
            if source == root or n not in manifest['tasks']:
                continue
            if source_selection['scored_tasks'][n - 1] != case:
                continue
            task = source/f'task-{n:02d}'; controls = task/'controls.json'
            snapshot = task/'preparation/snapshot.json'
            if not controls.is_file() or not snapshot.is_file():
                continue
            c = read(controls)
            # Ordinary failures must be investigated/revalidated locally, never
            # silently imported or selected using candidate model success.
            if not c.get('passed') and n not in ALLOWED_FAILED:
                continue
            if not c.get('original_completed'):
                continue
            if c.get('passed') and not c.get('reference_resolved'):
                continue
            scripts = lab/'data/swe_bench_pro_verified/run_scripts'/case['instance_id']
            keys = [str((scripts/name).relative_to(lab)) for name in ('run_script.sh', 'parser.py')]
            frozen = manifest['source_hashes']
            if any(not (lab/k).is_file() or frozen.get(k) != sha(lab/k) for k in keys):
                continue
            if any(not (task/name).exists() for name in FILES):
                continue
            for name in ('controls-original', 'controls-reference'):
                if not (task/name/'evaluation.json').is_file():
                    break
            else:
                snap = read(snapshot)
                ids = [snap.get(k, '') for k in ('original_image_id', 'prepared_image_id')]
                for image in ids:
                    if image not in images:
                        images[image] = image_exists(image)
                if not all(images[i] for i in ids):
                    continue
                proof = {'task': n, 'instance_id': case['instance_id'], 'source_batch': str(source.relative_to(lab)),
                         'source_manifest_sha256': hashlib.sha256(manifest_bytes).hexdigest(),
                         'source_controls_sha256': sha(controls), 'snapshot_sha256': sha(snapshot),
                         'dataset_sha256': selection['dataset_sha256'], 'core_hashes': {k: frozen[k] for k in CORE},
                         'evaluator_hashes': {k: frozen[k] for k in keys},
                         'dependency_overrides_sha256': frozen.get(OVERRIDES),
                         'image_ids': ids, 'passed': bool(c.get('passed')),
                         'approved_exclusion': not c.get('passed') and n in manifest.get('control_exclusions', []),
                         'model_tokens': 0}
                candidates.append((task, proof, manifest_bytes))
                break
    if dry_run:
        return [p for _, p, _ in candidates]
    if not candidates:
        return []
    directory.mkdir(exist_ok=True, mode=0o700)
    with (directory/'.runner.lock').open('a') as lock:
        try:
            fcntl.flock(lock.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError:
            return []
        if (root/'manifest.json').exists():
            return []
        if not local_selection.exists():
            shutil.copy2(selected_path, local_selection)
        elif read(local_selection) != selection:
            raise ValueError('Selection changed while acquiring lock')
        root.mkdir(exist_ok=True, mode=0o700)
        imported = []
        for task, proof, manifest_bytes in candidates:
            dest = root/task.name
            if dest.exists():
                continue
            if sha(task/'controls.json') != proof['source_controls_sha256'] or sha(task/'preparation/snapshot.json') != proof['snapshot_sha256']:
                raise RuntimeError('Source control changed during import; nothing overwritten')
            evidence = root/'control-reuse-sources'
            evidence.mkdir(exist_ok=True)
            (evidence/(proof['source_manifest_sha256']+'.json')).write_bytes(manifest_bytes)
            with tempfile.TemporaryDirectory(prefix='.reuse-', dir=root) as temporary:
                staged = Path(temporary)/task.name; staged.mkdir()
                for name in FILES:
                    item = task/name
                    if item.is_dir():
                        shutil.copytree(item, staged/name)
                    else:
                        shutil.copy2(item, staged/name)
                if sha(staged/'controls.json') != proof['source_controls_sha256'] or sha(staged/'preparation/snapshot.json') != proof['snapshot_sha256']:
                    raise RuntimeError('Source changed while copying; staged import discarded')
                save(staged/'control-reuse.json', proof)
                staged.rename(dest)
            imported.append(proof)
        audit = {'at': datetime.now(timezone.utc).isoformat(), 'policy': 'Exact frozen sources, dataset, task, evaluator and pinned image compatibility; no model outputs copied',
                 'importer_sha256': sha(Path(__file__)), 'controls_reexecuted': False, 'model_tokens': 0,
                 'imported': imported, 'failed_controls_require_explicit_exclusion': [p['task'] for p in imported if not p['passed']]}
        save(root/'control-reuse.json', audit)
        # Pin the importer itself as evidence, without changing run.py's freeze.
        shutil.copy2(Path(__file__), root/'control-reuse-importer.py')
        print(f"Control reuse: {len(imported)} task controls imported; source/image/hash checks passed; no model results copied", flush=True)
        return imported


def seed_from_argv(argv, lab=LAB):
    p=argparse.ArgumentParser(add_help=False, allow_abbrev=False)
    for key in ('experiment','batch','tasks','selection'):p.add_argument('--'+key)
    for key in ('resume-from','next'):p.add_argument('--'+key)
    for key in ('repair-controls','list','help'):p.add_argument('--'+key,action='store_true')
    args,_=p.parse_known_args(argv)
    if args.help or args.list or args.repair_controls or args.resume_from or args.next:
        return []
    if not args.experiment or not args.batch or not args.tasks:
        return []
    return import_controls(lab,args.experiment,args.batch,args.tasks,args.selection or 'selection-extended.json')


if __name__=='__main__':
    seed_from_argv(__import__('sys').argv[1:])
