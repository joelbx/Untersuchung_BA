# Upload directory validation

Task: reject admin file uploads when the requested folder does not exist beneath the configured upload path. Return `[[error:invalid-path]]` with HTTP 500 and keep path errors consistent.

Progress: added folder validation in `src/controllers/admin/uploads.js` before `saveFileToLocal`. It checks that the requested folder stays under the configured upload path and is an existing directory. Added admin endpoint regression tests for missing folders and file targets in `test/uploads.js`.

Verification: `./node_modules/.bin/mocha test/uploads.js` passed (43 tests). ESLint passed for both changed JavaScript files. `git diff --check` passed. The temporary Redis instance used by the test suite was stopped.
