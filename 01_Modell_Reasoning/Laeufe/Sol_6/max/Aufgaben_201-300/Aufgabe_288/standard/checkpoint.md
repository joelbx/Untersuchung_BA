# Checkpoint

Task complete: mail detail views now use the mailbox's visible element IDs and loading state to decide when to navigate back.

`useShouldMoveOut` calls `onBack` after element loading finishes if the active ID is undefined, empty, or absent from the list. `MailboxContainer` passes `elementIDs` and `loadingElements` to both views. `ConversationView` selects the message ID for `isAlwaysMessageLabels(labelID)` and otherwise checks the current conversation route ID. `MessageOnlyView` checks its message ID. Cache and label checks were removed from the hook.

Verification passed: 32 tests in hook, conversation view, and mailbox element suites; 7 mailbox hotkey tests; mail workspace TypeScript check; ESLint on changed files; Prettier check; `git diff --check`.
