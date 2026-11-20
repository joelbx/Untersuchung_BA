# Checkpoint

Task: route forked worker display messages to the parent through the final results queue, remove shutdown output workaround, and verify relevant tests.

Status: implementation and focused verification complete. `rg` is unavailable locally; used `grep`/`find` for repository searches.

Root cause: `WorkerProcess` inherits the singleton `Display`, whose `display()` writes directly to inherited stdout/stderr. Unlike callbacks and task results, display calls have no event path through `FinalQueue`; `WorkerProcess.run()` redirects streams in `finally` to avoid a shutdown flush deadlock. The strategy results thread already drains a queue to a sentinel, so it is the dispatch point for display events.

Working pattern: `CallbackSend` holds `args`/`kwargs`; `FinalQueue.send_callback()` enqueues with `block=False`; `results_thread_main()` dispatches by item type. Proposed hypothesis: add analogous display events, set the queue at worker startup, and dispatch in the parent; then inherited stream writes and the redirect become unnecessary.

Red test: `PYTHONPATH=lib:test python -m pytest -q test/units/executor/test_forked_display.py` failed at collection because `DisplaySend` did not exist. First post-patch run found a recursion error in the new test's patched `os.getpid`; corrected the fixture. Also found a shutdown ordering gap: the strategy sentinel was enqueued before workers had exited, so their last display events could arrive after it. Worker cleanup now precedes strategy cleanup and sentinel insertion.

Verification: `PYTHONPATH=lib:test python -m pytest -q test/units/executor/test_forked_display.py test/units/utils/display/test_display.py test/units/executor/test_task_queue_manager_callbacks.py test/units/utils/test_display.py` exited 0 with 11 passed, 2 skipped. The new tests cover parent guard, worker queue setup, event payload and nonblocking enqueue, results-thread dispatch, stream flushes, and a real fork that sends a display event while the parent display lock is held. `git diff --check` exited 0.
