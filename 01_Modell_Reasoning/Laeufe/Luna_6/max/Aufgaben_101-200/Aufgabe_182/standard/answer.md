Implemented worker display proxying and main process dispatch:

- Added `proxy_display` to route `display`, `warning`, and `deprecated` calls with their original method name and caller supplied arguments.
- Updated `DisplaySend`, the queue sender, and the result thread to preserve and invoke the requested method.
- Updated the existing fork display assertion to check the method name and absence of synthesized kwargs.

**Verification:** The display and queue tests passed (11 passed, 1 skipped); both warning tests passed when run individually. `git diff --check` passed. The combined direct pytest run encountered shared `Display` deduplication state between warning tests. `ansible-test` could not start because pytest does not recognize `-n` in this environment.