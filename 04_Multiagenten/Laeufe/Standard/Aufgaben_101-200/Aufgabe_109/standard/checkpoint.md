Task: Add flag-gated Polls history button to RoomSummaryCard and create PollHistoryDialog.
Status: Complete. Registered feature_poll_history as an opt-in Messaging labs setting, added translated button and poll icon, and added the named PollHistoryDialog component opened with the current roomId.
Validation: Right-panel Jest suites passed (11 tests); ESLint, Prettier, stylelint, and git diff --check passed. Full TypeScript check is blocked by an existing error in src/components/views/messages/RoomCreate.tsx:50 (RoomState.findPredecessor missing).
