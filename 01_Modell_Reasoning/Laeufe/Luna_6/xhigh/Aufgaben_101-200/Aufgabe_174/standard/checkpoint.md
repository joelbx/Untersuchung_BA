# Checkpoint

Issue: route `Display.display` calls from forked workers through a final/results queue to the parent, serialize parent output with a lock, drain display events in the strategy results loop, and flush stdout/stderr during task queue cleanup.

Initial inspection: repository is `/app`; `rg` is unavailable, so use `find` and standard shell tools. Next: inspect repository guidance and relevant implementation/tests, then patch and run the existing focused tests.

Implementation complete:
- `Display` now keeps a parent output lock and worker queue reference, rejects `set_queue` in the creating process, forwards display arguments from workers, and serializes parent output.
- `FinalQueue.send_display` enqueues `DisplaySend` records nonblocking; the strategy results thread dispatches them through the parent `Display`.
- Workers install the display queue before task execution; the late `/dev/null` stdout/stderr redirection was removed.
- `TaskQueueManager.cleanup` flushes stdout and stderr before process shutdown.

Verification: `python -m pytest -q test/units/utils/display/test_display.py test/units/utils/test_display.py test/units/executor/test_task_queue_manager_callbacks.py` — 5 passed, 2 skipped. `git diff --check` clean.
