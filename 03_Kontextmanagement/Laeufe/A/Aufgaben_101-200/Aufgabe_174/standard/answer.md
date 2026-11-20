Forked workers now send `Display.display` calls through `FinalQueue`, and the parent strategy thread replays them under a display lock. I removed the worker’s shutdown redirection to `/dev/null` and added stdout and stderr flushes during queue manager cleanup.

The relevant unit tests passed: **7 passed, 9 skipped**. The skips include the existing disabled strategy tests.