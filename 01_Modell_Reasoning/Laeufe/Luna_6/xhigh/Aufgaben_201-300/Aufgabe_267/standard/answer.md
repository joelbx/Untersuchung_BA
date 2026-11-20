Implemented the room-loaded widget refresh and permalink focus fallback.

- Added public `Action.RoomLoaded = "room_loaded"` and dispatches exactly `{ action: Action.RoomLoaded }` from `RoomView` after room load.
- Moved button option recomputation to `RoomViewStore.setViewRoomOpts()`, triggered only by `RoomLoaded`.
- Initial event focus now falls back to `this.state.initialEventId` when the store value is nullish.
- Updated the store test to verify `RoomLoaded` works without a prior `ViewRoom`.

The focused suites passed: **63 tests across 2 suites**. ESLint, Prettier, and `git diff --check` passed. `yarn lint:types` ran out of Node heap before completing. Checkpoint: [.codex-role-output/checkpoint.md](/app/.codex-role-output/checkpoint.md).