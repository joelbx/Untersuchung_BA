Implemented automatic upload cleanup on post purge.

- Added [Posts.uploads.deleteFromDisk](/app/src/posts/uploads.js:100) for single paths and arrays, with input validation and traversal protection.
- [Post purge](/app/src/posts/delete.js:73) deletes orphaned uploads and resized copies while preserving files referenced by other posts.
- Added the `preserveOrphanedUploads` ACP option, disabled by default, on the [Uploads settings page](/app/src/views/admin/settings/uploads.tpl:23).
- Updated topic thumbnail cleanup to honor shared references and the preserve setting.

Validation passed: 52 upload and thumbnail tests, ESLint, JSON parsing, and `git diff --check`.