Updated the display queue path so worker calls to `display`, `warning`, and `deprecated` reach the main process with their method name and exact caller arguments. The main process now applies shared warning and deprecation deduplication.

Relevant tests: **14 passed, 7 skipped**. `git diff --check` passed.