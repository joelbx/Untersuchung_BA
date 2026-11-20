#!/usr/bin/env python3
"""Fresh Sol 6 medium versus native Ultra on identical resident controlled snapshots.

prepare: reuse verified host-only controls, never download/build/infer.
models/resume: explicit subscription inference for both fresh arms.
"""
import argparse
import asyncio
from contextvars import ContextVar
import fcntl
import importlib.util
import json
from pathlib import Path
import shutil
import subprocess
import tempfile
import uuid

from control_reuse import CORE, numbers
import native_ultra

LAB = Path(__file__).resolve().parent
EXPERIMENT = 'experiment-sol6-medium-ultra'
SOURCES = {2: 'experiment-mas-sol6-medium/batch-02',
           3: 'experiment-mas-sol6-medium-300/batch-03'}
EXCLUSIONS = {127, 184, 186, 217, 218, 258, 261, 285}
ARM = ContextVar('native_comparison_arm', default='medium')


def core_module():
    spec = importlib.util.spec_from_file_location('sol_ultra_shared_core', LAB/'run.py')
    core = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(core)
    return core


def read(path):
    return json.loads(Path(path).read_text())


def present_images():
    result = subprocess.run(['docker', 'image', 'ls', '-aq', '--no-trunc'],
                            capture_output=True, text=True, check=True)
    return set(result.stdout.split())


