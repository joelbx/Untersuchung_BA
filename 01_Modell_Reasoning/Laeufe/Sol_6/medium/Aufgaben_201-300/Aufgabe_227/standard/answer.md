The MIME suffix workaround now checks **runtime Qt only** at both bounds: 6.2.3 inclusive and 6.7.0 exclusive. I clarified `compiled=False` in the version utility and changed the `compiled=True, exact=True` error to `RuntimeError`.

The existing suffix behavior is preserved: outside that range it returns an empty set; inside it adds missing extensions. Regression tests cover both boundaries with differing runtime and compiled versions.

Verification passed: 13 version utility tests, all 24 webview tests with `QT_QPA_PLATFORM=offscreen`, and `git diff --check`.