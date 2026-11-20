VERDICT: ACCEPT

The applied patch meets the stated behavior: XHR requests omit the global `Accept-Language` value when there is no domain override, while other requests retain it. I found no correctness or regression issue. No project code was changed during this review.

`QT_QPA_PLATFORM=offscreen python -m pytest -q tests/unit/browser/test_shared.py tests/unit/browser/webengine/test_webengineinterceptor.py` — **29 passed**. `git diff --check` — passed.