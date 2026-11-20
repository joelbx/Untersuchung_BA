Task: Resolve atomic_move default permission and mode warning issue in /app.
Status: Implemented restrictive 0600 default, created-path tracking for omitted mode, formatted warnings, and clearing on explicit mode setting. Added regression tests including a real filesystem check under umask 022.
Verification: 68 relevant atomic_move, set_mode_if_different, and exit_json tests pass. The existing deprecate test passes alone; when run after test_warn, that test file leaks global warning state and fails independently of this change. git diff --check passes.
Constraints: Edit checked-out files only; run relevant existing tests; do not alter git history, index baseline, or harness configuration.
