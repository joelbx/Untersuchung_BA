# Checkpoint

Task: Resolve duplicate loop and delegation evaluation in TaskExecutor.
Status: patch complete; focused and adjacent tests pass.

Changes:
- Worker passes VariableManager into TaskExecutor; executor resolves delegation before loop evaluation.
- VariableManager exposes get_delegated_vars_and_hostname and no longer resolves delegation in get_vars by default.
- Task.get_play traverses parent blocks; removed loop cache and legacy duplicate loop calculation.
- Legacy _get_delegated_vars is marked deprecated.

Verification:
- RED: `PYTHONPATH=lib:test python -m pytest -q test/units/executor/test_task_executor.py -k 'delegation_is_resolved_before_loop_once or task_get_play_through_nested_blocks' test/units/vars/test_variable_manager.py -k 'delegated_vars_and_hostname_do_not_evaluate_loop or delegation_is_resolved_before_loop_once or task_get_play_through_nested_blocks'` failed on the three missing interfaces.
- GREEN: `PYTHONPATH=lib:test python -m pytest -q test/units/executor test/units/vars test/units/playbook/test_task.py test/units/playbook/test_block.py`: 113 passed, 1 skipped, 8 warnings.
- `git diff --check`: passed.
- Broad suite command: `PYTHONPATH=lib:test python -m pytest -q test/units`. Stopped after 36 failures and 27 errors, 64 passed. Failures in `test/units/cli/test_adhoc.py` and `test/units/cli/test_cli.py` include missing CLI argument keys (`module_name`, `args`); `test/units/cli/test_galaxy.py` setup errors on `os.path.join(..., None)` for `type`. The broad suite was interrupted after repeated unrelated CLI failures, so its full status remains unknown.

Tooling: `rg` unavailable (`/bin/bash: rg: command not found`); used grep/find. No downloads or external research.
