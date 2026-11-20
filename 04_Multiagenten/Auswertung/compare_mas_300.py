#!/usr/bin/env python3
"""Aggregate the three fixed fresh MAS v1 cohorts; never start or alter runs."""
import csv
from datetime import datetime, timezone
import hashlib
import itertools
import json
from pathlib import Path

import compare_mas
from compare_reasoning import paired_comparison, stats
from control_reuse import CORE

LAB = Path(__file__).resolve().parent
BATCHES = ('experiment-mas-sol6-medium/batch-01',
           'experiment-mas-sol6-medium/batch-02',
           'experiment-mas-sol6-medium-300/batch-03')
SETUPS = ('standard', 'roles-b', 'self-organizing')
LABELS = dict(zip(SETUPS, ('Standard', 'Rollen B', 'Organizer')))
EXCLUSIONS = [40, 65, 127, 184, 186, 217, 218, 258, 261, 285]


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def build():
    master = json.loads((LAB / 'selection-extended.json').read_text())
    combined = {s: {} for s in SETUPS}
    seen = set()
    excluded = []
    cohorts = []
    delegations = []
    evidence = {}
    audit = {'evaluations_checked': 0, 'controls_checked': 0, 'stages_checked': 0,
             'container_images_checked': 0, 'invocations_checked': 0}
    first = None
    for name in BATCHES:
        root = LAB / name
        data = compare_mas.build(root)
        m = json.loads((root / 'manifest.json').read_text())
        assert m['status'] == 'completed' and data['final_comparison'], name
        assert tuple(m['setups']) == SETUPS and not m.get('active_trials')
        assert not (seen & set(m['tasks'])), 'Duplicate task across cohorts'
        seen.update(m['tasks'])
        excluded.extend(data['control_exclusions'])
        selection = json.loads((LAB / m['selection_file']).read_text())
        assert selection['dataset_sha256'] == master['dataset_sha256']
        for n in m['tasks']:
            assert selection['scored_tasks'][n-1] == master['scored_tasks'][n-1]
        if first is None:
            first = m
        else:
            assert m['native_codex'] == first['native_codex']
            assert m['architecture_protocol'] == first['architecture_protocol']
            for source in CORE:
                assert m['execution_source_hashes'][source] == first['execution_source_hashes'][source], source
        evidence[str((root / 'manifest.json').relative_to(LAB))] = sha(root / 'manifest.json')
        evidence[m['selection_file']] = sha(LAB / m['selection_file'])
        for n in data['eligible_tasks']:
            task = root / f'task-{n:02d}'
            control = json.loads((task / 'controls.json').read_text())
            assert control['passed'] and control['reference_resolved'] and not control['original_resolved']
            audit['controls_checked'] += 1
            snapshot = json.loads((task / 'preparation/snapshot.json').read_text())
            for path in (task / 'controls.json', task / 'preparation/snapshot.json'):
                evidence[str(path.relative_to(LAB))] = sha(path)
            for setup in SETUPS:
                row = data['variants'][setup]['rows'][n]
                combined[setup][n] = row
                result = row['result']
                assert result['status'] == 'completed' and result['patch_applicable']
                evaluation = task / setup / 'evaluation/evaluation.json'
                e = json.loads(evaluation.read_text())
                assert e['completed'] and e['resolved'] == result['resolved']
                audit['evaluations_checked'] += 1
                for path in (Path(row['source']), evaluation):
                    evidence[str(path.relative_to(LAB))] = sha(path)
                for stage in result['stages']:
                    assert stage['exit_code'] == 0 and not stage['timed_out']
                    assert stage['usage_complete'] and not stage['unexpected_web_tools']
                    audit['stages_checked'] += 1
                for stage_path in (task / setup).rglob('stage.json'):
                    evidence[str(stage_path.relative_to(LAB))] = sha(stage_path)
                    container = stage_path.parent / 'container.json'
                    invocation = stage_path.parent / 'invocation.json'
                    if container.exists():
                        evidence[str(container.relative_to(LAB))] = sha(container)
                        assert json.loads(container.read_text())['image'] == snapshot['prepared_image_id']
                        audit['container_images_checked'] += 1
                    if invocation.exists():
                        evidence[str(invocation.relative_to(LAB))] = sha(invocation)
                        args = json.loads(invocation.read_text())
                        argv = args['argv']
                        assert argv[argv.index('--model')+1] == 'gpt-6-sol'
                        assert 'model_reasoning_effort="medium"' in argv
                        assert args['auth_mode'] == 'chatgpt'
                        audit['invocations_checked'] += 1
        for d in data['delegations']:
            d['resolved'] = combined[d['setup']][d['task']]['result']['resolved']
            delegations.append(d)
            path = Path(d['audit'])
            evidence[str(path.relative_to(LAB))] = sha(path)
        archives = [str(p.relative_to(LAB)) for p in root.glob('technical-interruptions/*') if p.is_dir()]
        cohorts.append({'source': name, 'tasks': m['tasks'], 'excluded': data['control_exclusions'],
                        'summaries': {s: data['variants'][s]['summary'] for s in SETUPS},
                        'interruption_archives': archives})
    assert seen == set(range(1, 301)) and sorted(excluded) == EXCLUSIONS
    numbers = sorted(combined['standard'])
    assert len(numbers) == 290 and all(set(combined[s]) == set(numbers) for s in SETUPS)
    summaries = {s: stats(combined[s], numbers) for s in SETUPS}
    for s in SETUPS:
        summaries[s]['correction_trials'] = sum(bool(v['result'].get('correction_started')) for v in combined[s].values())
        summaries[s]['summed_trial_wall_seconds'] = sum(v['result'].get('trial_wall_seconds', 0) for v in combined[s].values())
    tests = {f'{a} vs {b}': paired_comparison(combined[a], combined[b], numbers)
             for a, b in itertools.combinations(SETUPS, 2)}
    previous = 0
    for i, test in enumerate(sorted(tests.values(), key=lambda x: x['mcnemar_exact_two_sided_p'])):
        previous = max(previous, min(1, (len(tests)-i)*test['mcnemar_exact_two_sided_p']))
        test['holm_adjusted_p'] = previous
    return {'created_at': datetime.now(timezone.utc).isoformat(), 'model': 'gpt-6-sol',
            'reasoning': 'medium', 'eligible_tasks': numbers, 'exclusions': EXCLUSIONS,
            'cohorts': cohorts, 'summaries': summaries, 'paired_tests': tests,
            'delegations': delegations, 'audit': audit, 'source_evidence_sha256': evidence,
            'analysis_source_sha256': {p: sha(LAB/p) for p in ('compare_mas_300.py','compare_mas.py','compare_reasoning.py')},
            'rows': combined}


