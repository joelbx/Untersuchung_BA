#!/usr/bin/env python3
"""Generate readable context-batch reports from existing evidence; no model calls."""
import argparse
import json
from pathlib import Path
import re

from run_context_main import ROOT, finished, write_report


def generate(root):
    manifest = json.loads((root / 'manifest.json').read_text())
    comparison = write_report(root)
    rows = []
    for item in manifest['schedule']:
        for arm in manifest['arms']:
            directory = root / f"task-{item['task']:02d}" / arm
            if not finished(directory):
                continue
            result = json.loads((directory / 'result.json').read_text())
            audit = result['context_audit']
            rows.append({'task': item['task'], 'setup': arm, 'status': result['status'],
                         'resolved': result.get('resolved'),
                         'usage': audit['known_task_usage'], 'usage_complete': audit['usage_complete'],
                         'elapsed_codex_seconds': result['stage'].get('elapsed_seconds'),
                         'trial_wall_seconds': result['trial_wall_seconds'],
                         'starting_load': audit.get('starting_load'),
                         'compactions': len(audit.get('compaction_rows', [])),
                         'result_path': str(directory / 'result.json')})
    excluded = sorted(int(n) for n, case in manifest['cases'].items() if case['excluded'])
    lines = [f'# SWE-bench Pro Verified – Kontextmanagement – {root.name}', '',
             f"Modell: {manifest['model']}, {manifest['reasoning']}; ChatGPT-Abonnement.", '',
             f"Status: **{manifest['status']}**. Gültige Ergebnisse: **{len(rows)}/{manifest['expected_trials']}**.",
             f"Aufgabenbereich: {min(manifest['tasks'])}–{max(manifest['tasks'])}; vorab ausgeschlossen: {excluded}.", '',
             'Standard: frischer Kontext. A: Kontext mit Zusatztext gefüllt. '
             'B: vorangegangene, aufgabenfremde Sitzungshistorie. '
             'Zielbelegung für A/B beim ersten Aufgabenrequest: 78–82 %.', '',
             '## Lösungsquoten', '', '| Arm | Gültige Ergebnisse | Gelöst | Lösungsquote |',
             '| --- | ---: | ---: | ---: |']
    for arm, value in comparison['arms'].items():
        rate = value['solve_rate']
        display = f'{100 * rate:.2f} %' if rate is not None else 'vorläufig; unvollständig'
        lines.append(f"| {arm} | {value['valid_final_results']}/{value['planned']} | {value['solved']} | {display} |")
    lines += ['', '## Verbrauch und Dauer der endgültigen Versuche', '',
              '| Arm | Input | Cached input | Output | Reasoning output¹ | Codex-Zeit (h) | Versuchsdauer (h) | Kompaktierungen |',
              '| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |']
    for arm, value in comparison['arms'].items():
        u = value['known_usage']
        duration = sum(r['elapsed_codex_seconds'] or 0 for r in rows if r['setup'] == arm)
        lines.append(f"| {arm} | {u['input_tokens']} | {u['cached_input_tokens']} | {u['output_tokens']} | "
                     f"{u['reasoning_output_tokens']} | {duration / 3600:.3f} | {value['trial_wall_seconds'] / 3600:.3f} | {value['compaction_records']} |")
    lines += ['', 'Cached input ist Teil der Input-Tokens; ¹Reasoning output ist Teil der Output-Tokens. '
              'Zeiten sind Summen über Versuche, keine Kalenderlaufzeit. '
              'Die Versuchsdauer enthält Vorbereitung im Versuch und Bewertung; die Codex-Zeit beschreibt den Agentenschritt. '
              'Pilot und Materialerstellung sind in dieser Tabelle nicht enthalten.', '',
              '## Gepaarte Vergleiche', '',
              '| Vergleich | Aufgaben | Nur links gelöst | Nur rechts gelöst | McNemar exakt p | Holm p |',
              '| --- | ---: | ---: | ---: | ---: | ---: |']
    for pair in comparison['pairs']:
        p = pair['mcnemar_exact_p']
        h = pair['holm_adjusted_p']
        lines.append(f"| {pair['left']} / {pair['right']} | {pair['paired']} | {pair['left_only_solved']} | "
                     f"{pair['right_only_solved']} | {p if p is not None else '–'} | {h if h is not None else '–'} |")
    extra = comparison['additional_attempt_consumption']
    lines += ['', '## Technische Unterbrechungen', '',
              f"Gezählte Starts laut Manifest: {manifest['trials_started']}; endgültige Ergebnisse: {len(rows)}. "
              'Archivierte Versuche fließen nicht in die Lösungsquoten ein.',
              f"Zusätzlicher bekannter Verbrauch: `{json.dumps(extra['known_usage'])}`.",
              f"Verbrauch der zusätzlichen Versuche vollständig erfasst: {'Ja' if extra['usage_complete'] else 'Nein'}. "
              f"Versuche ohne vollständige Stage-Datei: {len(extra['unknown_attempts'])}. "
              'Fehlender Verbrauch wird nicht als null angenommen. Details stehen in comparison.json.', '',
              '## Ergebnisse', '',
              '| Aufgabe | Arm | Status | Gelöst | Codex-Zeit (s) | Versuchsdauer (s) | Startbelegung | Kompaktierungen |',
              '| --- | --- | --- | --- | ---: | ---: | ---: | ---: |']
    for row in rows:
        codex = row['elapsed_codex_seconds']
        load = row['starting_load']
        duration = f'{codex:.2f}' if codex is not None else '–'
        occupancy = f'{load * 100:.2f} %' if load is not None else '–'
        lines.append(f"| [{row['task']}]({row['result_path']}) | {row['setup']} | {row['status']} | "
                     f"{'Ja' if row['resolved'] is True else 'Nein'} | {duration} | "
                     f"{row['trial_wall_seconds']:.2f} | {occupancy} | {row['compactions']} |")
    lines += ['', '## Kontrollen und Nachweise', '',
              f'- [Manifest und Versionshashes]({root / "manifest.json"})',
              f'- [Vergleich einschließlich Zusatzverbrauch]({root / "comparison.json"})',
              f'- [Strukturierte Einzelergebnisse]({root / "results.json"})']
    for item in manifest['schedule']:
        n = item['task']
        lines.append(f'- Aufgabe {n}: [Umgebung und Kontrollnachweise]({root / f"task-{n:02d}" / "environment.json"})')
    lines += ['', 'Je Versuch: result.json, context-audit.json, submission.patch, standard/stage.json, '
              'standard/events.jsonl und Evaluationsprotokolle. Archivierte Unterbrechungen bleiben unter '
              'technical-interruptions/ erhalten. Reparaturen sind unter technical-repairs/ dokumentiert.', '']
    summary = {'version': manifest['version'], 'status': manifest['status'],
               'model': manifest['model'], 'reasoning': manifest['reasoning'],
               'expected_trials': manifest['expected_trials'], 'rows': rows, 'comparison': comparison}
    (root / 'results.json').write_text(json.dumps(summary, indent=2) + '\n')
    (root / 'report.md').write_text('\n'.join(lines))
    return summary


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--batch', default='batch-03')
    args = parser.parse_args()
    if not re.fullmatch(r'batch-[A-Za-z0-9_-]+', args.batch):
        parser.error('Use a local batch-* name')
    root = ROOT / 'main' / args.batch
    if root.is_symlink():
        parser.error('Symlink output directory not allowed')
    result = generate(root)
    print(f"{result['status']}: {len(result['rows'])}/{result['expected_trials']} Ergebnisse; {root / 'report.md'}")


if __name__ == '__main__':
    main()
