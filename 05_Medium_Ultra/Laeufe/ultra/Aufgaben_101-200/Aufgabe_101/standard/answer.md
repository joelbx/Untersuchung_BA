Updated `listRemoveAll()` in the [Redis](/app/src/database/redis/list.js), [MongoDB](/app/src/database/mongo/list.js), and [PostgreSQL](/app/src/database/postgres/list.js) backends to accept an array of values. Each removes every requested match, preserves the order of remaining elements, and completes before a subsequent read. Added [regression tests](/app/test/database/list.js) for the reported example, repeated matches, and an absent value.

Verification: the Redis backed list suite passed (21 tests), and ESLint passed for all changed files. MongoDB and PostgreSQL integration tests were not run locally.

I delegated the backend changes to one agent and the test audit to another, then reviewed and verified the combined patch.