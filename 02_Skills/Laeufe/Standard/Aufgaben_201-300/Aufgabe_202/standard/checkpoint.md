# Checkpoint

Task: Validate admin file upload target directories against the configured upload path and return HTTP 500 with `[[error:invalid-path]]` for missing directories.

Status: Complete.

Changes:
- `src/controllers/admin/uploads.js`: Check that the requested folder is within the configured upload path and that `fs.promises.stat` identifies it as a directory before saving. Missing paths and paths whose parent is not a directory produce `[[error:invalid-path]]`.
- `test/uploads.js`: Added integration tests for a missing target folder and a file used as the target folder.

Checks:
- `node_modules/.bin/eslint src/controllers/admin/uploads.js test/uploads.js` — passed.
- `git diff --check` — passed.
- `node_modules/.bin/mocha test/uploads.js --grep 'admin uploads' --timeout 30000` — 18 passing.
- `node_modules/.bin/mocha test/uploads.js --timeout 30000` — 43 passing.

Environment notes:
- `rg` is unavailable (`/bin/bash: rg: command not found`); used `find` and `grep` for repository searches.
- Initial `node_modules/.bin/mocha test/uploads.js --grep 'admin uploads' --timeout 30000` failed before tests with `connect ECONNREFUSED 127.0.0.1:6379`. Started the installed `redis-server` temporarily, reran the tests successfully, then stopped it.
