# Checkpoint

Issue: avoid calculating loop expressions and `delegate_to` more than once in task execution.

Implemented: TaskExecutor now resolves delegation through VariableManager before evaluating loop items; VariableManager exposes `get_delegated_vars_and_hostname`, and `Task.get_play()` finds the containing play. Removed the loop evaluation cache and deprecated the legacy delegation helper.

Verification: existing executor, variable manager, and task unit suites passed (33 tests). `git diff --check` passed.

Constraints followed: repository code and existing tests only; no history, index baseline, or harness configuration changes.
