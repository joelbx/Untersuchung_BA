Implemented the room button refresh and permalink focus fixes.

- Added `Action.RoomLoaded = "room_loaded"` and dispatch it from `RoomView` after a room loads.
- Moved widget option recomputation out of room navigation and into the `RoomLoaded` handler, which stores `{ buttons: [...] }`.
- Added the `initialEventId` fallback to `RoomView` state when the store returns `null` or `undefined`.
- Updated the store test to verify `RoomLoaded` works without a preceding `ViewRoom`.

**Verification:** The RoomView component suite passed, and `yarn test --runInBand test/stores/RoomViewStore-test.ts` passed all 35 tests. `git diff --check` passed.