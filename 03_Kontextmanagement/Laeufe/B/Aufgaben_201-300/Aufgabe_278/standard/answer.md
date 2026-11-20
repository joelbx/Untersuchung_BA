Resolved the mailbox list reload issue in `/app`. Reloads now wait for tracked backend actions, failed requests retry after 2 seconds, and stale responses are discarded and retried after 1 second.

Validation passed: 23 relevant tests, TypeScript, Prettier, and `git diff --check`. This work item is complete.