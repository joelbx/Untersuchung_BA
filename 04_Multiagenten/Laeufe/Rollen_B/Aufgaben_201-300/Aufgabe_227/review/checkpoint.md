VERDICT: FIX
Code defect: qutebrowser/browser/webengine/webview.py:142 returns dot-prefixed entries already in accepted_mimetypes; chooseFiles at line 288 appends them unchanged, so e.g. ['.jpg'] becomes ['.jpg', '.jpg']. The modified test at tests/unit/browser/webengine/test_webview.py:129 expects this duplication. Keep the required helper result and deduplicate entries when building the chooseFiles filters; update the test to assert one occurrence.

Runtime version bounds and version_check(compiled=False) logic satisfy the stated gating requirement; compiled=True with exact=True raises RuntimeError.

Tests:
- QT_QPA_PLATFORM=offscreen python -m pytest -q tests/unit/utils/test_qtutils.py -k version_check tests/unit/browser/webengine/test_webview.py -k 'version_check or suffixes_workaround' => 31 passed, 164 deselected.
- QT_QPA_PLATFORM=offscreen python -m pytest -q tests/unit/utils/test_qtutils.py tests/unit/browser/webengine/test_webview.py => 193 passed, 2 failed, 6 rerun.

TEST_ENVIRONMENT_PROBLEM: The full run under Qt runtime 6.9.1 fails test_qdatastream_status_count because Qt has 5 statuses where the existing test expects 4, and TestSavefileOpen.test_failing_flush because Qt 6.9.1 emits QSaveFile::commit warning that the pytest-qt warning policy treats as failure. These failures are outside the changed lines. Run the full suite on a supported Qt version, or update those unrelated compatibility expectations if Qt 6.9 support is intended.
