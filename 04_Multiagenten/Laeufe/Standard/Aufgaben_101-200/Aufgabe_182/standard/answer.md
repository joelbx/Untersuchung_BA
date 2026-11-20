Worker calls to `display`, `warning`, and `deprecated` now go through `proxy_display`, which sends the method name and exactly the caller-supplied arguments to the main process. The main process invokes the matching method, so warning and deprecation deduplication applies across workers.

The relevant tests passed: 22 passed, 7 skipped.