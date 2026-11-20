# Checkpoint

Task: Fix forked `Display.display` output by queueing worker display calls for parent dispatch, add parent output locking, and flush stdout/stderr during cleanup.

Initial inspection: repository at `/app`; target files are `lib/ansible/utils/display.py`, `lib/ansible/executor/process/worker.py`, and `lib/ansible/executor/task_queue_manager.py`. `rg` is unavailable in this environment, so use `find`/`grep`.

Next: inspect existing queue lifecycle and tests, implement requested changes, run relevant existing tests.

Implementation completed:
- `Display` now owns a parent-side `threading.Lock`, forwards calls to a worker queue when configured, and rejects `set_queue` in the parent.
- `FinalQueue` transports `DisplaySend` call arguments; the strategy result thread dispatches those calls in the parent.
- Workers configure display forwarding before task execution; the late `/dev/null` stdout/stderr replacement is removed.
- TQM cleanup flushes stdout and stderr.

Verification: Python compileall and `git diff --check` pass. Focused pytest run yielded 3 passed, 7 skipped, 3 failed; warning output assertions failed in the grouped run, and the strategy failure is a pre-existing fixture/type error (`TypeError: argument of type 'type' is not iterable` while loading test play data). A separate warning test run had 1 pass and 1 failure (captured stderr empty).
