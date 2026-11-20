"""Fifteen sequential, fresh pilot attempts only; never main-run inference."""
import hashlib
import json
from pathlib import Path
import shutil
import tempfile
import time

import context_live as live
import context_materials
import run_context
from context_telemetry import analyze, parse_rows

ROOT = run_context.ROOT
FINAL = {'completed', 'empty_submission', 'invalid_submission'}


def freeze(core):
    restoration = run_context.read(ROOT / 'pilot/restoration.json')
    preparation = run_context.read(ROOT / 'materials/native-preparation.json')
    if restoration['status'] != 'verified' or preparation['status'] != 'prepared_pending_task_start_validation':
        raise RuntimeError('Pilot preparation incomplete')
    selected = run_context.read(ROOT / 'pilot/selection.json')['tasks']
    schedule = [{'task': n, 'pool_id': i + 1, 'arm_order': list(run_context.ORDERS[i % 6])}
                for i, n in enumerate(selected)]
    files = [run_context.LAB / p for p in (*run_context.CORE, 'run_context.py', 'context_live.py', 'context_materials.py',
                                          'context_pilot.py', 'context_telemetry.py', 'compare_context.py')]
    files += [ROOT / p for p in ('plan.json', 'pilot/restoration.json', 'pilot/selection.json',
                                  'materials/native-preparation.json', 'materials/manifest.json')]
    files += list((ROOT / 'materials').glob('A/pool-*/reservoir.txt'))
    files += list((ROOT / 'materials').glob('B/pool-*/native/session.json'))
    files += list((ROOT / 'materials/tokenizer-cache').glob('*'))
    files += list((ROOT / 'pilot/preparation').glob('task-*/restoration-proof.json'))
    files += list((ROOT / 'pilot/rebuilt-controls').glob('task-*/controls.json'))
    files += list((ROOT / 'pilot/rebuilt-controls').glob('task-*/controls-*/evaluation.json'))
    files += [core.BINARY, core.BINARY.parent / 'codex-code-mode-host']
    manifest = {'version': 'context-pilot-v1', 'tasks': selected, 'schedule': schedule,
                'schedule_note': 'Pilot uses each of five material pools once across its five tasks; independent from main-task pool mapping.',
                'workers': 1, 'arms': list(run_context.ARMS), 'model': 'gpt-6-sol', 'reasoning': 'medium',
                'main_run_authorized': False, 'source_hashes': {str(p): core.sha(p) for p in files}}
    path = ROOT / 'pilot/manifest.json'
    run_context.frozen_write(path, json.dumps(manifest, indent=2) + '\n')
    for p in files:
        if p in (core.BINARY, core.BINARY.parent / 'codex-code-mode-host'):
            continue
        target = ROOT / 'pilot/source-snapshot' / p.relative_to(run_context.LAB)
        target.parent.mkdir(parents=True, exist_ok=True)
        if target.exists():
            if core.sha(target) != core.sha(p):
                raise RuntimeError('Pilot source snapshot changed')
        else:
            shutil.copy2(p, target)
    return manifest, restoration, preparation


