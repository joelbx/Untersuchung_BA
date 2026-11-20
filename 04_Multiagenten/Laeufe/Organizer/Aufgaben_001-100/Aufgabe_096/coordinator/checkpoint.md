Task: Fix atomic_move default file permissions and deferred warnings for created files without mode.
Status: Complete. Changed _DEFAULT_PERM to 0600; atomic_move retains umask-aware destination chmod and records new paths for modules with an omitted mode argument; _return_formatted emits exact per-path warnings; set_mode_if_different removes tracked paths when mode is supplied.
Tests: Focused 69 passed. Full module_utils/basic suite with --forked: 300 passed, 14 skipped. A non-isolated broad run showed pre-existing shared warning/deprecation state contamination between tests; isolated run passed.
Delegation: None. All edits made directly.
