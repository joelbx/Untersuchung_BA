# Checkpoint

## Objective
Consolidate user-provided and configuration-required QtWebEngine `--enable-features` flags into one argument, preserving non-QtWebEngine arguments unchanged.

## Initial state
- Repository: `/app`
- Working tree was clean at task start.
- No `AGENTS.md` files were found in the repository parent tree.
- `rg` is unavailable; used `find`/`grep` for local searches.

## Changes
- QtWebEngine now extracts both equals-form feature flags and `--qt-arg enable-features VALUE`, removes them from the original argument list, splits their comma-separated features, and emits one consolidated flag.
- Configuration adds `OverlayScrollbar` to that flag only for Qt > 5.11, non-macOS, with overlay scrollbars enabled.
- Other backends retain the assembled arguments unchanged.
- Added regression coverage for both CLI forms, config flags, empty values, helper parsing, overlay behavior, and non-WebEngine preservation.

## Verification
- `git diff --check`: passed.
- Focused Qt argument tests: 11 passed.
- Full `tests/unit/config/test_qtargs.py` encounters an environment crash in `TestDarkMode.test_new_chromium`, which segfaults inside QtWebEngine user-agent initialization; 81 cases pass when that test is excluded.
