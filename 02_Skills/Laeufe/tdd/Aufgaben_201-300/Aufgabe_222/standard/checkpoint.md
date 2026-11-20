# Checkpoint

Task: Extract `RoleMixin._build_doc` for role entry-point documentation.
Status: Implemented and verified the extracted method and its caller.

TDD: Added `test_build_role_doc_returns_full_selected_entry_specs` first. `PYTHONPATH=lib pytest -q test/units/cli/test_doc.py -k build_role_doc` failed as expected with `AttributeError: 'RoleMixin' object has no attribute '_build_doc'`. After implementation, `PYTHONPATH=lib pytest -q test/units/cli/test_doc.py -k build_role_doc -o reruns=0` passed (4 cases).

Checks:
- `PYTHONPATH=lib pytest -q test/units/cli/test_doc.py -o reruns=0`: 18 passed.
- `PYTHONPATH=lib timeout 120 pytest -q -o reruns=0`: timed out with exit 124 at about 30%; collection reported 19 errors and numerous unrelated test failures/errors, so the full suite result is unknown. The configured rerun plugin still reran failed tests.
- `PYTHONPATH=lib pytest -q -x --reruns 0 test/units/cli/test_adhoc.py`: 2 passed, then `test_simple_command` failed with `AnsibleOptionsError: No argument passed to command module` at `lib/ansible/cli/adhoc.py:120`.
- `git diff --check`: passed.
