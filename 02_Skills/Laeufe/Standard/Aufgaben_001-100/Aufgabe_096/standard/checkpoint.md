# Checkpoint

Task: secure newly created files in `atomic_move()` and warn when a module accepts `mode` but omits it.

Status: patch complete. `rg` is unavailable (`/bin/bash: rg: command not found`); used `grep` for local inspection.

Changes: set `_DEFAULT_PERM` to `0o0600`; new destinations receive `DEFAULT_PERM & ~umask`. Added per-module created-file tracking and exact warnings during result formatting, with tracking cleared when a mode is supplied to `set_mode_if_different()`.

Checks: `PYTHONPATH=lib python -m pytest -q test/units/module_utils/basic/test_atomic_move.py test/units/module_utils/basic/test_set_mode_if_different.py` passed (47 tests). `git diff --check` passed.
