# Checkpoint

Task: Preserve custom Accept-Language on XHR requests while retaining global fallback for other requests and domain overrides.

Changes: `custom_headers` accepts `fallback_accept_language=True`. With a URL and `False`, it queries the URL-specific Accept-Language value without global fallback and skips `UNSET`. The WebEngine interceptor passes `False` for XHR requests. Unit tests cover fallback, URL overrides, and actual interceptor header calls.

Verification:
- `QT_QPA_PLATFORM=offscreen QTWEBENGINE_DISABLE_SANDBOX=1 python -m pytest -q tests/unit/browser/test_shared.py tests/unit/browser/webengine/test_webengineinterceptor.py tests/unit/browser/webkit/network/test_networkmanager.py tests/unit/browser/webengine/test_webenginesettings.py` — exit 0; 41 passed, 1 rerun.
- `git diff --check && python -m compileall -q qutebrowser/browser/shared.py qutebrowser/browser/webengine/interceptor.py tests/unit/browser/test_shared.py tests/unit/browser/webengine/test_webengineinterceptor.py` — exit 0.

Environment notes: `rg` is unavailable (`/bin/bash: rg: command not found`), so searches used `grep`. An initial settings test command without `QTWEBENGINE_DISABLE_SANDBOX=1` exited 1 because QtWebEngine reported `Running as root without --no-sandbox is not supported`; the full relevant command above passed with the environment override. No remaining uncertainty from that check.
