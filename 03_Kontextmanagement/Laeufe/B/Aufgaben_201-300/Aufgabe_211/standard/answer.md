Post and topic purges now delete uploads that have no remaining post references. Shared files stay on disk, and administrators can enable **Keep files after their last associated post is purged** in the ACP. `Posts.uploads.deleteFromDisk` accepts a path or list of paths and rejects unsafe paths.

Verification: **20 upload tests passed**; ESLint and diff checks passed.