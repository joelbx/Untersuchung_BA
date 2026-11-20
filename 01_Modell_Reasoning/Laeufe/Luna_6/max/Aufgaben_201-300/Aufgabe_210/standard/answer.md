Implemented the delegation and loop execution changes.

- [TaskExecutor](/app/lib/ansible/executor/task_executor.py:110) resolves delegation before evaluating loop items and receives the variable manager from [WorkerProcess](/app/lib/ansible/executor/process/worker.py:188).
- [VariableManager](/app/lib/ansible/vars/manager.py:514) now exposes `get_delegated_vars_and_hostname`; the old loop cache is removed, and the legacy helper is deprecated.
- [Task](/app/lib/ansible/playbook/task.py:119) now provides `get_play()` by traversing its parent hierarchy.

Verification: 33 existing executor, variable manager, and task unit tests passed. `git diff --check` passed.