#!/usr/bin/env python3
"""Compare fresh architectures in one batch; never merge historical candidates.

Primary denominator: all prevalidated, nonexcluded tasks. Empty/invalid
submissions count as failures. Technical/incomplete results prevent final tests.
"""
import argparse
from collections import Counter
import csv
import hashlib
import itertools
import json
from pathlib import Path
import re

from compare_reasoning import paired_comparison, stats

LAB = Path(__file__).resolve().parent
FINAL_STATUSES = {'completed', 'empty_submission', 'invalid_submission'}


def build(root):
    root = Path(root)
    manifest = json.loads((root / 'manifest.json').read_text())
    if manifest['model'] != 'gpt-6-sol' or manifest['reasoning'] != 'medium':
        raise ValueError('MAS v1 requires Sol 6 / medium')
    excluded = manifest.get('control_exclusions', [])
    eligible = [n for n in manifest['tasks'] if n not in excluded]
    controls_ready = all((root / f'task-{n:02d}/controls.json').is_file() and
                         json.loads((root / f'task-{n:02d}/controls.json').read_text()).get('passed')
                         for n in eligible)
    variants = {}; delegations = []
    for setup in manifest['setups']:
        rows = {}
        for n in eligible:
            path = root / f'task-{n:02d}' / setup / 'result.json'
            result = json.loads(path.read_text()) if path.is_file() else {'status': 'missing'}
            rows[n] = {'result': result, 'source': str(path),
                       'sha256': hashlib.sha256(path.read_bytes()).hexdigest() if path.is_file() else None}
            audit = path.parent / 'delegations.json'
            if audit.is_file():
                records = json.loads(audit.read_text())['records']
                for r in records:
                    if r['action'] != 'delegate':
                        continue
                    decisions = [d for d in records if d.get('agent_id') == r['agent_id'] and d['action'] != 'delegate']
                    delegations.append({'task': n, 'setup': setup, 'agent_id': r['agent_id'],
                        'role': r['request']['role'], 'status': r['status'],
                        'decision': decisions[-1]['action'] if decisions else 'undecided',
                        'elapsed_seconds': r.get('elapsed_seconds'), 'audit': str(audit)})
        summary = stats(rows, eligible) if eligible else {'tasks': 0, 'solved': 0, 'statuses': {}, 'usage': {}}
        summary['finished'] = sum(r['result']['status'] in FINAL_STATUSES for r in rows.values())
        variants[setup] = {'summary': summary, 'rows': rows}
    final = bool(eligible) and controls_ready and all(v['summary']['finished'] == len(eligible) for v in variants.values())
    comparisons = {}
    if final:
        for a, b in itertools.combinations(variants, 2):
            comparisons[a + ' vs ' + b] = paired_comparison(variants[a]['rows'], variants[b]['rows'], eligible)
        previous = 0
        ranked = sorted(comparisons.values(), key=lambda p: p['mcnemar_exact_two_sided_p'])
        for i, value in enumerate(ranked):
            previous = max(previous, min(1, value['mcnemar_exact_two_sided_p'] * (len(ranked) - i)))
            value['holm_adjusted_p'] = previous
    return {'model': manifest['model'], 'reasoning': manifest['reasoning'], 'batch_status': manifest['status'],
            'manifest': {'source': str(root / 'manifest.json'),
                         'sha256': hashlib.sha256((root / 'manifest.json').read_bytes()).hexdigest()},
            'architecture_protocol': manifest.get('architecture_protocol'), 'native_codex': manifest.get('native_codex'),
            'analysis_script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'statistics_module_sha256': hashlib.sha256((Path(__file__).parent / 'compare_reasoning.py').read_bytes()).hexdigest(),
            'final_comparison': final, 'eligible_tasks': eligible, 'control_exclusions': excluded,
            'controls_ready': controls_ready, 'variants': variants, 'paired_tests': comparisons,
            'delegations': delegations,
            'delegated_role_names': dict(Counter(r['role'] for r in delegations)),
            'limits': ['No equal token budget: all coordinator and worker usage is aggregated.',
                       'Only active final attempt usage; archived interrupted attempts cost additional tokens.',
                       'Cached input is a subset of input; reasoning output is a subset of output.',
                       'No post-hoc exclusion of empty or invalid submissions.',
                       'Per-container resources equal; C may retain its parent while one worker runs.',
                       'Single attempt per architecture/task; paired tests are exploratory.']}


