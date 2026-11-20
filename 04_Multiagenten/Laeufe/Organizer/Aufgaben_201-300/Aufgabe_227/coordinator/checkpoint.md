# Checkpoint

Issue: Gate the MIME suffix workaround using runtime Qt only.

Implemented:
- The workaround calls version_check("6.2.3", compiled=False) and version_check("6.7.0", compiled=False).
- Documented compiled=False as reading qVersion() only; compiled=True checks compiled Qt and PyQt as well.
- compiled=True with exact=True now raises RuntimeError.
- Added focused tests for both bounds with divergent runtime/compiled/PyQt versions and for runtime-only utility behavior.

Verification:
- `QT_QPA_PLATFORM=offscreen pytest -q tests/unit/utils/test_qtutils.py tests/unit/browser/webengine/test_webview.py -k 'version_check or suffixes_workaround'`: 32 passed.
- Full two-file run: 194 passed, 2 unrelated failures (`test_qdatastream_status_count` due a new Qt enum member; `TestSavefileOpen::test_failing_flush` due a Qt warning).
- `git diff --check` passed.

Delegation: None.
