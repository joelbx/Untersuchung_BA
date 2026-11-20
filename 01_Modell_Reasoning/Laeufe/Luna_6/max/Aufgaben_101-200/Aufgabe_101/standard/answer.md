Implemented multi value removal across all three database adapters:

- [MongoDB](/app/src/database/mongo/list.js:53) removes every requested value in one update.
- [PostgreSQL](/app/src/database/postgres/list.js:93) filters the list while preserving element order.
- [Redis](/app/src/database/redis/list.js:27) removes values in a transaction.
- Added a regression test for removing `['b', 'd']` and immediately reading `['a', 'c', 'e']` in [test/database/list.js](/app/test/database/list.js:185).

Syntax checks, ESLint, and `git diff --check` passed. I did not run the database integration test because its fixture loads `/app/config.json`, which would read local credentials. The requested checkpoint is in `.codex-role-output/checkpoint.md`.