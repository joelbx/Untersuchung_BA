# Checkpoint

Task: fix `lib/ansible/modules/async_wrapper.py` exit responses, atomic job records, lifecycle state, timeout diagnostics, and cleanup behavior.

Status: complete. `end` centralizes JSON exits; `jwrite` atomically replaces job records. Startup, completion, timeout, fork, setup, and execution failures now carry consistent status and job identifiers. Cleanup policy is included in immediate responses and applied on terminal paths.

Verification: `python -m pytest -q test/units/modules/test_async_wrapper.py` (9 passed), `python -m py_compile lib/ansible/modules/async_wrapper.py`, and `git diff --check` passed. The tests include real async normal and timeout executions.
