# Work checkpoint

Task: Remove uploads exclusively referenced by purged posts, with an ACP preservation option and safe disk deletion API.

Status: Implemented and verified.

Changes:
- Post purge dissociates uploads, then deletes orphaned originals and resized copies unless `preserveOrphanedUploads` is enabled.
- Added the ACP upload setting and default value 0.
- Added `Posts.uploads.deleteFromDisk` for string and array inputs with lexical and symlink-directory traversal checks.
- Added tests for shared uploads, topic purge, preservation, invalid input, traversal, and symlink traversal.

Checks:
- Initial `./node_modules/.bin/mocha test/posts/uploads.js` failed before tests: `Error: connect ECONNREFUSED 127.0.0.1:6379` (local Redis unavailable). Started the installed local Redis server and reran.
- `./node_modules/.bin/mocha test/posts/uploads.js test/topics.js`: 249 passing.
- `./node_modules/.bin/mocha test/posts/uploads.js` after final symlink test: 21 passing.
- `./node_modules/.bin/eslint src/posts/delete.js src/posts/uploads.js test/posts/uploads.js && git diff --check`: passed.
- `rg` unavailable (`/bin/bash: rg: command not found`); used `find` and `grep`.
