#!/usr/bin/env python3
"""Four fresh Sol 6/medium arms. No phase starts models except models/resume."""
import argparse
import asyncio
from contextlib import asynccontextmanager
from contextvars import ContextVar
import fcntl
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import random
import re
import shutil
import subprocess
import sys
import tempfile
import uuid

from control_reuse import CORE, import_controls, numbers

LAB = Path(__file__).resolve().parent
EXPERIMENT = 'experiment-skills-sol6-medium'
ARMS = ('standard', 'tdd', 'debugging', 'verification')
SKILLS = {'tdd': 'test-driven-development', 'debugging': 'systematic-debugging',
          'verification': 'verification-before-completion'}
EXCLUSIONS = {40, 65, 127, 184, 186, 217, 218, 258, 261, 285}
SEED = 20261026
FINAL = {'completed', 'invalid_submission', 'empty_submission'}
ARM = ContextVar('skill_arm', default='standard')
COMMON = ("\nAutonomous benchmark: no human is available. Resolve uncertainty from local evidence; "
          "do not ask questions or load additional skills. You may create local tests. "
          "If offline tooling prevents a check, record the exact command, error and uncertainty in "
          ".codex-role-output/checkpoint.md; continue with the best supported patch. "
          "Never claim an unexecuted or failing check passed. Do not download dependencies.\n")


def read(path):
    return json.loads(Path(path).read_text())


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def core_module():
    # Set before importing LiteLLM indirectly; no remote model-price fetch.
    os.environ['LITELLM_LOCAL_MODEL_COST_MAP'] = 'True'
    spec = importlib.util.spec_from_file_location('skills_shared_core', LAB / 'run.py')
    core = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(core)
    return core


def schedule(tasks):
    """Independent task seeds keep each task's order invariant across blocks."""
    jobs = []
    for n in sorted(tasks):
        arms = list(ARMS)
        random.Random(f'skills-v1:{SEED}:{n}').shuffle(arms)
        jobs.extend({'task': n, 'arm': arm} for arm in arms if n not in EXCLUSIONS)
    return jobs


def skill_provenance():
    root = LAB / 'skills-study'
    p = read(root / 'provenance.json')
    for group, folder in (('originals', 'upstream'), ('adapted', 'adapted')):
        for name, expected in p[group].items():
            if digest(root / folder / name) != expected:
                raise ValueError('Frozen skill changed: ' + name)
    return p


def configuration():
    return {'protocol': 'skills-v1', 'model': 'gpt-6-sol', 'reasoning': 'medium',
            'arms': list(ARMS), 'baseline': 'fresh', 'seed': SEED,
            'approved_control_exclusions': sorted(EXCLUSIONS), 'storage_reserve_gib': 25,
            'model_timeout_seconds': None, 'evaluation_timeout_seconds': 3600,
            'skill_commit': skill_provenance()['commit'], 'max_model_workers': 5,
            'loading': 'full adapted SKILL.md in developer instructions; supporting files only for assigned arm'}


def ensure_experiment(directory, core):
    config = configuration()
    path = directory / 'experiment.json'
    if path.exists() and read(path) != config:
        raise ValueError('Experiment configuration changed; use a fresh directory')
    directory.mkdir(exist_ok=True)
    if not path.exists():
        core.save(path, config)


