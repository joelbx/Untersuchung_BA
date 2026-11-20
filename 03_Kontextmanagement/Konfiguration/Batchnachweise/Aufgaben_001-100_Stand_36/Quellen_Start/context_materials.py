"""Real unrelated work histories and separately measured text calibration.

Preparation calls are not benchmark attempts. No benchmark outcome is used to
select material. Tokenizer counts are estimates; native request usage is evidence.
"""
import asyncio
import json
import os
from pathlib import Path
import tempfile

import context_live as live
import run_context

ROOT = run_context.ROOT


def tokenizer():
    import tiktoken
    os.environ['TIKTOKEN_CACHE_DIR'] = str(ROOT / 'materials/tokenizer-cache')
    return tiktoken.get_encoding('o200k_base')


def prefix(text, count, enc):
    values = enc.encode(text)
    if len(values) < count:
        raise RuntimeError('Material reservoir too short')
    # Token prefix may end within a Unicode code point. Decode a valid prefix;
    # the actual request measurement is still mandatory.
    return enc.decode(values[:count], errors='ignore')


def snapshot():
    proof = run_context.read(ROOT / 'pilot/restoration.json')
    return next(v['snapshot'] for v in proof['tasks'].values() if v['snapshot']['repo_language'] == 'python')


async def credential(core, tmp):
    path = Path(tmp) / 'auth.json'
    secret = core.AUTH.read_bytes()
    core.learn_secrets(json.loads(secret)); path.write_bytes(secret); path.chmod(0o600)
    return path


async def text_calibration(core, enc, snap):
    directory = ROOT / 'materials/calibration-A'
    if (directory / 'result.json').exists():
        result = run_context.read(directory / 'result.json')
        if result['status'] != 'passed':
            raise RuntimeError('Prior A calibration failed; explicit inspection required')
        return result
    # Window comes from the successful LIVE portability probe, not cached capacity.
    window = run_context.read(ROOT / 'feasibility/native-portability/result.json')['context_audit']['window']
    reservoir = (ROOT / 'materials/A/pool-1/reservoir.txt').read_text()
    estimated_overhead = 9400
    fill_count = round(window * .80) - estimated_overhead
    content = prefix(reservoir, fill_count, enc)
    prompt = ('The following is unrelated background text. It contains no current work item.\n'
              '<background>\n' + content + '\n</background>\n'
              'This is a technical input-length calibration. Reply only READY. Do not use tools or change files.')
    with tempfile.TemporaryDirectory(prefix='context-calibration-auth-') as tmp:
        auth = await credential(core, tmp)
        async with core.container(snap['prepared_image_id'], directory / 'container', agent=True) as env:
            await core.network_checks(env, directory / 'container')
            await live.setup_auth(core, env, auth)
            stage, entry, _ = await live.invoke(core, env, directory / 'call', prompt, auth)
    audit = stage['context_audit']
    observed = audit['first_request_input_tokens']
    result = {'status': 'passed' if audit['protocol_valid'] and not audit['compaction_rows'] and .78 <= audit['starting_load'] <= .82 else 'failed',
              'tokenizer': 'o200k_base estimate, not assumed model identity',
              'encoded_prompt_tokens': len(enc.encode(prompt)), 'measured_input_tokens': observed,
              'measured_overhead': observed - len(enc.encode(prompt)), 'window': audit['window'],
              'stage': stage, 'note': 'Calibration only, no benchmark question or evaluation.'}
    core.save(directory / 'result.json', result)
    if result['status'] != 'passed':
        raise RuntimeError('A calibration outside target/compacted; inspect without a benchmark retry')
    return result


def work_data(pool, chunk, budget, enc):
    # A separate synthetic catalogue domain. These are actual generated work
    # inputs, not fabricated assistant/tool messages or benchmark-derived data.
    lines = ['record_id,collection,year,position,quantity,condition']
    i = 0
    while True:
        i += 1
        lines.append(f'{pool}-{chunk}-{i},collection-{(i * 7 + pool) % 31},{1950 + i % 75},{i % 97},{(i * 17 + chunk) % 251},category-{i % 9}')
        if i % 1000 == 0 and len(enc.encode('\n'.join(lines))) >= budget + 100:
            break
    return prefix('\n'.join(lines), budget, enc)


