#!/usr/bin/env python3
"""Explicit live feasibility/pilot tooling; no main-run entry point.

Uses unchanged shared container preparation, policy and evaluator. New session
state is captured only from fresh experiment containers, never personal homes.
"""
import argparse
import asyncio
from contextlib import contextmanager
import fcntl
import hashlib
import json
import os
from pathlib import Path
import shutil
import tempfile
import time
import uuid

os.environ.setdefault('LITELLM_LOCAL_MODEL_COST_MAP', 'True')
import native_ultra
import run_context
from context_telemetry import analyze, parse_rows
from run_sol_ultra import core_module

ROOT = run_context.ROOT
RUNTIME_ENV = {'CODEX_HOME': '/opt/v2-codex', 'OPENAI_API_KEY': '', 'CODEX_API_KEY': '',
               'AZURE_OPENAI_API_KEY': '', 'ANTHROPIC_API_KEY': '', 'OPENAI_BASE_URL': ''}


def base():
    core = core_module()
    core.HERE = ROOT
    core.RUN_MODEL = 'gpt-6-sol'
    core.RUN_REASONING = 'medium'
    core.save(ROOT / 'experiment.json', {'model': 'gpt-6-sol', 'reasoning': 'medium',
              'storage_reserve_gib': 25, 'main_run_authorized': False})
    return core


def resident_ids():
    result = run_context.command(['docker', 'image', 'ls', '-aq', '--no-trunc'])
    if not result['ok']:
        raise RuntimeError('Docker unavailable: ' + result.get('stderr', result.get('error', '')))
    return set(result['stdout'].split())


