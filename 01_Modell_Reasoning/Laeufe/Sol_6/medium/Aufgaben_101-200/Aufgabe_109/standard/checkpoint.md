# Checkpoint

Task: Add a feature gated Polls history entry in RoomSummaryCard and a room associated PollHistoryDialog.
Status: Implemented and checked.
Changes: Registered feature_poll_history in Labs (off by default); added gated room card button and icon; added named PollHistoryDialog receiving roomId; added English string.
Verification: RightPanel and RoomHeaderButtons Jest suites passed (7 tests); ESLint passed; git diff --check passed. Full TypeScript check has an unrelated existing RoomCreate.tsx error: RoomState lacks findPredecessor.
