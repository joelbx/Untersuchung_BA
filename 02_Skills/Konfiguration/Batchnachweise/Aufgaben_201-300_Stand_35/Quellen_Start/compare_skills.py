#!/usr/bin/env python3
"""Read-only four-arm analysis; never start models, controls or Docker."""
import argparse
import collections
import csv
import hashlib
import json
import math
from pathlib import Path
import random

from run_skills import ARMS, EXCLUSIONS, FINAL, SEED


def read(path):
    return json.loads(Path(path).read_text())


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def holm(pvalues):
    """Holm adjusted two-sided p-values for the prespecified three comparisons."""
    result, previous = {}, 0
    for rank, (name, p) in enumerate(sorted(pvalues.items(), key=lambda x: x[1])):
        previous = max(previous, min(1., (len(pvalues) - rank) * p))
        result[name] = previous
    return result


def paired(a, b, seed, replicates=10000):
    if len(a) != len(b) or not a:
        raise ValueError('Nonempty paired outcomes required')
    diffs = [int(y) - int(x) for x, y in zip(a, b)]
    a_only = diffs.count(-1);b_only = diffs.count(1);discordant = a_only + b_only
    p = min(1., 2 * sum(math.comb(discordant, i) for i in range(min(a_only, b_only) + 1)) / 2 ** discordant) if discordant else 1.
    rng = random.Random(seed)
    samples = sorted(sum(rng.choices(diffs, k=len(diffs))) / len(diffs) for _ in range(replicates))
    return {'standard_only_solved': a_only, 'skill_only_solved': b_only,
            'difference_skill_minus_standard': sum(diffs) / len(diffs),
            'paired_bootstrap_95_ci': [samples[int(.025 * replicates)], samples[int(.975 * replicates)]],
            'mcnemar_exact_two_sided_p': p, 'bootstrap_replicates': replicates,
            'ci_method': 'paired task bootstrap, unadjusted 95%; no repository cluster correction'}