def controls(args):
    """Use unchanged run.py: compatible controls imported, missing ones validated."""
    experiment = args.experiment + '-controls'
    root = LAB / experiment / args.batch
    if (LAB / args.experiment / args.batch / 'manifest.json').exists():
        raise ValueError('Study batch already frozen; controls cannot be changed underneath it')
    if root.resolve() != root.absolute():
        raise ValueError('Symlink control batches forbidden')
    config = {'protocol': 'skills-controls-v1', 'storage_reserve_gib': 25,
              'model': 'gpt-6-sol', 'reasoning': 'medium'}
    control_directory = root.parent
    control_directory.mkdir(exist_ok=True)
    path = control_directory / 'experiment.json'
    if path.exists() and read(path) != config:
        raise ValueError('Control configuration differs')
    if not path.exists():
        path.write_text(json.dumps(config, indent=2) + '\n')
    import_controls(LAB, experiment, args.batch, args.tasks)
    excluded = []
    for n in numbers(args.tasks, 300):
        p = root / f'task-{n:02d}' / 'controls.json'
        if n in EXCLUSIONS and p.exists() and not read(p).get('passed'):
            excluded.append(n)
    argv = [sys.executable, str(LAB / 'run.py'), '--experiment', experiment,
            '--batch', args.batch, '--tasks', args.tasks, '--selection', 'selection-extended.json',
            '--model', 'gpt-6-sol', '--reasoning', 'medium', '--setup', 'standard',
            '--parallel-controls', '--control-workers', str(args.control_workers)]
    if excluded:
        argv += ['--exclude-invalid-controls', ','.join(map(str, excluded))]
    if args.repair_controls:
        argv.append('--repair-controls')
    # No --run, no auth/model stage. New failed controls are not auto-excluded.
    print('Shared controls only; model tokens 0. Donor: ' + str(root), flush=True)
    return subprocess.run(argv, cwd=LAB, env={**os.environ, 'LITELLM_LOCAL_MODEL_COST_MAP': 'True'}).returncode


def present_images():
    p = subprocess.run(['docker', 'image', 'ls', '-aq', '--no-trunc'],
                       capture_output=True, text=True, check=True)
    return set(p.stdout.split())


def proof_cases(tasks, donor, core, images):
    master = read(LAB / 'selection-extended.json')
    if digest(core.DATA / 'swebench_pro_verified.jsonl') != master['dataset_sha256']:
        raise ValueError('Benchmark dataset changed')
    m = read(donor / 'manifest.json')
    if m['status'] not in ('controls_passed', 'completed'):
        raise ValueError('Control donor not validated; run controls (or controls --repair-controls) first')
    for name in CORE:
        if m['source_hashes'].get(name) != digest(LAB / name):
            raise ValueError('Control source mismatch: ' + name)
    selection = read(LAB / m['selection_file'])
    if selection['dataset_sha256'] != master['dataset_sha256']:
        raise ValueError('Control donor dataset mismatch')
    cases = {}
    for n in tasks:
        case = master['scored_tasks'][n - 1]
        if n not in m['tasks'] or selection['scored_tasks'][n - 1] != case:
            raise ValueError(f'Task {n}: control task identity mismatch')
        task = donor / f'task-{n:02d}'
        control = read(task / 'controls.json')
        excluded = n in EXCLUSIONS
        if excluded:
            if control.get('passed') or n not in m.get('control_exclusions', []):
                raise ValueError(f'Task {n}: approved exclusion needs recorded failed control and explicit donor exclusion')
        elif not (control.get('passed') and control.get('original_completed') and
                  control.get('reference_resolved') and not control.get('original_resolved')):
            raise ValueError(f'Task {n}: controls invalid; no new automatic exclusion')
        snapshot_path = task / 'preparation/snapshot.json'
        snapshot = read(snapshot_path)
        if not excluded and not {snapshot['prepared_image_id'], snapshot['original_image_id']} <= images:
            raise ValueError(f'Task {n}: required Docker image missing; restore/revalidate controls explicitly')
        files = [donor / 'manifest.json', LAB / m['selection_file'], task / 'controls.json', snapshot_path]
        for name in ('parser.py', 'run_script.sh'):
            p = core.DATA / 'run_scripts' / case['instance_id'] / name
            if m['source_hashes'].get(str(p.relative_to(LAB))) != digest(p):
                raise ValueError(f'Task {n}: evaluator source mismatch')
            files.append(p)
        # Keep no reference patch, model answer or official test content in agent inputs.
        cases[str(n)] = {'case': case, 'snapshot': snapshot, 'excluded': excluded,
                         'control_donor': str(donor.relative_to(LAB)),
                         'evidence_sha256': {str(p.relative_to(LAB)): digest(p) for p in files}}
    return cases


