Updated the worker display path so `display`, `warning`, and `deprecated` send their method name and exact caller arguments through the final queue. The results thread now invokes the matching method in the main process, where warnings and deprecations are deduplicated globally.

Verification: 20 tests passed, 1 skipped; `git diff --check` passed.