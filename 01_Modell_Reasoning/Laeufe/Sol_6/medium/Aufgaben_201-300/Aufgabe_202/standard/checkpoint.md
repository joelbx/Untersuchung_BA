# Upload path validation

- Status: complete.
- Goal: reject uploads to directories absent under the configured upload path with HTTP 500 and `[[error:invalid-path]]`.
- Changed `src/controllers/admin/uploads.js` to validate the requested directory under `nconf.get('upload_path')` before saving, and added a regression test in `test/uploads.js`.
- Verification: `mocha test/uploads.js` passed (42 tests); ESLint on both changed JavaScript files and `git diff --check` passed.
