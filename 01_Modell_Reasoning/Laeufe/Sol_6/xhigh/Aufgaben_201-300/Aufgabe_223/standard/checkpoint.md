# Checkpoint

Issue: Preserve module-declared shebang interpreters and arguments in new-style Python modules, with explicit overrides taking precedence.

Status: Complete.

Changed `lib/ansible/executor/module_common.py` to parse source shebangs, resolve configured overrides, preserve original shebang text unless the interpreter changes, and place the encoding declaration immediately after the shebang. Added regression coverage in the two module_common unit test files for Python, env Python, Ruby, interpreter arguments, explicit overrides, and missing shebangs.

Verification: `python -m pytest -q test/units/executor/module_common test/units/plugins/action/test_action.py` — 84 passed (one pre-existing ZipFile cleanup warning). `git diff --check` passed.
