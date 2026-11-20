The forked display output issue is resolved. Workers now send `Display.display` calls through `FinalQueue` for the parent to replay. Parent output is locked, the worker shutdown redirection is removed, and cleanup flushes stdout and stderr.

Validation passed: **8 tests passed, 9 skipped**, and a fork round trip confirmed the event was delivered and the worker exited cleanly.