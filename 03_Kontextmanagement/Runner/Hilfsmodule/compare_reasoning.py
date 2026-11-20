#!/usr/bin/env python3
"""Read-only comparison of active standard results, with explicit task pairing."""
import argparse
import collections
import csv
import itertools
import hashlib
import json
import math
from pathlib import Path
import statistics

LAB = Path(__file__).resolve().parent
ORDER = {name: i for i, name in enumerate(('low', 'medium', 'high', 'xhigh', 'max'))}


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load(directory, master, numbers=range(1, 101)):
    selection = json.loads((directory / 'selection.json' if (directory / 'selection.json').exists() else LAB / 'selection.json').read_text())
    if selection['dataset_sha256'] != master['dataset_sha256']:
        raise ValueError(f'Dataset differs: {directory}')
    selected = set(numbers)
    rows, manifests = {}, []
    for path in sorted(directory.glob('batch-*/manifest.json')):
        m = json.loads(path.read_text())
        if 'standard' not in m['setups'] or not selected.intersection(m['tasks']):
            continue
        manifests.append({'path': str(path.relative_to(LAB)), 'sha256': digest(path),
                          'status': m['status'], 'workers': m.get('model_workers'), 'execution_mode': m.get('execution_mode')})
        for n in m['tasks']:
            if n not in selected:
                continue
            if selection['scored_tasks'][n - 1]['instance_id'] != master['scored_tasks'][n - 1]['instance_id']:
                raise ValueError(f'Task IDs differ at {n}: {directory}')
            if n in rows:
                raise ValueError(f'Duplicate active task {n}: {directory}; select a single attempt explicitly')
            p = path.parent / f'task-{n:02d}/standard/result.json'
            result = json.loads(p.read_text()) if p.exists() else {'status': 'missing'}
            rows[n] = {'result': result, 'source': str(p.relative_to(LAB)), 'sha256': digest(p) if p.exists() else None,
                       'model': m['model'], 'reasoning': m['reasoning']}
    return rows, manifests


def stats(rows, numbers):
    results = [rows[n]['result'] for n in numbers]
    stages = [s for r in results for s in r.get('stages', [])]
    usage = {k: sum((s.get('usage') or {}).get(k, 0) for s in stages)
             for k in ('input_tokens', 'cached_input_tokens', 'output_tokens')}
    usage['uncached_input_tokens'] = usage['input_tokens'] - usage['cached_input_tokens']
    usage['input_plus_output_tokens'] = usage['input_tokens'] + usage['output_tokens']
    duration = [sum(s.get('elapsed_seconds', 0) for s in r.get('stages', [])) for r in results if r.get('stages')]
    return {'tasks': len(results), 'solved': sum(r.get('resolved') is True for r in results),
            'statuses': dict(collections.Counter(r['status'] for r in results)), 'usage': usage,
            'stage_count': len(stages), 'complete_usage_stages': sum(bool(s.get('usage_complete')) for s in stages),
            'timed_out_stages': sum(bool(s.get('timed_out')) for s in stages),
            'mean_model_seconds': statistics.mean(duration) if duration else None,
            'median_model_seconds': statistics.median(duration) if duration else None}


def paired_comparison(a, b, numbers):
    only_a = [n for n in numbers if a[n]['result'].get('resolved') is True and b[n]['result'].get('resolved') is not True]
    only_b = [n for n in numbers if b[n]['result'].get('resolved') is True and a[n]['result'].get('resolved') is not True]
    count = len(only_a) + len(only_b)
    p = min(1, 2 * sum(math.comb(count, i) for i in range(min(len(only_a), len(only_b)) + 1)) / 2**count) if count else 1
    return {'a_only_solved': only_a, 'b_only_solved': only_b, 'mcnemar_exact_two_sided_p': p}


def common_tasks(variants, candidates=range(1, 101)):
    return sorted(n for n in candidates if all(
        n in v['rows'] and v['rows'][n]['result']['status'] == 'completed'
        for v in variants.values()))


