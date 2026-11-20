Implemented uploaded file cleanup on post purge. The purge now dissociates the post’s uploads, deletes files with no remaining post references, and removes their resized variants. Administrators can retain these files with the new **Keep uploaded files when posts are purged** setting.

`Posts.uploads.deleteFromDisk` accepts a filename or an array, rejects other input types, and ignores invalid paths.

**Verification:** ESLint and `git diff --check` passed. The relevant upload tests could not run because Redis was unavailable (`ECONNREFUSED 127.0.0.1:6379`).