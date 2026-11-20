# Checkpoint

Implemented optional `fields` support in `getObject` and `getObjects` for MongoDB, Postgres, and Redis. Empty or omitted fields now return complete objects through both wrappers and field helpers; selected missing fields are represented as `null`; wrappers return `null` for missing keys and preserve key order. Updated application and upgrade call sites to use `getObjects(keys, fields)`.

Validation: ESLint passes for changed JavaScript files. `test/database/hash.js` passes (53 tests) with a temporary local Redis server. The initial attempt without Redis failed to connect; no test failures remained after starting the local service.
