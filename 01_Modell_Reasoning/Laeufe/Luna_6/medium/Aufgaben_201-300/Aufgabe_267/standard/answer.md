Implemented the room loaded refresh and permalink fallback.

- Added `Action.RoomLoaded = "room_loaded"`.
- `RoomView` dispatches `{ action: Action.RoomLoaded }` when a room loads.
- `RoomViewStore` recomputes `viewRoomOpts` on that action, independently of `ViewRoom`.
- Initial event focus falls back to `this.state.initialEventId` when the store value is nullish.
- Updated the store test to cover `RoomLoaded` without a preceding navigation action.

Validation passed: `yarn test --runInBand test/stores/RoomViewStore-test.ts` (35 tests).