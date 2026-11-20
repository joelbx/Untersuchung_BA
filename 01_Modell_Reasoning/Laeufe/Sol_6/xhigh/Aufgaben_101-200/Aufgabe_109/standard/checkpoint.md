# Checkpoint

Task: Add a flag-gated “Polls history” button to RoomSummaryCard and a PollHistoryDialog for the current room.

Implemented: Registered disabled Labs flag `feature_poll_history`; added the room summary button, icon, translated label, and named dialog interface; added RightPanel coverage for hidden and enabled/click behavior.

Verification: RightPanel tests pass (3/3). Prettier, ESLint, Stylelint, and `git diff --check` pass. Full TypeScript check reports one existing error in unchanged `src/components/views/messages/RoomCreate.tsx:50`: `RoomState.findPredecessor` is missing from the installed SDK type.

Status: Complete.
