#!/usr/bin/env python3
"""Main context experiment: prepare/check/models/stop/resume/report.

Only explicit models/resume commands invoke models. Preparation reuses passing
control evidence only with exact evaluation image identity, or runs new controls
after rebuilding missing dependency caches. Pilot outcomes are never imported.
"""
import argparse
import asyncio
from collections import deque
import fcntl
import itertools
import json
from pathlib import Path
import re
import shutil
import tempfile
import time
import uuid

import compare_context
import context_live as live
import context_materials as materials
import context_go_cache
from context_telemetry import analyze, parse_rows, USAGE_KEYS
from control_reuse import numbers
import run_context as shared
from run_sol_ultra import core_module

ROOT = shared.ROOT
FINAL = {'completed', 'invalid_submission', 'empty_submission'}


def core_module_for_main():
    core = core_module()
    core.HERE = ROOT
    core.RUN_MODEL, core.RUN_REASONING = 'gpt-6-sol', 'medium'
    return core


def finished(directory):
    path = directory / 'result.json'
    if not path.exists():
        return False
    r = shared.read(path)
    return r.get('status') in FINAL and r.get('context_audit', {}).get('protocol_valid') is True


def prerequisites(core):
    shared.validate(ROOT)
    audit = shared.read(ROOT / 'pilot/audited-summary.json')
    if audit['status'] != 'pilot_verified':
        raise ValueError('Verified technical pilot required')
    pilot = shared.read(ROOT / 'pilot/manifest.json')
    for path, digest in pilot['source_hashes'].items():
        if core.sha(path) != digest:
            raise ValueError('Pilot runtime/material changed: ' + path)
    return shared.read(ROOT / 'plan.json'), shared.read(ROOT / 'materials/native-preparation.json')


def private_data(core, root):
    """Never edit the shared dependency override file or old evidence."""
    path = root / 'trusted-data'
    path.mkdir(parents=True, exist_ok=True)
    for name in ('swebench_pro_verified.jsonl', 'run_scripts'):
        target = path / name
        if not target.exists():
            target.symlink_to(core.DATA / name)
    return path


