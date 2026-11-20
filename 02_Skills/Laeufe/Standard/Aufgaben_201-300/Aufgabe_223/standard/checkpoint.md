# Checkpoint

Resolved: new-style Python wrappers use the module's declared interpreter and arguments. An explicit inventory or configuration override takes precedence; absent a shebang, `/usr/bin/python` is used. `_get_shebang` always returns a complete shebang and interpreter, `_extract_interpreter` parses with `shlex.split`, and `modify_module` changes a shebang only when the interpreter changes. Existing argument text is preserved on replacement, and the encoding line follows the shebang.

Files changed: `lib/ansible/executor/module_common.py`, `test/units/executor/module_common/test_module_common.py`, `test/units/executor/module_common/test_modify_module.py`.

Validation: `python -m pytest -q test/units/executor/module_common` passed (64 tests). The suite emitted one pre-existing `ZipFile.__del__` unraisable-exception warning from `test_recursive_finder.py`. `git diff --check` passed.

Tooling note: `rg` was unavailable (`/bin/bash: rg: command not found`), so local `grep` and `find` were used. No check remains blocked.
