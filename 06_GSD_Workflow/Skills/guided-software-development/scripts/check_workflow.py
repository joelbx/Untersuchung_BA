#!/usr/bin/env python3
"""Read-only structural gate check; cannot authenticate consent or verify software."""
import argparse
import hashlib
import json
from pathlib import Path
import re

FEATURE_STATES = {'draft', 'clarification', 'specified', 'approved', 'planned',
                  'implementing', 'reviewing', 'acceptance', 'done'}
TICKET_STATES = {'draft', 'planned', 'implementing', 'reviewing', 'acceptance', 'done'}
ACTIVE = {'implementing', 'reviewing', 'acceptance', 'done'}


def validate(root):
    root = Path(root).resolve()
    errors = []

    def fail(message):
        errors.append(message)

    def file(name):
        if not isinstance(name, str) or not name or Path(name).is_absolute():
            raise ValueError(f'Invalid relative artifact path: {name!r}')
        path = (root / name).resolve()
        if root not in path.parents or not path.is_file():
            raise ValueError(f'Missing artifact or path escapes feature directory: {name}')
        return path

    try:
        state = json.loads(file('workflow.json').read_text())
        if not isinstance(state, dict):
            raise ValueError('workflow.json must contain an object')
    except (OSError, ValueError) as error:
        return [str(error)]
    if state.get('schema_version') != 1:
        fail('Unsupported schema_version')
    feature = state.get('feature_id')
    if not isinstance(feature, str) or not feature.strip():
        fail('feature_id is required')
    if (not isinstance(state.get('project_roots'), list) or not state['project_roots'] or
            any(not isinstance(p, str) or not p for p in state['project_roots'])):
        fail('project_roots must identify the actual target repository/repositories')
    status = state.get('status')
    if not isinstance(status, str) or status not in FEATURE_STATES:
        return errors + ['Invalid feature status']
    receipts = {}
    name = state.get('approval_log', 'approvals.jsonl')
    try:
        if not isinstance(name, str) or not name:
            raise ValueError('approval_log must be a relative filename')
        # Log may be absent before the first approval, but may not escape root.
        candidate = (root / name).resolve()
        if root not in candidate.parents or Path(name).is_absolute():
            raise ValueError('approval_log escapes feature directory')
        if candidate.exists():
            for line_number, line in enumerate(candidate.read_text().splitlines(), 1):
                if not line.strip():
                    continue
                row = json.loads(line)
                if (not isinstance(row, dict) or not isinstance(row.get('id'), str) or
                        not row['id'] or row['id'] in receipts):
                    raise ValueError(f'Invalid or duplicate approval ID at line {line_number}')
                receipts[row['id']] = row
    except (OSError, ValueError, TypeError) as error:
        fail(f'Approval log: {error}')

    def gate(identifier, kind, subject, revision, required):
        receipt = receipts.get(identifier) if isinstance(identifier, str) else None
        if not receipt:
            fail(f'{subject}: missing {kind} approval ({identifier})')
            return
        evidence = receipt.get('evidence') or {}
        if not isinstance(evidence, dict):
            evidence = {}
        if (receipt.get('kind') != kind or receipt.get('subject') != subject or
                not revision or receipt.get('revision') != revision or
                receipt.get('actor') != 'human' or receipt.get('decision') != 'approved' or
                not isinstance(evidence.get('source'), str) or not evidence['source'].strip() or
                not isinstance(evidence.get('quote'), str) or not evidence['quote'].strip()):
            fail(f'{subject}: invalid kind/scope/revision/human evidence for {identifier}')
        artifacts = receipt.get('artifacts')
        if not isinstance(artifacts, dict) or not artifacts:
            fail(f'{subject}: approval {identifier} has no artifact fingerprints')
            return
        for name in required:
            if not name or name not in artifacts:
                fail(f'{subject}: approval {identifier} does not cover {name!r}')
        for name, expected in artifacts.items():
            try:
                actual = hashlib.sha256(file(name).read_bytes()).hexdigest()
                if not isinstance(expected, str) or not re.fullmatch(r'[0-9a-f]{64}', expected) or actual != expected:
                    fail(f'{subject}: stale or invalid approval fingerprint: {name}')
            except (OSError, ValueError) as error:
                fail(str(error))

    artifacts = state.get('artifacts') or {}
    if not isinstance(artifacts, dict):
        return errors + ['Feature artifacts must be an object']
    if status == 'specified':
        try:
            file(artifacts.get('specification'))
        except (OSError, ValueError) as error:
            fail(str(error))
    if status in {'approved', 'planned'} | ACTIVE or state.get('spec_approval'):
        gate(state.get('spec_approval'), 'specification', feature, state.get('spec_revision'),
             [artifacts.get('specification')])
    tickets = state.get('tickets')
    if not isinstance(tickets, list) or not all(isinstance(t, dict) for t in tickets):
        return errors + ['tickets must be a list of objects']
    ids = [t.get('id') for t in tickets]
    if any(not isinstance(i, str) or not i for i in ids) or len(ids) != len(set(ids)):
        return errors + ['Ticket IDs must be nonempty and unique']
    by_id = {t['id']: t for t in tickets}
    if status in {'planned'} | ACTIVE and not tickets:
        fail('Feature in a ticket-work phase requires at least one ticket')
    for key in ('current_ticket', 'next_ticket'):
        if state.get(key) is not None and state[key] not in by_id:
            fail(f'{key} refers to unknown ticket')
    for ticket in tickets:
        tid = ticket['id'];ts = ticket.get('status');ta = ticket.get('artifacts') or {}
        if not isinstance(ts, str) or ts not in TICKET_STATES:
            fail(f'{tid}: invalid ticket status')
            continue
        if not isinstance(ta, dict):
            fail(f'{tid}: artifacts must be an object')
            continue
        dependencies = ticket.get('depends_on', [])
        if not isinstance(dependencies, list) or any(not isinstance(d, str) or d not in by_id or d == tid for d in dependencies):
            fail(f'{tid}: invalid dependencies')
            dependencies = []
        if ts in ACTIVE and any(by_id[d].get('status') != 'done' for d in dependencies):
            fail(f'{tid}: dependency not done')
        required_files = ['ticket'] + (['plan'] if ts != 'draft' else [])
        if ts in {'acceptance', 'done'}:
            required_files.append('review')
        if ts == 'done':
            required_files.append('acceptance')
        for key in required_files:
            try:
                file(ta.get(key))
            except (OSError, ValueError) as error:
                fail(f'{tid}: {error}')
        if ts != 'draft':
            gate(ticket.get('spec_approval'), 'specification', feature, ticket.get('spec_revision'),
                 [ta.get('specification')])
        if ts in ACTIVE or ticket.get('plan_approval'):
            gate(ticket.get('plan_approval'), 'implementation_plan', tid, ticket.get('plan_revision'),
                 [ta.get('ticket'), ta.get('plan')])
        aids = ticket.get('temporary_test_aids', [])
        cleanup_files = []
        if not isinstance(aids, list) or not all(isinstance(aid, dict) for aid in aids):
            fail(f'{tid}: temporary_test_aids must be a list of objects')
            aids = []
        aid_ids = set()
        for aid in aids:
            aid_id = aid.get('id')
            if not isinstance(aid_id, str) or not aid_id.strip() or aid_id in aid_ids:
                fail(f'{tid}: temporary test aid IDs must be nonempty and unique')
            else:
                aid_ids.add(aid_id)
            if aid.get('status') not in ('planned', 'present', 'removed'):
                fail(f'{tid}: invalid temporary test aid status: {aid_id}')
            if ts == 'done':
                if aid.get('status') != 'removed':
                    fail(f'{tid}: temporary test aid not removed: {aid_id}')
                human = aid.get('human_check')
                if (not isinstance(human, dict) or any(
                        not isinstance(human.get(key), str) or not human[key].strip()
                        for key in ('source', 'quote'))):
                    fail(f'{tid}: missing human functional check for test aid: {aid_id}')
                for key in ('removal_evidence', 'verification_evidence'):
                    name = aid.get(key)
                    try:
                        file(name)
                        cleanup_files.append(name)
                    except (OSError, ValueError) as error:
                        fail(f'{tid}: test aid {key}: {error}')
        if ts == 'done' or ticket.get('acceptance_approval'):
            gate(ticket.get('acceptance_approval'), 'acceptance', tid, ticket.get('acceptance_revision'),
                 [ta.get('review'), ta.get('acceptance')] + cleanup_files)
    visiting, visited = set(), set()

    def visit(tid):
        if tid in visiting:
            fail(f'Dependency cycle at {tid}')
            return
        if tid in visited:
            return
        visiting.add(tid)
        dependencies = by_id[tid].get('depends_on', [])
        for dep in dependencies if isinstance(dependencies, list) else []:
            if isinstance(dep, str) and dep in by_id:
                visit(dep)
        visiting.remove(tid);visited.add(tid)
    for tid in by_id:
        visit(tid)
    if status == 'done' and (not tickets or any(t.get('status') != 'done' for t in tickets) or state.get('blocked')):
        fail('Feature done requires all tickets done and no unresolved blockers')
    return errors


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('feature_directory', type=Path)
    args = p.parse_args()
    errors = validate(args.feature_directory)
    for error in errors:
        print('ERROR: ' + error)
    if not errors:
        print('Stored structure and gate evidence consistent. Human authenticity, code quality and actual test execution are NOT verified.')
    return 1 if errors else 0


if __name__ == '__main__':
    raise SystemExit(main())
