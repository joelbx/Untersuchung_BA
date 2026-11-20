# Checkpoint

Task: Fix DeviceConfig loading and migration without destructive storage writes.

Implementation: DeviceConfig persists one config object with the required underscored keys. It loads current data without a write, migrates legacy credential arrays to userId-keyed objects, creates a token when missing, and serializes credentials from a Map. Unchanged setter calls skip storage writes.

Tests: `npx tsc --noEmit --pretty false` and `npx tsc -p test/tsconfig.json --noEmit --pretty false` passed. `npm run testclient` passed (3,061 assertions). `npm test` passed: workspace tests, 3,530 API assertions, and 3,061 client assertions.

Tooling notes: `rg` was unavailable (`/bin/bash: rg: command not found`), so repository searches used `find`/`grep`. An earlier `npm run testclient` attempt failed while rebuilding the local better-sqlite3 dependency: `fatal error: opening dependency file ./Release/.deps/Release/obj.target/sqlite3/gen/sqlite3/sqlite3.o.d.raw: No such file or directory`. A later attempt used the cached local binary and passed. No dependency was downloaded.