def build(numbers=range(1, 101), models=None):
    master = json.loads((LAB / 'selection-extended.json').read_text())
    numbers = sorted(set(numbers))
    if not numbers or min(numbers) < 1 or max(numbers) > len(master['scored_tasks']):
        raise ValueError('Task range outside the frozen selection')
    variants = {}
    for folder in sorted(LAB.glob('experiment-reasoning-*')):
        if not (folder / 'selection.json').exists():
            continue
        rows, manifests = load(folder, master, numbers)
        if not rows:
            continue
        configs = {(r['model'], r['reasoning']) for r in rows.values()}
        if len(configs) != 1:
            raise ValueError(f'Mixed configurations: {folder}')
        model, reasoning = configs.pop()
        key = f'{model}/{reasoning}'
        if key in variants:
            raise ValueError(f'Duplicate configuration: {key}')
        variants[key] = {'model': model, 'reasoning': reasoning, 'rows': rows, 'manifests': manifests, 'historical_prefix': False}
    for current, legacy in [('experiment-luna-100', 'experiment-luna-01'), ('experiment-sol-100', 'experiment-v2-repeat-01')]:
        rows, manifests = load(LAB / current, master, numbers)
        old, old_manifests = load(LAB / legacy, master, numbers)
        if not rows and not old:
            continue
        model = next(iter({**old, **rows}.values()))['model']; key = f'{model}/medium'
        extra = variants.pop(key, None)
        if extra and set(extra['rows']).intersection(set(old) | set(rows)):
            raise ValueError(f'Duplicate active medium tasks: {key}')
        for n, value in old.items():
            if n > 20 or n in rows or value['model'] != model or value['reasoning'] != 'medium':
                raise ValueError('Historical prefix is not the same model/effort and disjoint first 20')
        variants[key] = {'model': model, 'reasoning': 'medium', 'rows': {**old, **rows},
                         'manifests': old_manifests + manifests, 'historical_prefix': bool(old)}
        if extra:
            variants[key]['rows'].update(extra['rows'])
            variants[key]['manifests'].extend(extra['manifests'])
    # New Sol 6 medium architecture run: standard rows only, never relabel Sol 6.1.
    architecture = LAB / 'experiment-sol6-100'
    if architecture.exists():
        rows, manifests = load(architecture, master, numbers)
        if rows:
            if any(v['model'] != 'gpt-6-sol' or v['reasoning'] != 'medium' for v in rows.values()):
                raise ValueError('Sol 6 architecture reference must use gpt-6-sol/medium')
            key = 'gpt-6-sol/medium'
            if key in variants:
                raise ValueError('Sol 6 medium supplied twice; use architecture standard results only')
            variants[key] = {'model': 'gpt-6-sol', 'reasoning': 'medium', 'rows': rows,
                             'manifests': manifests, 'historical_prefix': False}
    if models:
        variants = {k:v for k,v in variants.items() if v['model'] in models}
        missing_models = set(models) - {v['model'] for v in variants.values()}
        if missing_models:
            raise ValueError(f'No results for requested models: {sorted(missing_models)}')
    if not variants:
        raise ValueError('No configurations found for the selected task range')
    for v in variants.values():
        for n in numbers:
            v['rows'].setdefault(n, {'result': {'status':'missing'}, 'source':None, 'sha256':None,
                                    'model':v['model'], 'reasoning':v['reasoning']})
    keys = sorted(variants, key=lambda k: (variants[k]['model'], ORDER[variants[k]['reasoning']]))
    common = common_tasks(variants, numbers)
    for k in keys:
        v = variants[k]
        v['paired'] = stats(v['rows'], common)
        v['all_selected'] = stats(v['rows'], sorted(v['rows']))
    comparisons = {}
    for model in sorted({v['model'] for v in variants.values()}):
        levels = sorted({v['reasoning'] for v in variants.values() if v['model'] == model}, key=ORDER.get)
        for first, second in itertools.combinations(levels, 2):
            a, b = f'{model}/{first}', f'{model}/{second}'
            if a in variants and b in variants:
                comparisons[f'{a} vs {b}'] = paired_comparison(variants[a]['rows'], variants[b]['rows'], common)
    # Holm adjustment across the displayed exploratory comparisons.
    ranked = sorted(comparisons.values(), key=lambda x: x['mcnemar_exact_two_sided_p'])
    previous = 0
    for i, value in enumerate(ranked):
        previous = max(previous, min(1, value['mcnemar_exact_two_sided_p'] * (len(ranked) - i)))
        value['holm_adjusted_p'] = previous
    return {'scope': f'Standard only; tasks {numbers[0]}-{numbers[-1]}; paired comparison officially evaluated in every selected variant',
            'selected_tasks': numbers, 'model_filter': sorted(models) if models else None,
            'primary_tasks': common, 'primary_excluded_tasks': sorted(set(numbers)-set(common)),
            'configured_control_exclusions': sorted(n for n in numbers if any(v['rows'][n]['result']['status']=='control_excluded' for v in variants.values())), 'dataset_sha256': master['dataset_sha256'],
            'variants': {k: variants[k] for k in keys}, 'paired_tests': comparisons,
            'limits': ['Medium 1-20 are historical standard results, included in full overview and paired comparison with explicit provenance and protocol caveats.',
                       'Official grading does not isolate agent capability in every case: known fixture/interface/dependency issues remain.',
                       'Workers and restart history differ; model times include waiting and local tests.',
                       'Active result usage only. Archived interrupted attempts and unrecorded usage are excluded.',
                       'Cached input is part of input; reasoning output, where recorded, is part of output.',
                       'P-values are exploratory; Holm adjustment includes all displayed comparisons. No equivalence claim.']}


