Forked workers now send `Display.display` calls through `FinalQueue`, and the parent replays them under a thread lock. The worker shutdown redirection is removed. Cleanup drains worker events before stopping the results reader and flushes both output streams.

Added a forked worker test. The relevant suite passed: **19 passed, 2 skipped**.