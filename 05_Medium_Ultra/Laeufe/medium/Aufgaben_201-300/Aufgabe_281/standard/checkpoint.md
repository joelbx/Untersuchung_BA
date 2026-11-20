Task: implement incrObjectFieldByBulk for MongoDB and Redis hash backends.
Status: implemented and verified locally.
Changes: shared tuple/field/increment validation; Mongo unordered per-key $inc bulk updates; Redis pipelined per-key atomic Lua scripts using HINCRBY; per-key cache invalidation; integration tests for creation, multiple fields, failures, invalid input, empty input, and concurrency.
Verification: Hash methods suite passed against temporary local Redis; ESLint and git diff --check passed. MongoDB integration was not run because mongod is unavailable locally.
Constraints respected: local code/tests only; no git history, index baseline, or harness changes.
