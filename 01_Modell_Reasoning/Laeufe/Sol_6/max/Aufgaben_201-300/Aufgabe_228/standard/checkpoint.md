# Version parsing update

- Started from a clean working tree.
- Located version handling in `qutebrowser/utils/utils.py`, `qutebrowser/utils/qtutils.py`, `qutebrowser/utils/version.py`, `qutebrowser/misc/earlyinit.py`, and `qutebrowser/misc/crashdialog.py`.
- Added `utils.parse_version` with `QVersionNumber.fromString(...).normalized()` and updated the specified version checks and distribution/crash-dialog consumers.
- Updated existing tests and added focused cases for normalization, runtime/compiled minimums, WebKit boundaries, and crash-dialog notes.
- Focused suite completed cleanly with `xvfb-run -a env QT_QPA_PLATFORM=offscreen QTWEBENGINE_DISABLE_SANDBOX=1 pytest -p no:xvfb -q tests/unit/utils/test_qtutils.py tests/unit/utils/test_utils.py tests/unit/utils/test_version.py tests/unit/misc/test_earlyinit.py tests/unit/misc/test_crashdialog.py`: 425 passed, 4 skipped.
- `git diff --check` passed; affected modules have no `pkg_resources.parse_version` calls.
