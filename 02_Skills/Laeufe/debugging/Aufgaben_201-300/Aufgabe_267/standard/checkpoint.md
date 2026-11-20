# Checkpoint

Task: restore widget room buttons and initial event focus in RoomView and RoomViewStore.

Status: investigating root cause. `rg` is unavailable locally; using `find` and `grep`.

Root cause: `RoomViewStore.viewRoom()` invokes `RoomViewLifecycle.ViewRoom` before `RoomView.onRoomLoaded()` completes and before room data is necessarily ready. `RoomView` reads the options from the store, so this early result can be empty or stale. A later store update also clears `initialEventId` when `getInitialEventId()` is null. The working store update path emits `UPDATE_EVENT`, which `RoomView` already listens to.

Hypothesis confirmed by pre-fix focused tests: `room_loaded` dispatch leaves `viewRoomOpts.buttons` empty (store test exit 1), and initial RoomView load emits no `room_loaded` action (view test exit 1). Fix will compute options only in the new action, dispatch it from `onRoomLoaded`, and retain the view's initial event when the store has none.

Implementation: added `Action.RoomLoaded`, dispatch from `RoomView.onRoomLoaded`, store handler `setViewRoomOpts()` with `{ buttons: [] }` initial shape, removed option recomputation from `viewRoom`, and used nullish fallback for `initialEventId`.

Verification: `./node_modules/.bin/jest test/stores/RoomViewStore-test.ts test/components/structures/RoomView-test.tsx --runInBand --silent` passed (65 tests, 8 snapshots); Prettier check passed; `git diff --check` passed. `./node_modules/.bin/tsc --noEmit --jsx react` is still running at this checkpoint.

Type check update: `./node_modules/.bin/tsc --noEmit --jsx react` printed `FATAL ERROR: CALL_AND_RETRY_LAST Allocation failed - JavaScript heap out of memory` near 2 GB and exited 134. Type correctness remains unverified by that command; retrying with a larger local heap.

Final verification: targeted Jest suites passed (65 tests, 8 snapshots), targeted ESLint passed (exit 0), Prettier passed (exit 0), and `git diff --check` passed. `NODE_OPTIONS=--max-old-space-size=4096 ./node_modules/.bin/tsc --noEmit --jsx react` exhausted available RAM and swap while still running; terminated locally after about 1m46s (exit 143) to avoid exhausting the container. Full-project type correctness remains unverified. No dependencies were downloaded.

Constraints: local repository evidence only; do not change git history, index baseline, or harness configuration.
