Updated move-out logic to use the active ID and the mailbox’s valid ID list after loading completes. Both conversation and message views now receive those values; conversation view uses the message ID for message-level labels.

Validation passed: 16 focused tests, TypeScript check, and `git diff --check`.