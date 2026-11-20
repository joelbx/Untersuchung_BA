# Checkpoint

Implemented runtime-only Qt version gating for the MIME suffix workaround, documented the `compiled` parameter, and changed the ambiguous `compiled=True, exact=True` rejection to `RuntimeError`. Updated the relevant tests for the exception type and for confirming runtime-only calls.

Verification: `test_version_check` cases passed (13). The combined targeted run then aborted while initializing the Qt application for subsequent webview tests; a broader run also exposed an unrelated Qt `QDataStream.Status` count mismatch before aborting.
