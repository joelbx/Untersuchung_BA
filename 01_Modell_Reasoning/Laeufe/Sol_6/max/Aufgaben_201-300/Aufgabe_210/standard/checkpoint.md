# Checkpoint

Task: resolve duplicate loop and delegation evaluation in TaskExecutor.

Initial state: repository at /app; investigation in progress. `rg` is unavailable, so repository searches use `grep`.

Finding: `VariableManager.get_vars()` currently resolves delegation by evaluating loop items; `TaskExecutor._get_loop_items()` then evaluates them again. `WorkerProcess` already holds a variable manager, and existing integration cases require delegation based on each loop item.

Implemented: TaskExecutor now receives VariableManager from WorkerProcess. For loops, it resolves targets independent of the item once before task iterations and resolves item-dependent targets once per item before play context setup. VariableManager exposes `get_delegated_vars_and_hostname`; `get_vars` defaults to no delegation and the legacy delegation method is deprecated. Task exposes `get_play`. Removed the loop evaluation cache path.

Verification: 37 relevant unit tests pass, including new counters for single loop and delegation evaluation. Existing delegation playbooks pass for random loop targets, loop caching, delegated facts, variable resolution, and lookup context. `git diff --check` passes.
