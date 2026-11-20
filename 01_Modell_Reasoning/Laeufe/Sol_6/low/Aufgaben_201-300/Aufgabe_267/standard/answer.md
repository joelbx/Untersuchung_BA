Added `Action.RoomLoaded = "room_loaded"` and dispatch it when `RoomView` loads a room. `RoomViewStore` now updates widget button options on that action, including when no `ViewRoom` action preceded it. Initial event selection also falls back to `RoomView` state when the store has no event ID.

The relevant RoomView and RoomViewStore tests passed: 63 tests total.