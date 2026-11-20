Implemented optional `fields` support across MongoDB, Postgres, and Redis. Empty or omitted fields return full objects; selected missing fields are `null`; missing keys return `null` from `getObject` and `null` entries from `getObjects`, preserving input order. Updated callers to use `getObjects(keys, fields)`.

Validation: ESLint passes, and `test/database/hash.js` passes all 53 tests with Redis. MongoDB and Postgres were not integration tested.

Key changes: [Redis hash](</app/src/database/redis/hash.js:64>), [Mongo hash](</app/src/database/mongo/hash.js:64>), [Postgres hash](</app/src/database/postgres/hash.js:73>).