async def attempt(core, n, arm, pool, snap, instance, preparation, enc):
    directory = ROOT / 'pilot/trials' / f'task-{n:02d}' / arm
    result_path = directory / 'result.json'
    if result_path.exists():
        result = run_context.read(result_path)
        if result.get('status') in FINAL and result.get('context_audit', {}).get('protocol_valid'):
            print(f'Pilot {n}/{arm}: final result retained, no repeat', flush=True)
            return result
        raise RuntimeError(f'Pilot {n}/{arm}: prior technical/protocol attempt exists; explicit archival required')
    if directory.exists() and any(directory.iterdir()):
        raise RuntimeError('Prior incomplete pilot attempt exists; no automatic repeat')
    started = time.monotonic()
    core.save(directory / 'started.json', {'task': n, 'arm': arm, 'pool_id': pool, 'at': core.now()})
    image = snap['prepared_image_id']
    prompt = core.issue_prompt(instance)
    source = None
    if arm == 'A':
        window = preparation['A_calibration']['window']
        overhead = preparation['A_calibration']['measured_overhead']
        start = 'The following is unrelated background text. It contains no current work item.\n<background>\n'
        end = '\n</background>\n' + prompt
        budget = round(window * .8) - overhead - len(enc.encode(start + end))
        content = (ROOT / f'materials/A/pool-{pool}/reservoir.txt').read_text()
        prompt = start + context_materials.prefix(content, budget, enc) + end
    elif arm == 'B':
        source = run_context.read(ROOT / f'materials/B/pool-{pool}/native/session.json')
    try:
        with tempfile.TemporaryDirectory(prefix=f'context-pilot-{n}-{arm}-auth-') as tmp:
            auth = await context_materials.credential(core, tmp)
            async with core.container(image, directory / 'container', agent=True) as env:
                await core.network_checks(env, directory / 'container')
                await core.verify_toolchain(env, snap['repo_language'])
                await env.upload(str(run_context.LAB / 'patch_export.py'), '/tmp/swe-patch-export.py')
                baseline = await core.capture_export_baseline(env, 'environment', directory)
                await live.setup_auth(core, env, auth)
                session = None
                if source:
                    await live.import_session(core, env, source)
                    meta = next(r['payload'] for r in parse_rows(source['content']) if r.get('type') == 'session_meta')
                    session = meta['id']
                print(f'Pilot {n}/{arm}: starting fresh Sol6 medium attempt', flush=True)
                stage, entry, answer = await live.invoke(core, env, directory / 'standard', prompt, auth, session=session)
                prior = stage['context_audit']
                audit = analyze(parse_rows(entry['content']), benchmark_turn_id=prior['benchmark_turn_id'],
                                start_row=prior['start_row'], arm=arm)
                if source:
                    retained = await live.capture(core, env, directory / 'post-task')
                    untouched = next((e for e in retained if e['path'] == source['path']), None)
                    audit['source_history_unchanged'] = bool(untouched and untouched['content'] == source['content'])
                    audit['native_history_link_valid'] = live.history_link(source, entry)
                    if not audit['source_history_unchanged'] or not audit['native_history_link_valid']:
                        audit['errors'].append('B source history/link not preserved')
                        audit['protocol_valid'] = False
                core.save(directory / 'context-audit.json', audit)
                patch = await core.export_patch(env, baseline)
                core.save(directory / 'submission.patch', patch)
            result = {'task': n, 'arm': arm, 'pool_id': pool, 'stage': stage,
                      'context_audit': audit, 'trial_wall_seconds': time.monotonic() - started,
                      'phase': 'pilot', 'main_result': False}
            if not audit['protocol_valid']:
                result.update(status='context_protocol_problem', resolved=None)
                core.save(result_path, result)
                raise RuntimeError(f'Pilot {n}/{arm}: invalid starting context; inspect before continuation')
            if not patch.strip():
                result.update(status='empty_submission', resolved=False)
            elif not await core.valid_patch(image, patch, directory / 'patch-check'):
                result.update(status='invalid_submission', resolved=False)
            else:
                evaluation = await core.evaluate(instance, snap['original_image_id'], patch, directory / 'evaluation')
                result.update(status='completed' if evaluation.get('completed') and not evaluation.get('error') else 'evaluation_problem',
                              resolved=evaluation.get('resolved') if evaluation.get('completed') else None)
            result['trial_wall_seconds'] = time.monotonic() - started
            core.save(result_path, result)
            if result['status'] not in FINAL:
                raise RuntimeError('Pilot evaluation problem; no automatic repeat')
            return result
    except BaseException as exc:
        core.save(directory / 'interruption.json', {'at': core.now(), 'error': core.redact(str(exc)),
                                                   'elapsed_seconds': time.monotonic() - started})
        raise


