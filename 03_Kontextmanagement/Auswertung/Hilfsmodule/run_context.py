#!/usr/bin/env python3
"""Offline preparation and preflight for the approved three-arm context pilot.

No inference on import or in any currently implemented phase. Main-run execution
is deliberately unavailable pending live feasibility, pilot and separate approval.
"""
import argparse
from datetime import datetime, timezone
import hashlib
import itertools
import json
from pathlib import Path
import subprocess

from control_reuse import CORE
from context_telemetry import ARMS, analyze, parse_rows

LAB = Path(__file__).resolve().parent
ROOT = LAB / 'experiment-context-sol6-medium'
DONORS = {1: 'experiment-mas-sol6-medium-restore-100/batch-01',
          2: 'experiment-mas-sol6-medium/batch-02',
          3: 'experiment-mas-sol6-medium-300/batch-03'}
EXCLUSIONS = {40, 65, 127, 184, 186, 217, 218, 258, 261, 285}
ORDERS = list(itertools.permutations(ARMS))
SEED = 'context-sol6-medium-v1'


def read(path):
    return json.loads(Path(path).read_text())


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def save(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    temp = path.with_suffix(path.suffix + '.tmp')
    temp.write_text(json.dumps(data, indent=2, ensure_ascii=False) + '\n')
    temp.replace(path)


def frozen_write(path, content):
    if path.exists():
        if path.read_text() != content:
            raise ValueError('Refusing to overwrite frozen preparation: ' + str(path))
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content)


