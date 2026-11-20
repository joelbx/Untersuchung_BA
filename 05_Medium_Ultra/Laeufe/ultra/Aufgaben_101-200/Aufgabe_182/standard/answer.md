Worker calls to `Display.display`, `warning`, and `deprecated` now send their method name and exact caller arguments through `_final_q`. The main process invokes the named method, so warning and deprecation deduplication runs across workers.

The focused tests passed: **19 passed, 1 skipped**. One delegated agent added proxy and results-thread tests; another reviewed the queue path. I integrated their work and verified the final patch. Two existing warning output tests each pass alone, but the second fails when run together because the shared `Display` singleton retains the first test’s warning.

A compatibility limitation remains: `deprecated(..., removed=True)` now raises in the main results thread rather than the worker, as required by proxying all deprecated calls.