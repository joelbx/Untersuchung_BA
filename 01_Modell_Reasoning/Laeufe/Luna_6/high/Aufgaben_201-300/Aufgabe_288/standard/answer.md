Updated move-out decisions to exit only when loading is complete and the active ID is missing from the mailbox slice. Conversation views choose the message or conversation ID using `isAlwaysMessageLabels`; both views receive the slice IDs and loading state from `MailboxContainer`.

Verification passed: the `ConversationView` suite (10 tests), mail workspace type check, and `git diff --check`.