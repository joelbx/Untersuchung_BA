Implemented optional `fields` arguments for `getObject` and `getObjects` across MongoDB, Postgres, and Redis. Empty or non-array `fields` values return full objects; specific fields are passed through to the existing helpers.

Verification was blocked: `./node_modules/.bin/mocha test/database/hash.js` could not connect to Redis at `127.0.0.1:6379`, so no tests ran. `git diff --check` passed.

The test attempt left an untracked `appendonlydir/` in the workspace.