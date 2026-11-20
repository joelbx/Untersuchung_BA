#!/usr/bin/env python3
"""Launch the unchanged skills runner, with bounded pre-model recovery and logs."""
import argparse
from collections import deque
from datetime import datetime, timezone
import fcntl
import json
from pathlib import Path
import subprocess
import sys
import time
import uuid

from run_skills import EXCLUSIONS

LAB = Path(__file__).resolve().parent


def read(path):
    return json.loads(path.read_text()) if path.exists() else {}


class Night:
    def __init__(self, block, *, lab=LAB, control_attempts=3, prepare_attempts=2,
                 delay=30, model_workers=5, control_workers=2, execute=None, sleep=time.sleep):
        self.lab = Path(lab)
        self.block = block
        self.batch = 'batch-' + block
        self.tasks = f'{(int(block)-1)*100+1}-{int(block)*100}'
        self.root = self.lab / 'experiment-skills-sol6-medium' / self.batch
        self.controls = self.lab / 'experiment-skills-sol6-medium-controls' / self.batch
        self.control_attempts = control_attempts
        self.prepare_attempts = prepare_attempts
        self.delay = delay
        self.model_workers = model_workers
        self.control_workers = control_workers
        self.execute = execute or self.command
        self.sleep = sleep
        self.log_root = None
        self.history = []

    def record(self, phase, **values):
        row = {'at': datetime.now(timezone.utc).isoformat(), 'phase': phase, **values}
        self.history.append(row)
        if self.log_root:
            p = self.log_root / 'state.json'
            temporary = p.with_suffix('.tmp')
            temporary.write_text(json.dumps({'batch': self.batch, 'history': self.history}, indent=2) + '\n')
            temporary.replace(p)

    def command(self, phase, repair=False):
        argv = [sys.executable, '-u', str(self.lab / 'run_skills.py'), phase,
                '--batch', self.batch, '--tasks', self.tasks,
                '--model-workers', str(self.model_workers),
                '--control-workers', str(self.control_workers)]
        if repair:
            argv.append('--repair-controls')
        self.record(phase, event='starting', command=argv)
        print(f'\nNIGHT: {phase}' + (' --repair-controls' if repair else ''), flush=True)
        tail = deque(maxlen=120)
        log = self.log_root / f'{len(self.history):03d}-{phase}.log'
        with log.open('w') as output:
            with subprocess.Popen(argv, cwd=self.lab, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                                  text=True, bufsize=1) as process:
                for line in process.stdout:
                    output.write(line);output.flush()
                    print(line, end='', flush=True)
                    tail.append(line)
                code = process.wait()
        self.record(phase, event='finished', exit_code=code, log=str(log))
        return code, ''.join(tail)

    def control_state(self):
        """Never retry a demonstrated, unapproved functional control failure."""
        m = read(self.controls / 'manifest.json')
        if m.get('execution_started_at'):
            return 'blocked', 'Control donor unexpectedly contains model starts'
        for p in sorted(self.controls.glob('task-*/controls.json')):
            n = int(p.parent.name[5:]);c = read(p)
            if c.get('passed') or n in EXCLUSIONS:
                continue
            original = read(p.parent / 'controls-original/evaluation.json')
            reference = read(p.parent / 'controls-reference/evaluation.json')
            # Completed=False/error is an evaluator interruption, rather than
            # a completed reference that simply fails required assertions.
            interrupted = any(e and (not e.get('completed') or e.get('error'))
                              for e in (original, reference))
            if not interrupted:
                return 'blocked', f'Task {n}: failed control needs inspection; no automatic exclusion or repetition'
        if m.get('status') in ('controls_passed', 'completed'):
            return 'ready', 'Validated controls recorded'
        for p in sorted(self.controls.glob('task-*/controls.json')):
            n = int(p.parent.name[5:])
            if n in EXCLUSIONS and not read(p).get('passed') and n not in m.get('control_exclusions', []):
                return 'finalize_exclusions', 'Apply only previously approved exclusions; no replacement tasks'
        return 'retry', 'Incomplete preparation, technical control interruption or child-process crash'

    @staticmethod
    def permanent_error(text):
        return any(s in text for s in ('Versioned sources changed', 'Frozen source/runtime changed',
                   'Frozen source/runtime', 'Study batch already frozen', 'Dataset hash mismatch',
                   'Task selection/worker count differs', 'Another coordinator is already running',
                   'BlockingIOError:', 'Control execution policy is frozen'))

    def run(self):
        m = read(self.root / 'manifest.json')
        if m.get('status') == 'completed':
            print('NIGHT: Batch already completed; no trials repeated.', flush=True)
            self.record('done', status='already_completed')
            return 0
        if m.get('execution_started_at') or m.get('status') in ('running', 'paused', 'technical_interruption'):
            raise RuntimeError(f'Model batch already started. Inspect it, then explicitly use: bash run_skills_batch.sh {self.block} resume')
        if not m:
            failures = 0
            finalizations = 0
            while True:
                state, reason = self.control_state()
                if state == 'ready':
                    print('NIGHT: Controls validated; continue to prepare.', flush=True)
                    break
                if state == 'blocked':
                    raise RuntimeError(reason)
                repair = (self.controls / 'manifest.json').exists()
                code, tail = self.execute('controls', repair)
                state, reason = self.control_state()
                self.record('control_decision', exit_code=code, decision=state, reason=reason)
                if code == 0 and state == 'ready':
                    break
                if state == 'blocked' or self.permanent_error(tail):
                    raise RuntimeError(reason + '\n' + tail[-1800:])
                if code in (130, -2):
                    raise RuntimeError('Control process explicitly interrupted; not restarting automatically')
                if state == 'finalize_exclusions' and finalizations == 0:
                    finalizations += 1
                    print('NIGHT: Finalizing existing approved exclusions with --repair-controls.', flush=True)
                    continue
                failures += 1
                if failures >= self.control_attempts:
                    raise RuntimeError(f'Controls still not validated after {failures} unsuccessful attempts. Models NOT started.\n' + tail[-1800:])
                print(f'NIGHT: Technical preparation incomplete. Retry {failures+1}/{self.control_attempts} in {self.delay}s.', flush=True)
                self.sleep(self.delay)
            for attempt in range(self.prepare_attempts):
                code, tail = self.execute('prepare')
                if code == 0:
                    break
                if self.permanent_error(tail) or code in (130, -2) or attempt + 1 == self.prepare_attempts:
                    raise RuntimeError('Prepare failed. Models NOT started.\n' + tail[-1800:])
                self.sleep(self.delay)
        else:
            print('NIGHT: Prepared batch exists; retain frozen controls and preparation.', flush=True)
        code, tail = self.execute('check')
        if code:
            raise RuntimeError('Check failed. Models NOT started.\n' + tail[-1800:])
        code, tail = self.execute('models')
        if code:
            raise RuntimeError(f'Model phase interrupted; no automatic model repeat. Inspect logs, then use: bash run_skills_batch.sh {self.block} resume\n' + tail[-1800:])
        if read(self.root / 'manifest.json').get('status') != 'completed':
            raise RuntimeError('Model command returned but the batch is not completed; inspect the manifest')
        self.record('done', status='completed')
        print('NIGHT: Batch completed.', flush=True)
        return 0


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--block', choices=('01', '02', '03'), default='03')
    p.add_argument('--run', action='store_true', help='Actually execute controls and models; otherwise show plan only')
    p.add_argument('--control-attempts', type=int, default=3)
    p.add_argument('--prepare-attempts', type=int, default=2)
    p.add_argument('--retry-delay', type=int, default=30)
    p.add_argument('--model-workers', type=int, choices=range(1, 6), default=5)
    p.add_argument('--control-workers', type=int, default=2)
    a = p.parse_args(argv)
    if min(a.control_attempts, a.prepare_attempts, a.control_workers) < 1 or a.retry_delay < 0:
        p.error('Attempts/workers must be positive; delay must be nonnegative')
    night = Night(a.block, control_attempts=a.control_attempts, prepare_attempts=a.prepare_attempts,
                  delay=a.retry_delay, model_workers=a.model_workers, control_workers=a.control_workers)
    if not a.run:
        print(f'Plan only: block {a.block}, tasks {night.tasks}; up to {a.control_attempts} technical control attempts '
              f'+ one finalization of existing exclusions, {a.prepare_attempts} prepare attempts, check, models once. Add --run to execute.')
        return 0
    base = LAB / 'validation/skills-overnight';base.mkdir(exist_ok=True)
    with (base / f'batch-{a.block}.lock').open('a') as lock:
        fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        night.log_root = base / (datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ') + '-' + a.block + '-' + uuid.uuid4().hex[:6])
        night.log_root.mkdir()
        print('NIGHT logs: ' + str(night.log_root), flush=True)
        try:
            return night.run()
        except KeyboardInterrupt:
            night.record('stopped', status='cancelled')
            return 130
        except Exception as error:
            night.record('stopped', status='failed', reason=str(error))
            print('\nNIGHT STOPPED: ' + str(error) + '\nLogs: ' + str(night.log_root), file=sys.stderr, flush=True)
            return 2


if __name__ == '__main__':
    raise SystemExit(main())