def pilot_selection(plan, ids):
    # Restore from exact resident evaluation images; missing snapshots are expected.
    all_eligible = [r for r in plan['tasks'] if not r['excluded']]
    priority = {3: 0, 2: 1, 1: 2}
    all_eligible.sort(key=lambda r: (priority[(r['task'] - 1) // 100 + 1], r['task']))
    eligible = [r for r in all_eligible if r['snapshot']['original_image_id'] in ids]
    # Fixed lexicographic selection; no candidate solutions/scores consulted.
    chosen = []
    for language in ('go', 'python', 'js', 'ts'):
        resident = [r for r in eligible if r['language'] == language]
        chosen.append(resident[0] if resident else next(r for r in all_eligible if r['language'] == language))
    chosen.append(next(r for r in eligible if r not in chosen))
    return chosen


async def restore(core):
    plan = run_context.validate(ROOT)
    ids = resident_ids()
    path = ROOT / 'pilot/selection.json'
    if path.exists():
        selection = run_context.read(path)
        chosen = [r for r in plan['tasks'] if r['task'] in selection['tasks']]
        chosen.sort(key=lambda r: selection['tasks'].index(r['task']))
    else:
        chosen = pilot_selection(plan, ids)
        selection = {'tasks': [r['task'] for r in chosen], 'languages': [r['language'] for r in chosen],
                     'reason': 'First exact resident evaluation image per language, block201 preferred; first eligible task if a language has no resident image (fetch pinned official source). Fifth first remaining resident task. No model outcomes consulted.',
                     'workers': 1, 'model_calls': 0}
        core.save(path, selection)
    restored = {}
    master = run_context.read(run_context.LAB / 'selection-mas-300.json')
    for row in chosen:
        n = row['task']
        directory = ROOT / 'pilot/preparation' / f'task-{n:02d}'
        rebuilt_controls = None
        if row['language'] == 'ts' and row['snapshot']['original_image_id'] not in ids:
            snap, rebuilt_controls = await restore_typescript(core, row, master['scored_tasks'][n - 1])
            directory = ROOT / 'pilot/rebuilt-controls' / f'task-{n:02d}/preparation'
            ids.update((snap['prepared_image_id'], snap['original_image_id']))
        elif (directory / 'snapshot.json').exists():
            snap = run_context.read(directory / 'snapshot.json')
            if snap['prepared_image_id'] not in ids:
                raise RuntimeError(f'Task {n}: restored snapshot disappeared; explicit recovery required')
        else:
            if directory.exists() and any(directory.iterdir()):
                raise RuntimeError(f'Task {n}: incomplete restoration exists; archive explicitly before continuation')
            print(f'Restoring pilot snapshot {n} ({row["language"]}); no model calls', flush=True)
            snap = await core.prepare(master['scored_tasks'][n - 1], directory)
            ids.add(snap['prepared_image_id'])
        old = row['snapshot']
        fields = ('official_image_id', 'canonical_tree', 'repo_language',
                  'toolchains', 'login_shell_toolchains')
        if not rebuilt_controls:
            fields += ('original_image_id',)
        different = [field for field in fields if old.get(field) != snap.get(field)]
        original_tracked = run_context.LAB / row['control_donor'] / f'task-{n:02d}/preparation/canonical-tracked-files.txt'
        if run_context.sha(original_tracked) != run_context.sha(directory / 'canonical-tracked-files.txt'):
            different.append('canonical-tracked-files.txt')
        proof = {'task': n, 'different_fields': different, 'control_donor': row['control_donor'],
                 'control_reuse': 'Fresh original/reference controls on rebuilt TS dependency image' if rebuilt_controls else 'Exact evaluation image and evaluator hashes unchanged; reconstructed snapshot tree/toolchains/tracked files compared.',
                 'rebuilt_controls': rebuilt_controls,
                 'old_prepared_image_id': old['prepared_image_id'], 'snapshot': snap, 'model_calls': 0}
        core.save(directory / 'restoration-proof.json', proof)
        if different:
            raise RuntimeError(f'Task {n}: reconstructed environment differs: {different}')
        restored[str(n)] = proof
    core.save(ROOT / 'pilot/restoration.json', {'status': 'verified', 'tasks': restored,
              'model_calls': 0, 'controls_reexecuted': False})
    print('Five pilot snapshots restored and compared against passing control evidence.', flush=True)
    return restored


async def restore_typescript(core, row, case):
    """Rebuild missing Node header/ownership overlay without changing shared data.

    A rebuilt cache has a new content ID: fresh controls are mandatory. The old
    donor is used only for canonical source/toolchain comparison, not to claim
    unchanged evaluation image identity.
    """
    import warm_control_dependencies
    directory = ROOT / 'trusted-dependency-preparation'
    directory.mkdir(exist_ok=True)
    private_data = directory / 'data'
    private_data.mkdir(exist_ok=True)
    target = private_data / 'swebench_pro_verified.jsonl'
    if not target.exists():
        target.symlink_to(core.DATA / 'swebench_pro_verified.jsonl')
    warmer = warm_control_dependencies.runner
    prior_lab, prior_data = warmer.LAB, warmer.DATA
    warmer.LAB, warmer.DATA = directory, private_data
    try:
        selection = run_context.read(run_context.LAB / 'selection-mas-300.json')
        await warm_control_dependencies.warm(selection, [row['task']])
    finally:
        warmer.LAB, warmer.DATA = prior_lab, prior_data
    old_data = core.DATA
    core.DATA = private_data
    try:
        instance = next(json.loads(line) for line in target.open() if json.loads(line)['instance_id'] == case['instance_id'])
        snap, passed = await core.validate_task_controls(row['task'], case, instance, ROOT / 'pilot/rebuilt-controls')
        if not passed:
            raise RuntimeError('Rebuilt TypeScript environment failed fresh controls; do not exclude or start models')
        return snap, {'passed': True, 'path': str(ROOT / 'pilot/rebuilt-controls' / f'task-{row["task"]:02d}/controls.json')}
    finally:
        core.DATA = old_data


def arguments(developer, *, session=None, continuation='fork'):
    args = ['codex', 'exec', '--json', '--ignore-user-config', '--cd', '/app',
            '--model', 'gpt-6-sol', '--dangerously-bypass-approvals-and-sandbox',
            '-c', 'forced_login_method="chatgpt"', '-c', 'web_search="disabled"',
            '-c', 'model_reasoning_effort="medium"', '-c', 'agents.enabled=false',
            '-c', 'features.multi_agent=false', '-c', 'features.apps=false',
            '-c', 'features.remote_plugin=false', '-c', 'developer_instructions=' + json.dumps(developer)]
    if continuation not in ('fork', 'resume'):
        raise ValueError('Unsupported native continuation')
    return args + ([continuation, session, '-'] if session else ['--', '-'])


def history_link(source_entry, fork_entry):
    source_rows = parse_rows(source_entry['content'])
    fork_rows = parse_rows(fork_entry['content'])
    source_meta = next(r['payload'] for r in source_rows if r.get('type') == 'session_meta')
    fork_meta = next(r['payload'] for r in fork_rows if r.get('type') == 'session_meta')
    boundary = fork_meta.get('forked_from_ordinal_exclusive')
    if fork_meta.get('forked_from_id') != source_meta['id'] or not isinstance(boundary, int) or boundary <= 0 or boundary > len(source_rows):
        return False
    types = {(r.get('payload') or {}).get('type') for r in source_rows[:boundary] if r.get('type') == 'response_item'}
    return bool(types & {'function_call', 'custom_tool_call'} and
                types & {'function_call_output', 'custom_tool_call_output'})


async def setup_auth(core, env, credential):
    await env.checked(['mkdir', '-p', '/opt/v2-codex'])
    await env.upload(str(credential), '/opt/v2-codex/auth.json')
    await env.checked(['chmod', '600', '/opt/v2-codex/auth.json'])
    result = await env.checked(['codex', 'login', 'status'], required_env=RUNTIME_ENV)
    if 'Logged in using ChatGPT' not in result.stdout + result.stderr:
        raise RuntimeError('ChatGPT login not confirmed')


async def capture(core, env, directory):
    captured = json.loads((await env.checked(['python', '-c', native_ultra.CAPTURE])).stdout)
    if not captured['complete']:
        raise RuntimeError('Native rollout capture incomplete')
    for entry in captured['files']:
        entry['content'] = core.redact(entry['content'])
        name = hashlib.sha256(entry['path'].encode()).hexdigest() + '.jsonl'
        core.save(directory / 'native-threads' / name, entry['content'])
    core.save(directory / 'capture.json', captured)
    return captured['files']


async def invoke(core, env, directory, prompt, credential, *, session=None, developer=None, continuation='fork'):
    directory.mkdir(parents=True, exist_ok=True)
    if (directory / 'started.json').exists():
        raise RuntimeError('Attempt exists; no automatic repeat: ' + str(directory))
    developer = developer or core.role_instructions('standard')
    core.save(directory / 'prompt.txt', prompt)
    core.save(directory / 'developer-instructions.txt', developer)
    argv = arguments(developer, session=session, continuation=continuation)
    core.save(directory / 'invocation.json', {'argv': argv, 'prompt_transport': 'stdin',
                                             'model': 'gpt-6-sol', 'reasoning': 'medium'})
    cmd = ['docker', 'exec', '-i', '-w', '/app']
    for k, v in RUNTIME_ENV.items():
        cmd += ['-e', f'{k}={v}']
    cmd += [env.container_id, *argv]
    core.save(directory / 'started.json', {'at': core.now(), 'source_session': session})
    started = time.monotonic()
    process = await asyncio.create_subprocess_exec(*cmd, stdin=asyncio.subprocess.PIPE,
                   stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE,
                   limit=64 * 1024 * 1024)

    async def stream(reader, path):
        with path.open('w') as output:
            while line := await reader.readline():
                output.write(core.redact(line.decode(errors='replace')))
                output.flush()

    async def send():
        process.stdin.write(prompt.encode())
        await process.stdin.drain()
        process.stdin.close()
    streams = asyncio.gather(stream(process.stdout, directory / 'events.jsonl'),
                             stream(process.stderr, directory / 'stderr.log'))
    interrupted = None
    process_elapsed = None
    try:
        await send()
        await process.wait()
        await streams
        process_elapsed = time.monotonic() - started
    except BaseException as error:
        interrupted = error
        if process.returncode is None:
            process.terminate()
            await process.wait()
        streams.cancel()
        await asyncio.gather(streams, return_exceptions=True)
    finally:
        try:
            refreshed = await env.read_text('/opt/v2-codex/auth.json')
            core.learn_secrets(json.loads(refreshed))
            credential.write_text(refreshed)
        except Exception:
            if interrupted is None:
                interrupted = RuntimeError('Credential refresh capture failed')
        for name in ('events.jsonl', 'stderr.log'):
            path = directory / name
            if path.exists():
                core.save(path, core.redact(path.read_text()))
    files = await capture(core, env, directory)
    events = core.CodexHarness._parse_json_events((directory / 'events.jsonl').read_text())
    roots = {r['thread_id'] for r in events if r.get('type') == 'thread.started' and r.get('thread_id')}
    if len(roots) != 1:
        raise RuntimeError('Expected one native root thread')
    thread = roots.pop()
    own = [f for f in files if any(r.get('type') == 'session_meta' and
           (r.get('payload') or {}).get('id') == thread for r in parse_rows(f['content']))]
    if len(own) != 1:
        raise RuntimeError('Native root rollout attribution ambiguous')
    answer = core.CodexHarness._extract_final_answer(events, '')
    core.save(directory / 'answer.md', answer)
    turns = [e for e in events if e.get('type') == 'turn.completed']
    usage = {k: sum(int((e.get('usage') or {}).get(k) or 0) for e in turns) for k in native_ultra.KEYS}
    result = {'thread_id': thread, 'elapsed_seconds': time.monotonic() - started,
              'process_elapsed_seconds': process_elapsed,
              'exit_code': process.returncode, 'usage': usage, 'usage_complete': bool(turns) and interrupted is None,
              'status': 'completed' if turns and process.returncode == 0 and interrupted is None else 'technical_interruption'}
    prohibited = [e for e in events if any(word in str((e.get('item') or {}).get('type', '')).lower()
                                          for word in ('web_search', 'collab', 'agent_tool'))]
    if prohibited:
        result['status'] = 'technical_interruption'
        result['configuration_error'] = 'Prohibited web or delegation tool event'
    rows = parse_rows(own[0]['content'])
    starts = [(i, (r.get('payload') or {}).get('turn_id')) for i, r in enumerate(rows)
              if r.get('type') == 'event_msg' and (r.get('payload') or {}).get('type') == 'task_started']
    if starts:
        offset, turn_id = starts[-1]
        audit = analyze(rows, benchmark_turn_id=turn_id, start_row=offset, arm='standard')
        result['cli_reported_usage'] = result['usage']
        result.update(context_audit=audit, usage=audit['known_task_usage'], usage_complete=audit['usage_complete'])
        contexts = [r.get('payload') or {} for r in rows[offset:] if r.get('type') == 'turn_context']
        if not contexts or any(c.get('model') != 'gpt-6-sol' or c.get('effort') != 'medium' or c.get('cwd') != '/app' for c in contexts):
            result['status'] = 'technical_interruption'
            result['configuration_error'] = 'Model/effort/cwd did not match fixed protocol'
        if not audit['protocol_valid']:
            result['status'] = 'technical_interruption'
    core.save(directory / 'stage.json', result)
    if interrupted:
        raise interrupted
    if result['status'] != 'completed' or core.CodexHarness._first_error_event(events):
        raise RuntimeError('Technical Codex interruption; inspect ' + str(directory))
    return result, own[0], answer


async def import_session(core, env, entry):
    relative = Path(entry['path'])
    if relative.is_absolute() or '..' in relative.parts or relative.suffix != '.jsonl':
        raise RuntimeError('Unsafe session path')
    target = Path('/opt/v2-codex/sessions') / relative
    await env.checked(['mkdir', '-p', str(target.parent)])
    # Only a newly generated experiment session is restored. No invented rows,
    # personal configuration, credentials or SQLite databases are imported.
    await env.write_text(str(target), entry['content'])


async def probe(core):
    if (ROOT / 'pilot/restoration.json').exists():
        proof = run_context.read(ROOT / 'pilot/restoration.json')
    else:
        partial = [run_context.read(p) for p in (ROOT / 'pilot/preparation').glob('task-*/restoration-proof.json')]
        proof = {'tasks': {str(r['task']): r for r in partial if not r['different_fields']}}
    n = next(k for k, v in proof['tasks'].items() if v['snapshot']['repo_language'] == 'python')
    image = proof['tasks'][n]['snapshot']['prepared_image_id']
    directory = ROOT / 'feasibility/native-portability'
    if directory.exists() and any(directory.iterdir()):
        raise RuntimeError('Probe artifacts exist. Inspect/archive explicitly before another attempt.')
    marker = 'context-history-' + uuid.uuid4().hex
    core.save(directory / 'expected-marker.json', {'marker': marker, 'purpose': 'Unrelated project memory probe, never a benchmark answer'})
    with tempfile.TemporaryDirectory(prefix='context-probe-auth-') as tmp:
        credential = Path(tmp) / 'auth.json'
        secret = core.AUTH.read_bytes()
        core.learn_secrets(json.loads(secret)); credential.write_bytes(secret); credential.chmod(0o600)
        async with core.container(image, directory / 'preparation-container', agent=True) as env:
            await core.network_checks(env, directory / 'preparation-container')
            # Wipe only /app in this fresh disposable container; the repo is not
            # host-mounted. The probe must not use benchmark project content.
            await env.checked(['python', '-c', "import pathlib,shutil; p=pathlib.Path('/app'); assert not p.is_symlink(); [(shutil.rmtree(x) if x.is_dir() and not x.is_symlink() else x.unlink()) for x in p.iterdir()]"])
            await env.checked(['git', 'init', '--quiet', '/app'])
            await env.write_text('/app/history-proof.txt', marker + '\n')
            await setup_auth(core, env, credential)
            source, entry, _ = await invoke(core, env, directory / 'source',
                'This is a separate, unrelated project. Read /app/history-proof.txt using a shell command. '
                'Report its exact contents and state that this work item is complete. Do not inspect any other files.', credential)
        async with core.container(image, directory / 'fresh-task-container', agent=True) as env:
            await core.network_checks(env, directory / 'fresh-task-container')
            await setup_auth(core, env, credential)
            await import_session(core, env, entry)
            original_sha = hashlib.sha256(entry['content'].encode()).hexdigest()
            forked, output, answer = await invoke(core, env, directory / 'fork',
                'The earlier work item is finished. This is a technical session-memory check in a new filesystem. '
                'Without reading project code, run pwd and verify that /app/history-proof.txt does not exist. '
                'Then report the exact marker read during the earlier work item from conversation memory. '
                'Do not search for it elsewhere and do not create or modify files.', credential,
                session=source['thread_id'])
            files = await capture(core, env, directory / 'post-fork')
            retained = next((e for e in files if e['path'] == entry['path']), None)
            rows = parse_rows(output['content'])
            starts = [(i, r['payload']['turn_id']) for i, r in enumerate(rows) if
                      r.get('type') == 'event_msg' and (r.get('payload') or {}).get('type') == 'task_started']
            if not starts:
                raise RuntimeError('No native task boundary in fork')
            offset, turn = starts[-1]
            audit = analyze(rows, benchmark_turn_id=turn, start_row=offset, arm='standard')
            unchanged = retained is not None and hashlib.sha256(retained['content'].encode()).hexdigest() == original_sha
            checks = {'new_thread_id': forked['thread_id'] != source['thread_id'],
                      'source_history_unchanged': unchanged, 'marker_recalled': marker in answer,
                      'old_file_absent': (await env.exec(['test', '!', '-e', '/app/history-proof.txt'])).returncode == 0,
                      'request_measurement_valid': audit['protocol_valid'],
                      'native_tool_history_present': history_link(entry, output)}
            core.save(directory / 'result.json', {'status': 'passed' if all(checks.values()) else 'failed',
                      'checks': checks, 'context_audit': audit, 'source_stage': source, 'fork_stage': forked,
                      'note': 'Small portability probe only. No 80-percent condition or benchmark outcome tested.'})
            if not all(checks.values()):
                raise RuntimeError('Portability probe failed: ' + repr(checks))
    print('Native session portability and attributable request telemetry verified.', flush=True)


def verify_probe(core):
    """Re-evaluate captured evidence after a parser fix, never repeat model calls."""
    directory = ROOT / 'feasibility/native-portability'
    path = directory / 'result.json'
    old = run_context.read(path)
    if old['status'] == 'passed':
        print('Portability evidence already passed; no model calls.')
        return
    if set(k for k, v in old['checks'].items() if not v) != {'native_tool_history_present'}:
        raise RuntimeError('Probe has other failed checks; offline schema correction cannot resolve them')
    source_id = old['source_stage']['thread_id']
    fork_id = old['fork_stage']['thread_id']
    def own(part, tid):
        entries = run_context.read(directory / part / 'capture.json')['files']
        return next(e for e in entries if any(r.get('type') == 'session_meta' and (r.get('payload') or {}).get('id') == tid for r in parse_rows(e['content'])))
    if not history_link(own('source', source_id), own('fork', fork_id)):
        raise RuntimeError('Native parent/tool evidence not established')
    run_context.frozen_write(directory / 'result-before-history-link-schema-fix.json', json.dumps(old, indent=2) + '\n')
    old['checks']['native_tool_history_present'] = True
    old['status'] = 'passed'
    old['schema_correction'] = 'Native fork stores parent ID and ordinal reference, not copied response rows. Existing source call/output within referenced prefix verified; no repeated model call.'
    core.save(path, old)
    print('Native source/fork history link verified from preserved raw evidence; no model calls.')


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('phase', choices=('restore', 'probe', 'verify-probe', 'materials', 'pilot', 'report'))
    args = p.parse_args()
    ROOT.mkdir(exist_ok=True)
    with (ROOT / '.live.lock').open('a') as lock:
        fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        core = base()
        if args.phase == 'pilot':
            import context_pilot
            asyncio.run(context_pilot.run(core))
        elif args.phase == 'report':
            import context_pilot
            print(context_pilot.write_report(core)['status'])
        elif args.phase == 'materials':
            import context_materials
            asyncio.run(context_materials.prepare(core))
        elif args.phase == 'verify-probe':
            verify_probe(core)
        elif args.phase == 'restore':
            asyncio.run(restore(core))
        else:
            run_context.validate(ROOT)
            asyncio.run(probe(core))


if __name__ == '__main__':
    main()
