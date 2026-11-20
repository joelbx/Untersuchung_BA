# Checkpoint

Issue: Gate the MIME suffix workaround on runtime Qt 6.2.3 through 6.6.x only.

Initial findings: `version_check` already accepts `compiled`, but its `compiled=True, exact=True` guard raises `ValueError`. `extra_suffixes_workaround` uses default mixed-version checks. Existing suffix tests expect extensions derived from MIME entries, excluding extensions already present in the input.

Plan: Make both workaround checks use `compiled=False`, document the utility parameter, change the ambiguous-argument error to `RuntimeError`, and extend local tests for version mismatches and boundaries. Run relevant existing tests.

First verification attempt: `pytest -q tests/unit/utils/test_qtutils.py -k version_check tests/unit/browser/webengine/test_webview.py -k 'version_check or suffixes_workaround'` exited 134. Output showed 15 version-check tests and 11 webview tests passing before `Fatal Python error: Aborted` in `pytestqt/plugin.py` while creating the qapp fixture. The full test selection did not complete; retrying with `QT_QPA_PLATFORM=offscreen`.

Patch: Both MIME workaround bounds call `version_check(..., compiled=False)`. `version_check` documents runtime-only behavior and raises `RuntimeError` for `compiled=True, exact=True`. Tests cover runtime 6.2.2, 6.2.3, 6.6.9, and 6.7.0 with mismatched compiled Qt and PyQt versions, and assert that both bound calls pass `compiled=False`.

Verification: `QT_QPA_PLATFORM=offscreen pytest -q tests/unit/utils/test_qtutils.py tests/unit/browser/webengine/test_webview.py -k 'version_check or suffixes_workaround'` exited 0: 33 passed, 164 deselected. `git diff --check` exited 0.

Broader test command: `QT_QPA_PLATFORM=offscreen pytest -q tests/unit/utils/test_qtutils.py tests/unit/browser/webengine/test_webview.py` exited 1: 195 passed, 2 failed, 6 rerun. Failures are `test_qdatastream_status_count` (installed Qt exposes five `QDataStream.Status` values; test expects four) and `TestSavefileOpen.test_failing_flush` (Qt emits `QSaveFile::commit: File (...) is not open` warning). These are outside the version-check and MIME workaround paths. The broader suite is not passing in this environment.
