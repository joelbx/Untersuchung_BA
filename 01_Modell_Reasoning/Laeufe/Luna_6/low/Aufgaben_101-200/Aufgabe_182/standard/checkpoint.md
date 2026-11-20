# Checkpoint

Issue: route worker-process `Display.display`, `warning`, and `deprecated` calls through the final queue while preserving method and caller-supplied arguments, so the main process applies global deduplication.

Plan: inspect `display.py`, `task_queue_manager.py`, and the strategy result handler; update the proxy/message dispatch path; run the focused existing tests.
