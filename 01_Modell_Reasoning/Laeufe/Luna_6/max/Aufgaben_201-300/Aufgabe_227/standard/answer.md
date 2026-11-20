Updated the Qt workaround to check runtime Qt only at both bounds (`>= 6.2.3` and `< 6.7.0`). It returns an empty set outside that range and filters added values to extension strings. I also documented `compiled` and changed `compiled=True, exact=True` to raise `RuntimeError`.

The focused tests passed: **24 passed**. The full test files encountered an unrelated Qt enum count failure, then aborted during Qt application setup.

Checkpoint: [.codex-role-output/checkpoint.md](/app/.codex-role-output/checkpoint.md)

Changed [webview.py](/app/qutebrowser/browser/webengine/webview.py:142), [qtutils.py](/app/qutebrowser/utils/qtutils.py:78), and their unit tests.