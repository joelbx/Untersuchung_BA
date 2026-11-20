Implemented automatic upload cleanup on post and topic purge. Purge now removes files with no remaining post references, including resized copies, while the new `preserveOrphanedUploads` ACP setting keeps them when enabled. [Posts.uploads.deleteFromDisk](/app/src/posts/uploads.js) accepts a string or array, rejects other input types, and ignores paths that escape the upload directory.

I delegated the ACP, purge, and test changes to native agents, then reviewed the integrated patch. The upload tests passed (25), the thumbnail tests passed (37), and ESLint and `git diff --check` passed.

Local thumbnails outside `/files` have no reverse post association data, so sharing of those paths cannot be detected.