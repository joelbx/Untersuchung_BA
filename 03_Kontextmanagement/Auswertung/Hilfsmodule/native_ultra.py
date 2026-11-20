"""Native Codex Ultra profile. No inference on import; old benchmark code stays unchanged."""
import asyncio
import hashlib
import json
from pathlib import Path
import re
import time

KEYS = ('input_tokens', 'cached_input_tokens', 'output_tokens', 'reasoning_output_tokens')


def usage(value):
    aliases = {'reasoning_output_tokens': ('reasoning_output_tokens', 'reasoning_tokens', 'output_reasoning_tokens')}
    out = {}
    for key in KEYS:
        out[key] = next((int(value[k] or 0) for k in aliases.get(key, (key,)) if k in value), 0)
    return out


def trace(events, files, *, capture_complete=True):
    """Latest cumulative usage per thread, never add it to the same thread's CLI usage."""
    roots = [e['thread_id'] for e in events if e.get('type') == 'thread.started' and e.get('thread_id')]
    root = roots[0] if len(set(roots)) == 1 else None
    threads = {}
    errors = []
    for entry in files:
        rows = []
        for line in entry['content'].splitlines():
            if not line.strip():
                continue
            try:
                rows.append(json.loads(line))
            except json.JSONDecodeError:
                errors.append('Malformed rollout JSON: ' + entry['path'])
        meta = next((r.get('payload', {}) for r in rows if r.get('type') == 'session_meta'), {})
        tid = meta.get('id')
        if not isinstance(tid, str):
            errors.append('Rollout has no thread ID: ' + entry['path'])
            continue
        current = None
        for row in rows:
            payload = row.get('payload') or {}
            if row.get('type') == 'event_msg' and payload.get('type') == 'token_count':
                total = (payload.get('info') or {}).get('total_token_usage')
                if isinstance(total, dict):
                    current = usage(total)
        # Duplicate files for the same ID are ambiguous, not additional usage.
        if tid in threads:
            errors.append('Duplicate thread ID: ' + tid)
        threads[tid] = {'thread_id': tid, 'metadata': meta, 'usage': current, 'rollout': entry['path']}
    turns = [e for e in events if e.get('type') == 'turn.completed']
    parent_usage = {k: sum(usage(e.get('usage') or {})[k] for e in turns) for k in KEYS} if turns else None
    if root and root not in threads:
        threads[root] = {'thread_id': root, 'metadata': {}, 'usage': parent_usage, 'rollout': None}
    elif root and threads[root]['usage'] is None:
        threads[root]['usage'] = parent_usage
    calls = []
    expected = set()
    for e in events:
        item = e.get('item') or {}
        kind = str(item.get('type', '')).lower()
        if e.get('type') == 'item.completed' and ('collab' in kind or 'agent_tool' in kind):
            calls.append(item)
            for field in ('receiver_thread_ids', 'receiverThreadIds'):
                expected.update(x for x in item.get(field, []) if isinstance(x, str))
            for field in ('agents_states', 'agentsStates'):
                states = item.get(field)
                if isinstance(states, dict):
                    expected.update(states)
    children = set(threads) - ({root} if root else set())
    unknown = sorted((expected | set(threads)) - {i for i, t in threads.items() if t['usage'] is not None})
    totals = {k: sum(t['usage'][k] for t in threads.values() if t['usage'] is not None) for k in KEYS}
    complete = bool(root and turns and threads.get(root, {}).get('rollout') and
                    capture_complete and not errors and not unknown)
    return {'root_thread_id': root, 'threads': list(threads.values()), 'collaboration_calls': calls,
            'child_thread_ids': sorted(children | (expected - ({root} if root else set()))),
            'known_usage': totals, 'usage_complete': complete, 'unknown_usage_thread_ids': unknown,
            'capture_complete': capture_complete, 'errors': errors,
            'usage_method': 'Latest cumulative token_count per unique rollout thread; root CLI usage only as a root fallback.'}


