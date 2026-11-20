Updated the mailbox list so cache resets and fetches wait for item-modifying backend operations to finish. Loading now uses the current page and query parameters. Failed fetches schedule a retry after 2 seconds; responses marked stale are rejected and retried after 1 second.

Verification passed: 12 mailbox element tests, the mail TypeScript check, and `git diff --check`.