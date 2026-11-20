# Checkpoint

Issue: Route `Display.display`, `warning`, and `deprecated` calls from forked workers through the main-process queue while preserving method identity and exact caller arguments, so main-process deduplication applies.

Implemented:
- Added `proxy_display` and decorated the three display methods. Forked calls send the method name and only the caller-supplied positional and keyword arguments.
- Added the method field to `DisplaySend`; `FinalQueue.send_display` accepts it first and the results thread dispatches with `getattr`.
- Updated display proxy tests to cover display, warning, and deprecated calls.

Verification:
- `pytest -q test/units/utils/test_display.py test/units/utils/display/test_display.py test/units/executor/test_task_queue_manager_callbacks.py`: 13 passed, 1 skipped.
- `pytest -q test/units/utils/display/test_warning.py`: 1 passed, 1 failed. `test_warning_no_color` observes no output because `Display` is a singleton and the prior test has already recorded the same warning; this reproduces when that test file runs alone.
- `git diff --check`: passed.
