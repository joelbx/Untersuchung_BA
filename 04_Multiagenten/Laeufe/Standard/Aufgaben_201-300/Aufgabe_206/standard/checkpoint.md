# Checkpoint

Task: prevent concurrent topic creation by the same actor.
Completed: added per-user/session lock to topic create and reply controllers, released in finally.
Regression: six simultaneous authenticated POST /api/v3/topics requests; asserted one 200/ok, five 400/bad-request, and one increment each in category, user, and global topic counters.
Verification: targeted Mocha test passed with temporary local Redis; ESLint and git diff --check passed.
