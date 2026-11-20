# Checkpoint

Task: Gate the MIME suffix workaround using runtime Qt only, and clarify `version_check`'s `compiled` behavior.

Root cause: `extra_suffixes_workaround` called `version_check` without `compiled=False`, so its lower and upper bounds also depended on `QT_VERSION_STR` and `PYQT_VERSION_STR`. The utility already supported runtime-only evaluation but its `compiled` documentation was unclear. It raised `ValueError` for `compiled=True, exact=True` instead of the required `RuntimeError`.

Reproduction: Added runtime-bound test cases with compiled versions on opposite sides of 6.2.3 and 6.7.0. Before the fix, `QT_QPA_PLATFORM=offscreen pytest -q tests/unit/browser/webengine/test_webview.py -k runtime_bounds` exited 1, failing at runtime 6.2.3 and 6.7.0 as expected. Updated exception test failed before the fix with `ValueError`.

Patch: Both workaround bound checks now pass `compiled=False`; utility docstring states runtime-only behavior and the incompatible-flag error is `RuntimeError`. Existing suffix derivation remains: only upstream entries starting with `.` are treated as existing suffixes, and no suffixes are added outside the range.

Checks:
- `QT_QPA_PLATFORM=offscreen pytest -q -o addopts='' tests/unit/utils/test_qtutils.py -k version_check tests/unit/browser/webengine/test_webview.py -k 'version_check or suffixes_workaround'`: exit 0, 31 passed.
- `QT_QPA_PLATFORM=offscreen pytest -q -o addopts='' tests/unit/utils/test_qtutils.py tests/unit/browser/webengine/test_webview.py`: exit 1, 193 passed, 2 failed. `test_qdatastream_status_count` expects four enum values but installed Qt 6.9.1 has five (`SizeLimitExceeded` is extra). `TestSavefileOpen.test_failing_flush` fails due to Qt warning `QSaveFile::commit: File (...) is not open`. Neither is in the modified logic.
- `git diff --check`: exit 0.
- Initial `rg` search was unavailable: `/bin/bash: line 1: rg: command not found`; used `grep`/`find`.