async def restore_one(core, root, row, case, instance, available, data):
    n = row['task']
    path = root / f'task-{n:02d}/environment.json'
    if path.exists():
        proof = shared.read(path)
        for name, digest in proof['evidence_sha256'].items():
            if core.sha(name) != digest:
                raise ValueError('Environment evidence changed: ' + name)
        if not {proof['snapshot']['original_image_id'], proof['snapshot']['prepared_image_id']} <= available:
            raise ValueError(f'Task {n}: prepared image disappeared; explicit recovery required')
        return proof
    # Reuse reconstructed pilot environments, never pilot patches or answers.
    pilot = shared.read(ROOT / 'pilot/restoration.json')['tasks'].get(str(n))
    if pilot and {pilot['snapshot']['original_image_id'], pilot['snapshot']['prepared_image_id']} <= available:
        old_fields = ('official_image_id', 'canonical_tree', 'repo_language', 'toolchains', 'login_shell_toolchains')
        if any(pilot['snapshot'].get(k) != row['snapshot'].get(k) for k in old_fields):
            raise ValueError('Pilot environment does not match task identity')
        inputs = [ROOT / 'pilot/restoration.json']
        proof = {'task': n, 'snapshot': pilot['snapshot'], 'method': 'Reuse verified pilot environment only',
                 'pilot_outputs_reused': False, 'evidence_sha256': {str(p): core.sha(p) for p in inputs}}
        core.save(path, proof)
        return proof
    directory = root / f'task-{n:02d}'
    if directory.exists() and any(directory.iterdir()):
        raise ValueError(f'Task {n}: incomplete preparation exists; inspect and archive it explicitly before retrying')
    directory.mkdir(parents=True)
    source = row['snapshot']
    official = await core.ensure_image(source['original_image'], directory / 'image')
    if official['Id'] != source['official_image_id']:
        raise ValueError(f'Task {n}: official image tag no longer matches pinned content')
    available.add(official['Id'])
    override_path = data / 'dependency-cache-overrides.json'
    overrides = shared.read(override_path) if override_path.exists() else {}
    exact = source['original_image_id'] in available
    if exact and source['original_image_id'] != source['official_image_id']:
        overrides[case['instance_id']] = {'official_image_id': source['official_image_id'],
            'cached_image_id': source['original_image_id'], 'base_commit': case['base_commit'],
            'canonical_tree': source['canonical_tree'], 'dataset_sha256': core.sha(data / 'swebench_pro_verified.jsonl')}
    else:
        overrides.pop(case['instance_id'], None)
    core.save(override_path, overrides)
    previous_data = core.DATA
    core.DATA = data
    try:
        if not exact:
            if row['language'] == 'go':
                await context_go_cache.warm(core, case, instance, directory / 'dependency-prefetch')
            elif row['language'] == 'ts':
                import warm_control_dependencies
                warmer = warm_control_dependencies.runner
                old_lab, old_data = warmer.LAB, warmer.DATA
                warmer.LAB, warmer.DATA = root / 'trusted-prefetch', data
                warmer.LAB.mkdir(exist_ok=True)
                try:
                    selection = shared.read(shared.LAB / 'selection-mas-300.json')
                    await warm_control_dependencies.warm(selection, [n])
                finally:
                    warmer.LAB, warmer.DATA = old_lab, old_data
            elif source['original_image_id'] != source['official_image_id']:
                raise ValueError('Unsupported missing dependency overlay')
        # A changed evaluation image always receives fresh original/reference controls.
        effective = (shared.read(override_path).get(case['instance_id']) or {}).get('cached_image_id', official['Id'])
        if effective != source['original_image_id']:
            snap, passed = await core.validate_task_controls(n, case, instance, root / 'fresh-controls')
            if not passed:
                raise ValueError(f'Task {n}: fresh controls failed. No automatic new exclusion.')
            preparation_dir = root / 'fresh-controls' / f'task-{n:02d}/preparation'
            evidence = [preparation_dir / 'snapshot.json', preparation_dir / 'canonical-tracked-files.txt',
                        preparation_dir.parent / 'controls.json']
            evidence += list(preparation_dir.parent.glob('controls-*/evaluation.json'))
            method = 'Rebuilt dependency image; new original/reference controls passed'
        else:
            snap = await core.prepare(case, directory / 'preparation')
            preparation_dir = directory / 'preparation'
            evidence = [preparation_dir / 'snapshot.json', preparation_dir / 'canonical-tracked-files.txt']
            method = 'Exact evaluation image; passing donor controls reused after source/toolchain comparison'
    finally:
        core.DATA = previous_data
    fields = ('official_image_id', 'canonical_tree', 'repo_language', 'toolchains', 'login_shell_toolchains')
    different = [k for k in fields if snap.get(k) != source.get(k)]
    original_tracked = shared.LAB / row['control_donor'] / f'task-{n:02d}/preparation/canonical-tracked-files.txt'
    if core.sha(original_tracked) != core.sha(preparation_dir / 'canonical-tracked-files.txt'):
        different.append('canonical-tracked-files.txt')
    if different:
        raise ValueError(f'Task {n}: restored environment differs: {different}')
    proof = {'task': n, 'snapshot': snap, 'method': method, 'pilot_outputs_reused': False,
             'evidence_sha256': {str(p): core.sha(p) for p in evidence}}
    core.save(path, proof)
    available.update((snap['original_image_id'], snap['prepared_image_id']))
    return proof


def fingerprints(core):
    pilot = shared.read(ROOT / 'pilot/manifest.json')
    files = [Path(p) for p in pilot['source_hashes']]
    files += [Path(__file__), shared.LAB / 'context_go_cache.py', shared.LAB / 'compare_context.py', ROOT / 'pilot/audited-summary.json']
    return {str(p): core.sha(p) for p in files}


