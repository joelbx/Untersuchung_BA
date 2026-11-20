# Checkpoint

Task: validate admin file upload target directories using configured upload path; reject missing directories with HTTP 500 and `[[error:invalid-path]]`.

Status: investigating root cause. `rg` is unavailable (`/bin/bash: rg: command not found`); using local `find`/`grep`.

Root cause: src/controllers/admin/uploads.js passes params.folder directly to file.saveFileToLocal; src/file.js calls mkdirp on the upload parent, so a missing folder is created. Existing path validation uses [[error:invalid-path]].

Hypothesis/reproduction: added test/uploads.js integration case for a missing folder. First run failed because Redis was unavailable (ECONNREFUSED 127.0.0.1:6379). Started local ephemeral Redis; reran and got expected regression failure: HTTP 200 instead of 500 at test/uploads.js:410. The upload created the folder.

Fix: admin upload handler now resolves the requested folder under configured upload_path, rejects paths outside that base, and requires fs.stat to identify an existing directory before calling saveFileToLocal. Missing or non-directory targets produce [[error:invalid-path]] through the route's existing HTTP 500 error handling. Temporary upload cleanup still runs in finally.

Verification: ./node_modules/.bin/mocha test/uploads.js passed (43 passing, exit 0); ./node_modules/.bin/eslint src/controllers/admin/uploads.js test/uploads.js passed (exit 0); git diff --check passed (exit 0). The new missing-directory test failed before the fix with HTTP 200 vs expected 500, then passed after the fix. Local ephemeral Redis was used for test execution.
