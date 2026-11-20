Issue: preserve module-declared shebang interpreter and arguments, with explicit overrides taking precedence.
Status: implemented in module_common.py. Both new-style wrappers and other text modules extract their shebang; they retain it when the resolved interpreter matches, and use /usr/bin/python when no shebang exists. UTF-8 coding line follows the shebang.
Verification: PYTHONPATH=lib:test/units/executor/module_common python -m pytest -q test/units/executor/module_common (62 passed; one ZipFile destructor warning). git diff --check passed.
