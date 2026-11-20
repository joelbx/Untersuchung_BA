# Checkpoint

Issue: WebKit certificate wrapper constructor and HTML rendering; shared certificate decision interfaces and Qt5/Qt6 WebEngine wrappers.

Changes: WebKit wrapper accepts `reply` and `errors`, holds the reply without acting on it during construction, and calls `ignoreSslErrors()` only on acceptance. Its single-error paragraph uses `html.escape` through the base class; multi-error list escapes each message directly. Added shared decision state, `UndeferrableError`, Qt5/Qt6 WebEngine wrappers and factory; updated WebKit/WebEngine callers. Added focused tests.

Verification:
- `QT_QPA_PLATFORM=offscreen python -m pytest -q tests/unit/browser/webkit/test_certificateerror.py tests/unit/browser/webengine/test_webengine_certificateerror.py tests/unit/utils/usertypes/test_misc.py tests/unit/browser/webkit/network/test_networkmanager.py` — exit 0, 12 passed (final rerun after explicit list escaping).
- `python -m compileall -q qutebrowser/browser/webkit/certificateerror.py qutebrowser/browser/webengine/certificateerror.py qutebrowser/utils/usertypes.py qutebrowser/browser/webengine/webview.py qutebrowser/browser/webengine/webenginetab.py qutebrowser/browser/webkit/network/networkmanager.py` — exit 0.
- `git diff --check` — exit 0.

Checks with limits:
- `QT_QPA_PLATFORM=offscreen python -m pytest -q tests/unit/browser/webkit/test_certificateerror.py tests/unit/browser/webengine/test_webengine_certificateerror.py tests/unit/utils/usertypes/test_misc.py tests/unit/browser/webkit/network tests/unit/browser/webengine` — exit 1 after output reached `tests/unit/browser/webengine/test_webengine_cookies.py ............`; no traceback or summary was emitted. Cause of the broad-suite exit is unknown; focused certificate and network-manager tests pass.
- An earlier broad run used `test_certificateerror.py` in both browser directories and failed collection with `import file mismatch`; renamed the new test to `test_webengine_certificateerror.py` and reran.
- `python -m flake8 qutebrowser/browser/webkit/certificateerror.py qutebrowser/browser/webengine/certificateerror.py qutebrowser/browser/webengine/webview.py qutebrowser/browser/webengine/webenginetab.py qutebrowser/browser/webkit/network/networkmanager.py qutebrowser/utils/usertypes.py tests/unit/browser/webkit/test_certificateerror.py tests/unit/browser/webengine/test_webengine_certificateerror.py tests/unit/utils/usertypes/test_misc.py` — exit 1, `/usr/local/bin/python: No module named flake8`; lint result unknown.
