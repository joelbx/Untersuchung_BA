Implemented the room load refresh and permalink focus fallback.

- Added `Action.RoomLoaded = "room_loaded"` and dispatches `{ action: Action.RoomLoaded }` after room state settles in [RoomView.tsx](/app/src/components/structures/RoomView.tsx).
- Moved widget option recomputation into the `RoomLoaded` handler in [RoomViewStore.tsx](/app/src/stores/RoomViewStore.tsx). The store test now verifies this works without a preceding `ViewRoom`.
- Initial event focus now falls back to the component’s existing `initialEventId` when the store value is nullish.

The targeted Jest suites passed: **2 suites, 63 tests, 8 snapshots**. ESLint, Prettier, and `git diff --check` passed. `yarn lint:types` stopped when Node ran out of heap during compilation, without reporting a source diagnostic.