def fingerprint_files(core):
    files = [LAB / p for p in CORE]
    files += [LAB / n for n in ('run_skills.py', 'compare_skills.py', 'skill_trace.py',
                                'control_reuse.py', 'selection-extended.json',
                                'run_skills_batch.sh', 'SKILLS-STUDY.md')]
    files += [p for p in (LAB / 'skills-study').rglob('*') if p.is_file()]
    files += [core.BINARY, core.BINARY.parent / 'codex-code-mode-host', core.DATA / 'swebench_pro_verified.jsonl']
    return files


def prepare(root, tasks, workers, donor, core):
    if (root / 'manifest.json').exists():
        m = validate(root, core)
        if m['tasks'] != tasks or m['model_workers'] != workers:
            raise ValueError('Task selection/worker count is frozen')
        print('Existing prepared batch verified; no controls or models executed.')
        return
    cases = proof_cases(tasks, donor, core, present_images())
    ensure_experiment(root.parent, core)
    files = fingerprint_files(core) + [root.parent / 'experiment.json']
    hashes = {str(p): digest(p) for p in files}
    m = {**configuration(), 'version': 'skills-v1', 'status': 'prepared', 'created_at': core.now(),
         'tasks': tasks, 'model_workers': workers, 'cases': cases,
         'control_exclusions': sorted(set(tasks) & EXCLUSIONS), 'source_hashes': hashes,
         'schedule': schedule(tasks), 'auth_mode': 'chatgpt',
         'network_policy': core.ALLOWLIST, 'container_limits': {'cpus': 4, 'memory_mib': 8192}}
    root.mkdir(exist_ok=True)
    for p in files:
        if p in (core.BINARY, core.BINARY.parent / 'codex-code-mode-host'):
            continue
        dest = root / 'source-snapshot' / p.relative_to(LAB)
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(p, dest)
    for n, case in cases.items():
        donor_task = LAB / case['control_donor'] / f'task-{int(n):02d}'
        for name in ('controls.json', 'preparation/snapshot.json'):
            dest = root / f'task-{int(n):02d}' / name
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(donor_task / name, dest)
        if case['excluded']:
            for arm in ARMS:
                core.save(root / f'task-{int(n):02d}' / arm / 'result.json',
                          {'status': 'control_excluded', 'resolved': None, 'stages': [], 'arm': arm})
    core.save(root / 'manifest.json', m)
    print(f"Prepared {len(m['schedule'])} fresh trials; no model calls, downloads or image builds.")


def validate(root, core):
    m = read(root / 'manifest.json')
    if m['version'] != 'skills-v1' or any(m.get(k) != v for k, v in configuration().items()):
        raise ValueError('Study protocol mismatch')
    if m['schedule'] != schedule(m['tasks']):
        raise ValueError('Frozen schedule changed')
    for name, expected in m['source_hashes'].items():
        if not Path(name).is_file() or digest(name) != expected:
            raise ValueError('Frozen source/runtime changed: ' + name)
    images = present_images()
    for n, case in m['cases'].items():
        for name, expected in case['evidence_sha256'].items():
            if digest(LAB / name) != expected:
                raise ValueError('Control evidence changed: ' + name)
        for name in ('controls.json', 'preparation/snapshot.json'):
            if digest(root / f'task-{int(n):02d}' / name) != digest(LAB / case['control_donor'] / f'task-{int(n):02d}' / name):
                raise ValueError('Copied control evidence changed')
        if case['snapshot'] != read(root / f'task-{int(n):02d}' / 'preparation/snapshot.json'):
            raise ValueError('Manifest snapshot differs from controlled snapshot')
        if not case['excluded'] and not {case['snapshot']['prepared_image_id'], case['snapshot']['original_image_id']} <= images:
            raise ValueError(f'Task {n}: required image missing; no implicit rebuild')
    return m


