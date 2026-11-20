Implemented orphaned upload cleanup in [/app/src/posts/uploads.js](/app/src/posts/uploads.js) and the purge paths. Purging a post now deletes its uploads and resized copies only when no other post references them. Topic thumbnails follow the same rule. Administrators can retain files with the new **Keep uploaded files when their posts are purged** setting in the ACP.

`Posts.uploads.deleteFromDisk` accepts a path or list of paths, rejects other input types, and ignores unsafe or invalid paths.

Verification: **343 post and topic tests passed**; ESLint and `git diff --check` passed.