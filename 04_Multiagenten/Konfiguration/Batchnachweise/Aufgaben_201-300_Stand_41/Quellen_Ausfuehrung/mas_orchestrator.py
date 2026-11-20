"""Host-enforced, bounded delegation for one persistent Codex coordinator.

The parent never receives the Docker socket or a callable host endpoint. A
container-local mailbox exposes only delegate/adopt/decline. Child containers
have no mailbox service and cannot create agents. Every boundary is archived.
"""
import asyncio
import hashlib
import json
from pathlib import Path
import re
import time
import uuid

MAILBOX = '/app/.codex-role-output/delegation-mailbox'
MAX_DELEGATIONS = 3

COORDINATOR_INSTRUCTIONS = '''You own the final solution and may solve alone or delegate.
You may formulate any worker specialization, role instructions and work order.
Only use `python /usr/local/bin/delegate-agent` to delegate; never launch Codex yourself.
There are at most THREE delegations TOTAL, including reassignments. Each is a new
isolated agent with empty conversation context, the same model/reasoning and the
base repository. No worker can delegate. Only ONE worker can run at a time.
The worker sees ONLY its supplied instructions/task/context, and your current
working changes ONLY if you pass --include-working-changes. Include issue details
needed by the worker in your task/context. Await its result before further work.
Example: python /usr/local/bin/delegate-agent delegate --role 'Go correctness reviewer'
  --instructions-file /app/.codex-role-output/role.txt
  --task-file /app/.codex-role-output/work-order.txt --include-working-changes
Use one actual shell command line (or shell line continuations). The JSON response
contains the full answer, an inspectable cumulative candidate patch, and a delta.
To adopt worker code use `python /usr/local/bin/delegate-agent adopt --id agent-1
--reason 'explain the decision'`. Adoption applies ONLY worker changes to your
current worktree after a conflict check; no implicit overwrite. To decline use
the decline subcommand with --id and --reason. Resolve all proposals explicitly,
and explain any manual integration in your final answer. You may edit/test yourself.
Never infer test success from a worker's assertion alone; report actual test evidence.
Final answer: describe the solution, relevant tests, and delegation/adoption decisions.
'''


