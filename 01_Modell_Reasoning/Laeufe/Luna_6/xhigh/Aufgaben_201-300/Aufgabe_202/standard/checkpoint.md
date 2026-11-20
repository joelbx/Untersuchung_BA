# Checkpoint

Task: Fix admin file uploads to reject a non-existent target directory with `[[error:invalid-path]]` and HTTP 500, checking relative to the configured upload path.

Implemented in `src/controllers/admin/uploads.js`: the admin generic file upload validates that the requested folder resolves under `nconf.get('upload_path')` and is an existing directory before saving. Missing/non-directory/out-of-base paths use `[[error:invalid-path]]`, and the existing cleanup path removes the temporary upload.

Verification: `./node_modules/.bin/eslint src/controllers/admin/uploads.js` passed. `npm test -- --grep 'admin uploads' test/uploads.js` passed (16 tests) with a temporary local Redis service. The first test attempt could not connect because Redis was not running; the local service was stopped after the successful run.
