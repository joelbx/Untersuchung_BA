# Checkpoint

Issue: forked Display methods bypass global deduplication.
Status: resolved in checked-out files.
Changes: `proxy_display` forwards the method name and exact arguments for `display`, `warning`, and `deprecated`; `DisplaySend` carries the name; the results thread invokes that Display method in the main process.
Verification: targeted display and queue tests: 18 passed, 1 skipped; task queue manager callback tests: 2 passed; `git diff --check` passed.
