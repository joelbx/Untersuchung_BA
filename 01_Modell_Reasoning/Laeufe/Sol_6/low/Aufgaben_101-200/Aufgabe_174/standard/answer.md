Forked worker calls to `Display.display` now go through `FinalQueue` as `DisplaySend` events. The results thread replays them in the parent, where a lock protects output. I removed the worker’s shutdown redirection to `/dev/null` and added stdout and stderr flushes to `TaskQueueManager.cleanup`.

The focused tests passed: **3 passed**. The broader strategy test selection had **7 skipped**.