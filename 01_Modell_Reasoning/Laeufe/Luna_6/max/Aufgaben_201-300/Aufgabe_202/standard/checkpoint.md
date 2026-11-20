# Checkpoint

Issue: reject admin file uploads when their requested destination folder does not exist, using HTTP 500 and `[[error:invalid-path]]`.

Implemented in `src/controllers/admin/uploads.js`: resolve the requested folder under configured `upload_path`, reject paths outside that root, and verify the target is a directory before `saveFileToLocal`. Missing and non-directory targets use the shared invalid-path token. Temp upload cleanup remains in `finally`.

Verification: ESLint, `node --check`, and `git diff --check` passed. The existing `test/uploads.js` setup reads and logs `config.json`, which may contain credentials, so that integration test was not run.
