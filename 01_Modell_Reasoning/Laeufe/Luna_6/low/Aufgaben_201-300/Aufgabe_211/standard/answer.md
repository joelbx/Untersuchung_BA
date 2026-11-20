Implemented configurable cleanup of orphaned uploads on post purge.

- Added `Posts.uploads.deleteFromDisk` for a filename or list of filenames. It rejects non-string/non-array inputs and ignores paths outside the uploads files directory.
- Post purge now deletes uploads with no remaining post references unless `preserveOrphanedUploads` is enabled.
- Added the preserve option to the ACP and English locale files, plus tests for deletion and unsafe paths.

ESLint and `git diff --check` passed. The upload tests could not run because Redis at `127.0.0.1:6379` is unavailable.