def arguments(model, developer, prompt):
    # Persistent logs live only in this fresh container, never resumed by another trial.
    return ['codex', 'exec', '--json', '--ignore-user-config', '--cd', '/app', '--model', model,
            '--dangerously-bypass-approvals-and-sandbox', '-c', 'forced_login_method="chatgpt"',
            '-c', 'web_search="disabled"', '-c', 'model_reasoning_effort="ultra"',
            '-c', 'agents.enabled=true', '-c', 'features.multi_agent=true',
            '-c', 'agents.default_subagent_model=' + json.dumps(model),
            '-c', 'agents.default_subagent_reasoning_effort="ultra"',
            '-c', 'features.apps=false', '-c', 'features.remote_plugin=false',
            '-c', 'developer_instructions=' + json.dumps(developer), '--', prompt]


CAPTURE = r'''
import json,pathlib
root=pathlib.Path('/opt/v2-codex/sessions')
files=[];size=0;complete=True
for p in sorted(root.rglob('*.jsonl')) if root.exists() else []:
    if p.is_symlink():
        complete=False;continue
    try:
        p.resolve().relative_to(root.resolve())
    except ValueError:
        complete=False;continue
    content=p.read_text(errors='replace');size+=len(content.encode())
    if size>128*1024*1024:
        complete=False;break
    files.append({'path':str(p.relative_to(root)),'content':content})
print(json.dumps({'files':files,'complete':complete}))
'''


