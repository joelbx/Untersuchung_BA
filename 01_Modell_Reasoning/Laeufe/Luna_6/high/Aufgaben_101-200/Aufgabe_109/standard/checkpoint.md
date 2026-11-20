# Checkpoint

Task: Add a feature-flagged “Polls history” action to RoomSummaryCard and a room-scoped PollHistoryDialog.

Implemented: Added the `PollHistoryDialog` named export with the requested props and BaseDialog title, and added the feature gated RoomSummaryCard button that passes the current room ID.

Verification:
- Existing poll tests passed: 75 tests across `MPollBody-test.tsx` and `PollCreateDialog-test.tsx`.
- ESLint, Prettier, and `git diff --check` passed for the changed files.
- `yarn lint:types` reached an existing TypeScript error in `src/components/views/messages/RoomCreate.tsx:50`: `RoomState.findPredecessor` is missing. No diagnostics pointed to these changes.
