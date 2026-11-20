Updated forked display handling so `display`, `warning`, and `deprecated` calls reach the main process with their method names and exact caller arguments. The main process now runs the corresponding method, allowing warnings and deprecations from multiple workers to share its deduplication state.

Relevant tests passed: **20 passed, 1 skipped**.