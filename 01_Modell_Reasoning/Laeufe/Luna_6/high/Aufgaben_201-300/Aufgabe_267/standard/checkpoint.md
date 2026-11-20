# Checkpoint

Implemented the `room_loaded` dispatcher action, dispatch from `RoomView` after room load, independent `RoomViewStore` handling to recompute `{ buttons: [...] }`, and the initial event fallback from RoomView state. Updated the store test to dispatch `RoomLoaded` without a preceding `ViewRoom`.

Verification: `yarn test --runInBand test/stores/RoomViewStore-test.ts` passed (35 tests). The combined RoomView/store run had the RoomView suite pass; the store test initially failed because the async dispatcher callback had not run yet, then passed after awaiting `untilDispatch`. `git diff --check` passed before the test edit.