def incomplete_trials(root, m):
    pending = []
    for job in m['schedule']:
        p = root / f"task-{job['task']:02d}" / job['arm']
        r = read(p / 'result.json') if (p / 'result.json').exists() else {}
        if r.get('status') in FINAL:
            continue
        # An interrupted evaluator can be rerun without giving the model another attempt.
        if r.get('status') == 'evaluation_problem':
            pending.append({**job, 'retry': 'evaluation_only'})
        elif (p / 'standard/stage.json').exists() and read(p / 'standard/stage.json').get('usage_complete'):
            if (p / 'submission.patch').exists():
                pending.append({**job, 'retry': 'evaluation_only'})
            else:
                raise ValueError(f"{p}: completed model stage without exported submission; inspect before retrying")
        else:
            pending.append({**job, 'retry': 'fresh_model'})
    return pending


def resume(root, core):
    m = read(root / 'manifest.json')
    pending = incomplete_trials(root, m)  # Entire plan validated before any move.
    if not pending:
        m.update(status='completed', completed_at=core.now());core.save(root / 'manifest.json', m)
        print('All trials final; no repeat needed.')
        return False
    archive = root / 'technical-interruptions' / ('resume-' + uuid.uuid4().hex[:12])
    archive.mkdir(parents=True)
    shutil.copy2(root / 'manifest.json', archive / 'manifest.json')
    for job in pending:
        p = root / f"task-{job['task']:02d}" / job['arm']
        if not p.exists():
            continue
        destination = archive / p.relative_to(root)
        destination.parent.mkdir(parents=True, exist_ok=True)
        if job['retry'] == 'evaluation_only':
            destination.mkdir()
            if (p / 'result.json').exists():
                shutil.copy2(p / 'result.json', destination / 'result.json')
            else:
                stage = read(p / 'standard/stage.json')
                core.save(p / 'result.json', {'status': 'evaluation_problem', 'setup': 'standard',
                          'arm': job['arm'], 'model': 'gpt-6-sol', 'reasoning': 'medium',
                          'auth_mode': 'chatgpt', 'resolved': None, 'stages': [stage],
                          'elapsed_codex_seconds': stage['elapsed_seconds'],
                          'note': 'Recovered completed model stage and preserved submission; no new model call'})
            if (p / 'evaluation').exists():
                shutil.move(str(p / 'evaluation'), str(destination / 'evaluation'))
            for name in ('technical-interruption.json', 'started.json'):
                if (p / name).exists():
                    shutil.move(str(p / name), str(destination / name))
            core.save(p / 'evaluation-retry.json', {'at': core.now(), 'model_rerun': False})
        else:
            shutil.move(str(p), str(destination))
    marker = root / 'STOP_AFTER_ACTIVE.json'
    if marker.exists():
        shutil.move(str(marker), str(archive / marker.name))
    core.save(archive / 'resume.json', {'at': core.now(), 'pending': pending,
              'reason': 'Explicit resume; final results retained independently of score'})
    m.update(status='prepared', active_trials=[], technical_errors=[])
    core.save(root / 'manifest.json', m)
    return True


