VERDICT: FIX
Code review: No correctness defect found in qutebrowser/browser/webengine/webview.py. The helper gates on Qt runtime >=6.2.3 and <6.7.0, expands exact MIME types with guess_all_extensions, expands wildcards through types_map, excludes existing suffixes, and chooseFiles appends new suffixes on both native chooser paths.
TEST_ENVIRONMENT_PROBLEM: The broad webengine run aborted during Qt qapp setup without a display (exit 134). Offscreen alone exited 1 during test_webengine_cookies.py after 12 tests, consistent with WebEngine's root sandbox restriction. Both display and sandbox overrides are needed here.
Commands/results:
- `python -m pytest -q tests/unit/browser/webengine/test_webview.py`: 12 passed.
- `python -m pytest -q tests/unit/browser/webengine`: aborted in test_darkmode.py, exit 134.
- `QT_QPA_PLATFORM=offscreen python -m pytest -q tests/unit/browser/webengine`: stopped in test_webengine_cookies.py, exit 1.
- `QT_QPA_PLATFORM=offscreen python -m pytest -q tests/unit/browser/webengine/test_webengine_cookies.py -x`: stopped after 12 tests, exit 1.
- `QT_QPA_PLATFORM=offscreen QTWEBENGINE_DISABLE_SANDBOX=1 python -m pytest -q tests/unit/browser/webengine`: 128 passed, 1 rerun.
Action: Run WebEngine tests in this root/headless environment with QT_QPA_PLATFORM=offscreen QTWEBENGINE_DISABLE_SANDBOX=1. Verdict follows the rule requiring FIX when any relevant test attempt is interrupted; the configured rerun passed.
