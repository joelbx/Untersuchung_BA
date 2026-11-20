Post and topic purges now delete uploads with no remaining post references, including resized image copies. The ACP uploads page has a `preserveOrphanedUploads` switch to keep them on disk. `Posts.uploads.deleteFromDisk` accepts one path or a list and rejects unsupported inputs while ignoring invalid paths.

Verification: 22 upload tests passed; ESLint and `git diff --check` passed.