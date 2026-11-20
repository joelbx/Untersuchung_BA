Added `lockPosting` to the [topic write controller](/app/src/controllers/write/topics.js). It guards create and reply requests by user ID or guest session ID, rejects overlapping requests with HTTP 400, and releases the lock after success or failure.

The [regression tests](/app/test/topics.js) confirm that one of eight concurrent creates succeeds, seven return `bad-request`, and topic and user counters increase once. The full topic suite passed (231 tests), as did ESLint.

The lock is process-local; separate server workers would need a shared lock for the same guarantee.