async def prepare(core, root, tasks, workers):
    plan, material = prerequisites(core)
    if (root / 'manifest.json').exists():
        m = validate(core, root, workers)
        if m['tasks'] != tasks:
            raise ValueError('Frozen task selection differs')
        print('Prepared batch retained; no model calls or repeated preparation.')
        return
    for other in (ROOT / 'main').glob('*/selection.json'):
        if other.parent != root and set(shared.read(other)['tasks']) & set(tasks):
            raise ValueError('Tasks already assigned to another main batch: ' + str(other.parent))
    root.mkdir(parents=True, exist_ok=True)
    selection = {'tasks': tasks, 'model_workers': workers, 'model': 'gpt-6-sol', 'reasoning': 'medium'}
    shared.frozen_write(root / 'selection.json', json.dumps(selection, indent=2) + '\n')
    available = live.resident_ids()
    by_number = {r['task']: r for r in plan['tasks']}
    order = sorted(tasks, key=lambda n: (by_number[n]['snapshot']['original_image_id'] not in available, tasks.index(n)))
    data = private_data(core, root)
    master = shared.read(shared.LAB / 'selection-mas-300.json')
    instances = {r['instance_id']: r for r in map(json.loads, (core.DATA / 'swebench_pro_verified.jsonl').read_text().splitlines())}
    cases, schedule = {}, []
    for n in order:
        row = by_number[n]
        if row['excluded']:
            cases[str(n)] = {'excluded': True, 'control_donor': row['control_donor']}
            continue
        print(f'Task {n}: prepare main environment; no model calls', flush=True)
        proof = await restore_one(core, root, row, master['scored_tasks'][n - 1], instances[row['instance_id']], available, data)
        cases[str(n)] = {'excluded': False, 'instance_id': row['instance_id'], 'environment': proof}
        schedule.append({'task': n, 'pool_id': row['pool_id'], 'arm_order': row['arm_order']})
    m = {'version': 'context-main-v1', 'status': 'prepared', 'model': 'gpt-6-sol', 'reasoning': 'medium',
         'tasks': tasks, 'schedule': schedule, 'cases': cases, 'model_workers': workers,
         'arms': list(shared.ARMS), 'source_hashes': fingerprints(core),
         'expected_trials': len(schedule) * 3, 'main_run_authorized': False, 'trials_started': 0,
         'model_timeout_seconds': None, 'evaluation_timeout_seconds': 3600,
         'pilot_results_reused': False, 'material_preparation': str(ROOT / 'materials/native-preparation.json')}
    core.save(root / 'manifest.json', m)
    for name in m['source_hashes']:
        p = Path(name)
        if p in (core.BINARY, core.BINARY.parent / 'codex-code-mode-host'):
            continue
        target = root / 'source-snapshot' / p.relative_to(shared.LAB)
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(p, target)
    print(f"Prepared {len(schedule)} tasks / {m['expected_trials']} fresh trials. Models not started.")


def validate(core, root, workers=None, images=True):
    prerequisites(core)
    m = shared.read(root / 'manifest.json')
    if (m.get('version'), m.get('model'), m.get('reasoning')) != ('context-main-v1', 'gpt-6-sol', 'medium'):
        raise ValueError('Unexpected experiment protocol')
    if workers is not None and workers != m['model_workers']:
        raise ValueError('Worker count differs from prepared batch')
    for path, digest in m['source_hashes'].items():
        if core.sha(path) != digest:
            raise ValueError('Frozen runtime/material changed: ' + path)
    ids = live.resident_ids() if images else None
    for record in m['cases'].values():
        if record['excluded']:
            continue
        proof = record['environment']
        for path, digest in proof['evidence_sha256'].items():
            if core.sha(path) != digest:
                raise ValueError('Control/environment evidence changed: ' + path)
        if ids is not None and not {proof['snapshot']['original_image_id'], proof['snapshot']['prepared_image_id']} <= ids:
            raise ValueError('Required image missing; no implicit rebuild during models')
    return m


