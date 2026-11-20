Added `lockPosting` to the topic write controller. It guards create and reply requests by user ID or guest session, rejects overlapping requests with HTTP 400 and `status.code: "bad-request"`, and releases the lock after the operation.

A regression test checks that a concurrent burst creates one topic and increments the related counters once. It failed against the unguarded create path (`200 !== 400`), then passed with the fix. The full topic suite passed (230 tests); ESLint and `git diff --check` passed.

The lock is local to one server process, so it does not coordinate requests routed to different processes.