def install_skill_hooks(core):
    original_container = core.container
    original_stage = core.model_stage
    provenance = skill_provenance()

    @asynccontextmanager
    async def assigned_container(image, directory, *, agent=False):
        async with original_container(image, directory, agent=agent) as env:
            arm = ARM.get()
            if agent and arm in SKILLS:
                skill = SKILLS[arm]
                for name in provenance['runtime_files'][skill]:
                    path = '/opt/experiment-skill/' + name
                    await env.write_text(path, (LAB / 'skills-study/adapted' / skill / name).read_text())
                    if name.endswith('.sh'):
                        await env.checked(['chmod', 'a+x', path])
                await env.checked(['chmod', '-R', 'a-w', '/opt/experiment-skill'])
            yield env

    async def assigned_stage(image, role, prompt, patch, directory, credential, **kwargs):
        arm = ARM.get()
        developer = core.role_instructions(role).replace(
            'Use local repository code and existing tests only.',
            'Use local repository code, documentation and tests; you may add local tests.') + COMMON
        load = {'arm': arm, 'loaded_into_developer_context': False, 'additional_model_calls': 0}
        if arm in SKILLS:
            skill = SKILLS[arm]
            body = (LAB / 'skills-study/adapted' / skill / 'SKILL.md').read_text()
            developer += ('\nApply the following assigned skill throughout this task. Its full instructions '
                          'are loaded below before your first action. Supporting files are in '
                          '/opt/experiment-skill; resolve relative references there. Do not load other skills.\n'
                          '<assigned_skill>\n' + body + '\n</assigned_skill>\n')
            load.update(loaded_into_developer_context=True, skill=skill, commit=provenance['commit'],
                        sha256=digest(LAB / 'skills-study/adapted' / skill / 'SKILL.md'),
                        mechanism='complete developer-instruction injection, not automatic skill discovery')
        core.save(Path(directory) / 'skill-loading.json', load)
        try:
            return await original_stage(image, role, prompt, patch, directory, credential,
                                        developer_override=developer, **kwargs)
        finally:
            from skill_trace import audit
            core.save(Path(directory) / 'skill-observations.json', audit(Path(directory)))

    core.container = assigned_container
    core.model_stage = assigned_stage


