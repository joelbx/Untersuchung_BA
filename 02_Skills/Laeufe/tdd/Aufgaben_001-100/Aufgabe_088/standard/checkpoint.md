# Checkpoint

Task: add optional field selection to getObject/getObjects and make empty fields mean full objects across MongoDB, Postgres, Redis.
Status: inspecting repository and tests; no implementation changes yet.
Constraints: test first, run relevant tests and full project suite, no downloads or external research.

Initial regression command: `./node_modules/.bin/mocha test/database.js --grep 'returns only requested fields|selects fields in input key order|returns every field when fields is empty'`
Result: blocked before tests by `Redis connection to 127.0.0.1:6379 failed - connect ECONNREFUSED 127.0.0.1:6379`. No test failure observed yet. Will use available local service or isolated module tests.

Implementation: optional fields in getObject/getObjects for Redis, MongoDB, PostgreSQL; empty or omitted fields return full objects in all four methods. Selected missing fields become null; wrappers return null for missing keys while field helpers retain their existing null-filled response for selected fields.

Verification:
- Red observed after starting local Redis: focused mocha run failed at `test/database/hash.js:138` because `getObject(key, ['name', 'missing'])` returned the full object.
- Focused regression command passed: 6 passing.
- `./node_modules/.bin/mocha test/database.js` passed: 267 passing (Redis backend).
- `./node_modules/.bin/eslint src/database/redis/hash.js src/database/mongo/hash.js src/database/postgres/hash.js test/database/hash.js` passed.
- `git diff --check` passed.
- `npm test` failed: 198 passing, 1 failing. Failure: `response status code should match one of the schema defined responses` at `test/api.js:416`; `GET /api/admin/extend/plugins` returned 500 after package request failed with `tunneling socket could not be established, statusCode=403`. The full suite remains unverified past this early failure due to `.mocharc.yml` bail mode and blocked external package access.
- MongoDB/PostgreSQL integration suites were not executed; those services are unavailable locally. Their changes were checked by inspection and lint.
