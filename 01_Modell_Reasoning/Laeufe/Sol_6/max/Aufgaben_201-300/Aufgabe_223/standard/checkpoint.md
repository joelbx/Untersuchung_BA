# Shebang resolution checkpoint

- Task: preserve module-declared interpreters and arguments while retaining explicit Ansible overrides.
- Found: `_find_module_utils` hardcodes `/usr/bin/python` for new-style Python wrappers; `modify_module` only parses source shebangs in the older path.
- Implemented: source shebang parsing, declared interpreter selection for new-style wrappers, explicit override precedence, exact source argument preservation on rewrites, and coding line placement.
- Verified: `PYTHONPATH=lib:test/units/executor/module_common python -m pytest -q test/units/executor/module_common` passed (73 tests); `git diff --check` passed.
