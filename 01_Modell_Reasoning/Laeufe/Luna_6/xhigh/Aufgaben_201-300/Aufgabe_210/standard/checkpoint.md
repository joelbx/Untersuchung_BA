# Checkpoint

Task: resolve duplicate loop and `delegate_to` calculation in TaskExecutor.

Implemented:
- Pass `VariableManager` into `TaskExecutor` and resolve delegation before loop action execution.
- Add `Task.get_play()` to find the containing play through parent blocks.
- Add `VariableManager.get_delegated_vars_and_hostname()` and stop resolving delegation inside `get_vars()`.
- Deprecate the former private delegation resolver and remove the `_ansible_loop_cache` workaround.

Verification: the executor, variable manager, and task unit suites passed on Python 3.9 (33 tests); `git diff --check` passed. An initial unpinned test run also attempted Python 3.11, where pytest is unavailable, so the successful final run was pinned to Python 3.9.
