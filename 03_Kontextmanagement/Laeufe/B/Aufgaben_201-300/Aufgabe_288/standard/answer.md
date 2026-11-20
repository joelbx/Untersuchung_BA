Resolved the move-out issue. The hook now calls `onBack` only after mailbox elements finish loading and the active ID is missing from the valid ID list. Both views receive that list and loading flag; conversation views use the message ID for message-level labels.

Verification passed: 16 targeted Jest tests, the mail TypeScript check, and `git diff --check`.