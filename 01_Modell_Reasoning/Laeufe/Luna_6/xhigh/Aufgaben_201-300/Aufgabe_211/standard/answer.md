Implemented configurable upload cleanup on post purge. Purged posts now remove uploaded files and resized variants when no other post references them. The ACP checkbox uses `preserveOrphanedUploads`; preservation defaults off, so cleanup is enabled by default.

Added `Posts.uploads.deleteFromDisk` for single paths or arrays. It rejects unsupported input types and skips invalid paths, including traversal and symlink escapes.

**Validation:** ESLint, syntax checks, JSON parsing, and `git diff --check` pass. The existing upload test could not initialize because Redis refused the connection at `127.0.0.1:6379`.

Changed: [uploads.js](/app/src/posts/uploads.js:41), [delete.js](/app/src/posts/delete.js:50), [uploads settings](/app/src/views/admin/settings/uploads.tpl:16), [defaults.json](/app/install/data/defaults.json:37).