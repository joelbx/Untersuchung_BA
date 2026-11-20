# Checkpoint

Status: complete.

Implemented orphaned upload deletion on post purge, including resized copies. Shared files remain until their final post reference is purged. Added `preserveOrphanedUploads` (default off) in the ACP uploads settings. Topic thumbnail purge now follows the same orphan and preservation rules. `Posts.uploads.deleteFromDisk` accepts a string or array, rejects other top-level inputs, and ignores invalid, escaping, symlinked, or missing paths.

Verification: `node_modules/.bin/mocha test/posts.js test/topics.js` passed (343 tests); focused upload and thumbnail suites passed (56 tests). ESLint on changed JavaScript and `git diff --check` passed. Temporary local Redis instance used for tests was stopped.
