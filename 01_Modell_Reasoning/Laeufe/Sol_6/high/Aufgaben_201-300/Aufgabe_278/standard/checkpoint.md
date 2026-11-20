# Checkpoint

Resolved mailbox list reload timing and freshness handling. Pending backend actions are counted across label, move, star, mark as, empty label, permanent delete, and undo flows; list requests wait for the count to reach zero, including after cache resets. Results returned during a pending action or marked stale are discarded and retried after one second. Fetch errors retry after two seconds. Loading now uses the current page and query context.

Validation: mailbox element suite 16/16 passed; mail TypeScript check passed; ESLint, Prettier, and git diff checks passed. No external research or downloads.
