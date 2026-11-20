# Checkpoint

Task: preserve an XHR request's custom Accept-Language header by changing `custom_headers` fallback behavior and the WebEngine interceptor call.

Starting state: clean git working tree. `rg` is unavailable (`/bin/bash: rg: command not found`), so local searches use grep/find. TDD cycle pending: inspect existing code and tests, add regression tests, observe failure, implement, run focused and full tests.

TDD: new shared helper test failed with `TypeError: custom_headers() got an unexpected keyword argument 'fallback_accept_language'`. New interceptor test failed with `AssertionError: assert b'de' == b'fr'` for XHR. After patch, focused command `QT_QPA_PLATFORM=offscreen pytest -q tests/unit/browser/test_shared.py tests/unit/browser/webengine/test_webengineinterceptor.py --reruns 0` passed (29 tests).

Tooling: initial `pytest -q tests/unit/browser/test_shared.py -k custom_headers_accept_language_fallback` aborted in pytest-qt's `qapp` fixture without a display; rerunning with `QT_QPA_PLATFORM=offscreen` worked. Full-suite command `QT_QPA_PLATFORM=offscreen pytest -q --reruns 0` reached end-to-end tests but spawned QtWebEngine as root; Chromium exited with `Running as root without --no-sandbox is not supported`. Numerous end-to-end failures followed, e.g. `test_going_back_in_a_new_tab_without_history`; interrupted after 22 failed, 12 errors. Full suite remains unverified in this environment.

Broader unit command `QT_QPA_PLATFORM=offscreen pytest -q tests/unit --reruns 0` exited 1 without a pytest summary; output ended at `tests/unit/browser/test_browsertab.py s` after collecting 8771 tests. Cause is uncertain from available output, so the full unit suite remains unverified. Relevant existing WebKit test command `QT_QPA_PLATFORM=offscreen pytest -q tests/unit/browser/webkit/network/test_networkmanager.py --reruns 0` passed (1 test). `git diff --check` passed.
