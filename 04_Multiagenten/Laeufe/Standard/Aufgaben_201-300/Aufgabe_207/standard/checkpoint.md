# Checkpoint

Task: Consolidate QtWebEngine `--enable-features` arguments from CLI, configuration, and required features.
Status: Implemented and verified. QtWebEngine consumes existing feature flags (including separate CLI name/value form), splits comma-separated features, deduplicates them in encounter order, and emits one combined flag when nonempty. QtWebKit arguments remain unchanged.
Verification: `pytest -q tests/unit/config/test_qtargs.py -k 'not new_chromium'` passed (85 tests); `git diff --check` and Python compile checks passed. The excluded existing Chromium version probe segfaults in this environment's Qt runtime inside `init_user_agent` (exit 139).
