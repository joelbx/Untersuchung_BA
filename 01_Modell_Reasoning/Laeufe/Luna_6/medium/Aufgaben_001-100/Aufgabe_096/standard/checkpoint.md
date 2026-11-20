# Checkpoint

Implemented the atomic move permission fix:

- Changed `_DEFAULT_PERM` from `0o0666` to `0o0600`.
- Retained destination chmod using `DEFAULT_PERM & ~umask` for newly created files.
- Added per-module `_created_files` tracking for new files when `mode` is accepted but omitted.
- Added `add_atomic_move_warnings()` to result formatting with the required warning text.
- Removed tracked paths when `set_mode_if_different()` is called.

Verification: `pytest -q test/units/module_utils/basic/test_atomic_move.py test/units/module_utils/basic/test_set_mode_if_different.py test/units/module_utils/basic/test_exit_json.py` passed (63 tests). `git diff --check` passed.
