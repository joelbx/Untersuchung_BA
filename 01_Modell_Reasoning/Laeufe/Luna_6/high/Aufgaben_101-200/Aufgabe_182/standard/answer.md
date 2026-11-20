Implemented worker display proxying. `display`, `warning`, and `deprecated` now send their method name and caller-supplied arguments through the queue; the results thread invokes the matching method in the main process, where deduplication applies.

Updated fork proxy coverage and recorded progress in the checkpoint.

**Verification:** 13 passed, 1 skipped in the focused display and task queue tests; `git diff --check` passed. The separate warning test file has 1 failure because its singleton retains the warning recorded by the preceding test.