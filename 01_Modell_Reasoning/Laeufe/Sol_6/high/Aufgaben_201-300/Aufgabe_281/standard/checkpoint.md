# Bulk object field increments

Implemented `incrObjectFieldByBulk` in MongoDB and Redis hash backends with shared input validation, per-key atomic updates, and cache invalidation for successful keys. Added integration tests for upsert, multiple fields, duplicate keys, invalid input, and partial failures. Verification: Redis hash suite passed (67 tests), ESLint passed, and `git diff --check` passed. The temporary local Redis instance was stopped.
