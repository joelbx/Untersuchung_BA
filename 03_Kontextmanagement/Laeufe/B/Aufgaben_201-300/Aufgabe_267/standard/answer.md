Updated `RoomView` and `RoomViewStore` so widget buttons are recomputed when the room finishes loading. Added `Action.RoomLoaded = "room_loaded"` and the initial event ID fallback for permalink focus.

The relevant tests passed: **65 tests and 8 snapshots**. The full TypeScript check remains blocked by unrelated OIDC and dependency type errors; it reported none in the changed files.