Implemented worker display forwarding through the shared results queue. Parent display writes are serialized with a lock, the strategy dispatches queued messages, and workers no longer redirect stdout/stderr to `/dev/null` at shutdown. Task queue cleanup now flushes both streams.

Relevant changes: [display.py](/app/lib/ansible/utils/display.py:205), [task_queue_manager.py](/app/lib/ansible/executor/task_queue_manager.py:55), [strategy](/app/lib/ansible/plugins/strategy/__init__.py:113), [worker.py](/app/lib/ansible/executor/process/worker.py:119).

Verification: focused tests passed (5 passed, 2 skipped); `git diff --check` is clean.