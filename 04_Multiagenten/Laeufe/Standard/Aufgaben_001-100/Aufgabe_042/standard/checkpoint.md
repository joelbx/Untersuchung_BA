Task: implement WebFinger endpoint in /app.
Status: complete. Added controller and route, integrated startup mounts, added focused tests.
Validation: node_modules/.bin/mocha test/well-known.js --reporter spec (5 passing); ESLint on changed JS files (passed); git diff --check (passed).
Note: repository integration tests require a database mock that reads and logs private config, so they were not run.