def write(root, data):
    root = Path(root)
    lines = ['# MAS-Vergleich – Sol 6 / medium', '',
             f"Status: {data['batch_status']}; endgültig auswertbar: {data['final_comparison']}.", '',
             f"Fester Nenner: {len(data['eligible_tasks'])} Aufgaben; Ausschlüsse: {data['control_exclusions']}.", '',
             '| Architektur | Fertige Versuche | Gelöst | Eingabe + Ausgabe (Mio.) |',
             '|---|---:|---:|---:|']
    for setup, variant in data['variants'].items():
        s = variant['summary'];tokens = s['usage'].get('input_plus_output_tokens', 0)
        lines.append(f"| {setup} | {s['finished']}/{s['tasks']} | {s['solved']}/{s['tasks']} | {tokens / 1e6:.2f} |")
    lines += ['', 'Leere und ungültige Abgaben zählen als nicht gelöst. Bei technischen oder fehlenden',
              'Ergebnissen ist dies nur ein Zwischenstand; gepaarte Tests werden dann nicht berechnet.', '',
              f"Delegationen insgesamt: {len(data['delegations'])}.", '',
              'Rollenbezeichnungen und Entscheidungen stehen in `mas-delegations.csv`; vollständige',
              'Prompts, Kontext, Antworten, Patches und Übernahmen in den jeweiligen `delegations.json`',
              'und Unterordnern. Die frei gewählten Rollenbezeichnungen sind keine normierte Taxonomie.', '',
              'Der Aufbau hat kein identisches Tokenbudget. Tokenzahlen betreffen aktive Endversuche;',
              'archivierte Unterbrechungen verursachten zusätzlichen Verbrauch. C kann gleichzeitig',
              'den Hauptagenten und einen Unteragenten-Container halten. Es gibt keine bewiesene',
              'Überlegenheit aus einem einzelnen Lauf pro Aufgabe.', '',
              '[Manifest und Quellversionen](manifest.json) · [Daten und Ergebnis-Prüfsummen](mas-comparison.json)', '']
    if data['paired_tests']:
        lines += ['| Vergleich | Nur links gelöst | Nur rechts gelöst | p (exakt) | p (Holm) |',
                  '|---|---:|---:|---:|---:|']
        for name, p in data['paired_tests'].items():
            lines.append(f"| {name} | {len(p['a_only_solved'])} | {len(p['b_only_solved'])} | {p['mcnemar_exact_two_sided_p']:.4f} | {p['holm_adjusted_p']:.4f} |")
    (root / 'mas-comparison.json').write_text(json.dumps(data, indent=2, ensure_ascii=False) + '\n')
    (root / 'mas-comparison.md').write_text('\n'.join(lines) + '\n')
    with (root / 'mas-delegations.csv').open('w', newline='') as stream:
        writer = csv.DictWriter(stream, fieldnames=['task', 'setup', 'agent_id', 'role', 'status', 'decision', 'elapsed_seconds', 'audit'])
        writer.writeheader(); writer.writerows(data['delegations'])


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--experiment', default='experiment-mas-sol6-medium')
    parser.add_argument('--batch', default='batch-01')
    args = parser.parse_args()
    if not re.fullmatch(r'experiment-[A-Za-z0-9][A-Za-z0-9_-]*', args.experiment) or not re.fullmatch(r'batch-[A-Za-z0-9][A-Za-z0-9_-]*', args.batch):
        parser.error('Use an experiment name and batch-NN within the laboratory')
    root = LAB / args.experiment / args.batch
    write(root, build(root))
    print(root / 'mas-comparison.md')
