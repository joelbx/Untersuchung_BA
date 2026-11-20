# Checkpoint

Task: Fix WebKit certificate error constructor, HTML rendering, and shared certificate decision interfaces.

Changes: WebKit accepts `reply` and `errors` (including the legacy errors-only form), calls `ignoreSslErrors()` only on acceptance, and retains escaped paragraph/list HTML. Added shared decision state and undeferrable exception; added Qt5/Qt6 WebEngine wrappers and a version factory; updated call sites and focused tests.

Checks:
- `python -m pytest tests/unit/browser/webkit/network tests/unit/browser/webkit/test_certificateerror.py tests/unit/browser/webengine/test_webengine_certificateerror.py -q`: 81 passed, 8 skipped, exit 0.
- `git diff --check`: exit 0.
- `python -m pytest tests/unit/browser/webengine/test_webenginetab.py -vv -s -x`: exit 1 before first test due to Chromium error `Running as root without --no-sandbox is not supported`.
- `QTWEBENGINE_DISABLE_SANDBOX=1 python -m pytest tests/unit/browser/webengine/test_webenginetab.py -q`: 25 test assertions passed, but command exited 1 during X11 teardown with `The X11 connection broke: I/O error (code 1)` / `XIO: fatal IO error 22`. This suite cannot be claimed as passing in this environment; the remaining uncertainty is its process teardown, not an observed assertion failure.
- `QTWEBENGINE_DISABLE_SANDBOX=1 QT_QPA_PLATFORM=offscreen python -m pytest -p no:xvfb tests/unit/browser/webengine/test_webenginetab.py -q`: exit 1 because repository `check_display` fixture requires a display (`No display and no Xvfb available!`).

Qt6 runtime is unavailable here; Qt6 decision behavior is covered with mock error objects and version selection tests.
