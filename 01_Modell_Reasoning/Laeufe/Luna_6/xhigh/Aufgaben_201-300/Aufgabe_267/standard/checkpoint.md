# Checkpoint

Issue: room widget action buttons can be missing or stale after room entry; permalink focus may also fail.

Requirements to implement:
- Add `Action.RoomLoaded` with value `room_loaded`.
- Dispatch exactly `{ action: Action.RoomLoaded }` globally after the initial room load completes.
- Resolve initial event focus from `roomViewStore.getInitialEventId()`, falling back to `this.state.initialEventId` only for nullish store values.
- `RoomViewStore.setViewRoomOpts()` stores a `viewRoomOpts` object whose `buttons` property is an array.
- Handle `RoomLoaded` in the store dispatch manager, independently of a prior `ViewRoom`; recompute options only for this action.

Files identified: `src/components/structures/RoomView.tsx`, `src/stores/RoomViewStore.tsx`, and their existing tests.

Completed:
- Added `Action.RoomLoaded` (`room_loaded`) and dispatches its exact action-only payload from `RoomView.onRoomLoaded()`.
- Added `RoomViewStore.setViewRoomOpts()` and invoke it only for `Action.RoomLoaded`, independently of `ViewRoom`.
- Made permalink initial-event selection fall back to `RoomView` state when the store value is nullish.
- Updated the existing store test to verify `RoomLoaded` works without `ViewRoom`.

Verification:
- `yarn test --runInBand test/stores/RoomViewStore-test.ts test/components/structures/RoomView-test.tsx`: passed (2 suites, 63 tests).
- Focused ESLint and Prettier checks: passed.
- `yarn lint:types` could not complete because Node ran out of heap near 2 GB; stopped after the OOM.
