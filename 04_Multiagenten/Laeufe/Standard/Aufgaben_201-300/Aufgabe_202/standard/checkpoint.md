Task: validate admin file upload target directory existence under configured upload path.
Status: implemented and reviewed.
Changes: src/controllers/admin/uploads.js stats the target directory before saving and returns [[error:invalid-path]] for missing paths or file targets. test/uploads.js covers missing and file targets with HTTP 500 assertions.
Verification: ESLint passed for changed JS files; git diff --check passed; isolated runtime check passed for missing, file, and existing directories. Existing upload integration tests were attempted but could not start because Redis on 127.0.0.1:6379 refused connections.
