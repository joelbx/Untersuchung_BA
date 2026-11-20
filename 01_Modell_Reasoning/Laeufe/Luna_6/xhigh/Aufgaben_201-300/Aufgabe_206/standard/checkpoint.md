# Checkpoint

Task: Prevent overlapping topic creation requests by the same actor from creating duplicate topics.

Implemented in `src/controllers/write/topics.js`: A synchronous per-actor lock covers topic creation and replies. A collision throws the provided message and the API route returns HTTP 400 with `status.code: "bad-request"`; successful topic creation keeps the existing 200/`ok` response. `finally` always releases acquired locks.

Verification: ESLint passed. All 229 tests in `test/topics.js` passed using a temporary local Redis instance, which was shut down after the test run. `git diff --check` passed.
