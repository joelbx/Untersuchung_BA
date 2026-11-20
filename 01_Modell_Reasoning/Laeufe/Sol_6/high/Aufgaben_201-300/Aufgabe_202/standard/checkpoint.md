# Upload path validation checkpoint

- Task: reject admin file uploads when the requested folder does not exist under the configured upload path.
- Initial state: working tree clean; repository is NodeBB; upload code and tests are under `src` and `test`.
- Found: `src/controllers/admin/uploads.js` passed folders to `file.saveFileToLocal`, which creates missing directories.
- Changed: admin upload now requires a folder value and an existing directory under the configured upload path; invalid folders return `[[error:invalid-path]]` through the existing HTTP 500 error path.
- Added integration coverage for missing folders, file paths used as folders, and omitted folders.
- Verified: `test/uploads.js` passed (44 tests); ESLint and `git diff --check` passed. A broader run also passed upload tests but hit the existing `test/file.js` read-only copy assertion because this workspace runs as root.