async def attempt(core, root, n, arm, pool, snap, instance, preparation, enc):
    directory = root / f'task-{n:02d}' / arm
    if finished(directory):
        return
    if directory.exists() and any(directory.iterdir()):
        raise ValueError('Prior incomplete attempt exists; use explicit resume')
    start_time = time.monotonic()
    core.save(directory / 'started.json', {'at': core.now(), 'task': n, 'arm': arm, 'pool_id': pool, 'phase': 'main'})
    prompt, source = core.issue_prompt(instance), None
    if arm == 'A':
        a = preparation['A_calibration']
        head = 'The following is unrelated background text. It contains no current work item.\n<background>\n'
        tail = '\n</background>\n' + prompt
        budget = round(a['window'] * .8) - a['measured_overhead'] - len(enc.encode(head + tail))
        prompt = head + materials.prefix((ROOT / f'materials/A/pool-{pool}/reservoir.txt').read_text(), budget, enc) + tail
    elif arm == 'B':
        source = shared.read(ROOT / f'materials/B/pool-{pool}/native/session.json')
    try:
        with tempfile.TemporaryDirectory(prefix=f'context-main-{n}-{arm}-') as tmp:
            auth = await materials.credential(core, tmp)
            async with core.container(snap['prepared_image_id'], directory / 'container', agent=True) as env:
                await core.network_checks(env, directory / 'container')
                await core.verify_toolchain(env, snap['repo_language'])
                await env.upload(str(shared.LAB / 'patch_export.py'), '/tmp/swe-patch-export.py')
                baseline = await core.capture_export_baseline(env, 'environment', directory)
                await live.setup_auth(core, env, auth)
                session = None
                if source:
                    await live.import_session(core, env, source)
                    session = next(r['payload']['id'] for r in parse_rows(source['content']) if r.get('type') == 'session_meta')
                print(f'Main {n}/{arm}: gpt-6-sol medium', flush=True)
                stage, entry, _ = await live.invoke(core, env, directory / 'standard', prompt, auth, session=session)
                previous = stage['context_audit']
                audit = analyze(parse_rows(entry['content']), benchmark_turn_id=previous['benchmark_turn_id'],
                                start_row=previous['start_row'], arm=arm)
                if source:
                    captured = await live.capture(core, env, directory / 'post-task')
                    retained = next((e for e in captured if e['path'] == source['path']), None)
                    audit['source_history_unchanged'] = bool(retained and retained['content'] == source['content'])
                    audit['native_history_link_valid'] = live.history_link(source, entry)
                    if not audit['source_history_unchanged'] or not audit['native_history_link_valid']:
                        audit['protocol_valid'] = False
                        audit['errors'].append('B native source history was not preserved')
                core.save(directory / 'context-audit.json', audit)
                patch = await core.export_patch(env, baseline)
                core.save(directory / 'submission.patch', patch)
            result = {'task': n, 'arm': arm, 'pool_id': pool, 'phase': 'main', 'main_result': True,
                      'stage': stage, 'context_audit': audit, 'trial_wall_seconds': time.monotonic() - start_time}
            if not audit['protocol_valid']:
                result.update(status='context_protocol_problem', resolved=None)
            elif not patch.strip():
                result.update(status='empty_submission', resolved=False)
            elif not await core.valid_patch(snap['prepared_image_id'], patch, directory / 'patch-check'):
                result.update(status='invalid_submission', resolved=False)
            else:
                e = await core.evaluate(instance, snap['original_image_id'], patch, directory / 'evaluation')
                result.update(status='completed' if e.get('completed') and not e.get('error') else 'evaluation_problem',
                              resolved=e.get('resolved') if e.get('completed') else None)
            result['trial_wall_seconds'] = time.monotonic() - start_time
            core.save(directory / 'result.json', result)
            if result['status'] not in FINAL:
                raise RuntimeError('Technical/context/evaluation problem; no automatic repeat')
    except BaseException as error:
        core.save(directory / 'interruption.json', {'at': core.now(), 'error': core.redact(str(error)),
                                                   'elapsed_seconds': time.monotonic() - start_time})
        raise


