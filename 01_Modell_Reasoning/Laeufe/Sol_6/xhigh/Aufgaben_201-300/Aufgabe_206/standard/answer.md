Added a per-user or guest-session posting lock for topic creation and replies. Overlapping requests now receive HTTP 400 with `status.code: "bad-request"`; the accepted request returns `status.code: "ok"`. A concurrency test confirms that only one topic is created and the related counters increase once.

Verification: 22 topic creation and reply tests passed; ESLint and `git diff --check` passed.

The lock is process-local, so deployments with multiple app workers need a shared lock for the same guarantee across workers.