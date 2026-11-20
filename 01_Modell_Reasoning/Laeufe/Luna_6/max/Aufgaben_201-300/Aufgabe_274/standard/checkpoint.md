# Checkpoint

## Objective
Implement version-aware `qt.workarounds.disable_accelerated_2d_canvas` modes (`always`, `auto`, `never`) with `auto` enabled only for Qt 6 and known Chromium major versions below 111.

## Changes made
- Changed the config option from `Bool` to a string enum with default `auto`.
- Added an `auto` resolver based on Qt 6 and a nonzero, known Chromium major version below 111.
- Passed WebEngine versions, CLI namespace, and special flags through the settings argument builder; callable mappings are resolved before final argument lookup.
- Added regression coverage for Qt 5.15.2, Qt 6.5.3, Qt 6.6.0, forced modes, and unknown/zero Chromium versions.

## Verification
- `QT_QPA_PLATFORM=offscreen pytest -q tests/unit/config/test_qtargs.py tests/unit/config/test_configdata.py` — 142 passed.
- `git diff --check` — passed.
- A first test invocation without offscreen mode aborted when Qt initialized in the headless environment; the offscreen rerun completed successfully.
