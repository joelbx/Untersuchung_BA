# Checkpoint

Task: Add a feature-flagged “Polls history” entry point to `RoomSummaryCard`, opening the room-scoped `PollHistoryDialog`.

Implemented:
- Added `src/components/views/dialogs/polls/PollHistoryDialog.tsx` with the requested named export, prop type, and translated `BaseDialog` title.
- `RoomSummaryCard` now uses `useFeatureEnabled("feature_poll_history")` to gate the “Polls history” button and opens the dialog with `{ roomId: room.roomId }`.
- Added the poll icon mask to the room summary card stylesheet.

Verification:
- Existing poll tests: 2 suites passed, 75 tests and 12 snapshots passed.
- ESLint, stylelint, Prettier, and `git diff --check` passed.
- `yarn lint:types` failed on the unrelated existing error `src/components/views/messages/RoomCreate.tsx(50,38): Property 'findPredecessor' does not exist on type 'RoomState'.`
