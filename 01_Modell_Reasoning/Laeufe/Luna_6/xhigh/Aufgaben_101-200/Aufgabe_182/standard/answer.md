Implemented worker display proxying. `display`, `warning`, and `deprecated` now send their method name and caller supplied arguments through the queue; the result thread dispatches to the matching method in the main process, where deduplication applies.

Updated the existing fork display assertion for the new queue call shape.

Verification: **10 passed, 1 skipped** across the focused display and task queue manager tests. `git diff --check` passed.

Key changes: [display.py](/app/lib/ansible/utils/display.py:256), [task_queue_manager.py](/app/lib/ansible/executor/task_queue_manager.py:63), [strategy/__init__.py](/app/lib/ansible/plugins/strategy/__init__.py:113).