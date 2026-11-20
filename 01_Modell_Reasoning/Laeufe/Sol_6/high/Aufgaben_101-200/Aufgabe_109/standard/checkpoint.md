# Checkpoint

- Task: add flag-gated Polls history entry point to RoomSummaryCard and PollHistoryDialog.
- Status: implemented and verified.
- Changed: Messaging lab flag (default false), room card button and poll icon, named PollHistoryDialog receiving roomId, English string.
- Checks: Jest SettingsStore and PinnedMessagesCard suites passed (7 tests); ESLint, Prettier, Stylelint, and git diff --check passed.
- TypeScript: full tsc blocked by existing RoomCreate.tsx:50 RoomState.findPredecessor type error in untouched file.
