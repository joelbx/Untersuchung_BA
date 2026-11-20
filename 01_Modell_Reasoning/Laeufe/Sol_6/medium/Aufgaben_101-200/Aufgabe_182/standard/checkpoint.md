# Checkpoint

Issue resolved: `Display.display`, `warning`, and `deprecated` proxy from workers with the original method name and exactly the supplied arguments. `DisplaySend` retains the method; the results thread invokes it on the main-process Display, which owns the warning and deprecation caches.

Changed files: `lib/ansible/utils/display.py`, `lib/ansible/executor/task_queue_manager.py`, `lib/ansible/plugins/strategy/__init__.py`, and relevant unit tests.

Verification: 20 passed, 1 skipped in the display/queue tests; 8 passed in the other display tests; `git diff --check` passed. Running all together encounters an existing module reload interaction in `test_logger.py` that changes color module identity for later tests.
