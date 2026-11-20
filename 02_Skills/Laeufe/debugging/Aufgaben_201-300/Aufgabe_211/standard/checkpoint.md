# Checkpoint

Root cause: `Posts.purge` dissociated upload paths but never removed the files. Topic purge also had a separate thumbnail deletion path that could remove files still referenced by other posts. Existing upload path validation used a string prefix check that could accept sibling paths.

Reproduction: added regression tests for `deleteFromDisk`, exclusive and shared uploads, preserved uploads, resized companions, and shared thumbnails. Before implementation, `node_modules/.bin/mocha test/posts/uploads.js --grep 'deleteFromDisk|Purge disk cleanup'` failed with `TypeError: posts.uploads.deleteFromDisk is not a function`. The first attempt to run this command was blocked by `Error: connect ECONNREFUSED 127.0.0.1:6379`; starting the locally installed Redis server resolved that environment issue.

Implementation: purge checks remaining upload associations after dissociation, deletes only orphaned files and resized companions, and respects `preserveOrphanedUploads`. Added ACP checkbox and default. `deleteFromDisk` accepts one path or an array, rejects other top-level inputs, ignores invalid entries, and checks canonical paths before deletion. Topic thumbnail purge now keeps files used by posts in other topics and respects preservation.

Verification:
- `node_modules/.bin/mocha test/posts/uploads.js test/topics/thumbs.js` — 55 passing.
- `node_modules/.bin/mocha test/topics.js test/posts.js --grep '[Pp]urge'` — 21 passing.
- `node_modules/.bin/eslint src/posts/uploads.js src/posts/delete.js src/topics/delete.js src/topics/thumbs.js test/posts/uploads.js test/topics/thumbs.js` — passed.
- `git diff --check` — passed.
