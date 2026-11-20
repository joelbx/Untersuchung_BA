# Checkpoint

Resolved mailbox element reload and freshness handling. Added pending backend action tracking to mailbox mutations, delayed list effects until the counter returns to zero, and implemented separate timed retries for failed and stale element queries. The loading selector now uses page/query context. Validation: mail TypeScript check passed; existing Mailbox.labels and Mailbox.elements Jest suites passed (20 tests); git diff --check passed.
