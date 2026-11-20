# Checkpoint

Implemented post purge upload cleanup in `src/posts/uploads.js` and connected it to `Posts.purge` in `src/posts/delete.js`. Purge now dissociates the post's uploads, checks reverse references, and deletes only orphaned files unless `preserveOrphanedUploads` is enabled. The deletion helper accepts a string or array, rejects other input types, skips invalid/traversing paths, and also removes resized image variants.

Added the `preserveOrphanedUploads` switch to ACP Uploads settings and English locale labels.

Verification: `eslint` passed on the changed JavaScript; `mocha test/posts/uploads.js` passed (16 tests) using a temporary local Redis instance. `git diff --check` and locale JSON parsing passed.
