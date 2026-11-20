VERDICT: FIX

**Code defect:** [TaskExecutor.run()](/app/lib/ansible/executor/task_executor.py:112) resolves `delegate_to` before evaluating `when`. A task with `delegate_to: '{{ missing_delegate }}'` and `when: false` fails on the undefined variable instead of skipping. Preserve conditional skip behavior while resolving delegation once before loop execution.

**Relevant tests run:**

- `PYTHONPATH=lib:test python -m pytest -q test/units/executor/test_task_executor.py test/units/vars/test_variable_manager.py` — 23 passed.
- `PYTHONPATH=lib python bin/ansible-playbook -i localhost, -c local test/integration/targets/delegate_to/test_delegate_to_loop_randomness.yml` — passed.
- `PYTHONPATH=lib python bin/ansible-playbook -i localhost, -c local test/integration/targets/delegate_to/test_loop_control.yml` — failed: the registered item lacks `_ansible_delegated_vars`. Its relationship to this patch remains unconfirmed; investigate the per-item result and registration path.
- A `/dev/stdin` playbook with undefined `delegate_to` and `when: false` — failed instead of skipping, confirming the defect above.

**TEST_ENVIRONMENT_PROBLEM:** None observed. No project code or tests were changed; the review record is in [checkpoint.md](/app/.codex-role-output/checkpoint.md).