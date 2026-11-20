#!/usr/bin/env python3
"""Add explicit solve rates to an existing skills report; never run or change trials."""
import argparse
import csv
import hashlib
import io
import json
from pathlib import Path

FINAL = {'completed', 'invalid_submission', 'empty_submission'}


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write_atomic(path, text):
    temporary = path.with_name(path.name + '.rates.tmp')
    temporary.write_text(text, encoding='utf-8')
    temporary.replace(path)


def enrich(experiment):
    experiment = experiment.resolve()
    report = experiment / 'report'
    data = json.loads((report / 'summary.json').read_text())
    markdown = (report / 'summary.md').read_text()
    eligible = data['eligible_tasks']
    if not eligible or len(eligible) != len(set(eligible)):
        raise ValueError('Expected nonempty, unique eligible tasks')
    if set(eligible) & set(data['excluded_tasks']):
        raise ValueError('Excluded tasks may not be in the solve-rate denominator')
    for item in data['manifests']:
        manifest = Path(item['path']).resolve()
        if experiment not in manifest.parents or sha(manifest) != item['sha256']:
            raise ValueError('Manifest changed since report generation; regenerate base report first')
    table = ['| Variante | Abgeschlossen | Gelöst / bewertbar | Lösungsquote | Bekannte Input + Output, Mio. | Tokens vollständig | Modellzeit, min. |',
             '|---|---:|---:|---:|---:|---|---:|']
    csv_stream = io.StringIO(newline='')
    writer = csv.writer(csv_stream)
    writer.writerow(['variant', 'solved', 'eligible', 'finished', 'solve_rate_percent',
                     'solve_rate_final', 'known_input_plus_output', 'model_seconds'])
    for arm, summary in data['summaries'].items():
        results = []
        for n in eligible:
            entry = data['rows'][str(n)][arm]
            source = Path(entry['source']).resolve()
            if entry.get('sha256'):
                if experiment not in source.parents or sha(source) != entry['sha256']:
                    raise ValueError(f'Task {n}, {arm}: source result changed; regenerate base report first')
            results.append(entry['result'])
        solved = sum(r.get('status') in FINAL and r.get('resolved') is True for r in results)
        finished = sum(r.get('status') in FINAL for r in results)
        if (summary['eligible'], summary['finished'], summary['solved']) != (len(eligible), finished, solved):
            raise ValueError(f'{arm}: summary counts disagree with task results')
        final = finished == len(eligible)
        rate = solved / len(eligible) if final else None
        summary.update(solve_rate=rate, solve_rate_percent=100 * rate if final else None,
                       solve_rate_denominator=len(eligible), solve_rate_final=final)
        displayed = f'{100 * rate:.2f}'.replace('.', ',') + ' %' if final else '— (offen)'
        table.append(f"| {arm} | {finished}/{len(eligible)} | {solved}/{len(eligible)} | {displayed} | "
                     f"{summary['known_input_plus_output']/1e6:.2f} | {summary['usage_complete']} | {summary['model_seconds']/60:.1f} |")
        writer.writerow([arm, solved, len(eligible), finished, f'{100*rate:.6f}' if final else '',
                         final, summary['known_input_plus_output'], summary['model_seconds']])
    lines = markdown.splitlines()
    start = next(i for i, line in enumerate(lines) if line.startswith('| Variante |'))
    end = start
    while end < len(lines) and lines[end].startswith('|'):
        end += 1
    lines[start:end] = table
    old_note = 'Bei offenen Versuchen sind dies Fortschrittszahlen, keine endgültigen Lösungsquoten. Technische Unterbrechungen zählen nicht als fachliche Fehlversuche.'
    new_note = ('Lösungsquote = gelöste Aufgaben / bewertbare Aufgaben × 100. '
                f'Der Nenner beträgt je Variante {len(eligible)}; die {len(data["excluded_tasks"])} ausgeschlossenen Aufgaben zählen nicht dazu. '
                'Bei offenen oder technisch unterbrochenen Versuchen wird noch keine endgültige Quote ausgewiesen.')
    if old_note in lines:
        lines[lines.index(old_note)] = new_note
    else:
        for i, line in enumerate(lines):
            if line.startswith('Lösungsquote = '):
                lines[i] = new_note
                break
    for i, line in enumerate(lines):
        if line.startswith('[Vollständige Daten]') and '[Variantenübersicht]' not in line:
            lines[i] += ' · [Variantenübersicht](variants.csv)'
    data['report_enrichment'] = {'script': Path(__file__).name, 'sha256': sha(Path(__file__)),
                                 'purpose': 'Explicit solve rates; no changes to trial outcomes or statistical tests',
                                 'denominator': 'eligible tasks, excluding prespecified exclusions; rates final only when all eligible trials are final'}
    write_atomic(report / 'summary.json', json.dumps(data, ensure_ascii=False, indent=2) + '\n')
    write_atomic(report / 'summary.md', '\n'.join(lines) + '\n')
    write_atomic(report / 'variants.csv', csv_stream.getvalue())
    return report / 'summary.md'


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--experiment', type=Path,
                        default=Path(__file__).resolve().parent / 'experiment-skills-sol6-medium')
    args = parser.parse_args()
    print(enrich(args.experiment))
