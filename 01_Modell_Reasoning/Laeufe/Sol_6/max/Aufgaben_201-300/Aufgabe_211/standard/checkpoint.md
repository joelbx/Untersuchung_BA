# Checkpoint

Completed purge-time cleanup for orphaned post uploads (including resized copies), a default-off `preserveOrphanedUploads` ACP option, a validated `Posts.uploads.deleteFromDisk` interface, and shared-file-safe topic thumbnail purging. Added regression tests for single/list deletion, bad inputs, traversal and symlink paths, shared files, preservation, resized copies, and whole topic purge.

Verification: focused upload and thumbnail suites 59 passing; post suite 114 passing; topic suite 231 passing; ESLint and `git diff --check` clean. A combined post-plus-topic run had 336 passing and one preexisting order-sensitive thumbnail test failure: it hardcodes topic ID 4 as nonexistent, but earlier suites created ID 4. The suites pass when run separately. Temporary Redis was started for tests and has been stopped.
