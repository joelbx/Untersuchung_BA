"""Fail-closed analysis of native Codex rollouts for the context experiment.

This measures request-input load, not a claimed UI/live-context percentage.
The caller must record the benchmark turn ID and rollout offset BEFORE submitting
the task. Source-history token records are never experiment-task consumption.
"""
import json

ARMS = ('standard', 'A', 'B')
USAGE_KEYS = ('input_tokens', 'cached_input_tokens', 'output_tokens', 'reasoning_output_tokens')


def parse_rows(content):
    return [json.loads(line) for line in content.splitlines() if line.strip()]


def analyze(rows, *, benchmark_turn_id, start_row, arm):
    if arm not in ARMS:
        raise ValueError('Unknown experiment arm')
    if not benchmark_turn_id or not isinstance(start_row, int) or not 0 <= start_row <= len(rows):
        raise ValueError('Explicit benchmark turn ID and valid pre-task offset required')
    errors = []
    selected = rows[start_row:]
    starts = [(i, r.get('payload') or {}) for i, r in enumerate(selected)
              if r.get('type') == 'event_msg' and (r.get('payload') or {}).get('type') == 'task_started'
              and (r.get('payload') or {}).get('turn_id') == benchmark_turn_id]
    if len(starts) != 1:
        errors.append('Expected exactly one benchmark task_started after recorded boundary')
    window = starts[0][1].get('model_context_window') if len(starts) == 1 else None
    if isinstance(window, bool) or not isinstance(window, int) or window <= 0:
        errors.append('Missing positive model-reported context window')
        window = None
    start_index = starts[0][0] if len(starts) == 1 else None
    requests = []
    seen = set()
    for i, row in enumerate(selected):
        p = row.get('payload') or {}
        if row.get('type') != 'token_usage_record' or p.get('turn_id') != benchmark_turn_id:
            continue
        response_id = p.get('response_id')
        u = p.get('usage') or {}
        if not response_id or response_id in seen:
            errors.append('Missing or duplicated response ID; request attribution ambiguous')
            continue
        seen.add(response_id)
        if start_index is None or i <= start_index:
            errors.append('Request usage precedes its benchmark task start')
        if not all(isinstance(u.get(k), int) and not isinstance(u[k], bool) and u[k] >= 0
                   for k in ('input_tokens', 'output_tokens')):
            errors.append('Invalid per-response usage')
            continue
        if not all(isinstance(u.get(k, 0), int) and not isinstance(u.get(k, 0), bool)
                   and u.get(k, 0) >= 0 for k in USAGE_KEYS):
            errors.append('Invalid optional per-response usage')
            continue
        if u.get('cached_input_tokens', 0) > u['input_tokens']:
            errors.append('Cached input exceeds total input')
        requests.append({'row': start_row + i, 'response_id': response_id,
                         'usage': {k: u.get(k, 0) for k in USAGE_KEYS}})
    compactions = []
    for i, row in enumerate(selected):
        kind = (row.get('payload') or {}).get('type', row.get('type', ''))
        if row.get('type') == 'compacted' or kind in ('context_compacted', 'context_compaction'):
            compactions.append(start_row + i)
    first = requests[0] if requests else None
    if not first:
        errors.append('No attributable benchmark request usage; cumulative usage is insufficient')
    before = [i for i in compactions if first is None or i < first['row']]
    # Usage is recorded after the response. A compaction before its usage record
    # cannot safely be assigned to "after the first request" without more evidence.
    if arm != 'standard' and before:
        errors.append('Compaction before first usage record; loaded start is not established')
    ratio = first['usage']['input_tokens'] / window if first and window else None
    if arm != 'standard' and (ratio is None or not 0.78 <= ratio <= 0.82):
        errors.append('First benchmark request is outside 78-82 percent')
    complete = any(r.get('type') == 'event_msg' and
                   (r.get('payload') or {}).get('type') == 'task_complete' and
                   (r.get('payload') or {}).get('turn_id') == benchmark_turn_id for r in selected)
    if not complete:
        errors.append('Benchmark task has no completion event; usage is partial')
    return {'metric': 'first_benchmark_request_input_tokens / model_reported_context_window',
            'benchmark_turn_id': benchmark_turn_id, 'start_row': start_row, 'arm': arm,
            'window': window, 'first_request_input_tokens': first['usage']['input_tokens'] if first else None,
            'starting_load': ratio, 'target_band': [0.78, 0.82] if arm != 'standard' else None,
            'protocol_valid': not errors, 'errors': errors, 'requests': requests,
            'known_task_usage': {k: sum(r['usage'][k] for r in requests) for k in USAGE_KEYS},
            'usage_complete': complete and not errors, 'compaction_rows': compactions,
            'compactions_before_first_usage_record': before,
            'limitations': 'Input load proxy. First response usage is post hoc; ambiguous early compaction fails closed. Cached input is already within input tokens.'}
