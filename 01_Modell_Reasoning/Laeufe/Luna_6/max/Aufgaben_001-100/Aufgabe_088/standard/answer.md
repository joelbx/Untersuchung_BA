Implemented field selection across MongoDB, Postgres, and Redis. Empty or omitted `fields` returns full objects; missing requested fields are `null`, missing keys remain falsy in `getObject(s)`, and `getObjects` preserves input order. Updated messaging, posts, topics, categories, and groups to call `getObjects(keys, fields)` directly.

Validation passed: 9 existing hash tests, mock-client checks across all three backends, ESLint, syntax checks, and `git diff --check`. The backend checks used mocks rather than live database services. The pre-existing untracked `appendonlydir/` was left untouched.

Updated implementations: [MongoDB]( /app/src/database/mongo/hash.js:64), [Postgres]( /app/src/database/postgres/hash.js:73), [Redis]( /app/src/database/redis/hash.js:64).