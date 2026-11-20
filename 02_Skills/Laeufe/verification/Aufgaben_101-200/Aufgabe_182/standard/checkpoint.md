# Checkpoint

Issue: forked worker Display calls need routing through the main process with method context and exact arguments.

Initial inspection: `DisplaySend` and `send_display` are in `lib/ansible/executor/task_queue_manager.py`; result handling is in `lib/ansible/plugins/strategy/__init__.py`. `rg` is unavailable (`/bin/bash: rg: command not found`), so repository searches use `grep`.

Implementation: `proxy_display` now forwards the original method name and exact arguments from child workers. `DisplaySend` retains the method name; result handling dispatches it on the main process. Added tests for argument preservation, queue transport, and main-process warning deduplication.

Verification: `PYTHONPATH=lib:test pytest -q test/units/utils/test_display.py test/units/plugins/strategy/test_display_proxy.py` returned 16 passed, 1 skipped. A broader command, `PYTHONPATH=lib:test pytest -q test/units/utils/display test/units/utils/test_display.py test/units/executor/test_task_queue_manager_callbacks.py test/units/plugins/strategy/test_display_proxy.py`, returned 2 failed, 26 passed, 1 skipped. The two failures were in `test/units/utils/display/test_warning.py` and involve reused singleton warning state. Each failing test passed when run alone with `PYTHONPATH=lib:test pytest -q test/units/utils/display/test_warning.py::test_warning` and the corresponding `::test_warning_no_color` command. The same broad command with `-k 'not test_warning'` returned 26 passed, 1 skipped, 2 deselected after the last code edit. `git diff --check` and `python -m compileall -q lib/ansible/utils/display.py lib/ansible/executor/task_queue_manager.py lib/ansible/plugins/strategy/__init__.py test/units/plugins/strategy/test_display_proxy.py` both exited 0.
