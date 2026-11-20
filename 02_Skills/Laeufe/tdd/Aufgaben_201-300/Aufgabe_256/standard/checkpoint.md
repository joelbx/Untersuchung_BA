# Checkpoint

Task: Fix invalid `hosts` values in `Play` so they raise parser errors and derive play names dynamically.

Implemented in `lib/ansible/playbook/play.py`: `Play.load` no longer derives or mutates `name`; `get_name` derives from hosts; `_validate_hosts` checks only when the source dataset contains `hosts`, including empty, None, non-string sequence members, and non-string/non-sequence values. This checkout provides `is_sequence` in `ansible.module_utils.common.collections`; there is no `ansible.utils.collection_loader.is_sequence` here.

Added regression tests in `test/units/playbook/test_play.py`. Before implementation, focused pytest reported 4 failing tests for input mutation, binary hosts, tuple hosts, and invalid-host errors. After implementation, `PYTHONPATH=lib:test python -m pytest -q test/units/playbook/test_play.py` passed: 15 tests, 1 pre-existing deprecation warning. `PYTHONPATH=lib:test python -m pytest -q test/units/playbook` passed: 249 tests, 16 deprecation warnings. `git diff --check` passed.

Repository-wide check attempted: `PYTHONPATH=lib:test python -m pytest -q`. It collected 3555 items with 20 collection errors and accumulated unrelated integration/CLI failures and errors, then was interrupted to avoid continuing fixture tests. At interruption: 37 failed, 64 passed, 56 errors, 222 reruns. Examples: `test/ansible_test/unit/test_diff.py` failed to import `to_text` from installed `ansible_test._internal.util`; `test/integration/targets/ansible-test/.../test_constraints.py` lacked `botocore`; integration module fixtures exited while trying to parse empty JSON stdin. The full suite did not pass; remaining unrelated coverage is uncertain.
