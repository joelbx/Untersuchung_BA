The MIME suffix workaround now checks **runtime Qt only** at both bounds: 6.2.3 inclusive and 6.7.0 exclusive. I clarified `version_check`’s `compiled` parameter and changed the `compiled=True, exact=True` error to `RuntimeError`.

Regression tests cover mismatched runtime, compiled Qt, and PyQt versions. All 33 focused tests passed with Qt’s offscreen platform; `git diff --check` passed.