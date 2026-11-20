# Checkpoint

Issue: Make `qt.workarounds.disable_accelerated_2d_canvas` a string enum with `always`, `auto`, and `never`, defaulting to `auto`. Resolve `auto` from active Qt/Chromium version data when constructing WebEngine arguments.

Implemented:
- Changed the option schema from `Bool` to a documented string enum with default `auto`.
- Passed WebEngine versions, the parsed CLI namespace, and special flags into `_qtwebengine_settings_args`.
- Added callable setting resolution and mapped `always`, `auto`, and `never` to the requested Chromium argument behavior.
- The resolver enables the workaround only for Qt 6 with a known, non-zero Chromium major below 111.

Verification:
- `QT_QPA_PLATFORM=offscreen pytest -q tests/unit/config/test_qtargs.py tests/unit/config/test_configdata.py` — 133 passed.
- Direct resolver checks for Qt 5.15.2/Chromium 83, Qt 6.5.3/Chromium 108, Qt 6.6.0/Chromium 112, unknown Chromium, and Chromium major 0 — all passed.
- `git diff --check` — passed.

The initial test attempts without `QT_QPA_PLATFORM=offscreen` aborted because the available Qt `xcb` platform plugin could not initialize in this headless environment.
