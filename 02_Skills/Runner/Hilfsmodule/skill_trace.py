"""Read-only trace observations. Heuristics are never a compliance verdict."""
import json
from pathlib import Path
import re

from runner_helpers import review_test_evidence


def audit(directory):
    directory = Path(directory)
    path = directory / 'events.jsonl'
    events, malformed = [], 0
    if path.exists():
        for line in path.read_text().splitlines():
            try:
                events.append(json.loads(line))
            except json.JSONDecodeError:
                malformed += 1
    tests, edits, statements = [], [], []
    for index, event in enumerate(events):
        item = event.get('item') or {}
        if event.get('type') != 'item.completed':
            continue
        evidence = review_test_evidence([event])['attempts']
        for test in evidence:
            tests.append({'event_index': index, **test})
        if item.get('type') == 'file_change':
            edits.append({'event_index': index, 'changes': item.get('changes', [])})
        if item.get('type') == 'agent_message':
            text = item.get('text', '')
            if re.search(r'root cause|hypothes|ursache|TEST_ENVIRONMENT_PROBLEM', text, re.I):
                statements.append({'event_index': index, 'text': text})
    pairs = []
    for test in tests:
        if not test['test_invocation_failed']:
            continue
        later = next((t for t in tests if t['event_index'] > test['event_index'] and
                      t['command'] == test['command'] and t['successful_test_evidence']), None)
        if later:
            pairs.append({'failed_event_index': test['event_index'], 'passed_event_index': later['event_index'],
                          'command': test['command']})
    return {'events_file': str(path), 'events_sha256': __import__('hashlib').sha256(path.read_bytes()).hexdigest()
            if path.exists() else None, 'malformed_event_lines': malformed,
            'recognized_test_commands': tests, 'reported_file_changes': edits,
            'root_cause_or_environment_statements': statements, 'failed_then_passed_same_command': pairs,
            'manual_assessment': 'pending',
            'limitations': 'Shell/script/code-mode edits and tests may not be recognized. A failed invocation '
                          'can be an environment error. Red/green does not prove the right assertion or test-first. '
                          'Absence of recognized evidence is not noncompliance. Inspect full events and checkpoint.'}
