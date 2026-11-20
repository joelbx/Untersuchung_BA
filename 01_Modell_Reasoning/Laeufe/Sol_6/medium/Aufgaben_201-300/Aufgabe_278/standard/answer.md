Updated the mailbox list so reloads wait for tracked backend mutations to finish. Element fetches now retry after failures, reject responses marked stale, and use the current page and query when calculating loading state.

Validation passed: the mail TypeScript check, `git diff --check`, and 20 existing mailbox tests across the elements and labels suites.