Task: implement incrObjectFieldByBulk in Mongo and Redis hash backends.
Status: implemented and verified Redis focused tests (3 passing), existing increment tests (6 passing), and ESLint. Mongo backend uses per-key atomic $inc; Redis uses pipelined per-key Lua validation and HINCRBY. Mongo integration tests could not run because this workspace is configured for Redis.
Files: src/database/hash-bulk.js, src/database/mongo/hash.js, src/database/redis/hash.js, test/database/hash.js.
