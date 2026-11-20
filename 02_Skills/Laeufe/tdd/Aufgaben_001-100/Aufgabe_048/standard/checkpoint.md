# Checkpoint

- Task: standardize plugin resolution context, errors, and deprecation formatting.
- Assigned skill: test-driven-development; test-first changes required.
- `rg` unavailable (`/bin/bash: rg: command not found`); using grep/find.

## Verification

- RED observed: `PYTHONPATH=lib pytest -q test/units/plugins/test_resolution_context.py` failed for missing `get_with_context`, `AnsiblePluginRemovedError`, and `get_deprecation_message`.
- Additional RED cases observed for removed `get_with_context` result, shared deprecation formatting, and removal date context.
- Focused check: `PYTHONPATH=lib pytest -q --reruns 0 test/units/plugins/test_resolution_context.py test/units/utils/display/test_display.py test/units/template/test_templar.py test/units/executor/test_task_executor.py test/units/plugins/action/test_action.py` passed: 81 tests, 6 pre-existing `assertRaisesRegexp` warnings.
- `PYTHONPATH=lib pytest -q` was interrupted after collection found 17 errors from integration/ansible-test fixture imports and several unrelated CLI failures; it is not a valid clean suite invocation here.
- `PYTHONPATH=lib pytest -q --reruns 0 test/units` ran to completion: 3099 passed, 22 skipped, 58 failed, 67 errors. Failures include CLI adhoc/galaxy, module_utils/basic, fact timeout, collection loader, display warning tests. Relevant focused files above pass. Exact output is in `/tmp/ansible-unit-result.log`; suite failures leave broad regression status uncertain.