def build(directory):
    directory = Path(directory)
    rows, manifests, identities, hashes = {}, [], {}, {}
    for manifest in sorted(directory.glob('batch-*/manifest.json')):
        m = read(manifest)
        if m.get('version') != 'skills-v1' or m.get('model') != 'gpt-6-sol' or m.get('reasoning') != 'medium' or m.get('baseline') != 'fresh':
            raise ValueError('Unexpected protocol: ' + str(manifest))
        if m['arms'] != list(ARMS) or set(m['control_exclusions']) != set(m['tasks']) & EXCLUSIONS:
            raise ValueError('Arm or exclusion mismatch')
        stable = {k: v for k, v in m['source_hashes'].items() if not k.endswith('/experiment.json')}
        if hashes and hashes != stable:
            raise ValueError('Mixed frozen study sources across batches')
        hashes = stable
        manifests.append({'path': str(manifest), 'sha256': sha(manifest), 'status': m['status']})
        for n in m['tasks']:
            if n in rows:
                raise ValueError(f'Duplicate task {n}; do not select the best attempt')
            record = m['cases'][str(n)]
            identities[n] = record['case']['instance_id']
            rows[n] = {}
            for arm in ARMS:
                trial = manifest.parent / f'task-{n:02d}' / arm
                p = trial / 'result.json'
                r = read(p) if p.exists() else {'status': 'missing', 'resolved': None}
                if r.get('submission_sha256') and sha(trial / 'submission.patch') != r['submission_sha256']:
                    raise ValueError('Submission changed after trial: ' + str(trial))
                if r.get('status') == 'completed':
                    e = read(trial / 'evaluation/evaluation.json')
                    if not e.get('completed') or e.get('error') or e.get('resolved') != r.get('resolved'):
                        raise ValueError('Result and official evaluation disagree: ' + str(p))
                review_path = trial / 'skill-review.json'
                review = read(review_path) if review_path.exists() else {'classification': 'pending'}
                if review.get('classification') not in ('pending', 'complied', 'not_followed', 'technically_blocked', 'unclear'):
                    raise ValueError('Unknown skill review class: ' + str(review_path))
                if review.get('classification') != 'pending' and not review.get('evidence'):
                    raise ValueError('Manual skill assessment needs evidence: ' + str(review_path))
                observations = trial / 'standard/skill-observations.json'
                rows[n][arm] = {'result': r, 'source': str(p), 'sha256': sha(p) if p.exists() else None,
                                'manual_skill_review': review,
                                'observations': read(observations) if observations.exists() else None}
    eligible = sorted(set(rows) - EXCLUSIONS)
    summaries = {}
    for arm in ARMS:
        results = [rows[n][arm]['result'] for n in eligible]
        stages = [s for r in results for s in r.get('stages', [])]
        usage = {key: sum(int((s.get('usage') or {}).get(key) or 0) for s in stages)
                 for key in ('input_tokens', 'cached_input_tokens', 'output_tokens', 'reasoning_output_tokens')}
        finished = sum(r['status'] in FINAL for r in results)
        seconds = sum(r.get('elapsed_codex_seconds', 0) for r in results)
        summaries[arm] = {'eligible': len(eligible), 'finished': finished,
                          'solved': sum(r.get('status') in FINAL and r.get('resolved') is True for r in results),
                          'statuses': dict(collections.Counter(r['status'] for r in results)),
                          'known_usage': usage, 'known_input_plus_output': usage['input_tokens'] + usage['output_tokens'],
                          'usage_complete': bool(eligible) and finished == len(eligible) and len(stages) == len(eligible)
                                            and all(s.get('usage_complete') for s in stages),
                          'model_seconds': seconds,
                          'mean_model_seconds_observed': seconds / len(stages) if stages else None,
                          'skill_reviews': dict(collections.Counter(rows[n][arm]['manual_skill_review']['classification'] for n in eligible))}
    if not manifests:
        raise ValueError('No prepared skill batches found; run controls and prepare first')
    all_final = bool(eligible) and all(s['finished'] == len(eligible) for s in summaries.values())
    full_series = set(rows) == set(range(1, 301))
    tests = {}
    # Never turn missing/technical trials into functional failures for significance tests.
    if all_final and full_series:
        standard = [rows[n]['standard']['result'].get('resolved') is True for n in eligible]
        for arm in ARMS[1:]:
            skill = [rows[n][arm]['result'].get('resolved') is True for n in eligible]
            tests[arm] = paired(standard, skill, f'{SEED}:{arm}')
        adjusted = holm({a: t['mcnemar_exact_two_sided_p'] for a, t in tests.items()})
        for a, t in tests.items():
            t['holm_adjusted_p'] = adjusted[a]
    archives = []
    archived_usage = {k: 0 for k in ('input_tokens', 'cached_input_tokens', 'output_tokens')}
    unknown_archived = 0
    for path in sorted(directory.glob('batch-*/technical-interruptions/**/standard/stage.json')):
        stage = read(path)
        archives.append({'path': str(path), 'sha256': sha(path), 'usage_complete': stage.get('usage_complete', False)})
        unknown_archived += not bool(stage.get('usage_complete'))
        for k in archived_usage:
            archived_usage[k] += int((stage.get('usage') or {}).get(k) or 0)
    return {'protocol': 'skills-v1', 'manifests': manifests, 'rows': rows, 'summaries': summaries,
            'identities': identities, 'eligible_tasks': eligible, 'excluded_tasks': sorted(set(rows) & EXCLUSIONS),
            'all_selected_final': all_final, 'full_300_task_series': full_series,
            'confirmatory_tests_available': all_final and full_series, 'paired_tests': tests,
            'archived_attempt_stages': archives, 'known_archived_usage': archived_usage,
            'archived_stages_with_unknown_or_partial_usage': unknown_archived,
            'analysis_sha256': sha(Path(__file__))}


