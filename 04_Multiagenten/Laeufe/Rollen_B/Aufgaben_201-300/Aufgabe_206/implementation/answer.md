Added `lockPosting` to the topic controller. Create and reply requests now share a per-user or guest-session lock, and overlapping requests are rejected with HTTP 400 and `status.code: "bad-request"`. The lock is released in `finally`.

A new concurrency test confirms one request returns HTTP 200 with `status.code: "ok"`, four overlapping requests are rejected, and the global, category, and user topic counts each increase by one. ESLint and the targeted tests pass.

The lock is process-local; deployments with multiple server processes need a shared lock to enforce the same behavior across processes.