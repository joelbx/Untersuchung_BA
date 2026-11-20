# Checkpoint

Task: resolve duplicate loop and `delegate_to` evaluation in TaskExecutor.

Implemented:
- Passed `VariableManager` to `TaskExecutor` from worker processes.
- Resolve a task's templated delegation hostname before loop lookup and fetch its delegated host variables once.
- Added `VariableManager.get_delegated_vars_and_hostname()` and `Task.get_play()`.
- Removed delegation's loop evaluation and the `_ansible_loop_cache` workaround from `get_vars()` and TaskExecutor.
- Marked the legacy `include_delegate_to` path deprecated.

Verification: `python -m pytest -q test/units/executor/test_task_executor.py test/units/vars/test_variable_manager.py` passed (19 tests); `git diff --check` passed.
