# Checkpoint

- Task: Add a flag-gated “Polls history” entry in `RoomSummaryCard` and a public `PollHistoryDialog` that receives the current `roomId`.
- Status: Added the disabled-by-default Messaging Labs flag, the conditional room card button, the public dialog, English strings, and the poll icon style. Added tests for the Labs entry and the room card dialog flow.
- Validation: RightPanel (3 tests), LabsUserSettingsTab (3 tests), and SettingsStore (1 test) passed. Targeted ESLint, Prettier, Stylelint, and `git diff --check` passed.
- TypeScript: Full `tsc --noEmit --jsx react` reports one error in unchanged `src/components/views/messages/RoomCreate.tsx:50` because the installed SDK's `RoomState` type lacks `findPredecessor`.
