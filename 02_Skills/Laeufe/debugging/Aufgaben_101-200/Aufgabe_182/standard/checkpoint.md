# Checkpoint

Task: Route forked `Display` calls through the main process for global deduplication.

## Investigation

`rg` is unavailable (`/bin/bash: rg: command not found`); local searches used `grep` and `find`.

Root cause: `Display.display` sent only rendered display arguments to the final queue, while `warning` and `deprecated` ran their formatting and deduplication in each worker before calling `display`. `DisplaySend` carried no method name and `results_thread_main` dispatched every message to `display.display`. Thus the main process never ran its shared warning or deprecation deduplication logic.

Working pattern: `CallbackSend` carries a method name and its receiver dispatches using that method name.

Hypothesis: Forwarding the original Display method name and exact caller arguments, then dispatching that method in the main process, will centralize deduplication. The new regressions failed before the fix: forked display sent synthesized defaults, `DisplaySend.method` was absent, and the results thread emitted four messages instead of two.

## Patch and checks

Added `proxy_display` to `display`, `warning`, and `deprecated`; added `method` to `DisplaySend` and `FinalQueue.send_display`; dispatch now uses `getattr(display, result.method)`.

Executed: `PYTHONPATH=lib:test python -m pytest -q --reruns 0 test/units/utils/test_display.py test/units/utils/display/test_display.py test/units/plugins/strategy/test_display_proxy.py` — 16 passed, 1 skipped.

Executed: `git diff --check` — passed.

Next: Run broader relevant queue and display tests; review final diff.

## Final verification

Executed: `PYTHONPATH=lib:test python -m pytest -q --reruns 0 test/units/utils/test_display.py test/units/utils/display/test_display.py test/units/executor/test_task_queue_manager_callbacks.py test/units/plugins/strategy/test_display_proxy.py test/units/plugins/strategy/test_linear.py` — 21 passed, 1 skipped.

Executed: `git diff --check` — passed.

A broader combined run (`PYTHONPATH=lib:test python -m pytest -q --reruns 0 test/units/utils/display test/units/utils/test_display.py test/units/executor/test_task_queue_manager_callbacks.py test/units/plugins/strategy/test_display_proxy.py test/units/plugins/strategy/test_linear.py`) had 4 failures, 25 passed, 1 skipped. `test_warning.py::test_warning_no_color` failed because the preceding warning test left the identical message in Display's singleton `_warns` cache; each warning test passed independently. In that combined run, `test_warning` also lacked expected color after `test_logger.py` removed Ansible modules from `sys.modules`. Two linear strategy tests failed at `playbook/task.py:193` with `TypeError: argument of type 'type' is not iterable`; the same tests passed independently and in the final focused combined run. These are collection/order dependent test interactions; no remaining failure reproduced in the focused checks.
