# Checkpoint

## Task
Fix room widget button refresh and permalink focus behavior by adding a `RoomLoaded` dispatch and handling it in `RoomViewStore`.

## Current status
- Added `Action.RoomLoaded = "room_loaded"`.
- `RoomView` now dispatches the minimal `RoomLoaded` payload after room load state settles, and permalink focus falls back to its existing state value when the store returns nullish.
- `RoomViewStore` now recomputes module buttons only in a `RoomLoaded` handler; the existing store test verifies this works without a preceding `ViewRoom` action.
- Targeted Jest suites pass: 2 suites, 63 tests, 8 snapshots.
- Targeted ESLint, Prettier, and `git diff --check` pass.
- `yarn lint:types` could not complete because Node ran out of heap during the repository-wide TypeScript compile; no source diagnostic was reported before the OOM.
- Final diff review confirms changes are limited to the dispatcher action, room view/store behavior, and the existing store test.

## Constraints
- Use only repository code and existing tests.
- Do not alter git history, index baseline, or harness configuration.
