Worker calls to `display`, `warning`, and `deprecated` now go through `_final_q` with the original method name and exactly the arguments the caller supplied. The main process dispatches each queued call to the corresponding `Display` method, so warning and deprecation deduplication happens across workers.

I updated the focused tests and ran the relevant existing suite: **17 passed, 7 skipped**.