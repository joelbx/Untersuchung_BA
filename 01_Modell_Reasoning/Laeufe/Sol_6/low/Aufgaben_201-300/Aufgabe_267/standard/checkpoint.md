# Checkpoint

Implemented `Action.RoomLoaded` and dispatch from `RoomView.onRoomLoaded`. `RoomViewStore` now computes widget button options only on that action, independently of `ViewRoom`. Initial event lookup falls back to local state when the store returns null or undefined. Updated the existing store test for the new dispatch behavior.

Verification: RoomView and RoomViewStore Jest suites passed (63 tests); updated RoomViewStore suite passed (35 tests). `git diff --check` passed.
