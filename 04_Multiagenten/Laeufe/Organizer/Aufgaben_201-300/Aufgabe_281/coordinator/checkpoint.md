Task: implement incrObjectFieldByBulk in Mongo and Redis hash backends.
Status: implemented shared validation and Mongo/Redis bulk increment methods; added hash integration tests.
Verification: Redis-backed hash suite passed (67 tests); ESLint and git diff --check passed; Mongo method smoke test with a stub client passed. MongoDB server was unavailable for an integration run.
Delegation: none.
Constraints: preserve per-key atomicity, safe integer validation, cache behavior, and no-op empty input.
