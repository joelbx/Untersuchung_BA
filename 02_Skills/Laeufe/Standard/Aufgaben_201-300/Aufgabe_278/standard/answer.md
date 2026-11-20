Updated the mailbox list so requests wait for tracked backend operations to finish. Failed queries retry after 2 seconds; stale responses are discarded and retried after 1 second. The loading selector now uses the current page and query parameters.

Added focused retry and lifecycle tests. TypeScript, the relevant mailbox tests, and `git diff --check` passed.