def jobs_for(root, m):
    jobs = []
    for item in m['schedule']:
        for arm in item['arm_order']:
            directory = root / f'task-{item["task"]:02d}' / arm
            if finished(directory):
                continue
            if directory.exists() and any(directory.iterdir()):
                raise ValueError('Incomplete attempt exists; use resume: ' + str(directory))
            jobs.append((item['task'], arm, item['pool_id']))
    return jobs


async def execute_queue(jobs, workers, run_job, stopped):
    queue, errors = deque(jobs), []
    async def worker():
        while queue and not errors and not stopped():
            job = queue.popleft()
            try:
                await run_job(*job)
            except Exception as error:
                errors.append({'task': job[0], 'arm': job[1], 'error': str(error)})
    await asyncio.gather(*(worker() for _ in range(workers)))
    return list(queue), errors


async def models(core, root, workers):
    m = validate(core, root, workers)
    if m['status'] in ('paused', 'technical_interruption'):
        raise ValueError('Batch interrupted/paused; use explicit resume')
    jobs = jobs_for(root, m)
    if not jobs:
        print('All results already final; no repeated model calls.')
        return 0
    if (root / 'STOP_AFTER_ACTIVE.json').exists():
        raise ValueError('Stop marker exists; use explicit resume')
    preparation = shared.read(Path(m['material_preparation']))
    enc = materials.tokenizer()
    rows = {r['instance_id']: r for r in map(json.loads, (core.DATA / 'swebench_pro_verified.jsonl').read_text().splitlines())}
    m.update(status='running', main_run_authorized=True, authorization='Explicit operator models/resume command', started_at=core.now())
    m['active_trials'] = []
    core.save(root / 'manifest.json', m)
    state = shared.read(ROOT / 'status.json')
    state.update(status='main_running', main_started=True, main_run_authorized=True,
                 current_main_batch=root.name)
    core.save(ROOT / 'status.json', state)
    async def run_job(n, arm, pool):
        for file, digest in m['source_hashes'].items():
            if core.sha(file) != digest:
                raise RuntimeError('Frozen runtime/material changed: ' + file)
        record = m['cases'][str(n)]
        identity = {'task': n, 'arm': arm}
        m['trials_started'] = m.get('trials_started', 0) + 1
        m['active_trials'].append(identity)
        core.save(root / 'manifest.json', m)
        try:
            await attempt(core, root, n, arm, pool, record['environment']['snapshot'], rows[record['instance_id']], preparation, enc)
        finally:
            m['active_trials'].remove(identity)
            core.save(root / 'manifest.json', m)
    try:
        pending, errors = await execute_queue(jobs, workers, run_job, lambda: (root / 'STOP_AFTER_ACTIVE.json').exists())
        m.update(status='technical_interruption' if errors else ('paused' if pending else 'completed'),
                 technical_errors=errors, pending_jobs=pending, ended_at=core.now())
        core.save(root / 'manifest.json', m)
        state.update(status='main_' + m['status'])
        core.save(ROOT / 'status.json', state)
        return 2 if errors else (75 if pending else 0)
    except BaseException as error:
        m.update(status='technical_interruption', interrupted_at=core.now(), interruption=core.redact(str(error)))
        core.save(root / 'manifest.json', m)
        state.update(status='main_technical_interruption')
        core.save(ROOT / 'status.json', state)
        raise
    finally:
        write_report(root)


