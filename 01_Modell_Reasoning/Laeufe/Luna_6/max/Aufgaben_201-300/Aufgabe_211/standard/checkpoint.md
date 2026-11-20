# Checkpoint

Implemented uploaded-file cleanup during post purge. The cleanup preserves files referenced by other posts and obeys the `preserveOrphanedUploads` ACP setting. Added the Uploads setting and secured `Posts.uploads.deleteFromDisk` against invalid types and paths. Topic thumbnail deletion now respects post references.

Validation: upload and topic-thumbnail suites passed (52 tests); ESLint passed; changed JSON files parsed; `git diff --check` passed.
