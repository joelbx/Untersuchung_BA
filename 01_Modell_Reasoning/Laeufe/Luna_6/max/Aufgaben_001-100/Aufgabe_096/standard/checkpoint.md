# Checkpoint

Task: Fix `atomic_move()` default permissions and warning tracking in `/app` for CVE-2020-1736.

Implemented:
- Changed `_DEFAULT_PERM` to `0o0600`; `atomic_move()` applies the resulting `DEFAULT_PERM & ~umask` permissions to newly created destinations.
- Added `AnsibleModule._created_files`, tracks new destinations when `mode` is in the module argument spec and its value is unset, and clears a tracked path when `set_mode_if_different()` is invoked for it.
- Added `add_atomic_move_warnings()` and call it from `_return_formatted()` to emit the requested warning for each tracked path.

Verification: `git diff --check` passed. Existing unit tests passed: `test_atomic_move.py`, `test_set_mode_if_different.py`, and `test_exit_json.py` (63 passed).
