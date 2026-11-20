Task: Fix widget action button refresh on room load and preserve permalink initial-event focus.
Completed:
- Added Action.RoomLoaded = "room_loaded".
- RoomView dispatches exactly { action: Action.RoomLoaded } from onRoomLoaded.
- RoomView initial event selection falls back to this.state.initialEventId when the store value is nullish.
- RoomViewStore handles RoomLoaded independently, recomputes ViewRoomOpts with buttons initialized to [], and updates state; navigation no longer recomputes options.
- Updated RoomViewStore test for direct RoomLoaded dispatch without prior ViewRoom.
Validation: `yarn test --runInBand test/stores/RoomViewStore-test.ts` passed (35 tests).
