Updated the mailbox list to wait for tracked backend item operations before reloading. Failed fetches now retry after two seconds; responses marked stale are discarded and retried after one second. The loading selector uses the current page and query parameters.

Validation passed: the mail TypeScript check, all 12 mailbox element tests, and `git diff --check`.