async def stage(base, image, role, prompt, patch, directory, credential, **kwargs):
    if role != 'standard' or patch:
        raise ValueError('Native Ultra profile supports a fresh standard trial only')
    directory = Path(directory)
    directory.mkdir(parents=True, exist_ok=True)
    developer = base.role_instructions('standard').replace('Do not request downloads or delegate.',
                                                          'Do not request downloads.')
    developer += ('\nNative Ultra profile: you may use native subagents when useful. '
                  'Keep all agents on the selected model and reasoning; do not override their model or effort. '
                  'All repository, privacy, test and no-external-research rules apply to every subagent. '
                  'Use only native delegation tools, never start a separate Codex process. '
                  'Wait for all delegated work and integrate/verify the final patch before finishing. '
                  'Describe any delegation and relevant tests in the final answer.')
    base.save(directory/'prompt.txt', prompt)
    base.save(directory/'developer-instructions.txt', developer)
    if base.PINNED_NATIVE is not None:
        assert {'binary_sha256': base.sha(base.BINARY),
                'code_mode_host_sha256': base.sha(base.BINARY.parent/'codex-code-mode-host')} == base.PINNED_NATIVE
    async with base.container(image, directory, agent=True) as env:
        await base.network_checks(env, directory)
        await base.verify_toolchain(env, base.IMAGE_LANGUAGES[image])
        await env.upload(str(base.SOURCE_DIR/'patch_export.py'), '/tmp/swe-patch-export.py')
        baseline = await base.capture_export_baseline(env, 'environment', directory)
        await env.checked(['mkdir', '-p', '/opt/v2-codex'])
        await env.upload(str(credential), '/opt/v2-codex/auth.json')
        await env.checked(['chmod', '600', '/opt/v2-codex/auth.json'])
        runtime_env = {'CODEX_HOME': '/opt/v2-codex', 'OPENAI_API_KEY': '', 'CODEX_API_KEY': '',
                       'AZURE_OPENAI_API_KEY': '', 'ANTHROPIC_API_KEY': '', 'OPENAI_BASE_URL': ''}
        login = await env.checked(['codex', 'login', 'status'], required_env=runtime_env)
        if 'Logged in using ChatGPT' not in login.stdout + login.stderr:
            raise RuntimeError('Subscription authentication was not verified')
        argv = arguments(base.RUN_MODEL, developer, prompt)
        base.save(directory/'invocation.json', {'argv': argv, 'auth_mode': 'chatgpt', 'timeout_seconds': None})
        cmd = ['docker', 'exec', '-w', '/app']
        for key, value in runtime_env.items():
            cmd += ['-e', f'{key}={value}']
        cmd += [env.container_id, *argv]
        started = time.monotonic()
        process = await asyncio.create_subprocess_exec(*cmd, stdout=asyncio.subprocess.PIPE,
                    stderr=asyncio.subprocess.PIPE, limit=64*1024*1024)

        async def stream(reader, path):
            with path.open('w') as output:
                while line := await reader.readline():
                    output.write(base.redact(line.decode(errors='replace'))); output.flush()

        streams = asyncio.gather(stream(process.stdout, directory/'events.jsonl'),
                                 stream(process.stderr, directory/'stderr.log'))
        error = None
        try:
            await process.wait()
            await streams
        except BaseException as exc:
            error = exc
            if process.returncode is None:
                try:
                    process.terminate()
                except ProcessLookupError:
                    pass
            streams.cancel()
            await asyncio.gather(streams, return_exceptions=True)
        elapsed = time.monotonic()-started
        try:
            refreshed = await env.read_text('/opt/v2-codex/auth.json')
            base.learn_secrets(json.loads(refreshed)); credential.write_text(refreshed)
        except Exception:
            if error is None:
                raise
        for path in (directory/'events.jsonl', directory/'stderr.log'):
            if path.exists():
                base.save(path, base.redact(path.read_text()))
        events = base.CodexHarness._parse_json_events((directory/'events.jsonl').read_text())
        capture_error = None
        try:
            captured = json.loads((await env.checked(['python', '-c', CAPTURE])).stdout)
        except Exception as exc:
            captured = {'files': [], 'complete': False}
            capture_error = base.redact(str(exc))
        for entry in captured['files']:
            entry['content'] = base.redact(entry['content'])
            name = hashlib.sha256(entry['path'].encode()).hexdigest()+'.jsonl'
            base.save(directory/'native-threads'/name, entry['content'])
            entry['path'] = 'native-threads/'+name
        audit = trace(events, captured['files'], capture_complete=captured['complete'])
        audit['capture_error'] = capture_error
        base.save(directory/'native-agents.json', audit)
        final = base.CodexHarness._extract_final_answer(events, '')
        base.save(directory/'answer.md', final)
        completed = any(e.get('type') == 'turn.completed' for e in events)
        errors = [e for e in events if e.get('type') in ('error', 'turn.failed')]
        web = [e for e in events if 'web_search' in str((e.get('item') or {}).get('type', ''))]
        metadata = {'role': role, 'profile': 'native-ultra', 'reasoning': 'ultra',
                    'elapsed_seconds': elapsed, 'exit_code': process.returncode,
                    'timed_out': False, 'timeout_seconds': None, 'reported_error_count': len(errors),
                    'usage': audit['known_usage'], 'usage_complete': audit['usage_complete'] and error is None,
                    'known_usage_only': not audit['usage_complete'], 'handoff': final[:6000],
                    'unexpected_web_tools': len(web), 'native_agent_count': len(audit['child_thread_ids'])}
        base.save(directory/'stage.json', metadata)
        base.save(directory/'reported-errors.json', errors)
        if error is not None:
            raise error
        if not completed or process.returncode != 0 or errors or web:
            raise RuntimeError('Native Ultra technical interruption; inspect preserved events, not a functional failure')
        if base.CodexHarness._first_error_event(events) is not None or re.search(
                r'failed to spawn .*host', (directory/'stderr.log').read_text()):
            raise RuntimeError('Native Codex/tool startup failed')
        diff = await base.export_patch(env, baseline)
        base.save(directory/'repository.patch', diff)
        metadata['patch_bytes'] = len(diff.encode())
        base.save(directory/'stage.json', metadata)
        return metadata, diff
