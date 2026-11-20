# Checkpoint

Task: reject admin file uploads when the requested destination folder does not exist, using `[[error:invalid-path]]` and HTTP 500.

Implemented in `src/controllers/admin/uploads.js`: `uploadFile` resolves the requested folder against the configured `upload_path`, rejects paths outside that base, and checks that the destination exists and is a directory before calling the file saver. Validation failures use the existing invalid-path error and existing upload cleanup still runs.

Verification: `npx eslint src/controllers/admin/uploads.js` passed. `npx mocha test/uploads.js` could not run because Redis at `127.0.0.1:6379` was unavailable; the suite failed in its root setup before tests ran.
