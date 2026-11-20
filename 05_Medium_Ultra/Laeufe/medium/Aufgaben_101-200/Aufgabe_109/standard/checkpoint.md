# Checkpoint

Task: add a feature-flagged Polls history button to RoomSummaryCard that opens PollHistoryDialog with the current roomId.
Status: implemented and reviewed.
Changes: registered feature_poll_history as a disabled-by-default Messaging labs feature; added the button, poll icon, translation, and named PollHistoryDialog component; wired Modal.createDialog with room.roomId.
Verification: 2 right-panel Jest suites passed (11 tests); ESLint, Prettier, Stylelint, and git diff --check passed. Full TypeScript check has an unrelated existing RoomCreate.tsx:50 error: RoomState.findPredecessor is missing.