def write(directory):
    directory = Path(directory);d = build(directory)
    destination = directory / 'report';destination.mkdir(exist_ok=True)
    (destination / 'summary.json').write_text(json.dumps(d, indent=2, ensure_ascii=False) + '\n')
    lines = ['# Skill-Untersuchung: Sol 6 / medium', '',
             f"Bewertbare Aufgaben im bisherigen Bericht: {len(d['eligible_tasks'])}; Ausschlüsse: {d['excluded_tasks']}.",
             f"Alle ausgewählten Versuche abgeschlossen: {d['all_selected_final']}; vollständige Reihe 1–300: {d['full_300_task_series']}.", '',
             '| Variante | Abgeschlossen | Gelöst / bewertbar | Bekannte Input + Output, Mio. | Tokens vollständig | Modellzeit, min. |',
             '|---|---:|---:|---:|---|---:|']
    for arm, s in d['summaries'].items():
        lines.append(f"| {arm} | {s['finished']}/{s['eligible']} | {s['solved']}/{s['eligible']} | {s['known_input_plus_output']/1e6:.2f} | {s['usage_complete']} | {s['model_seconds']/60:.1f} |")
    lines += ['', 'Bei offenen Versuchen sind dies Fortschrittszahlen, keine endgültigen Lösungsquoten. Technische Unterbrechungen zählen nicht als fachliche Fehlversuche.',
              'Jede Variante startet frisch mit demselben Snapshot. Alle verwenden Sol 6 / medium, Abo-Anmeldung, dieselben Offline-Regeln und den unveränderten offiziellen Evaluator.',
              'Die drei angepassten Superpowers-Anweisungspakete überschneiden sich. Ergebnisse isolieren keine einzelnen Mechanismen und reproduzieren nicht den tdd-workflow von Han et al.',
              'Die Modellwahl erfolgte auf bereits bekannten Aufgaben. Die Reihe untersucht Zusatznutzen auf diesem Aufgabensatz; sie ist kein unabhängiger Test auf neuen Aufgaben.', '',
              '## Gepaarte Vergleiche gegen Standard', '']
    if d['paired_tests']:
        lines += ['| Skill | Unterschied, Prozentpunkte | 95%-Intervall | McNemar p | Holm p |', '|---|---:|---|---:|---:|']
        for arm, t in d['paired_tests'].items():
            lo, hi = t['paired_bootstrap_95_ci']
            lines.append(f"| {arm} | {100*t['difference_skill_minus_standard']:.2f} | [{100*lo:.2f}; {100*hi:.2f}] | {t['mcnemar_exact_two_sided_p']:.6f} | {t['holm_adjusted_p']:.6f} |")
        lines += ['', 'Intervalle: gepaarter Aufgaben-Bootstrap, 10.000 Ziehungen, feste Seeds, unadjustierte 95%-Intervalle. Holm korrigiert die drei p-Werte; keine Repository-Clusterkorrektur.']
    else:
        lines += ['Die vorab festgelegten drei Signifikanztests werden erst ausgegeben, wenn alle 290 bewertbaren Aufgaben in allen vier Bedingungen final vorliegen.']
    lines += ['', '## Skill-Befolgung und Protokolle', '',
              'skill-loading.json belegt die vollständige Einfügung in die Modellanweisungen. Das beweist keine Befolgung.',
              'skill-observations.json enthält konservative Beobachtungen aus Ereignissen, keine automatischen Compliance-Urteile. Nicht erkannte Shell-/Code-Mode-Aktionen bleiben unklar.',
              'Manuelle Bewertungen stehen gegebenenfalls in skill-review.json pro Versuch und benötigen Belegstellen. Fehlende Bewertungen bleiben pending, technische Hindernisse werden getrennt von Nichtbefolgung erfasst.', '',
              '## Zusätzlicher Aufwand durch Unterbrechungen', '',
              f"Archivierte Modellstufen: {len(d['archived_attempt_stages'])}; davon Nutzung unbekannt/unvollständig: {d['archived_stages_with_unknown_or_partial_usage']}.",
              f"Bekannte zusätzliche Input + Output: {sum(d['known_archived_usage'][k] for k in ('input_tokens','output_tokens')):,} Tokens.",
              'Die Haupttabelle enthält nur aktive Endversuche; archivierte Anläufe sind separat ausgewiesen. Fehlende Tokenwerte sind unbekannt, nicht null.',
              'Cache-Tokens sind Teil der Eingabe, Reasoning-Tokens Teil der Ausgabe. Es werden keine API-Kosten oder Abo-Prozente daraus abgeleitet.', '',
              '[Vollständige Daten](summary.json) · [Aufgaben](tasks.csv)', '']
    output = destination / 'summary.md';output.write_text('\n'.join(lines))
    with (destination / 'tasks.csv').open('w', newline='') as stream:
        writer = csv.writer(stream)
        writer.writerow(['task', 'instance_id', 'arm', 'status', 'resolved', 'input_tokens', 'output_tokens', 'model_seconds', 'skill_review', 'source', 'sha256'])
        for n in sorted(d['rows']):
            for arm in ARMS:
                entry = d['rows'][n][arm];r = entry['result'];stages = r.get('stages', [])
                values = [sum(int((s.get('usage') or {}).get(k) or 0) for s in stages) if stages else '' for k in ('input_tokens', 'output_tokens')]
                writer.writerow([n, d['identities'][n], arm, r['status'], r.get('resolved'), *values,
                                 r.get('elapsed_codex_seconds'), entry['manual_skill_review']['classification'], entry['source'], entry['sha256']])
    return output


if __name__ == '__main__':
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--experiment', default='experiment-skills-sol6-medium')
    a = p.parse_args()
    lab = Path(__file__).resolve().parent
    target = lab / a.experiment
    if target.resolve().parent != lab or not a.experiment.startswith('experiment-'):
        p.error('Use a local experiment-* directory')
    print(write(target))
