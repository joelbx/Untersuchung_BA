# Checkpoint

Issue: concurrent POST /api/v3/topics requests from the same authenticated user can create duplicate topics.

Implemented: `src/controllers/write/topics.js` exports `lockPosting(req, error)` and uses the actor lock across topic creation and replies. A `finally` block releases it on success or failure. Added the posting-in-progress message to en-GB and en-US source translations.

Regression coverage: `test/topics.js` sends eight simultaneous authenticated create requests with only `cid`, `title`, and `content`; it checks one HTTP 200/`ok`, seven HTTP 400/`bad-request`, and one increment in global, category, and user counters. A second test verifies a failed create releases the lock.

Verification: full `test/topics.js` suite passed (231 tests). ESLint, syntax/JSON parsing, and `git diff --check` passed. Redis was started locally for the test run.
