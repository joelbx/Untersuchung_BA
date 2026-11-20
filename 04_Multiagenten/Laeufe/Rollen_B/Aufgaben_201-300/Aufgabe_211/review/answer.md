VERDICT: FIX

**Code defect:** Image uploads can create a separate `-resized` file in [src/controllers/uploads.js](/app/src/controllers/uploads.js:111). Upload tracking records the original filename in [src/posts/uploads.js](/app/src/posts/uploads.js:61), and purge deletes only that tracked path in [src/posts/delete.js](/app/src/posts/delete.js:68). Purging the last post that references the image therefore leaves the resized file on disk. Delete both variants once the original has no remaining post references and preservation is disabled, then cover that case in the existing upload tests.

**TEST_ENVIRONMENT_PROBLEM:** `./node_modules/.bin/mocha test/posts/uploads.js test/topics/thumbs.js` exited 1 in the root setup hook: Redis connection refused at `127.0.0.1:6379` (0 passing, 1 failing). Start the configured local test Redis and rerun. `./node_modules/.bin/eslint --no-cache src/posts/delete.js src/posts/uploads.js src/topics/delete.js src/topics/thumbs.js test/posts/uploads.js test/topics/thumbs.js` exited 0.

This was a review only; no project code was changed.