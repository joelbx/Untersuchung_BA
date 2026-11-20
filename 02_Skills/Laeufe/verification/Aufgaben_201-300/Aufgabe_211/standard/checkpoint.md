# Checkpoint

Implemented orphaned upload deletion on post purge. Purge now checks reverse post associations after dissociation, removes unreferenced originals and resized copies, and respects the new ACP `preserveOrphanedUploads` setting (default 0). Added `Posts.uploads.deleteFromDisk` for string and array inputs, with type rejection, path containment and symlinked-directory checks. Added coverage for shared references, preservation, topic purge, direct deletion, traversal and symlinks.

Verification:
- `./node_modules/.bin/mocha test/posts/uploads.js test/posts.js --grep 'upload|purge posts and purge topic'`: exit 0, 22 passing.
- `./node_modules/.bin/eslint src/posts/uploads.js src/posts/delete.js test/posts/uploads.js`: exit 0.
- `git diff --check`: exit 0.

Initial check `./node_modules/.bin/mocha test/posts/uploads.js` failed with `connect ECONNREFUSED 127.0.0.1:6379`; started locally installed Redis and reran. A parallel check of `./node_modules/.bin/mocha test/posts.js --grep 'should purge posts and purge topic'` failed with `EADDRINUSE: address already in use 0.0.0.0:4567` because two Mocha processes tried to start NodeBB concurrently; the sequential combined run above passed.