async def history(core, enc, snap, calibration, pool):
    directory = ROOT / f'materials/B/pool-{pool}/native'
    result_path = directory / 'result.json'
    if result_path.exists():
        result = run_context.read(result_path)
        if result['status'] != 'prepared':
            raise RuntimeError(f'Pool {pool}: previous preparation needs inspection')
        return result
    session = None
    stages = []
    last_input = 0
    window = calibration['window']
    with tempfile.TemporaryDirectory(prefix=f'context-history-{pool}-auth-') as tmp:
        auth = await credential(core, tmp)
        async with core.container(snap['prepared_image_id'], directory / 'container', agent=True) as env:
            await core.network_checks(env, directory / 'container')
            await env.checked(['python', '-c', "import pathlib,shutil; p=pathlib.Path('/app'); assert not p.is_symlink(); [(shutil.rmtree(x) if x.is_dir() and not x.is_symlink() else x.unlink()) for x in p.iterdir()]"])
            await env.checked(['git', 'init', '--quiet', '/app'])
            await live.setup_auth(core, env, auth)
            for chunk in range(1, 6):
                # Four bounded batches, then size the fifth from native usage.
                budget = 40000 if chunk < 5 else round(window * .782) - last_input - 1800
                if not 1000 <= budget <= 60000:
                    raise RuntimeError('History length estimate cannot reach target with fixed five work units')
                data = work_data(pool, chunk, budget, enc)
                filename = f'catalogue-{chunk}.csv'
                await env.write_text('/app/' + filename, data + '\n')
                prompt = ('The previous work item, if any, is complete. This is the next independent work item '
                    f'in the unrelated demonstration catalogue project, batch {chunk} of 5. '
                    f'The actual input file is /app/{filename}. The same source data is supplied below. '
                    'Use local Python standard-library tools to inspect the actual file, count complete records, '
                    'report column-count anomalies and create a small JSON summary file for this batch. '
                    'Do not print the whole input. Do not download, delegate or inspect other projects. '
                    'The last line may be an incomplete source fragment; report it separately. '
                    'Validate the summary with a second local check, then give a brief final answer stating '
                    'this work item is complete. No further work is pending after that answer.\n'
                    '<catalogue-source>\n' + data + '\n</catalogue-source>')
                print(f'Preparing genuine B history pool {pool}, work unit {chunk}/5', flush=True)
                stage, entry, _ = await live.invoke(core, env, directory / f'unit-{chunk}', prompt, auth,
                                                     session=session, continuation='resume')
                session = stage['thread_id']
                audit = stage['context_audit']
                if audit['compaction_rows']:
                    raise RuntimeError('History compacted during construction; material requires inspection')
                last_input = audit['requests'][-1]['usage']['input_tokens']
                stages.append(stage)
                core.save(directory / 'progress.json', {'completed_units': chunk, 'stages': stages})
            # Capture full untouched source session; later fork tests may add an
            # extra calibration request only in separate clean containers.
            core.save(directory / 'session.json', entry)
            result = {'status': 'prepared', 'pool_id': pool, 'session_id': session,
                      'completed_work_units': 5, 'last_input_tokens': last_input,
                      'native_session_sha256': __import__('hashlib').sha256(entry['content'].encode()).hexdigest(),
                      'stages': stages, 'usage': {k: sum(s['usage'][k] for s in stages) for k in live.native_ultra.KEYS},
                      'note': 'Controlled genuine five-turn synthetic catalogue work. Long source inputs plus actual tool work; no claims of naturally occurring production history. No old files transferred to benchmark tasks.'}
            core.save(result_path, result)
            return result


async def prepare(core):
    portability = run_context.read(ROOT / 'feasibility/native-portability/result.json')
    if portability['status'] != 'passed':
        raise RuntimeError('Native portability prerequisite not passed')
    enc = tokenizer()
    snap = snapshot()
    calibration = await text_calibration(core, enc, snap)
    # Sequential prep: never more than one model active; pilot also sequential.
    results = []
    for pool in range(1, 6):
        results.append(await history(core, enc, snap, calibration, pool))
    core.save(ROOT / 'materials/native-preparation.json', {'status': 'prepared_pending_task_start_validation',
              'A_calibration': calibration, 'B_pools': results,
              'model': 'gpt-6-sol', 'reasoning': 'medium', 'main_run_authorized': False})
