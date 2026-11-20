Task: implement incrObjectFieldByBulk in Mongo and Redis hash backends.
Status: implemented shared tuple/field validation, Mongo per-key $inc upserts, Redis pipelined atomic Lua/HINCRBY updates, and hash integration tests.
Verification: Redis hash suite 67 passing; focused bulk cases 3 passing after final Redis script change; ESLint passed; git diff --check passed. Mongo integration was unavailable because no mongod binary was present.
Constraints: use repository code and existing tests only; leave git history, index, and harness configuration intact.