def resume(root, m):
    archive = root / 'technical-interruptions' / ('resume-' + uuid.uuid4().hex[:12])
    moved = []
    for item in m['schedule']:
        for arm in item['arm_order']:
            directory = root / f'task-{item["task"]:02d}' / arm
            if directory.exists() and not finished(directory):
                target = archive / directory.relative_to(root)
                target.parent.mkdir(parents=True, exist_ok=True)
                shutil.move(str(directory), str(target)); moved.append(str(target))
    marker = root / 'STOP_AFTER_ACTIVE.json'
    if moved or marker.exists():
        archive.mkdir(parents=True, exist_ok=True)
        shared.save(archive / 'manifest-before-resume.json', m)
        if marker.exists():
            shutil.move(str(marker), str(archive / marker.name))
        shared.save(archive / 'resume.json', {'archived_attempts': moved, 'reason': 'Explicit resume command; all completed outcomes retained'})
    m.update(status='prepared', technical_errors=[], pending_jobs=[])
    shared.save(root / 'manifest.json', m)


def repair_preparation(root, tasks):
    """Explicit recovery only, retaining every completed environment proof."""
    if (root / 'manifest.json').exists():
        raise ValueError('Preparation already finalized; use check/models/resume instead')
    selection = shared.read(root / 'selection.json')
    if selection['tasks'] != tasks:
        raise ValueError('Recovery tasks differ from original selection')
    archive = root / 'technical-preparations' / ('repair-' + uuid.uuid4().hex[:12])
    moved = []
    for n in tasks:
        directory = root / f'task-{n:02d}'
        if (directory / 'environment.json').exists():
            continue
        if any((directory / arm).exists() for arm in shared.ARMS):
            raise ValueError('Model attempt data found; preparation recovery may not archive it')
        for source in (directory, root / 'fresh-controls' / directory.name):
            if source.exists():
                target = archive / source.relative_to(root)
                target.parent.mkdir(parents=True, exist_ok=True)
                shutil.move(str(source), str(target))
                moved.append(str(source.relative_to(root)))
    if moved:
        shared.save(archive / 'recovery.json', {'archived_paths': moved,
            'reason': 'Explicit preparation repair; old failed Go all-prefetch logs preserved', 'model_calls': 0})
    return moved


