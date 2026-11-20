# Checkpoint

Task: gate the MIME suffix workaround using runtime Qt only.

Changes:
- `extra_suffixes_workaround` checks both version bounds with `compiled=False`.
- `version_check` documents the `compiled` behavior and raises `RuntimeError` for `compiled=True, exact=True`.
- Unit tests cover mismatched runtime, compiled Qt, and PyQt versions at the bounds.

Checks:
- `QT_QPA_PLATFORM=offscreen python -m pytest -q tests/unit/browser/webengine/test_webview.py tests/unit/utils/test_qtutils.py -k 'version_check or suffixes_workaround'`: 34 passed.
- `QT_QPA_PLATFORM=offscreen python -m pytest -q tests/unit/utils/test_qtutils.py tests/unit/browser/webengine/test_webview.py`: 196 passed, 2 failed. `test_qdatastream_status_count` expects 4 statuses but this Qt exposes 5 (`SizeLimitExceeded` added); `TestSavefileOpen.test_failing_flush` emits `QSaveFile::commit: File ... is not open`, which the Qt warning fixture rejects. These failures are outside the changed version and MIME paths. The remaining uncertainty is the status of the full affected modules in an environment with their expected Qt warning/status behavior.
- `git diff --check`: passed.

Tooling: `rg` is unavailable (`/bin/bash: rg: command not found`); local `grep`/`find` fallback used.
