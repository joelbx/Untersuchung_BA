Implemented the version-aware canvas workaround.

- Changed the setting to a string enum with `always`, `auto`, and `never`; default is `auto`.
- Passed WebEngine versions, CLI namespace, and special flags into the settings resolver.
- `auto` enables the flag only on Qt 6 when Chromium’s major version is known, nonzero, and below 111.
- Added tests for Qt 5.15.2, Qt 6.5.3, and Qt 6.6.0, plus the manual overrides.

Verification: `QT_QPA_PLATFORM=offscreen pytest -q tests/unit/config/test_qtargs.py` passed (109 tests). `git diff --check` passed.