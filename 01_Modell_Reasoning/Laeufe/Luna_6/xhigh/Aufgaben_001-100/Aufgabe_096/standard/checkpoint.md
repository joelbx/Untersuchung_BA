# Checkpoint

Task: resolve atomic_move default-permission behavior and warnings in the checked-out Ansible repository.

Plan: inspect repository guidance and the relevant implementation/tests; update atomic_move permission calculation and created-file tracking; clear tracking when a mode is subsequently set; issue warnings during result formatting; run relevant existing tests.

Constraints: use local repository code and tests only; do not change git history, index baseline, or harness configuration.

Implementation complete:
- Changed `_DEFAULT_PERM` to `0o0600`; `atomic_move()` continues applying it through the current umask.
- Added per-module `_created_files` tracking for new files when `mode` is accepted and unset; explicit later mode handling clears tracked paths.
- Added `add_atomic_move_warnings()` and invoked it from result formatting with the required warning text.
- Added or updated unit coverage for restrictive permissions, tracking and clearing, warning formatting, and existing-file mode preservation.

Verification: `PYTHONPATH=lib python -m pytest -q test/units/module_utils/basic/test_atomic_move.py test/units/module_utils/basic/test_set_mode_if_different.py test/units/module_utils/basic/test_exit_json.py` — 65 passed.
