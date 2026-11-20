# Checkpoint

Task completed: MIME suffix workaround gating now uses runtime Qt version only at both boundaries. `version_check` documents `compiled=False` as runtime-only and rejects `compiled=True, exact=True` with `RuntimeError`.

Verification:
- `python -m pytest tests/unit/utils/test_qtutils.py -q -k version_check` — 13 passed.
- `python -m pytest tests/unit/browser/webengine/test_webview.py -q -k suffixes_workaround_extras_returned` — 7 passed.
- `git diff --check` — passed.
- A broader test invocation hit an unrelated Qt enum count assertion (`QDataStream.Status` has 5 members where the test expects 4) and then the Qt process aborted during fixture setup under the installed Qt 6.9 runtime. Targeted tests passed when run separately.