def render(data):
    numbers = data.get('selected_tasks', list(range(1,101)))
    label = f'{numbers[0]}–{numbers[-1]}'
    lines = [f'# Vergleich der Reasoning-Stufen – Aufgaben {label}', '',
        'Architektur: ausschließlich Standard. low, medium, high, xhigh und max sind enthalten, sofern Ergebnisse vorhanden sind.', '',
        'medium umfasst die Standard-Abgaben aus den ursprünglichen Architektur-Batches: Luna Aufgaben 1–20 aus experiment-luna-01 und 21–100 aus experiment-luna-100; Sol Aufgaben 1–20 aus experiment-v2-repeat-01 und 21–100 aus experiment-sol-100. Rollen-B-Ergebnisse werden nicht in eine Standard-Konfiguration gemischt. Für Aufgaben ab 101 stammen die medium-Ergebnisse aus den jeweiligen experiment-reasoning-Ordnern. Jede aktive Abgabe wird genau einmal verwendet; technische Archive sind keine zusätzlichen Versuche in der Ergebnisquote.', '',
        'Versionszuordnung: Die historischen Sol-Reihen verwenden gpt-6.1-sol. Neue gpt-6-sol-Reihen stehen separat unter experiment-reasoning-sol6-*; ihre medium-Referenzen stammen aus experiment-reasoning-sol6-medium beziehungsweise aus vorhandenen Standard-Architektur-Batches. Die Generationen werden niemals zusammengeführt oder umbenannt.', '',
        f'## Gesamtübersicht: alle Aufgaben {label}', '',
        f'Alle {len(numbers)} ausgewählten Aufgaben pro Konfiguration werden ausgewiesen. Fehlende Ergebnisse, Kontrollausschlüsse und ungültige Exporte bleiben als solche sichtbar; sie werden nicht als bewertete Lösungsfehler umgedeutet.', '',
        '| Modell | Reasoning | Aufgaben | Gelöst | Offiziell bewertet | Ungültig | Leer | Ausgeschlossen | Fehlend | Input + Output (Mio.) | Vollständige Zähler |',
        '| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |']
    for v in data['variants'].values():
        s=v['all_selected'];c=s['statuses'];prefix='≥ ' if s['complete_usage_stages']<s['stage_count'] else ''
        lines.append(f"| {v['model']} | {v['reasoning']} | {s['tasks']} | {s['solved']} | {c.get('completed',0)} | {c.get('invalid_submission',0)} | {c.get('empty_submission',0)} | {c.get('control_excluded',0)} | {c.get('missing',0)} | {prefix}{s['usage']['input_plus_output_tokens']/1e6:.2f} | {s['complete_usage_stages']}/{s['stage_count']} |")
    lines += ['', 'Die unterschiedlichen Mengen bewerteter Abgaben erklären, warum die Rohzahlen oben nicht direkt identische Nenner haben. Alle Einzelaufgaben einschließlich Status und Herkunft stehen in [reasoning-tasks.csv](reasoning-tasks.csv).', '',
        f"## Gepaarter Vergleich: dieselben {len(data['primary_tasks'])} Aufgaben aus {label}", '',
        f"Nur Aufgaben, für die jede Konfiguration ein offizielles Bewertungsergebnis hat. Nicht enthalten: {data['primary_excluded_tasks']}. Vereinbarte Kontrollausschlüsse im gewählten Bereich: {data['configured_control_exclusions']}; andere Fälle fehlen oder haben ungültige Exporte in mindestens einer Variante. Die ersten 20 Aufgaben sind in diesem Vergleich enthalten, soweit sie diese Bedingung erfüllen.", '',
        '| Modell | Reasoning | Gelöst | Quote | Input + Output (Mio.) | Nicht gecachter Input (Mio.) | Ø Rollenzeit (min) |',
        '| --- | --- | ---: | ---: | ---: | ---: | ---: |']
    for v in data['variants'].values():
        s=v['paired'];u=s['usage'];prefix='≥ ' if s['complete_usage_stages']<s['stage_count'] else ''
        quota=f"{s['solved']/s['tasks']:.1%}" if s['tasks'] else '–'
        duration=f"{s['mean_model_seconds']/60:.2f}" if s['mean_model_seconds'] is not None else '–'
        lines.append(f"| {v['model']} | {v['reasoning']} | {s['solved']}/{s['tasks']} | {quota} | {prefix}{u['input_plus_output_tokens']/1e6:.2f} | {prefix}{u['uncached_input_tokens']/1e6:.2f} | {duration} |")
    lines += ['', 'Die Quote misst das Bestehen offizieller Pflicht-Tests. Sie isoliert nicht in jedem Fall die Fähigkeiten der Agenten; bekannte Testdaten-/Schnittstellenprobleme bleiben erhalten.', '',
        '## Gepaarte statistische Vergleiche', '',
        '| Vergleich | Nur erste Stufe gelöst | Nur zweite Stufe gelöst | Exakter McNemar-p-Wert | Holm-korrigiert |', '| --- | ---: | ---: | ---: | ---: |']
    for name,t in data['paired_tests'].items():
        lines.append(f"| {name} | {len(t['a_only_solved'])} | {len(t['b_only_solved'])} | {t['mcnemar_exact_two_sided_p']:.4f} | {t['holm_adjusted_p']:.4f} |")
    lines += ['', 'Explorative Tests mit Holm-Korrektur über alle dargestellten Vergleiche, einschließlich high und xhigh. Nicht signifikant bedeutet nicht gleichwertig. Dies sind einzelne Versuche pro Aufgabe/Konfiguration.', '',
        '## Interpretation', '']
    for model in sorted({v['model'] for v in data['variants'].values()}):
        configs=[v for v in data['variants'].values() if v['model']==model]
        lines.append(f"- {model}: " + '; '.join(f"{v['reasoning']}: {v['paired']['solved']}/{v['paired']['tasks']}" for v in configs) + '.')
    lines += ['', 'Höheres Reasoning garantiert keine höhere Quote: high und max können ähnliche Ergebnisse liefern, und einzelne Stufen können schlechter abschneiden als medium. Tokenaufwand und Zeit sind deshalb neben der Lösungsquote zu betrachten.', '',
        '## Vergleichbarkeit und Herkunft', '',
        '- medium setzt sich aus historischen Standard-Batches zusammen. Gleiche Architektur, Modell-ID und Reasoning-Stufe bedeuten keine vollständig identische technische Durchführung: Workerzahlen, Neustarts und frühere Harness-Stände unterscheiden sich.',
        '- Bei Sol/medium, Aufgabe 2, ist die historische Standard-Rolle als timed_out protokolliert; die abgegebene Lösung wurde offiziell bewertet und als gelöst gespeichert. Das Ergebnis wird wie angefordert übernommen. Der Tokenzähler ist unvollständig; Tokenwerte sind daher Untergrenzen (≥). Das Timeout-Flag ist widersprüchlich zur gespeicherten timeout_seconds=None und wird nicht nachträglich umgedeutet.',
        '- Rollenzeit umfasst Wartezeit und lokale Tests; sie ist nicht CPU-Zeit oder Gesamtdauer paralleler Batches. Alte Zeitlimit-/Abbruchereignisse schränken die Zeitvergleiche zusätzlich ein.',
        '- Tokenwerte umfassen aktive Abgaben, nicht archivierte Anläufe. Cached Input ist bereits im Input enthalten. Ein Abo-Prozentsatz lässt sich nicht zuverlässig ableiten.',
        '- Bekannte Fälle: 14/88 Redis-Dateien im Export; 25/81 Fixtures im Referenz- statt Testpatch; 57 Mischfall einer genannten Fixture; 87 widersprüchliche Schnittstellenpfade; 99 Abhängigkeiten/Checksummen. Keine neuen Ausschlüsse, Patchreparaturen oder Testläufe für diesen Report.', '',
        '[Maschinenlesbare Auswertung mit Quellenhashes](reasoning-comparison.json) · [Alle Aufgaben und Herkunft](reasoning-tasks.csv)', '', '## Verwendete Batches', '']
    for v in data['variants'].values():
        for m in v['manifests']:
            lines.append(f"- [{v['model']}/{v['reasoning']}: {m['path']}]({LAB/m['path']})")
    if not any(v['model']=='gpt-6.1-sol' for v in data['variants'].values()) or 2 not in numbers:
        lines = [line for line in lines if not line.startswith('- Bei Sol/medium, Aufgabe 2,')]
    audit_path = LAB/'validation/sol-medium-high/audit.json'
    if audit_path.exists() and any(v['model']=='gpt-6.1-sol' for v in data['variants'].values()) and 43 in numbers:
        audit = json.loads(audit_path.read_text())
        details = audit['task43']
        if all((LAB/details[f'{effort}_result']).exists() and
               digest(LAB/details[f'{effort}_result']) == details[f'{effort}_sha256']
               for effort in ('medium', 'high')):
            lines += ['', '## Bestehende Prüfung: Sol/high gegenüber Sol/medium', '',
                'Der Unterschied zwischen medium und high liegt ausschließlich bei Aufgabe 43. Die gespeicherte Prüfung fand keine Modell-/Verbindungsfehler in den endgültigen High-Rollen.', '',
                f"Der offizielle Test erwartet `{details['expected']}`, high liefert `{details['actual_high']}`. high verwendet Zahlenformatierung und hat seine lokalen Tests an dieses Format angepasst. Damit erklärt eine einzelne Fehlertext-Abweichung den gesamten Scoreabstand, nicht eine belegte generell geringere Fähigkeit oder ein Internetproblem.", '',
                '[Prüfnachweis](../validation/sol-medium-high/audit.json)']
    # Pad the compact table so columns also align in the VS Code source editor.
    summary = [['Modell', 'Reasoning', 'Tokenverbrauch (Mio.)', 'Davon cached (Mio.)', '% gelöst']]
    for v in data['variants'].values():
        s = v['paired']
        prefix = '≥ ' if s['complete_usage_stages'] < s['stage_count'] else ''
        quota = f"{s['solved']/s['tasks']:.1%}" if s['tasks'] else '–'
        summary.append([v['model'], v['reasoning'],
                        f"{prefix}{s['usage']['input_plus_output_tokens']/1e6:.2f}",
                        f"{prefix}{s['usage']['cached_input_tokens']/1e6:.2f}", quota])
    widths = [max(len(row[i]) for row in summary) for i in range(len(summary[0]))]

    def summary_row(row):
        return '| ' + ' | '.join(cell.ljust(widths[i]) if i < 2 else cell.rjust(widths[i])
                                 for i, cell in enumerate(row)) + ' |'

    table = [summary_row(summary[0]),
             '| ' + ' | '.join('-' * width if i < 2 else '-' * (width - 1) + ':'
                               for i, width in enumerate(widths)) + ' |']
    table.extend(summary_row(row) for row in summary[1:])
    insert_at = lines.index(f'## Gesamtübersicht: alle Aufgaben {label}')
    lines[insert_at:insert_at] = [
        '## Tokenverbrauch und % gelöst', '',
        f"Basis: dieselben {len(data['primary_tasks'])} offiziell bewerteten Aufgaben je Konfiguration. Tokenverbrauch = Input + Output inklusive gecachtem Input. Davon cached = bereits im Input enthaltene gecachte Tokens; ≥ kennzeichnet unvollständige Tokenzähler.",
        '', *table, '']
    return '\n'.join(lines)+'\n'


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',default='reports')
    parser.add_argument('--tasks',default='1-100',help='Inclusive task range, e.g. 1-200 or 101-200')
    parser.add_argument('--models',nargs='+',help='Only these model IDs, e.g. gpt-6-luna gpt-6-sol')
    args=parser.parse_args()
    try:
        first,last=map(int,args.tasks.split('-'))
        if first<1 or last<first: raise ValueError()
    except ValueError:
        parser.error('--tasks requires a positive ascending range such as 1-200')
    data=build(range(first,last+1),args.models);output=LAB/args.output;output.mkdir(parents=True,exist_ok=True)
    (output/'reasoning-comparison.json').write_text(json.dumps(data,indent=2)+'\n')
    (output/'reasoning-comparison.md').write_text(render(data))
    with (output/'reasoning-tasks.csv').open('w',newline='') as f:
        writer=csv.DictWriter(f,fieldnames=['model','reasoning','task','status','resolved','source','sha256','timed_out','usage_complete'])
        writer.writeheader()
        for v in data['variants'].values():
            for n,row in sorted(v['rows'].items()):
                r=row['result'];stages=r.get('stages',[])
                writer.writerow({'model':v['model'],'reasoning':v['reasoning'],'task':n,'status':r['status'],
                    'resolved':r.get('resolved'),'source':row['source'],'sha256':row['sha256'],
                    'timed_out':any(s.get('timed_out') for s in stages),
                    'usage_complete':bool(stages) and all(s.get('usage_complete') for s in stages)})
    print('Primary tasks:',len(data['primary_tasks']))
    for key,v in data['variants'].items():print(key,json.dumps(v['paired']))
    print('Paired tests:',json.dumps(data['paired_tests']))
    print('Report:',output/'reasoning-comparison.md')


if __name__=='__main__':main()
