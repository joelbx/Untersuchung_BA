# Checkpoint

Task: fix Qt WebEngine file picker extension workaround for Qt 6.2.3 through 6.6.x.
Status: implemented MIME suffix expansion and integrated it into `chooseFiles` after observing the regression tests fail first. Focused tests pass.
Tooling: `rg` is unavailable (`/bin/bash: rg: command not found`); using `find` and `grep` for local searches.

## Verification

- `QT_QPA_PLATFORM=offscreen pytest -q tests/unit/browser/webengine/test_webview.py`: 12 passed.
- `QTWEBENGINE_DISABLE_SANDBOX=1 QT_QPA_PLATFORM=offscreen pytest -q tests/unit/browser/webengine --maxfail=1`: 128 passed, 1 rerun; Qt printed `Release of profile requested but WebEnginePage still not deleted. Expect troubles !` at shutdown.
- `QT_QPA_PLATFORM=offscreen pytest -q`: end-to-end setup errors including `tests/end2end/test_adblock_e2e.py::test_adblock[auto]` and `tests/end2end/test_hints_html.py` because Chromium reports `Running as root without --no-sandbox is not supported`.
- `QT_QPA_PLATFORM=offscreen pytest -q tests/unit --maxfail=1`: exited 1 after `tests/unit/browser/test_browsertab.py` with no pytest summary in captured output; likely environment/browser startup issue, but exact cause is uncertain.
- `QTWEBENGINE_DISABLE_SANDBOX=1 QT_QPA_PLATFORM=offscreen pytest -q tests/unit --maxfail=1`: 132 passed, 11 skipped, then `tests/unit/browser/test_caret.py::test_toggle[webengine]` failed due to Qt warning `This plugin does not support propagateSizeHints()`.
- `git diff --check`: passed.

Python's host MIME database may include additional suffixes beyond the example mappings (e.g. `.jpeg` and `.mp4`); the implementation deliberately returns every suffix provided by `mimetypes.guess_all_extensions` as required.
