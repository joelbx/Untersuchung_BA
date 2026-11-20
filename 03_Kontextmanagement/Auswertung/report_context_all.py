#!/usr/bin/env python3
"""Combine context-study batches from primary evidence; never calls models or Docker."""
import argparse
import csv
from datetime import datetime, timezone
import hashlib
import itertools
import json
from pathlib import Path
import statistics

from compare_context import mcnemar_exact
from context_telemetry import ARMS, USAGE_KEYS

DEFAULT_ROOT = Path(__file__).resolve().parent / 'experiment-context-sol6-medium'
FINAL = {'completed', 'empty_submission', 'invalid_submission'}


def collect(root):
    hashes = {}
    def read(path):
        content = path.read_bytes()
        hashes[str(path)] = hashlib.sha256(content).hexdigest()
        return json.loads(content)

    plan = read(root / 'plan.json')
    expected = {item['task']: item for item in plan['tasks'] if not item['excluded']}
    excluded = [item['task'] for item in plan['tasks'] if item['excluded']]
    assigned, manifests, rows, issues, extra = {}, [], [], [], []
    identity = None
    for path in sorted((root / 'main').glob('batch-*/manifest.json')):
        manifest = read(path)
        current = (manifest['model'], manifest['reasoning'], tuple(manifest['arms']))
        if identity is not None and current != identity:
            raise ValueError('Incompatible model/reasoning/arms: ' + str(path))
        identity = current
        if set(manifest['arms']) != set(ARMS):
            raise ValueError('Expected standard, A and B arms')
        tasks = [item['task'] for item in manifest['schedule']]
        if len(tasks) != len(set(tasks)) or any(n in assigned for n in manifest['tasks']):
            raise ValueError('Overlapping/duplicate task assignment: ' + str(path))
        if set(tasks) != {n for n in manifest['tasks'] if n in expected}:
            raise ValueError('Schedule differs from approved task plan: ' + str(path))
        assigned.update({n: path.parent.name for n in manifest['tasks']})
        manifests.append({'batch': path.parent.name, 'path': str(path), 'status': manifest['status'],
                          'expected_trials': len(tasks) * len(ARMS),
                          'trials_started': manifest.get('trials_started')})
        valid_dirs = set()
        for n in tasks:
            case = manifest['cases'][str(n)]
            if case.get('excluded') or case.get('instance_id') != expected[n]['instance_id']:
                raise ValueError('Task identity differs: ' + str(n))
            for arm in ARMS:
                directory = path.parent / f'task-{n:02d}' / arm
                result_path = directory / 'result.json'
                problem = None
                value = read(result_path) if result_path.exists() else None
                if value is None:
                    problem = 'missing_result'
                elif (value.get('task'), value.get('arm'), value.get('phase')) != (n, arm, 'main'):
                    problem = 'result_identity_mismatch'
                elif value.get('status') not in FINAL:
                    problem = value.get('status', 'missing_status')
                elif value.get('context_audit', {}).get('protocol_valid') is not True:
                    problem = 'invalid_context_protocol'
                elif not isinstance(value.get('resolved'), bool):
                    problem = 'missing_boolean_resolved'
                elif value['status'] != 'completed' and value['resolved']:
                    problem = 'invalid_successful_submission'
                elif value['status'] == 'completed':
                    evaluation_path = directory / 'evaluation/evaluation.json'
                    evaluation = read(evaluation_path) if evaluation_path.exists() else None
                    if (not evaluation or not evaluation.get('completed') or evaluation.get('error')
                            or evaluation.get('resolved') is not value['resolved']):
                        problem = 'evaluation_missing_or_inconsistent'
                if problem:
                    issues.append({'task': n, 'arm': arm, 'batch': path.parent.name, 'problem': problem})
                    continue
                audit = value['context_audit']
                rows.append({'task': n, 'arm': arm, 'batch': path.parent.name,
                             'status': value['status'], 'resolved': value['resolved'],
                             'usage': audit.get('known_task_usage', {}),
                             'usage_complete': audit.get('usage_complete') is True,
                             'codex_seconds': value.get('stage', {}).get('elapsed_seconds'),
                             'trial_seconds': value.get('trial_wall_seconds'),
                             'starting_load': audit.get('starting_load'),
                             'compactions': len(audit.get('compaction_rows', [])),
                             'result_path': str(result_path)})
                valid_dirs.add(directory)
        starts = list(path.parent.glob('task-*/*/standard/started.json'))
        starts += list((path.parent / 'technical-interruptions').glob('*/task-*/*/standard/started.json'))
        for started in sorted(set(starts)):
            if started.parent.parent in valid_dirs:
                continue
            read(started)
            stage_path = started.parent / 'stage.json'
            stage = read(stage_path) if stage_path.exists() else {}
            extra.append({'path': str(started.parent), 'usage': stage.get('usage', {}),
                          'usage_complete': stage.get('usage_complete') is True,
                          'codex_seconds': stage.get('elapsed_seconds'), 'stage_present': bool(stage)})
    for n in sorted(set(expected) - set(assigned)):
        issues.extend({'task': n, 'arm': arm, 'problem': 'batch_not_available'} for arm in ARMS)
    rows.sort(key=lambda x: (x['task'], list(ARMS).index(x['arm'])))
    complete = len(rows) == len(expected) * len(ARMS) and not issues
    outcomes = {(row['task'], row['arm']): row for row in rows}

    def usage_summary(selected):
        known = {key: sum((item.get('usage') or {}).get(key, 0) or 0 for item in selected) for key in USAGE_KEYS}
        missing = [item.get('path', item.get('result_path')) for item in selected
                   if not item.get('usage_complete') or any(key not in (item.get('usage') or {}) for key in USAGE_KEYS)]
        return {'known_usage': known, 'usage_complete': not missing, 'incomplete_usage_paths': missing}

    arms = {}
    for arm in ARMS:
        selected = [row for row in rows if row['arm'] == arm]
        solved = sum(row['resolved'] for row in selected)
        loads = [row['starting_load'] for row in selected if row['starting_load'] is not None]
        arms[arm] = {'planned_tasks': len(expected), 'completed': len(selected), 'solved': solved,
                     'final_solve_rate': solved / len(expected) if complete and expected else None,
                     'observed_solve_rate': solved / len(selected) if selected else None,
                     **usage_summary(selected),
                     'codex_seconds': sum(row['codex_seconds'] or 0 for row in selected),
                     'trial_seconds': sum(row['trial_seconds'] or 0 for row in selected),
                     'duration_complete': all(row['codex_seconds'] is not None and row['trial_seconds'] is not None for row in selected),
                     'median_codex_seconds': statistics.median(row['codex_seconds'] for row in selected if row['codex_seconds'] is not None)
                         if any(row['codex_seconds'] is not None for row in selected) else None,
                     'compaction_records': sum(row['compactions'] for row in selected),
                     'trials_with_compaction': sum(row['compactions'] > 0 for row in selected),
                     'starting_load': {'count': len(loads), 'min': min(loads), 'median': statistics.median(loads), 'max': max(loads)} if loads else None}
    pairs = []
    for left, right in itertools.combinations(ARMS, 2):
        available = [n for n in expected if (n, left) in outcomes and (n, right) in outcomes]
        b = sum(outcomes[n, left]['resolved'] and not outcomes[n, right]['resolved'] for n in available)
        c = sum(not outcomes[n, left]['resolved'] and outcomes[n, right]['resolved'] for n in available)
        pairs.append({'left': left, 'right': right, 'available_pairs': len(available),
                      'left_only_solved': b, 'right_only_solved': c,
                      'difference_percentage_points': 100 * (b - c) / len(expected) if complete and expected else None,
                      'mcnemar_exact_p': mcnemar_exact(b, c) if complete else None, 'holm_adjusted_p': None})
    if complete:
        running = 0
        for rank, pair in enumerate(sorted(pairs, key=lambda x: x['mcnemar_exact_p'])):
            running = max(running, min(1, (len(pairs) - rank) * pair['mcnemar_exact_p']))
            pair['holm_adjusted_p'] = running
    return {'generated_at': datetime.now(timezone.utc).isoformat(), 'status': 'final' if complete else 'interim',
            'model': identity[0] if identity else None, 'reasoning': identity[1] if identity else None,
            'planned_tasks': len(expected), 'expected_trials': len(expected) * len(ARMS),
            'completed_trials': len(rows), 'excluded_tasks': excluded, 'batches': manifests,
            'arms': arms, 'pairs': pairs, 'issues': issues, 'rows': rows,
            'additional_attempt_consumption': {'attempt_count': len(extra), **usage_summary(extra), 'attempts': extra},
            'pilot_and_material_preparation_included': False, 'source_sha256': hashes}


