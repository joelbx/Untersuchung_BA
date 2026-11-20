# Checkpoint

Task complete: post purge now removes uploads with no remaining post references unless `preserveOrphanedUploads` is enabled. Added the ACP switch and English labels. `Posts.uploads.deleteFromDisk` accepts a path or list, rejects other top-level types, skips invalid paths, and blocks traversal through parent components, absolute paths, and linked directories.

Verification: `mocha test/posts/uploads.js test/posts.js test/topics.js` passed (342 tests); focused upload suite passed (20 tests); ESLint and `git diff --check` passed.