class DelegationBroker:
    def __init__(self, api, image, directory, credential):
        self.api, self.image = api, image
        self.directory, self.credential = Path(directory), credential
        self.records, self.stages, self.proposals = [], [], {}
        self.seen = set()
        self.baseline_path = None
        self.waiting_seconds = 0

    def persist(self):
        self.api.save(self.directory / 'delegations.json', {
            'policy': {'max_delegations': MAX_DELEGATIONS, 'max_active_workers': 1,
                       'recursive_delegation': False, 'fresh_context': True,
                       'free_role_prompts': True}, 'records': self.records})

    async def respond(self, env, request_id, response):
        path = MAILBOX + '/response-' + request_id
        await env.write_text(path + '.tmp', json.dumps(response))
        await env.checked(['mv', '--', path + '.tmp', path + '.json'])

    async def dispatch(self, env, request):
        self.api.save(self.directory / 'requests' / (uuid.uuid4().hex + '.json'),
                      {'at': self.api.now(), 'payload': request})
        if not isinstance(request, dict):
            raise RuntimeError('Delegation request must be a JSON object')
        request_id = request.get('request_id', '')
        if not re.fullmatch(r'[a-f0-9]{32}', request_id):
            raise RuntimeError('Malformed delegation mailbox request ID')
        if request_id in self.seen:
            return
        self.seen.add(request_id)
        action = request.get('action')
        if action not in ('delegate', 'adopt', 'decline'):
            await self.respond(env, request_id, {'ok': False, 'error': 'Unknown delegation action'})
            return
        if action == 'delegate':
            delegates = [r for r in self.records if r['action'] == 'delegate']
            if len(delegates) >= MAX_DELEGATIONS:
                self.records.append({'action': 'rejected', 'request': request, 'at': self.api.now(),
                                     'reason': 'Delegation limit reached; no model started'})
                self.persist()
                await self.respond(env, request_id, {'ok': False, 'error': 'Three delegations already used. Continue yourself.'})
                return
            for field, limit in [('role', 200), ('instructions', 32 * 1024), ('task', 32 * 1024), ('context', 32 * 1024)]:
                value = request.get(field, '')
                if not isinstance(value, str) or '\x00' in value or len(value.encode()) > limit or (field != 'context' and not value.strip()):
                    await self.respond(env, request_id, {'ok': False, 'error': 'Invalid or oversized ' + field})
                    return
            if not isinstance(request.get('include_working_changes', False), bool):
                await self.respond(env, request_id, {'ok': False, 'error': 'include_working_changes must be boolean'})
                return
            agent_id = 'agent-' + str(len(delegates) + 1)
            folder = self.directory / 'delegations' / agent_id
            record = {'action': 'delegate', 'agent_id': agent_id, 'parent_id': 'coordinator',
                      'request': request, 'started_at': self.api.now(), 'status': 'running'}
            self.records.append(record)
            self.persist()
            print(f"{self.directory.parent.name}: self-organizing {agent_id}, role {request['role']!r}: starting", flush=True)
            self.api.save(folder / 'request.json', record)
            current = await self.api.export_patch(env, self.baseline_path)
            self.api.save(folder / 'parent-before.patch', current)
            incoming = current if request.get('include_working_changes') else ''
            self.api.save(folder / 'input.patch', incoming)
            prompt = ('WORK ORDER:\n' + request['task'] + '\n\nEXPLICIT CONTEXT:\n' + request.get('context', ''))
            developer = (self.api.role_instructions('standard') + '\nASSIGNED ROLE:\n' + request['role'] +
                         '\nSPECIALIZATION:\n' + request['instructions'])
            try:
                started = time.monotonic()
                stage, candidate = await self.api.model_stage(
                    self.image, 'self-organizing-worker', prompt, incoming, folder, self.credential,
                    developer_override=developer, result_setup='self-organizing')
                stage.update(agent_id=agent_id, parent_id='coordinator', assigned_role=request['role'])
                self.api.save(folder / 'stage.json', stage)
                self.stages.append(stage)
                delta = (folder / 'delta.patch').read_text()
                answer = (folder / 'answer.md').read_text()
                proposal = {'folder': folder, 'delta': delta, 'candidate': candidate, 'decided': False}
                self.proposals[agent_id] = proposal
                record.update(status='completed', completed_at=self.api.now(), usage=stage.get('usage'),
                              elapsed_seconds=stage['elapsed_seconds'], exit_code=stage['exit_code'],
                              candidate_sha256=hashlib.sha256(candidate.encode()).hexdigest())
                await env.write_text(MAILBOX + '/' + agent_id + '.patch', candidate)
                await env.write_text(MAILBOX + '/' + agent_id + '.delta.patch', delta)
                response = {'ok': True, 'agent_id': agent_id, 'answer': answer,
                            'candidate_patch': MAILBOX + '/' + agent_id + '.patch',
                            'delta_patch': MAILBOX + '/' + agent_id + '.delta.patch',
                            'delegations_remaining': MAX_DELEGATIONS - len(delegates) - 1,
                            'changes_adopted': False}
                self.api.save(folder / 'response.json', response)
                await self.respond(env, request_id, response)
                print(f'{self.directory.parent.name}: self-organizing {agent_id}: complete; awaiting adoption decision', flush=True)
            except BaseException as error:
                record.update(status='technical_interruption', error=self.api.redact(str(error)))
                partial = folder / 'stage.json'
                if partial.is_file():
                    stage = json.loads(partial.read_text())
                    stage.update(agent_id=agent_id, parent_id='coordinator', assigned_role=request['role'])
                    if not any(s.get('agent_id') == agent_id for s in self.stages):
                        self.stages.append(stage)
                raise
            finally:
                self.waiting_seconds += time.monotonic() - started
                self.persist()
        else:
            agent_id = request.get('agent_id')
            proposal = self.proposals.get(agent_id) if isinstance(agent_id, str) else None
            reason = request.get('reason')
            if not proposal or proposal['decided'] or not isinstance(reason, str) or not reason.strip():
                await self.respond(env, request_id, {'ok': False, 'error': 'Unknown/decided proposal or missing reason'})
                return
            before = await self.api.export_patch(env, self.baseline_path)
            decision = {'action': action, 'agent_id': agent_id, 'reason': reason, 'at': self.api.now()}
            if action == 'adopt' and proposal['delta'].strip():
                patch_path = '/tmp/swe-adoption.patch'
                await env.write_text(patch_path, proposal['delta'])
                checked = await env.exec(['git', 'apply', '--check', '--binary', patch_path])
                if checked.returncode:
                    decision.update(applied=False, error=checked.stderr)
                    self.records.append(decision); self.persist()
                    await self.respond(env, request_id, {'ok': False, 'error': 'Patch conflicts; original worktree retained', 'details': checked.stderr})
                    return
                await env.checked(['git', 'apply', '--binary', patch_path])
                await env.checked(['rm', '-f', patch_path])
            after = await self.api.export_patch(env, self.baseline_path)
            proposal['decided'] = True
            decision['applied'] = action == 'adopt'
            index = len(self.records) + 1
            folder = self.directory / 'decisions' / f'{index:02d}-{agent_id}'
            self.api.save(folder / 'before.patch', before)
            self.api.save(folder / 'after.patch', after)
            self.api.save(folder / 'decision.json', decision)
            self.records.append(decision); self.persist()
            print(f'{self.directory.parent.name}: self-organizing {agent_id}: {action}', flush=True)
            await self.respond(env, request_id, {'ok': True, 'agent_id': agent_id, 'decision': action, 'applied': decision['applied']})

    async def serve(self, env, process):
        self.persist()
        while process.returncode is None:
            # Bound mailbox reads before parsing/logging; never evaluate requests
            # as shell commands or use agent text as a host path/image/config.
            result = await env.exec(['python', '-c',
                "from pathlib import Path; p=Path('/app/.codex-role-output/delegation-mailbox/request.json'); "
                "print(p.read_text() if p.is_file() and p.stat().st_size <= 524288 else '{}')"])
            if result.returncode:
                raise RuntimeError('Cannot read coordinator delegation mailbox')
            request = json.loads(result.stdout)
            if request:
                await self.dispatch(env, request)
            await asyncio.sleep(1)

    def finalize(self):
        for agent_id, proposal in self.proposals.items():
            if not proposal['decided']:
                self.records.append({'action': 'undecided', 'agent_id': agent_id,
                                     'note': 'No explicit adoption/decline. Inspect coordinator events and final patch for manual integration.'})
        self.persist()
