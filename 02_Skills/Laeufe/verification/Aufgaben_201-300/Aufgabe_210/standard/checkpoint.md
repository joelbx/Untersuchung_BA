# Task checkpoint

Issue: resolve task delegation before loops and avoid repeated loop and delegation evaluation.

Status: implementation and focused verification complete. `rg` is unavailable in this environment; used local `grep`/`find`.

Changes: TaskExecutor receives the variable manager, evaluates loop items once, and resolves each item's delegation before executing the loop. VariableManager exposes `get_delegated_vars_and_hostname`; `get_vars` no longer resolves delegation by default, and its legacy path is deprecated. Task exposes `get_play`. Removed `_ansible_loop_cache`.

Verification:
- `python -m pytest -q test/units/executor/test_task_executor.py test/units/vars/test_variable_manager.py test/units/playbook/test_task.py`: 35 passed.
- `PYTHONPATH=lib bin/ansible-playbook -i localhost, -c local test/integration/targets/delegate_to/test_delegate_to_loop_randomness.yml`: exit 0, 11 tasks passed, no failures.
- `PYTHONPATH=lib bin/ansible-playbook -i localhost, -c local test/integration/targets/delegate_to/test_loop_control.yml`: exit 2. The final assertion fails because registered `out.results[0]` lacks `_ansible_delegated_vars`. The executor does populate that internal field, but `TaskResult.clean_copy` strips internal fields and preserves only selected connection fields; the test's assertion requires `ansible_delegated_host`, which is absent from its `_SUB_PRESERVE` list. This appears separate from delegation resolution. Baseline status of this playbook was not verified.