def write_report(root):
    m = shared.read(root / 'manifest.json')
    eligible = [x['task'] for x in m['schedule']]
    values, missing = {}, []
    for n in eligible:
        for arm in shared.ARMS:
            directory = root / f'task-{n:02d}' / arm
            if finished(directory):
                values[n, arm] = shared.read(directory / 'result.json')
            else:
                missing.append({'task': n, 'arm': arm})
    complete = not missing
    arms = {}
    for arm in shared.ARMS:
        selected = [v for (n, a), v in values.items() if a == arm]
        arms[arm] = {'planned': len(eligible), 'valid_final_results': len(selected),
                     'solved': sum(v.get('resolved') is True for v in selected),
                     'solve_rate': sum(v.get('resolved') is True for v in selected) / len(eligible) if complete and eligible else None,
                     'known_usage': {k: sum(v['context_audit']['known_task_usage'][k] for v in selected) for k in USAGE_KEYS},
                     'usage_complete': complete and all(v['context_audit']['usage_complete'] for v in selected),
                     'trial_wall_seconds': sum(v['trial_wall_seconds'] for v in selected),
                     'compaction_records': sum(len(v['context_audit']['compaction_rows']) for v in selected)}
    pairs = []
    for left, right in itertools.combinations(shared.ARMS, 2):
        paired = [n for n in eligible if (n, left) in values and (n, right) in values]
        b = sum(values[n, left].get('resolved') is True and values[n, right].get('resolved') is not True for n in paired)
        c = sum(values[n, left].get('resolved') is not True and values[n, right].get('resolved') is True for n in paired)
        pairs.append({'left': left, 'right': right, 'paired': len(paired), 'left_only_solved': b, 'right_only_solved': c,
                      'mcnemar_exact_p': compare_context.mcnemar_exact(b, c) if complete else None, 'holm_adjusted_p': None})
    if complete:
        previous = 0
        for rank, item in enumerate(sorted(pairs, key=lambda x: x['mcnemar_exact_p'])):
            previous = max(previous, min(1, (3 - rank) * item['mcnemar_exact_p']))
            item['holm_adjusted_p'] = previous
    extra, unknown = [], []
    starts = list(root.glob('task-*/*/standard/started.json'))
    starts += list((root / 'technical-interruptions').glob('*/task-*/*/standard/started.json'))
    for started in starts:
        trial_dir = started.parent.parent
        if 'technical-interruptions' not in trial_dir.parts and finished(trial_dir):
            continue
        stage = started.parent / 'stage.json'
        if stage.exists():
            s = shared.read(stage)
            extra.append({'stage': str(stage.relative_to(root)), 'usage': s.get('usage'),
                          'usage_complete': s.get('usage_complete', False), 'elapsed_seconds': s.get('elapsed_seconds')})
        else:
            unknown.append(str(started.parent.relative_to(root)))
    report = {'status': 'final' if complete else 'interim', 'arms': arms, 'pairs': pairs, 'missing_or_technical': missing,
              'additional_attempt_consumption': {'attempts': extra, 'unknown_attempts': unknown,
                  'known_usage': {k: sum((e['usage'] or {}).get(k, 0) for e in extra) for k in USAGE_KEYS},
                  'usage_complete': not unknown and all(e['usage_complete'] for e in extra)},
              'pilot_results_reused': False, 'note': 'Preparation, pilot and archived technical interruption consumption are additional; only final main attempts are summed here.'}
    shared.save(root / 'comparison.json', report)
    return report


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('phase', choices=('prepare', 'repair-prepare', 'check', 'models', 'stop', 'resume', 'report'))
    p.add_argument('--tasks', default='201-300')
    p.add_argument('--batch', default='batch-03')
    p.add_argument('--model-workers', type=int, default=5)
    args = p.parse_args(argv)
    if not re.fullmatch(r'batch-[A-Za-z0-9_-]+', args.batch):
        p.error('Use a local batch-* name')
    if not 1 <= args.model_workers <= 5:
        p.error('Total worker count must be between one and five')
    tasks = numbers(args.tasks, 300)
    root = ROOT / 'main' / args.batch
    if root.is_symlink() or root.parent.is_symlink():
        p.error('Symlink output directory not allowed')
    if args.phase == 'stop':
        if not (root / 'selection.json').exists():
            p.error('Batch does not exist')
        shared.save(root / 'STOP_AFTER_ACTIVE.json', {'reason': 'Explicit stop; finish active whole attempts'})
        print('Stop requested; active attempts finish.')
        return 0
    if args.phase == 'report':
        print(write_report(root)['status']); return 0
    ROOT.mkdir(exist_ok=True)
    with (ROOT / '.main-runner.lock').open('a') as lock:
        fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        core = core_module_for_main()
        if args.phase in ('prepare', 'repair-prepare'):
            if args.phase == 'repair-prepare':
                print('Archived incomplete preparation:', repair_preparation(root, tasks))
            asyncio.run(prepare(core, root, tasks, args.model_workers)); return 0
        m = validate(core, root, args.model_workers)
        if m['tasks'] != tasks:
            p.error('Tasks differ from prepared selection')
        if args.phase == 'check':
            print(f"Verified {len(m['schedule'])} tasks / {m['expected_trials']} trials; no model calls."); return 0
        if args.phase == 'resume':
            resume(root, m)
        return asyncio.run(models(core, root, args.model_workers))


if __name__ == '__main__':
    raise SystemExit(main())
