# Checkpoint

Implemented local image cleanup for group covers and thumbnails, user covers and avatars, and account deletion. User image removal now scans legacy and timestamped .png, .jpeg, .jpg, and .bmp variants, validates upload URLs against the profile upload directory, clears the associated database fields, and returns previous avatar fields. Group cover removal accepts both stored raw upload URLs and site-subpath URLs, and clears cover metadata. Missing files (ENOENT) are ignored; other unlink errors propagate. Socket removal hooks remain in place.

TDD: `./node_modules/.bin/mocha --reporter spec test/image-cleanup.js` passed (5 tests). Each added behavior was observed failing before its corresponding fix. `./node_modules/.bin/eslint src/groups/cover.js src/socket.io/user/picture.js src/socket.io/user/profile.js src/user/delete.js src/user/picture.js test/image-cleanup.js` passed. `git diff --check` passed.

Full suite: `npm test` was executed after the patch. It failed in the before-all hook for "should correctly compare a password and a hash" with `Error: connect ECONNREFUSED 127.0.0.1:6379`. The Redis test database is unavailable locally, so the remaining integration tests could not run. No dependencies were downloaded.
