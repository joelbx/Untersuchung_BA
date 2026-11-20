# Checkpoint

Issue: honor module-declared interpreters and shebang arguments in new-style module processing while preserving explicit overrides and encoding-marker placement.

Implemented in `lib/ansible/executor/module_common.py`:
- Added `_extract_interpreter` using `shlex.split`, returning `(None, [])` without a shebang.
- Made `_get_shebang` always return a complete `#!` line and interpreter, preserving/quoting args and routing versioned/env Python shebangs through the Python override.
- New-style Python wrappers now resolve from the source shebang when present and fall back to Python interpreter discovery/config only when absent.
- `modify_module` only replaces a shebang when the resolved interpreter differs, and places the encoding marker directly after an existing shebang.

Added focused unit coverage in `test/units/executor/module_common/test_module_common.py`.

Verification: `python -m pytest -q test/units/executor/module_common/test_module_common.py test/units/executor/module_common/test_modify_module.py` passed (43 tests); `git diff --check` passed.