def write(root, report):
    output = root / 'main'
    output.mkdir(exist_ok=True)
    lines = ['# Kontextmanagement – gemeinsamer Bericht', '',
             f"Erstellt: {report['generated_at']}. Modell: **{report['model']}**, Reasoning: **{report['reasoning']}**.", '',
             f"Status: **{report['status']}**. Gültige Ergebnisse: **{report['completed_trials']}/{report['expected_trials']}** "
             f"für {report['planned_tasks']} freigegebene Aufgaben.",
             f"Vorab ausgeschlossen: {', '.join(map(str, report['excluded_tasks']))}.", '',
             'Standard startet mit frischem Kontext. A erhält aufgabenfremden Zusatztext; '
             'B erhält eine zuvor erzeugte, aufgabenfremde Sitzungshistorie. '
             'Zielbelegung bei A/B: 78–82 % beim ersten Aufgabenrequest.', '',
             '## Lösungsquoten', '', '| Arm | Ergebnisse | Gelöst | Quote der vorhandenen Ergebnisse |',
             '| --- | ---: | ---: | ---: |']
    for arm, value in report['arms'].items():
        rate = value['observed_solve_rate']
        rate_text = f'{rate * 100:.2f} %' if rate is not None else '–'
        lines.append(f"| {arm} | {value['completed']}/{value['planned_tasks']} | {value['solved']} | {rate_text} |")
    if report['status'] != 'final':
        lines += ['', '**Vorläufig:** Fehlende/technische Versuche zählen nicht als ungelöst. '
                  'Die Arme haben gegebenenfalls unterschiedliche Nenner; finale Quoten und p-Werte bleiben offen.']
    lines += ['', '## Aufgabenblöcke', '', '| Block | Manifeststatus | Ergebnisse | Standard gelöst | A gelöst | B gelöst |',
              '| --- | --- | ---: | ---: | ---: | ---: |']
    for batch in report['batches']:
        rows = [row for row in report['rows'] if row['batch'] == batch['batch']]
        solved = [sum(row['resolved'] for row in rows if row['arm'] == arm) for arm in ARMS]
        lines.append(f"| {batch['batch']} | {batch['status']} | {len(rows)}/{batch['expected_trials']} | " + ' | '.join(map(str, solved)) + ' |')
    lines += ['', '## Gepaarte Vergleiche', '',
              '| Vergleich | Aufgabenpaare | Nur links gelöst | Nur rechts gelöst | Differenz (Prozentpunkte) | McNemar exakt p | Holm p |',
              '| --- | ---: | ---: | ---: | ---: | ---: | ---: |']
    def number(value):
        return '–' if value is None else f'{value:.6g}'
    for pair in report['pairs']:
        lines.append(f"| {pair['left']} / {pair['right']} | {pair['available_pairs']} | {pair['left_only_solved']} | "
                     f"{pair['right_only_solved']} | {number(pair['difference_percentage_points'])} | "
                     f"{number(pair['mcnemar_exact_p'])} | {number(pair['holm_adjusted_p'])} |")
    lines += ['', 'Zweiseitiger exakter McNemar-Test; Holm-Korrektur über die drei Vergleiche. '
              'Die Differenz ist jeweils links minus rechts. Signifikanztests werden erst bei vollständigen Ergebnissen ausgewiesen.', '',
              '## Tokenverbrauch und Dauer der endgültigen Versuche', '',
              '| Arm | Input | Cached input | Output | Reasoning output | Codex-Zeit (h) | Median Codex (s) | Versuchsdauer (h) | Tokenangaben vollständig |',
              '| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |']
    for arm, value in report['arms'].items():
        u = value['known_usage']
        lines.append(f"| {arm} | {u['input_tokens']} | {u['cached_input_tokens']} | {u['output_tokens']} | "
                     f"{u['reasoning_output_tokens']} | {value['codex_seconds']/3600:.3f} | "
                     f"{number(value['median_codex_seconds'])} | {value['trial_seconds']/3600:.3f} | "
                     f"{'Ja' if value['usage_complete'] else 'Nein'} |")
    lines += ['', 'Cached input ist Teil der Input-Tokens; Reasoning output ist Teil der Output-Tokens. '
              'Zeitangaben sind Summen über Versuche, keine Kalenderlaufzeit. Die Versuchsdauer umfasst auch '
              'Vorbereitung innerhalb des Versuchs und Bewertung. Fehlende Zeiten oder Tokenangaben sind im JSON gekennzeichnet. '
              'Pilot und Materialerstellung werden nicht in diese Hauptlaufwerte eingerechnet.', '',
              '## Kontextbelegung und Kompaktierungen', '',
              '| Arm | Startbelegung min. | Median | max. | Versuche mit Kompaktierung | Kompaktierungsereignisse |',
              '| --- | ---: | ---: | ---: | ---: | ---: |']
    for arm, value in report['arms'].items():
        load = value['starting_load']
        values = [f"{load[key]*100:.3f} %" if load else '–' for key in ('min', 'median', 'max')]
        lines.append(f"| {arm} | " + ' | '.join(values) + f" | {value['trials_with_compaction']} | {value['compaction_records']} |")
    extra = report['additional_attempt_consumption']
    lines += ['', '## Zusätzliche und unterbrochene Versuche', '',
              f"Zusätzliche Modellversuche mit Startnachweis: **{extra['attempt_count']}**. "
              'Diese werden nicht in die Lösungsquoten eingerechnet.',
              f"Bekannter Zusatzverbrauch: `{json.dumps(extra['known_usage'])}`.",
              f"Zusatzverbrauch vollständig erfasst: **{'Ja' if extra['usage_complete'] else 'Nein'}**. "
              f"Versuche mit unvollständigen Tokenangaben: {len(extra['incomplete_usage_paths'])}. "
              'Unbekannter Verbrauch wird nicht als null interpretiert. Einzelnachweise stehen im JSON.', '',
              '## Offene oder ungültige Ergebnisse', '']
    lines += [f"- Task {item['task']}/{item['arm']}: {item['problem']}" for item in report['issues']] or ['Keine.']
    lines += ['', '## Ergebnisse je Aufgabe', '', '| Aufgabe | Block | Standard | A | B |', '| ---: | --- | --- | --- | --- |']
    indexed = {(row['task'], row['arm']): row for row in report['rows']}
    for n in sorted({row['task'] for row in report['rows']}):
        cells = []
        for arm in ARMS:
            row = indexed.get((n, arm))
            cells.append(f"[{'Ja' if row['resolved'] else 'Nein'}]({row['result_path']})" if row else 'offen')
        batch = next(indexed[n, arm]['batch'] for arm in ARMS if (n, arm) in indexed)
        lines.append(f'| {n} | {batch} | ' + ' | '.join(cells) + ' |')
    lines += ['', '## Nachweise', '',
              '- [Strukturierter Gesamtbericht und SHA-256 der Eingaben](report.json)',
              '- [Alle endgültigen Versuche als CSV](results.csv)', '',
              'Die Auswertung liest aktive Endergebnisse und die zugehörigen Evaluationsprotokolle. '
              'Archivierte Modellantworten werden nicht als Ersatz für aktive Ergebnisse verwendet. '
              'Einzelberichte, Manifeste und Laufprotokolle werden nicht verändert.', '']
    (output / 'report.md').write_text('\n'.join(lines))
    (output / 'report.json').write_text(json.dumps(report, indent=2) + '\n')
    columns = ['task', 'arm', 'batch', 'status', 'resolved', 'usage_complete', *USAGE_KEYS,
               'codex_seconds', 'trial_seconds', 'starting_load', 'compactions', 'result_path']
    with (output / 'results.csv').open('w', newline='') as handle:
        writer = csv.DictWriter(handle, fieldnames=columns)
        writer.writeheader()
        for row in report['rows']:
            writer.writerow({**{key: row[key] for key in columns if key in row},
                             **{key: row['usage'].get(key) for key in USAGE_KEYS}})


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--experiment', type=Path, default=DEFAULT_ROOT)
    args = parser.parse_args()
    root = args.experiment.resolve()
    report = collect(root)
    write(root, report)
    print(f"{report['status']}: {report['completed_trials']}/{report['expected_trials']} Ergebnisse; {root / 'main/report.md'}")


if __name__ == '__main__':
    main()