async def models(root, core):
    m = validate(root, core)
    if m['status'] in ('completed', 'paused', 'technical_interruption'):
        print('Batch ' + m['status'] + '; use resume for incomplete trials.')
        return 0 if m['status'] == 'completed' else 2
    core.HERE = root.parent
    core.RUN_MODEL = 'gpt-6-sol';core.RUN_REASONING = 'medium'
    core.PINNED_NATIVE = {'binary_sha256': digest(core.BINARY),
                          'code_mode_host_sha256': digest(core.BINARY.parent / 'codex-code-mode-host')}
    install_skill_hooks(core)
    original_trial = core.trial

    async def assigned_trial(instance, image, arm, directory, credential):
        token = ARM.set(arm)
        try:
            if (directory / 'evaluation-retry.json').exists():
                result = read(directory / 'result.json')
                patch = (directory / 'submission.patch').read_text()
                applicable = await core.valid_patch(image, patch, directory / 'retry-patch-check')
                if not applicable:
                    result.update(status='invalid_submission', resolved=False)
                elif not patch.strip():
                    result.update(status='empty_submission', resolved=False)
                else:
                    evaluation = await core.evaluate(instance, core.ORIGINAL_IMAGES[instance['instance_id']],
                                                     patch, directory / 'evaluation')
                    result.update(status='completed' if evaluation.get('completed') and not evaluation.get('error')
                                  else 'evaluation_problem', resolved=evaluation.get('resolved', False))
                core.save(directory / 'result.json', result)
                if result['status'] in FINAL:
                    (directory / 'evaluation-retry.json').unlink()
            else:
                await original_trial(instance, image, 'standard', directory, credential)
        finally:
            p = directory / 'result.json'
            if p.exists():
                r = read(p);r.update(arm=arm, model='gpt-6-sol', reasoning='medium')
                if (directory / 'submission.patch').exists():
                    r['submission_sha256'] = digest(directory / 'submission.patch')
                core.save(p, r)
            ARM.reset(token)

    core.trial = assigned_trial
    wanted = {c['case']['instance_id'] for c in m['cases'].values() if not c['excluded']}
    instances = {r['instance_id']: r for r in map(json.loads, (core.DATA / 'swebench_pro_verified.jsonl').read_text().splitlines())
                 if r['instance_id'] in wanted}
    if set(instances) != wanted:
        raise ValueError('Dataset instances missing')
    jobs = []
    for job in m['schedule']:
        n, arm = job['task'], job['arm']
        record = m['cases'][str(n)];case = record['case'];snap = record['snapshot']
        core.ORIGINAL_IMAGES[case['instance_id']] = snap['original_image_id']
        core.BASE_COMMITS[snap['prepared_image_id']] = case['base_commit']
        core.IMAGE_LANGUAGES[snap['prepared_image_id']] = case['repo_language']
        directory = root / f'task-{n:02d}' / arm
        result = read(directory / 'result.json') if (directory / 'result.json').exists() else {}
        if result.get('status') in FINAL:
            continue
        if ((directory / 'started.json').exists() or result) and not (directory / 'evaluation-retry.json').exists():
            raise ValueError('Prior attempt exists; use explicit resume: ' + str(directory))
        jobs.append((n, case, arm, directory, instances[case['instance_id']], snap['prepared_image_id']))
    if not jobs:
        m.update(status='completed', completed_at=core.now());core.save(root / 'manifest.json', m)
        return 0
    if not core.AUTH.is_file():
        raise ValueError('Subscription login missing')
    m.update(status='running', execution_started_at=m.get('execution_started_at', core.now()))
    core.save(root / 'manifest.json', m)
    try:
        with tempfile.TemporaryDirectory(prefix='swe-skills-credentials-') as private:
            secret = core.AUTH.read_bytes();core.learn_secrets(json.loads(secret))
            result = await core.parallel_trials(jobs, m, root / 'manifest.json', Path(private), secret, m['model_workers'])
    except BaseException:
        m.update(status='technical_interruption', interrupted_at=core.now())
        core.save(root / 'manifest.json', m)
        raise
    if result == 0:
        m.update(status='completed', completed_at=core.now());core.save(root / 'manifest.json', m)
    return result


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('phase', choices=('controls', 'prepare', 'models', 'resume', 'check', 'stop', 'report'))
    p.add_argument('--experiment', default=EXPERIMENT)
    p.add_argument('--batch', default='batch-01')
    p.add_argument('--tasks', default='1-100')
    p.add_argument('--model-workers', type=int, default=5)
    p.add_argument('--control-workers', type=int, default=2)
    p.add_argument('--repair-controls', action='store_true')
    args = p.parse_args(argv)
    if not re.fullmatch(r'experiment-[A-Za-z0-9][A-Za-z0-9_-]*', args.experiment) or not re.fullmatch(r'batch-[A-Za-z0-9][A-Za-z0-9_-]*', args.batch):
        p.error('Use local experiment-* and batch-* names')
    tasks = numbers(args.tasks, 300)
    if not 1 <= args.model_workers <= 5 or args.control_workers < 1:
        p.error('Model workers must be 1–5; control workers must be positive')
    if args.repair_controls and args.phase != 'controls':
        p.error('--repair-controls only applies to controls')
    directory = LAB / args.experiment;root = directory / args.batch
    if any(x.resolve() != x.absolute() for x in (directory, root, LAB / (args.experiment + '-controls'))):
        p.error('Symlink output directories forbidden')
    if args.phase == 'report':
        from compare_skills import write
        print(write(directory));return 0
    if args.phase == 'stop':
        from stop_run import request_stop
        print(request_stop(args.experiment, args.batch));return 0
    directory.mkdir(exist_ok=True)
    with (directory / '.skills.lock').open('a') as lock:
        fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        if args.phase == 'controls':
            return controls(args)
        core = core_module()
        ensure_experiment(directory, core)
        if args.phase == 'prepare':
            prepare(root, tasks, args.model_workers, LAB / (args.experiment + '-controls') / args.batch, core)
            return 0
        m = validate(root, core)
        if m['tasks'] != tasks or m['model_workers'] != args.model_workers:
            raise ValueError('Task selection/worker count differs from preparation')
        if args.phase == 'check':
            print('Frozen protocol, skill files, controls and resident images verified.');return 0
        if args.phase == 'resume' and not resume(root, core):
            return 0
        return asyncio.run(models(root, core))


if __name__ == '__main__':
    raise SystemExit(main())
