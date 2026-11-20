Task: Automatic upload cleanup on post/topic purge with ACP retention option.
State: Implemented safe Posts.uploads.deleteFromDisk, purge-time orphan detection/deletion, default preserveOrphanedUploads=0, ACP toggle and English label, and focused tests.
Verification: eslint passed for changed JS; mocha test/posts/uploads.js test/topics/thumbs.js passed (54 tests); git diff --check passed.
Delegation: none.
