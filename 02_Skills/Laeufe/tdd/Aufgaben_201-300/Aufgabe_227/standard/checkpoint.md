# Checkpoint

Task: MIME suffix workaround must use runtime Qt bounds; document `version_check(compiled)` and reject compiled plus exact with RuntimeError.

Status: Production patch and regression tests complete. `git diff --check` passed.

TDD: Added boundary cases for runtime 6.2.2, 6.2.3, 6.6.9, 6.7.0 with divergent compiled/PyQt versions. Before patch, 12 MIME suffix cases and the RuntimeError case failed for the expected reasons. After patch, `QT_QPA_PLATFORM=offscreen pytest -q tests/unit/browser/webengine/test_webview.py tests/unit/utils/test_qtutils.py -k 'suffixes_workaround or version_check'` passed: 31 tests.

Broader checks:
- `QT_QPA_PLATFORM=offscreen pytest -q tests/unit/browser/webengine/test_webview.py tests/unit/utils/test_qtutils.py`: 193 passed, 2 failed. Existing unrelated failures: `tests/unit/utils/test_qtutils.py::test_qdatastream_status_count` (expected 4 statuses, runtime Qt has 5) and `tests/unit/utils/test_qtutils.py::TestSavefileOpen::test_failing_flush` (Qt warning `QSaveFile::commit: File ... is not open`).
- `QT_QPA_PLATFORM=offscreen pytest -q` started. End-to-end browser tests repeatedly fail at setup because Chromium refuses root execution without `--no-sandbox`: `Running as root without --no-sandbox is not supported`. The run was terminated after repeated setup failures (exit 143); this environment prevents meaningful end-to-end verification.

Environment: `rg` is unavailable (`/bin/bash: rg: command not found`); used `grep`.
