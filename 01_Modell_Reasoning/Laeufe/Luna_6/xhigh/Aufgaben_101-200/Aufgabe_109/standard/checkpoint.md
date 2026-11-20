# Checkpoint

Task: Add a feature-flagged “Polls history” entry point to `RoomSummaryCard` and implement the room-scoped `PollHistoryDialog` public interface.

Progress: Registered `feature_poll_history` in Messaging Labs (default off), added the room summary button gated by that feature, and added the room-scoped `PollHistoryDialog` component.

Validation: Existing right panel Jest suite passed (3 suites, 69 tests). ESLint, Prettier, and Stylelint passed. `yarn lint:types` is blocked by an existing error in `src/components/views/messages/RoomCreate.tsx:50` (`RoomState.findPredecessor` is missing from the installed SDK type).
