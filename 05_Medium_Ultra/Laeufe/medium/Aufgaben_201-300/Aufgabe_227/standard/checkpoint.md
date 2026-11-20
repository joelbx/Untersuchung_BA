# Checkpoint

Updated the MIME suffix workaround to pass `compiled=False` at both runtime Qt bounds. Clarified `version_check` documentation and changed its incompatible `compiled=True, exact=True` error to `RuntimeError`. Added runtime boundary tests with divergent compiled Qt and PyQt versions. Relevant tests passed: 31 selected tests in `test_qtutils.py` and `test_webview.py`.