async def run(core):
    run_context.validate(ROOT)
    manifest, restoration, preparation = freeze(core)
    for file, digest in manifest['source_hashes'].items():
        if core.sha(file) != digest:
            raise RuntimeError('Frozen pilot runtime changed: ' + file)
    available = live.resident_ids()
    for proof in restoration['tasks'].values():
        snap = proof['snapshot']
        if not {snap['prepared_image_id'], snap['original_image_id']} <= available:
            raise RuntimeError('A pilot image disappeared; no implicit recovery or model start')
    enc = context_materials.tokenizer()
    rows = {r['instance_id']: r for r in map(json.loads, (core.DATA / 'swebench_pro_verified.jsonl').read_text().splitlines())}
    plan = run_context.read(ROOT / 'plan.json')
    cases = {r['task']: r for r in plan['tasks']}
    try:
        for item in manifest['schedule']:
            for arm in item['arm_order']:
                for file, digest in manifest['source_hashes'].items():
                    if core.sha(file) != digest:
                        raise RuntimeError('Frozen runtime/material changed before next attempt: ' + file)
                await attempt(core, item['task'], arm, item['pool_id'],
                              restoration['tasks'][str(item['task'])]['snapshot'],
                              rows[cases[item['task']]['instance_id']], preparation, enc)
    finally:
        write_report(core)


def write_report(core):
    results = []
    for path in sorted((ROOT / 'pilot/trials').glob('task-*/*/result.json')):
        r = run_context.read(path)
        audit = r.get('context_audit', {})
        results.append({'task': r['task'], 'arm': r['arm'], 'status': r['status'], 'resolved': r.get('resolved'),
                        'starting_load': audit.get('starting_load'), 'protocol_valid': audit.get('protocol_valid'),
                        'known_task_usage': audit.get('known_task_usage'), 'usage_complete': audit.get('usage_complete'),
                        'compactions': len(audit.get('compaction_rows', [])), 'trial_wall_seconds': r.get('trial_wall_seconds')})
    complete = len(results) == 15 and all(r['status'] in FINAL and r['protocol_valid'] for r in results)
    preparation_stages = []
    unknown_preparation_attempts = []
    started_paths = list((ROOT / 'feasibility/native-portability').glob('*/started.json'))
    started_paths += list((ROOT / 'materials/calibration-A').glob('call/started.json'))
    started_paths += list((ROOT / 'materials/B').glob('pool-*/native/unit-*/started.json'))
    for started in started_paths:
        path = started.parent / 'stage.json'
        if path.exists():
            preparation_stages.append(run_context.read(path))
        else:
            unknown_preparation_attempts.append(str(started.parent.relative_to(ROOT)))
    report = {'status': 'pilot_completed' if complete else 'pilot_interim', 'results': results,
              'main_run_authorized': False, 'main_started': False,
              'preparation_consumption': {
                  'started_codex_calls': len(started_paths), 'recorded_stages': len(preparation_stages),
                  'known_attributed_model_requests': sum(len(s.get('context_audit', {}).get('requests', [])) for s in preparation_stages),
                  'calls_without_per_request_summary': sum('context_audit' not in s for s in preparation_stages),
                  'known_usage': {k: sum(s.get('usage', {}).get(k, 0) for s in preparation_stages)
                                  for k in live.native_ultra.KEYS},
                  'usage_complete': not unknown_preparation_attempts and all(s.get('usage_complete') for s in preparation_stages),
                  'unknown_attempts': unknown_preparation_attempts,
                  'known_elapsed_seconds': sum(s.get('elapsed_seconds', 0) for s in preparation_stages)},
              'note': 'Technical pilot only, not part of main inference or hypothesis tests. Review loading/portability first; no material selection by solve rate.'}
    core.save(ROOT / 'pilot/report.json', report)
    return report
