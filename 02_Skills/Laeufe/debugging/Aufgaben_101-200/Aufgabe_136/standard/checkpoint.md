# Certificate error wrapper checkpoint

## Investigation
- Working tree: /app.
- `rg` is unavailable (`/bin/bash: rg: command not found`); using `find` and `grep` for local inspection.
- Root cause and verification pending.

## Root cause and pattern
- WebKit `CertificateErrorWrapper.__init__` accepts only `errors`; a named `reply` raises `TypeError`. Its existing HTML implementation already uses the shared escaped paragraph for one error and Jinja autoescaping for a list.
- The network manager owns `reply` separately and calls `ignoreSslErrors()` only after a decision, so attaching the reply to the wrapper can stay side-effect free at construction.
- WebEngine currently uses one Qt5-style wrapper with an `ignore` boolean. Qt6 certificate errors expose decision methods instead; the requested factory and subclasses need to route decisions by Qt version.
- Hypothesis: accepting `reply` in WebKit and routing certificate decisions through explicit wrapper methods fixes the constructor contract and gives both Qt versions the required lifecycle.

## Verification notes
- New WebKit test failed before the fix with `TypeError: CertificateErrorWrapper.__init__() got an unexpected keyword argument 'reply'`.
- New WebEngine tests failed before the fix because `machinery`/`UndeferrableError` and the requested factory/classes did not exist.
- `python -m pytest -q -o reruns=0 tests/unit/browser/webkit/test_certificateerror.py tests/unit/browser/webengine/test_webengine_certificateerror.py`: 7 passed, exit 0.
- `python -m pytest -q -o reruns=0 tests/unit/browser/webengine/test_webenginetab.py -x`: exit 1 before tests, Chromium error `Running as root without --no-sandbox is not supported`.
- `QTWEBENGINE_DISABLE_SANDBOX=1 python -m pytest -q -o reruns=0 tests/unit/browser/webengine/test_webenginetab.py -x`: 25 passed, then X11 teardown `The X11 connection broke` / `XIO: fatal IO error 22`; exit 1. Test assertions passed but process did not exit cleanly.
- PyQt6 is unavailable locally, so Qt6-specific behavior is verified with a fake error object under the Qt5 runtime, not a real Qt6 binding.
- Further Qt6 API review found that Qt6 uses `description()`/`type()` instead of Qt5's `errorDescription()`/`error()`. Added a fake Qt6 regression that failed with `TypeError: 'NoneType' object is not callable` before the Qt6 override, then passed after it.
- The network manager caches reply-free copies of errors so accepted/rejected history does not retain completed replies.
- `QT_QPA_PLATFORM=offscreen QTWEBENGINE_DISABLE_SANDBOX=1 python -m pytest --no-xvfb -q -o reruns=0 tests/unit/browser/webengine/test_webenginetab.py -x`: exit 1 at setup with `Exception: No display and no Xvfb available!`; this cannot provide a clean headless run in the current test setup.
- Final `python -m pytest -q -o reruns=0 tests/unit/browser/webkit/test_certificateerror.py tests/unit/browser/webengine/test_webengine_certificateerror.py tests/unit/browser/webkit/network/test_networkmanager.py`: 8 passed, exit 0.
- Final `git diff --check` and `python -m compileall -q qutebrowser/browser/webkit/certificateerror.py qutebrowser/browser/webengine/certificateerror.py qutebrowser/utils/usertypes.py`: exit 0.
