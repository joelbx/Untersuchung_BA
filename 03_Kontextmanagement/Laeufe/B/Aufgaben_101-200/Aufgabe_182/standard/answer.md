Resolved. Worker calls to `display`, `warning`, and `deprecated` now send their method name and exact caller arguments through the final queue. The main process dispatches each call to the matching `Display` method, so warning deduplication applies across workers.

The relevant tests passed: **19 passed, 1 skipped**.