Added a per actor posting lock in [topics.js](/app/src/controllers/write/topics.js). Create and reply now reject overlapping requests from the same user or guest session, and release the lock when processing finishes or fails.

A new [concurrency test](/app/test/topics.js) verifies that a burst of five minimal create requests produces one `ok` response, four HTTP 400 `bad-request` responses, and exactly one increase in the topic counters. All three focused tests, ESLint, and the locale JSON check pass. The test runtime warned about the new [error message](/app/public/language/en-GB/error.json) because its generated language bundle has not been rebuilt.

The lock is held in process memory, so it does not coordinate separate server processes.