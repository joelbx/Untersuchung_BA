#!/usr/bin/env python3
"""Paired context-study report. Missing/technical outcomes never become failures.

A final comparison requires every planned task in all three arms. No inference,
API pricing conversion or subscription-percent conversion is performed here.
"""
import argparse
import itertools
import json
import math
from pathlib import Path

from context_telemetry import ARMS, USAGE_KEYS

FINAL = {'completed', 'empty_submission', 'invalid_submission'}


def mcnemar_exact(b, c):
    n = b + c
    return min(1.0, 2 * sum(math.comb(n, k) for k in range(min(b, c) + 1)) / 2 ** n) if n else 1.0


def report(root):
    plan = json.loads((root / 'plan.json').read_text())
    tasks = [row['task'] for row in plan['tasks'] if not row['excluded']]
    outcomes = {}
    issues = []
    for n in tasks:
        for arm in ARMS:
            path = root / 'main' / f'task-{n:02d}' / arm / 'result.json'
            if not path.exists():
                issues.append({'task': n, 'arm': arm, 'problem': 'missing'})
                continue
            value = json.loads(path.read_text())
            valid = value.get('context_audit', {}).get('protocol_valid') is True
            if value.get('status') not in FINAL or not valid:
                issues.append({'task': n, 'arm': arm, 'problem': value.get('status', 'missing_status'),
                               'context_protocol_valid': valid})
                continue
            if value['status'] == 'completed' and not isinstance(value.get('resolved'), bool):
                issues.append({'task': n, 'arm': arm, 'problem': 'missing_boolean_resolved'})
                continue
            outcomes[n, arm] = value
    complete = len(outcomes) == len(tasks) * 3
    arms = {}
    for arm in ARMS:
        values = [v for (n, a), v in outcomes.items() if a == arm]
        solved = sum(v.get('resolved') is True and v['status'] == 'completed' for v in values)
        usage = [v.get('context_audit', {}) for v in values]
        arms[arm] = {'planned_tasks': len(tasks), 'valid_final_results': len(values), 'solved': solved,
                     'final_solve_rate': solved / len(tasks) if complete and tasks else None,
                     'known_task_usage': {k: sum(u.get('known_task_usage', {}).get(k, 0) for u in usage)
                                          for k in USAGE_KEYS},
                     'usage_complete': complete and all(u.get('usage_complete') is True for u in usage),
                     'known_trial_wall_seconds': sum(v.get('trial_wall_seconds', 0) for v in values),
                     'missing_duration_count': sum('trial_wall_seconds' not in v for v in values),
                     'compactions': sum(len(u.get('compaction_rows', [])) for u in usage)}
    pairs = []
    for left, right in itertools.combinations(ARMS, 2):
        paired = [n for n in tasks if (n, left) in outcomes and (n, right) in outcomes]
        def won(n, arm):
            v = outcomes[n, arm]
            return v['status'] == 'completed' and v.get('resolved') is True
        b = sum(won(n, left) and not won(n, right) for n in paired)
        c = sum(not won(n, left) and won(n, right) for n in paired)
        pairs.append({'left': left, 'right': right, 'available_pairs': len(paired),
                      'left_only_solved': b, 'right_only_solved': c,
                      'solve_rate_difference_left_minus_right': (b - c) / len(tasks) if complete and tasks else None,
                      'mcnemar_two_sided_exact_p': mcnemar_exact(b, c) if complete else None,
                      'holm_adjusted_p': None})
    if complete:
        running = 0.0
        for rank, pair in enumerate(sorted(pairs, key=lambda x: x['mcnemar_two_sided_exact_p'])):
            running = max(running, min(1.0, (len(pairs) - rank) * pair['mcnemar_two_sided_exact_p']))
            pair['holm_adjusted_p'] = running
    return {'status': 'final' if complete else 'interim', 'arms': arms, 'pairs': pairs,
            'issues': issues, 'historical_standard_results_reused': False,
            'pilot_and_preparation_usage_included_in_main': False,
            'note': 'Missing, technical and unvalidated-context trials prevent a final report. Empty/invalid submissions count as failures only after context validation. Preparation/pilot/archived interruptions have separate additional consumption.'}


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--experiment', type=Path, default=Path(__file__).resolve().parent / 'experiment-context-sol6-medium')
    args = p.parse_args()
    result = report(args.experiment)
    path = args.experiment / 'comparison.json'
    path.write_text(json.dumps(result, indent=2) + '\n')
    print(result['status'] + ': ' + str(path))


if __name__ == '__main__':
    main()
