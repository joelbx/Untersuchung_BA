# Token utilities checkpoint

Task: implement the internal token lifecycle interface in `src/api/utils.js` and verify it with relevant existing tests.

Completed: added `utils.tokens` lifecycle methods, persisted token metadata and three sorted indexes, preserved existing `utils.log` and `utils.getLastSeen` callers, and enabled bearer authentication for indexed tokens alongside legacy settings tokens. Added focused integration tests in `test/authentication.js`.

Verification: ESLint and `git diff --check` passed. `node_modules/.bin/mocha test/authentication.js --grep 'api tokens'` passed using a temporary local Redis instance, which was stopped afterward.