def write(data):
    out = LAB / 'reports/mas-300'
    out.mkdir(parents=True, exist_ok=True)
    (out/'summary.json').write_text(json.dumps(data, indent=2, ensure_ascii=False)+'\n')
    with (out/'tasks.csv').open('w', newline='') as stream:
        fields = ['task','instance_id','excluded'] + [f'{s}_resolved' for s in SETUPS]
        writer = csv.DictWriter(stream, fieldnames=fields); writer.writeheader()
        master = json.loads((LAB/'selection-extended.json').read_text())['scored_tasks']
        for n in range(1,301):
            row = {'task':n,'instance_id':master[n-1]['instance_id'],'excluded':n in EXCLUSIONS}
            row.update({f'{s}_resolved': data['rows'][s][n]['result']['resolved'] if n not in EXCLUSIONS else '' for s in SETUPS})
            writer.writerow(row)
    with (out/'delegations.csv').open('w', newline='') as stream:
        writer = csv.DictWriter(stream, fieldnames=list(data['delegations'][0]) if data['delegations'] else ['task','role'])
        writer.writeheader();writer.writerows(data['delegations'])
    summaries = data['summaries']; base = summaries['standard']
    lines = ['# Architekturvergleich: Sol 6 / medium, Aufgaben 1–300', '',
             'Alle drei Batches sind abgeschlossen. Zehn vorab genehmigte Kontrollausschlüsse gelten für alle Varianten:',
             ', '.join(map(str, EXCLUSIONS))+'. Damit umfasst der Vergleich 290 Aufgaben je Architektur und 870 Endversuche.', '',
             '## Ergebnisse und Aufwand', '',
             '| Architektur | Gelöst | Quote | Eingabe + Ausgabe, Mio. | Tokenfaktor zu Standard | Ø Modellzeit je Aufgabe |',
             '|---|---:|---:|---:|---:|---:|']
    for setup, s in summaries.items():
        tokens=s['usage']['input_plus_output_tokens']
        lines.append(f"| {LABELS[setup]} | {s['solved']}/290 | {s['solved']/290:.1%} | {tokens/1e6:.2f} | {tokens/base['usage']['input_plus_output_tokens']:.2f} | {s['mean_model_seconds']/60:.2f} min |")
    lines += ['', 'Tokenzahlen sind Eingabe einschließlich Cache-Tokens plus Ausgabe. Cache-Eingaben und Reasoning-Ausgaben',
              'werden nicht doppelt addiert. Es handelt sich nicht um Aboprozente oder API-Kosten.',
              'Enthalten ist die Nutzung der aktiven Endversuche; archivierte Unterbrechungen verursachten zusätzlichen Verbrauch.',
              'Die Modellzeit summiert protokollierte Rollen-/Agentenzeiten, ohne Containerstart und offizielle Bewertung;',
              'sie ist keine Gesamtlaufzeit bei fünf parallelen Workern.', '',
              '| Architektur | Eingabe, Mio. | Davon Cache, Mio. | Ungecachte Eingabe, Mio. | Ausgabe, Mio. | Korrekturrunden |',
              '|---|---:|---:|---:|---:|---:|']
    for setup,s in summaries.items():
        u=s['usage'];lines.append(f"| {LABELS[setup]} | {u['input_tokens']/1e6:.2f} | {u['cached_input_tokens']/1e6:.2f} | {u['uncached_input_tokens']/1e6:.2f} | {u['output_tokens']/1e6:.2f} | {s['correction_trials']} |")
    lines += ['', '## Einzelne Aufgabenblöcke', '', '| Aufgaben | Bewertbar | Standard | Rollen B | Organizer |','|---|---:|---:|---:|---:|']
    for c in data['cohorts']:
        lines.append(f"| {min(c['tasks'])}–{max(c['tasks'])} | {len(c['tasks'])-len(c['excluded'])} | " + ' | '.join(str(c['summaries'][s]['solved']) for s in SETUPS)+' |')
    lines += ['', '## Gepaarte Vergleiche', '',
              'Zweiseitiger exakter McNemar-Test auf denselben 290 Aufgaben; Holm-Korrektur für drei Architekturvergleiche.', '',
              '| Vergleich | Nur links gelöst | Nur rechts gelöst | p exakt | p Holm |','|---|---:|---:|---:|---:|']
    for name,t in data['paired_tests'].items():
        lines.append(f"| {name} | {len(t['a_only_solved'])} | {len(t['b_only_solved'])} | {t['mcnemar_exact_two_sided_p']:.4f} | {t['holm_adjusted_p']:.4f} |")
    lines += ['', 'Keiner der Vergleiche zeigt einen statistisch signifikanten Lösungsunterschied.',
              'Das beweist keine Gleichwertigkeit. Es gibt nur einen Endversuch pro Aufgabe und Architektur;',
              'Modellstreuung wird nicht durch Wiederholungen geschätzt. Aufgaben innerhalb desselben Repositories',
              'können abhängig sein; diese Tests sind explorativ und berücksichtigen solche Cluster nicht.', '',
              '## Tatsächliche Delegation', '',
              f"Der Organizer erzeugte {len(data['delegations'])} Unteragenten bei {len({d['task'] for d in data['delegations']})} von 290 Aufgaben.",
              'Aufgabe 46: Python module dependency resolver implementer. Aufgabe 257: Go service listener specialist',
              'und Go tsh CLI implementation specialist. Alle drei Vorschläge wurden übernommen; beide Aufgaben blieben ungelöst.',
              'Bei den übrigen 288 Aufgaben arbeitete der Koordinator ohne Unteragenten.', '',
              'Der Vergleich untersucht daher vor allem die freiwillige Nutzung einer Delegationsmöglichkeit.',
              'Er erlaubt keine belastbare Aussage über den Nutzen regelmäßig tatsächlich eingesetzter Unteragenten.',
              'Auch ohne Delegation unterscheidet sich der Koordinator-Prompt von Standard.', '',
              '## Prüfung und Grenzen', '',
              f"Geprüft: {data['audit']['controls_checked']} bestandene Original-/Referenzkontrollen, "
              f"{data['audit']['evaluations_checked']} offizielle Bewertungen und {data['audit']['stages_checked']} abgeschlossene Modellstufen.",
              'Alle Endversuche haben Status completed; die Ergebniswerte stimmen mit den offiziellen Bewertungen überein.',
              'Alle geprüften Stufen melden vollständige Nutzung, Exitcode 0, keine Modelltimeouts und keine unerwarteten Webtools.',
              'Aufgabenidentitäten stimmen mit der Masterauswahl überein; alle Architekturen verwenden je Aufgabe dasselbe vorbereitete Image.',
              'Modell/Reasoning, eingefrorene Ausführungsquellen, Architekturregeln und Codex-Binärdateien stimmen über alle drei Batches überein.',
              'Die Bewertung folgt den offiziellen Pflicht-Testmengen; resolved bedeutet nicht, dass jeder beliebige Repository-Test besteht.',
              'Diese Prüfung ersetzt keine manuelle Ursachenanalyse sämtlicher ungelöster Aufgaben.', '',
              'Technische Unterbrechungen und Wiederaufnahmen bleiben archiviert. Der Bericht wählt ausschließlich den aktiven Endversuch,',
              'keine Best-of-Auswahl historischer Kandidaten. Images aus abgeschlossenen Aufgaben wurden teilweise gelöscht;',
              'Logs und Nachweise bleiben erhalten, eine exakte sofortige Wiederholung aller alten Umgebungen ist damit nicht möglich.',
              'Es gibt kein angeglichenes Tokenbudget. Pro Container gelten gleiche Limits, der Organizer kann gleichzeitig',
              'einen Hauptagenten- und einen Unteragenten-Container halten. Modell/Reasoning wurden nach einer früheren',
              'Reasoning-Untersuchung auf überlappenden Aufgaben gewählt; der Vergleich ist explorativ und kein unabhängiger Holdout-Test.', '',
              '## Interpretation', '',
              'Standard und Organizer erreichen jeweils 166 Lösungen, Rollen B 165. Rollen B benötigt deutlich mehr Tokens und Modellzeit,',
              'ohne dass sich hier eine höhere Lösungsquote zeigt. Standard ist unter diesen Versuchsbedingungen die sparsamste',
              'der drei Varianten bei gleicher beobachteter Lösungsquote wie der Organizer.',
              'Aus diesem Ergebnis folgt keine allgemeine Wirkungslosigkeit von Multiagentensystemen.', '',
              '## Reproduktion und Nachweise', '',
              'Erneut erzeugen: `.venv/bin/python compare_mas_300.py` aus dem Laborordner.',
              '[Maschinenlesbare Daten, Prüfungen und Quell-Prüfsummen](summary.json) · [Alle Aufgaben](tasks.csv) · [Delegationen](delegations.csv)', '']
    for c in data['cohorts']:
        lines.append(f"- [{c['source']}](../../{c['source']}/manifest.json)")
        for archive in c['interruption_archives']:
            lines.append(f'  - [Unterbrechungsarchiv](../../{archive}/)')
    (out/'summary.md').write_text('\n'.join(lines)+'\n')
    return out


if __name__ == '__main__':
    data = build()
    out = write(data)
    print(out/'summary.md')
    print(json.dumps({'summaries':data['summaries'], 'paired_tests':data['paired_tests'], 'audit':data['audit']},indent=2))