def donor_proofs(tasks, core, images):
    master = read(LAB/'selection-extended.json')
    if core.sha(core.DATA/'swebench_pro_verified.jsonl') != master['dataset_sha256']:
        raise ValueError('Actual benchmark dataset hash differs from the frozen selection')
    sources = {}
    for name in set(SOURCES[(n-1)//100+1] for n in tasks):
        path = LAB/name/'manifest.json'
        m = read(path)
        if m['status'] != 'completed' or m['model'] != 'gpt-6-sol' or m['reasoning'] != 'medium':
            raise ValueError('Control donor is not a completed matching MAS batch: '+name)
        for file in CORE:
            if m['source_hashes'].get(file) != core.sha(LAB/file):
                raise ValueError('Donor control sources differ: '+file)
        selection = read(LAB/m['selection_file'])
        if selection['dataset_sha256'] != master['dataset_sha256']:
            raise ValueError('Donor dataset differs')
        sources[name] = (m, selection)
    cases = {}
    for n in tasks:
        name = SOURCES[(n-1)//100+1]
        m, selection = sources[name]
        case = master['scored_tasks'][n-1]
        if n not in m['tasks'] or selection['scored_tasks'][n-1] != case:
            raise ValueError(f'Task {n}: donor task identity differs')
        root = LAB/name/f'task-{n:02d}'
        control = read(root/'controls.json')
        excluded = n in m.get('control_exclusions', [])
        if excluded:
            if n not in EXCLUSIONS or control.get('passed'):
                raise ValueError(f'Task {n}: exclusion lacks the approved failed control evidence')
        elif not (control.get('passed') and control.get('original_completed') and
                  control.get('reference_resolved') and not control.get('original_resolved')):
            raise ValueError(f'Task {n}: donor controls are not valid')
        snapshot = read(root/'preparation/snapshot.json')
        if not excluded and not {snapshot['prepared_image_id'], snapshot['original_image_id']} <= images:
            raise ValueError(f'Task {n}: required snapshot/evaluation image is missing; no automatic download or rebuild')
        evidence = {str(p.relative_to(LAB)): core.sha(p) for p in
                    [LAB/name/'manifest.json', LAB/m['selection_file'], root/'controls.json',
                     root/'preparation/snapshot.json']}
        for file in ('parser.py', 'run_script.sh'):
            p = LAB/'data/swe_bench_pro_verified/run_scripts'/case['instance_id']/file
            key = str(p.relative_to(LAB))
            if not p.is_file() or m['source_hashes'].get(key) != core.sha(p):
                raise ValueError(f'Task {n}: evaluator source changed: {file}')
            evidence[key] = core.sha(p)
        cases[n] = {'case': case, 'snapshot': snapshot, 'excluded': excluded,
                    'controls': control, 'control_donor': name, 'evidence_sha256': evidence}
    return cases


def capsule(directory, core):
    policy = (LAB/'requirements.toml').read_text()
    if policy.count('multi_agent = false') != 1:
        raise ValueError('Unexpected baseline managed policy; review the Ultra policy explicitly')
    policy = policy.replace('multi_agent = false\n', '')
    root = directory/'runtime-capsule'
    root.mkdir(exist_ok=True)
    files = {'requirements.toml': policy,
             **{p: (LAB/p).read_text() for p in ('egress_proxy.py','patch_export.py')}}
    for name, content in files.items():
        p = root/name
        if p.exists() and p.read_text() != content:
            raise ValueError('Runtime capsule changed: '+name)
        if not p.exists():
            p.write_text(content)
    return root


def fingerprints(directory, core):
    files = [LAB/p for p in (*CORE, 'run_sol_ultra.py', 'native_ultra.py', 'compare_sol_ultra.py')]
    files += list((directory/'runtime-capsule').glob('*'))
    files += [core.BINARY, core.BINARY.parent/'codex-code-mode-host']
    files += [directory/'experiment.json', LAB/'selection-extended.json', core.DATA/'swebench_pro_verified.jsonl']
    return {str(p): core.sha(p) for p in files}


def prepare(root, tasks, workers, core):
    if (root/'manifest.json').exists():
        m = read(root/'manifest.json')
        if m['tasks'] != tasks:
            raise ValueError('Batch selection is frozen; use another batch')
        validate(root, core)
        print('Prepared batch retained; no controls, downloads or inference executed.')
        return
    models = read(Path.home()/'.codex/models_cache.json').get('models', [])
    if not any(m.get('slug') == 'gpt-6-sol' and any(e['effort'] == 'ultra' for e in m.get('supported_reasoning_levels', [])) for m in models):
        raise ValueError('Local account model catalog does not advertise Sol 6 Ultra')
    cases = donor_proofs(tasks, core, present_images())
    runtime = capsule(root.parent, core)
    frozen = fingerprints(root.parent, core)
    root.mkdir(exist_ok=True)
    for n, record in cases.items():
        task = root/f'task-{n:02d}'
        core.save(task/'controls.json', record['controls'])
        core.save(task/'preparation/snapshot.json', record['snapshot'])
    manifest = {'version':'sol-native-ultra-v1','status':'prepared','created_at':core.now(),
                'model':'gpt-6-sol','arms':['medium','ultra'],'tasks':tasks,
                'control_exclusions':[n for n, c in cases.items() if c['excluded']],
                'model_workers':workers,'auth_mode':'chatgpt','model_timeout_seconds':None,
                'storage_reserve_gib':25,'source_hashes':frozen,'cases':cases,
                'baseline':'fresh','runtime_capsule':str(runtime),
                'protocol':{'medium':'shared standard prompt, medium, native agents disabled',
                            'ultra':'ultra effort, native agents enabled; no custom Roles B/C coordinator',
                            'container_resources':'4 CPUs / 8 GiB total per trial, including native child threads',
                            'research':'same offline allowlist policy for every process in the container',
                            'native_agent_limits':'Codex defaults; no custom total delegation cap',
                            'context':'fresh container/CODEX_HOME for each arm; no prior model answers or patches supplied'}}
    core.save(root/'manifest.json', manifest)
    for p in frozen:
        path = Path(p)
        # Never copy credentials or user config. Only explicit versioned files/binaries.
        if path in (core.BINARY, core.BINARY.parent/'codex-code-mode-host'):
            continue
        relative = path.relative_to(LAB)
        destination = root/'source-snapshot'/relative
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(path, destination)
    core.save(root/'preparation.json', {'model_tokens':0,'controls_reexecuted':False,
                                      'images_downloaded':0,'images_built':0,
                                      'eligible_tasks':len(tasks)-len(manifest['control_exclusions'])})
    print(f"Prepared {len(tasks)-len(manifest['control_exclusions'])} paired tasks from resident controlled images; no downloads or model calls.")


def validate(root, core):
    m = read(root/'manifest.json')
    if m['model'] != 'gpt-6-sol' or m['baseline'] != 'fresh':
        raise ValueError('Unexpected comparison protocol')
    for name, digest in m['source_hashes'].items():
        if not Path(name).is_file() or core.sha(name) != digest:
            raise ValueError('Frozen source/runtime changed: '+name)
    images = present_images()
    for n, record in m['cases'].items():
        for name, digest in record['evidence_sha256'].items():
            if core.sha(LAB/name) != digest:
                raise ValueError(f'Task {n}: source control evidence changed: {name}')
        if not record['excluded'] and not {record['snapshot']['prepared_image_id'],record['snapshot']['original_image_id']} <= images:
            raise ValueError(f'Task {n}: required image missing; no implicit rebuild')
    return m


def resume(root, core):
    m = read(root/'manifest.json')
    archive = root/'technical-interruptions'/('resume-'+uuid.uuid4().hex[:12])
    pending = []
    for n in m['tasks']:
        if n in m['control_exclusions']:
            continue
        for arm in m['arms']:
            p = root/f'task-{n:02d}'/arm
            result = read(p/'result.json') if (p/'result.json').exists() else {}
            if result.get('status') in ('completed','invalid_submission','empty_submission'):
                continue
            if p.exists():
                destination = archive/f'task-{n:02d}'/arm
                destination.parent.mkdir(parents=True, exist_ok=True)
                shutil.move(str(p), str(destination))
            pending.append({'task':n,'arm':arm})
    if not pending:
        print('All trials already final; no resume or repeats needed.')
        return False
    archive.mkdir(parents=True, exist_ok=True)
    shutil.copy2(root/'manifest.json', archive/'manifest.json')
    marker=root/'STOP_AFTER_ACTIVE.json'
    if marker.exists():shutil.move(str(marker),str(archive/marker.name))
    core.save(archive/'resume.json',{'at':core.now(),'fresh_trials':pending,
                                  'reason':'Explicit resume; completed results retained regardless of score'})
    m.update(status='prepared',active_trials=[],technical_errors=[])
    core.save(root/'manifest.json',m)
    return True


async def models(root, workers, core):
    m = validate(root, core)
    if m['status'] in ('completed','paused','technical_interruption'):
        print('Batch '+m['status']+'; use explicit resume for incomplete trials.')
        return 0 if m['status']=='completed' else 2
    if workers != m['model_workers']:
        raise ValueError('Model worker count differs from preparation')
    core.HERE=root.parent
    core.SOURCE_DIR=Path(m['runtime_capsule'])
    core.RUN_MODEL='gpt-6-sol';core.RUN_REASONING='medium'
    core.PINNED_NATIVE={'binary_sha256':core.sha(core.BINARY),
                        'code_mode_host_sha256':core.sha(core.BINARY.parent/'codex-code-mode-host')}
    rows={d['instance_id']:d for d in map(json.loads,(core.DATA/'swebench_pro_verified.jsonl').read_text().splitlines())}
    original_stage=core.model_stage
    original_trial=core.trial

    async def dispatch_stage(*args,**kwargs):
        if ARM.get()=='ultra':
            return await native_ultra.stage(core,*args,**kwargs)
        return await original_stage(*args,**kwargs)

    async def dispatch_trial(instance,image,arm,directory,credential):
        token=ARM.set(arm)
        try:
            await original_trial(instance,image,'standard',directory,credential)
        finally:
            p=directory/'result.json'
            if p.exists():
                d=read(p);d.update(comparison_arm=arm,reasoning=arm,native_multi_agent=arm=='ultra')
                core.save(p,d)
            ARM.reset(token)

    core.model_stage=dispatch_stage;core.trial=dispatch_trial
    jobs=[]
    for n in m['tasks']:
        record=m['cases'][str(n)]
        if record['excluded']:continue
        case=record['case'];snap=record['snapshot']
        core.ORIGINAL_IMAGES[case['instance_id']]=snap['original_image_id']
        core.BASE_COMMITS[snap['prepared_image_id']]=case['base_commit']
        core.IMAGE_LANGUAGES[snap['prepared_image_id']]=case['repo_language']
        for arm in m['arms']:
            directory=root/f'task-{n:02d}'/arm
            result=read(directory/'result.json') if (directory/'result.json').exists() else {}
            if result.get('status') in ('completed','invalid_submission','empty_submission'):
                continue
            if result or (directory/'started.json').exists():
                raise ValueError('Prior attempt exists; use explicit resume')
            jobs.append((n,case,arm,directory,rows[case['instance_id']],snap['prepared_image_id']))
    # Resume retains results: skip them without calling them again.
    if not jobs:
        m.update(status='completed',completed_at=core.now());core.save(root/'manifest.json',m)
        return 0
    if not core.AUTH.is_file():raise ValueError('Subscription credentials missing')
    m.update(status='running',execution_started_at=core.now())
    core.save(root/'manifest.json',m)
    with tempfile.TemporaryDirectory(prefix='swe-sol-ultra-credentials-') as folder:
        secret=core.AUTH.read_bytes();core.learn_secrets(json.loads(secret))
        result=await core.parallel_trials(jobs,m,root/'manifest.json',Path(folder),secret,workers)
    if result==0:
        m.update(status='completed',completed_at=core.now());core.save(root/'manifest.json',m)
    return result


def main(argv=None):
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('phase',choices=('prepare','models','resume','stop','report','check'))
    p.add_argument('--experiment',default=EXPERIMENT)
    p.add_argument('--batch',default='batch-03')
    p.add_argument('--tasks',default='201-300')
    p.add_argument('--model-workers',type=int,default=5)
    args=p.parse_args(argv)
    import re
    if not re.fullmatch(r'experiment-[A-Za-z0-9][A-Za-z0-9_-]*',args.experiment) or not re.fullmatch(r'batch-[A-Za-z0-9][A-Za-z0-9_-]*',args.batch):p.error('Use local experiment-* and batch-* names')
    tasks=numbers(args.tasks,300)
    if any(n<101 for n in tasks):p.error('Resident comparison pool is tasks 101–300')
    if args.model_workers<1:p.error('Workers must be positive')
    directory=LAB/args.experiment;root=directory/args.batch
    if directory.is_symlink() or root.is_symlink():p.error('Symlink output directories are not allowed')
    if args.phase=='report':
        from compare_sol_ultra import write
        print(write(root));return 0
    if args.phase=='stop':
        from stop_run import request_stop
        print(request_stop(args.experiment,args.batch));return 0
    core=core_module()
    directory.mkdir(exist_ok=True)
    with (directory/'.runner.lock').open('a') as lock:
        fcntl.flock(lock,fcntl.LOCK_EX|fcntl.LOCK_NB)
        if args.phase=='prepare':
            config={'model':'gpt-6-sol','reasoning':'medium versus native ultra',
                    'protocol':'sol-native-ultra-v1','storage_reserve_gib':25}
            f=directory/'experiment.json'
            if f.exists() and read(f)!=config:raise ValueError('Experiment configuration differs')
            if not f.exists():core.save(f,config)
            prepare(root,tasks,args.model_workers,core);return 0
        m=validate(root,core)
        if m['tasks']!=tasks:raise ValueError('Task selection differs from prepared batch')
        if m['model_workers']!=args.model_workers:raise ValueError('Worker count differs from prepared batch; no state changed')
        if args.phase=='check':print('Frozen sources, donor controls and resident images verified.');return 0
        if args.phase=='resume' and not resume(root,core):return 0
        return asyncio.run(models(root,args.model_workers,core))


if __name__=='__main__':
    raise SystemExit(main())
