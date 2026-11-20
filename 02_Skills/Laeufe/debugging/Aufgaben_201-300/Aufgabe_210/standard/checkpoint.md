# Checkpoint

Investigating duplicate loop and delegation evaluation. `rg` is unavailable; using local `grep`/`sed`.

Phase 1: pending reproduction and call-flow trace.

## Root cause and hypothesis
`get_vars()` calls `_get_delegated_vars()`, which evaluates the loop and templates delegation per item before execution. `TaskExecutor.run()` separately evaluates the same loop, with `_ansible_loop_cache` as a partial workaround. Worker already owns the variable manager but does not pass it to TaskExecutor. Hypothesis: move single delegation lookup to TaskExecutor before `_get_loop_items()`, then remove delegation from normal `get_vars()` and the cache.

## Failing reproduction
`PYTHONPATH=lib:test python -m pytest -q test/units/executor/test_task_executor.py -k delegation_is_resolved_before_loop_items` fails with `TypeError: __init__() got an unexpected keyword argument 'variable_manager'` (exit 1). This establishes the missing executor interface before the fix.

## Implementation and verification
TaskExecutor now receives VariableManager from WorkerProcess, resolves fixed delegation before loop evaluation, evaluates loop items once, and resolves item dependent delegation from those same items before executing iterations. Task.get_play traverses parent objects to the containing Block. Normal get_vars no longer resolves delegation by default. The old private delegation method is explicitly deprecated and no longer evaluates loops or writes `_ansible_loop_cache`.

Checks passed:
- `PYTHONPATH=lib:test python -m pytest -q test/units/executor/test_task_executor.py test/units/vars/test_variable_manager.py` (22 passed, exit 0)
- `PYTHONPATH=/app/lib /app/bin/ansible-playbook test_delegate_to_loop_randomness.yml -i inventory` (exit 0)
- `PYTHONPATH=/app/lib /app/bin/ansible-playbook test_delegate_to_loop_caching.yml -i inventory` (exit 0)
- `PYTHONPATH=/app/lib /app/bin/ansible-playbook delegate_facts_loop.yml -i inventory` (exit 0)

`test_loop_control.yml` fails (exit 2) because its assertion expects `_ansible_delegated_vars` in the registered loop result. The target's `runme.sh` explicitly excludes this test, noting it relies on a variable that should not be available. This is a known excluded check; its failure does not establish a regression here.
- `PYTHONPATH=/app/lib /app/bin/ansible-playbook test_delegate_to_lookup_context.yml -i inventory` (exit 0)
- `git diff --check` (exit 0)
