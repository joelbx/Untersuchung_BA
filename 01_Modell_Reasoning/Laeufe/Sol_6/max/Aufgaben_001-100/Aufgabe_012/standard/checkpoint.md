# Checkpoint

Issue: XHR requests with a JavaScript-supplied Accept-Language header were overridden by the global `content.headers.accept_language` setting.

Resolution: `custom_headers` now accepts `fallback_accept_language=True`. When it is false and a URL is provided, only a matching URL-specific Accept-Language value is emitted. The WebEngine interceptor passes false for XHR requests and true for other request types.

Verification: 27 selected browser unit tests passed with `QT_QPA_PLATFORM=offscreen QTWEBENGINE_DISABLE_SANDBOX=1`; `git diff --check` passed. `flake8` was unavailable in the environment.