def metadata_plan(lab=LAB):
    """Validate donor evidence without claiming any image is actually present."""
    master = read(lab / 'selection-mas-300.json')
    dataset = lab / 'data/swe_bench_pro_verified/swebench_pro_verified.jsonl'
    if sha(dataset) != master['dataset_sha256']:
        raise ValueError('Dataset differs from selection')
    rows, evidence = [], {}
    eligible_index = 0
    for n, case in enumerate(master['scored_tasks'], 1):
        donor = lab / DONORS[(n - 1) // 100 + 1]
        manifest = read(donor / 'manifest.json')
        if manifest['status'] not in ('controls_passed', 'completed'):
            raise ValueError('Donor controls incomplete')
        if manifest['model'] != 'gpt-6-sol' or manifest['reasoning'] != 'medium':
            raise ValueError('Donor model/effort differs')
        for file in CORE:
            if manifest['source_hashes'].get(file) != sha(lab / file):
                raise ValueError('Donor control source mismatch: ' + file)
        selection = read(lab / manifest['selection_file'])
        if selection['dataset_sha256'] != master['dataset_sha256'] or selection['scored_tasks'][n - 1] != case or n not in manifest['tasks']:
            raise ValueError(f'Task {n}: donor identity mismatch')
        directory = donor / f'task-{n:02d}'
        controls = read(directory / 'controls.json')
        snapshot = read(directory / 'preparation/snapshot.json')
        excluded = n in manifest.get('control_exclusions', [])
        if excluded != (n in EXCLUSIONS) or (excluded and controls.get('passed')):
            raise ValueError(f'Task {n}: exclusion evidence differs')
        if not excluded and not (controls.get('passed') and controls.get('original_completed')
                                 and controls.get('reference_resolved') and not controls.get('original_resolved')):
            raise ValueError(f'Task {n}: controls not valid')
        files = [donor / 'manifest.json', lab / manifest['selection_file'],
                 directory / 'controls.json', directory / 'preparation/snapshot.json']
        for name in ('parser.py', 'run_script.sh'):
            path = lab / 'data/swe_bench_pro_verified/run_scripts' / case['instance_id'] / name
            if manifest['source_hashes'].get(str(path.relative_to(lab))) != sha(path):
                raise ValueError(f'Task {n}: evaluator differs')
            files.append(path)
        for p in files:
            evidence[str(p.relative_to(lab))] = sha(p)
        rows.append({'task': n, 'language': case['repo_language'], 'instance_id': case['instance_id'],
                     'control_donor': str(donor.relative_to(lab)), 'excluded': excluded,
                     'snapshot': snapshot, 'pool_id': eligible_index % 5 + 1 if not excluded else None,
                     'arm_order': list(ORDERS[eligible_index % 6]) if not excluded else []})
        if not excluded:
            eligible_index += 1
    return {'protocol': SEED, 'model': 'gpt-6-sol', 'reasoning': 'medium', 'setup': 'standard',
            'arms': list(ARMS), 'tasks': rows, 'eligible_tasks': eligible_index,
            'planned_main_trials': eligible_index * 3, 'max_workers_total': 5,
            'pilot_workers': 1, 'target_band': [0.78, 0.82],
            'model_timeout_seconds': None, 'evaluation_timeout_seconds': 3600,
            'cpus_per_container': 4, 'memory_mib_per_container': 8192,
            'storage_reserve_gib': 25, 'automatic_retries': False,
            'main_run_authorized': False, 'live_pilot_completed': False,
            'image_presence': 'unknown_until_docker_preflight',
            'evidence_sha256': evidence,
            'frozen_sources': {p: sha(lab / p) for p in (*CORE, 'run_context.py', 'context_telemetry.py', 'compare_context.py')},
            'selection_sha256': sha(lab / 'selection-mas-300.json'),
            'limitations': ['A/B differ in both content and conversation structure',
                            'Request input load is not a proven UI/live-context percentage',
                            'B native history portability is a live pilot prerequisite']}


def validate(root, lab=LAB):
    plan = read(root / 'plan.json')
    current = metadata_plan(lab)
    if plan != current:
        raise ValueError('Frozen plan/source/donor evidence changed; review instead of silently updating')
    materials = root / 'materials/manifest.json'
    if materials.exists():
        for name, digest in read(materials)['sha256'].items():
            p = root / 'materials' / name
            if p.is_symlink() or sha(p) != digest:
                raise ValueError('Material changed: ' + name)
    return plan


TOPICS = [
    ('Licht und Schatten', 'Ein Schatten entsteht, wenn ein undurchsichtiger Gegenstand einen Teil des einfallenden Lichts verdeckt. Die Lage der Lichtquelle beeinflusst die Richtung des Schattens. Bei einer ausgedehnten Lichtquelle können Übergänge zwischen hellen und dunklen Bereichen entstehen.'),
    ('Wasser und Landschaft', 'Wasser kann in fester, flüssiger und gasförmiger Form vorkommen. Niederschlag gelangt auf unterschiedliche Weise in Böden und Gewässer. Die Form eines Flussbettes hängt unter anderem von Gefälle, Untergrund und Wasserführung ab.'),
    ('Pflanzen und Jahreszeiten', 'Pflanzen nutzen Licht bei der Photosynthese. Wachstum und Blüte hängen unter anderem von Art, Temperatur und Wasserangebot ab. Blätter unterscheiden sich in Form, Größe und Anordnung. Saisonale Veränderungen verlaufen je nach Standort unterschiedlich.'),
    ('Klang und Raum', 'Schall breitet sich als mechanische Welle in einem Medium aus. Die wahrgenommene Tonhöhe hängt mit der Frequenz zusammen. Reflexionen an Oberflächen beeinflussen den Klang eines Raumes. Material und Form der Oberflächen wirken auf diese Reflexionen ein.'),
    ('Gestein und Oberfläche', 'Gesteine bestehen aus Mineralen oder anderen geologischen Bestandteilen. Verwitterung verändert Oberflächen durch physikalische und chemische Vorgänge. Die Eigenschaften eines Gesteins hängen unter anderem von seiner Zusammensetzung und Entstehung ab.')]


def materials(root):
    """Create inspectable candidates, never assert calibrated/frozen native history."""
    hashes = {}
    for pool, (title, source) in enumerate(TOPICS, 1):
        name = f'A/pool-{pool}/reservoir.txt'
        paragraphs = []
        for i in range(1, 4201):
            # Explicitly synthetic descriptive register, not an imported experiment result.
            value = (i * 37 + pool * 11) % 997
            paragraphs.append(f'{title}. Abschnitt {i}. {source} '
                              f'Ein synthetischer Katalogeintrag trägt die Nummer {pool}-{i}; '
                              f'seine beschreibenden Größen betragen {value} und {value + pool}.')
        p = root / 'materials' / name
        frozen_write(p, '\n\n'.join(paragraphs) + '\n')
        hashes[name] = sha(p)
        prompt_name = f'B/pool-{pool}/preparation-request.txt'
        prompt = (f'Work only on the separate, non-benchmark demonstration project in /app. '
                  f'Create and validate a small descriptive catalogue about {title}. '
                  'Use only locally available standard-library tools and authored synthetic records. '
                  'Inspect files and actual tool outputs; complete each requested unit of work before replying. '
                  'Do not access any benchmark, external service, credentials or other projects. '
                  'Describe the finished work and explicitly state that this work item is complete.\n')
        p = root / 'materials' / prompt_name
        frozen_write(p, prompt)
        hashes[prompt_name] = sha(p)
    manifest = {'status': 'candidates_only_not_calibrated', 'pool_size_per_arm': 5,
                'A': 'Authored factual paragraphs and explicitly synthetic catalogue entries; repetitive reservoir. Exact 80% slices await calibration. Repetition is a content limitation.',
                'B': 'Preparation requests only. No native work histories have been generated yet. Never substitute these prompts or a pasted transcript for real history.',
                'freeze_gate': 'Live feasibility and measured calibration before pilot/main; never select materials by benchmark solution outcomes',
                'sha256': hashes}
    frozen_write(root / 'materials/manifest.json', json.dumps(manifest, indent=2, ensure_ascii=False) + '\n')
    return manifest


def command(argv):
    try:
        p = subprocess.run(argv, text=True, capture_output=True, timeout=30)
        return {'ok': p.returncode == 0, 'exit_code': p.returncode,
                'stdout': p.stdout, 'stderr': p.stderr[:3000]}
    except (OSError, subprocess.TimeoutExpired) as exc:
        return {'ok': False, 'error': str(exc)}


def inventory(plan, ids):
    rows = []
    for row in plan['tasks']:
        item = {k: row[k] for k in ('task', 'excluded', 'language', 'pool_id', 'arm_order')}
        required = {row['snapshot']['prepared_image_id'], row['snapshot']['original_image_id']}
        item['images_present'] = None if ids is None else required <= ids
        rows.append(item)
    # Presence is the primary priority; preferred block order only breaks ties.
    priority = {3: 0, 2: 1, 1: 2}
    eligible = [r for r in rows if not r['excluded']]
    eligible.sort(key=lambda r: (not bool(r['images_present']), priority[(r['task'] - 1) // 100 + 1], r['task']))
    pilot = []
    if ids is not None:
        available = [r for r in eligible if r['images_present']]
        for language in sorted({r['language'] for r in available}):
            pilot.append(next(r['task'] for r in available if r['language'] == language))
        for row in available:
            if len(pilot) >= 5:
                break
            if row['task'] not in pilot:
                pilot.append(row['task'])
    return {'tasks': rows, 'provisional_task_order': [r['task'] for r in eligible],
            'pilot_candidate_tasks': pilot, 'pilot_selection_complete': len(pilot) == 5 and
            {r['language'] for r in eligible if r['task'] in pilot} == {'go', 'python', 'js', 'ts'}}


def preflight(root):
    plan = validate(root)
    docker = command(['docker', 'image', 'ls', '-aq', '--no-trunc'])
    ids = set(docker['stdout'].split()) if docker['ok'] else None
    report = {'at': datetime.now(timezone.utc).isoformat(), 'docker': docker,
              'cli_version': command(['codex', '--version']),
              'fork_help': command(['codex', 'exec', 'fork', '--help']),
              'resume_help': command(['codex', 'exec', 'resume', '--help']),
              'inventory': inventory(plan, ids), 'model_calls': 0,
              'pilot_started': False, 'main_run_authorized': False,
              'blockers': ([] if docker['ok'] else ['Docker service unavailable; resident images unknown']) +
              ['Native history portability and first-request measurement need live verification',
               'Five real B histories not generated; A/B start loads not calibrated']}
    stamp = datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%fZ')
    save(root / 'preflight' / (stamp + '.json'), report)
    save(root / 'status.json', {'status': 'blocked_before_live_feasibility',
                              'blockers': report['blockers'], 'model_calls': 0,
                              'pilot_started': False, 'main_run_authorized': False})
    return report


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__)
    sub = p.add_subparsers(dest='phase', required=True)
    for phase in ('prepare', 'preflight', 'check', 'pilot', 'models'):
        sub.add_parser(phase)
    a = sub.add_parser('analyze')
    a.add_argument('rollout', type=Path)
    a.add_argument('--turn-id', required=True)
    a.add_argument('--start-row', required=True, type=int)
    a.add_argument('--arm', choices=ARMS, required=True)
    args = p.parse_args(argv)
    if args.phase == 'analyze':
        print(json.dumps(analyze(parse_rows(args.rollout.read_text()), benchmark_turn_id=args.turn_id,
                                 start_row=args.start_row, arm=args.arm), indent=2))
        return 0
    if args.phase == 'models':
        p.error('Main run is not authorized. No model was started.')
    if args.phase == 'prepare':
        plan = metadata_plan()
        frozen_write(ROOT / 'plan.json', json.dumps(plan, indent=2, ensure_ascii=False) + '\n')
        materials(ROOT)
        print(f"Prepared {plan['eligible_tasks']} task evidence records and material candidates; no model calls.")
        report = preflight(ROOT)
    elif args.phase == 'check':
        validate(ROOT)
        print('Frozen metadata, donor controls, evaluator sources and material candidates verified. Images not checked.')
        return 0
    else:
        report = preflight(ROOT)
    for blocker in report['blockers']:
        print('BLOCKED: ' + blocker)
    if args.phase == 'pilot':
        print('Pilot execution adapter is not implemented: requires live session-portability proof first. No model was started.')
    return 2


if __name__ == '__main__':
    raise SystemExit(main())
