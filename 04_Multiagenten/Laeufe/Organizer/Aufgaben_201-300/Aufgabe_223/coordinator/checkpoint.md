Task: fix module shebang handling in /app.
Status: implementation and focused verification complete.
Changes: extract module interpreter and args with shlex; preserve declared new-style Python shebangs; use configured overrides when supplied; preserve original argument text when replacing only the interpreter; insert encoding immediately after shebang; use /usr/bin/python for new-style modules without shebangs.
Verification: python -m pytest -q test/units/executor/module_common/test_module_common.py test/units/executor/module_common/test_modify_module.py (49 passed); git diff --check passed.
Delegation: none.
