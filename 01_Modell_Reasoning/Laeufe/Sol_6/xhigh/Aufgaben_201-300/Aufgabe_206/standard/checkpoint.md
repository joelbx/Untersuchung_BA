# Checkpoint

Task: Prevent overlapping topic creation/reply requests from the same authenticated user or guest session.

Status: Implemented an actor-scoped posting lock in `src/controllers/write/topics.js`, released in `finally` for both create and reply. Added the English error message and a deterministic HTTP concurrency test that checks responses and topic/post counters.

Verification: `mocha test/topics.js --grep 'Topic.s \\.(post|reply)'` passed (22 tests); ESLint and `git diff --check` passed. A temporary local Redis instance was used for tests and shut down afterward.
