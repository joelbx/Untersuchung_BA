# Checkpoint

Implemented optional `fields` arguments for MongoDB, Postgres, and Redis `getObject` / `getObjects`, forwarding selection to the existing field helpers. Normalized non-array field inputs to `[]`; empty lists return full stored objects. Field helper behavior retains `null` for requested absent fields and requested fields preserve input key order.

Verification: `./node_modules/.bin/mocha test/database/hash.js` could not start because the configured Redis service at `127.0.0.1:6379` is unavailable (`ECONNREFUSED`). No test cases ran.
