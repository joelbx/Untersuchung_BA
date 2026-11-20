#!/usr/bin/env python3
"""Container-local client; only the trusted host can start a worker or adopt code."""
import argparse
import fcntl
import json
from pathlib import Path
import time
import uuid

MAILBOX = Path('/app/.codex-role-output/delegation-mailbox')


def exchange(request, mailbox=MAILBOX):
    mailbox.mkdir(parents=True, exist_ok=True)
    with (mailbox / 'client.lock').open('a') as lock:
        # Serializes competing tool calls as well as repeated delegations.
        fcntl.flock(lock, fcntl.LOCK_EX)
        request = {**request, 'request_id': uuid.uuid4().hex}
        encoded = json.dumps(request, ensure_ascii=False)
        if len(encoded.encode()) > 512 * 1024:
            raise ValueError('Delegation request exceeds 512 KiB')
        temporary = mailbox / 'request.tmp'
        temporary.write_text(encoded)
        temporary.replace(mailbox / 'request.json')
        response = mailbox / ('response-' + request['request_id'] + '.json')
        # No model deadline: interruption is handled by the outer coordinator.
        while not response.is_file():
            time.sleep(0.25)
        return json.loads(response.read_text())


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest='action', required=True)
    delegate = commands.add_parser('delegate', help='Request a fresh isolated worker; maximum three per task')
    delegate.add_argument('--role', required=True)
    for field in ('instructions', 'task'):
        group = delegate.add_mutually_exclusive_group(required=True)
        group.add_argument('--' + field)
        group.add_argument('--' + field + '-file')
    delegate.add_argument('--context-file')
    delegate.add_argument('--include-working-changes', action='store_true')
    for action in ('adopt', 'decline'):
        sub = commands.add_parser(action)
        sub.add_argument('--id', required=True, dest='agent_id')
        sub.add_argument('--reason', required=True)
    args = vars(parser.parse_args(argv))
    if args['action'] == 'delegate':
        for field in ('instructions', 'task'):
            file = args.pop(field + '_file')
            if file:
                args[field] = Path(file).read_text()
        context = args.pop('context_file')
        args['context'] = Path(context).read_text() if context else ''
    response = exchange(args)
    print(json.dumps(response, ensure_ascii=False))
    return 0 if response.get('ok') else 1


if __name__ == '__main__':
    raise SystemExit(main())
