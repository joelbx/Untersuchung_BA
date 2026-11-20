Task: Fix room widget buttons and initial permalink focus in RoomView / RoomViewStore.

Plan: Inspect existing room load dispatch, action definitions, store state updates, and tests. Update the checked-out code, run the relevant existing tests, and record the results here.

Status: Complete. Implemented `Action.RoomLoaded`, dispatch from `RoomView.onRoomLoaded`, store option calculation on that action alone, and the initial event ID fallback. Added store and component regression tests.

Verification: RoomView and RoomViewStore Jest suites pass (67 tests combined); ESLint, Prettier, and `git diff --check` pass. A full TypeScript check with a 4 GB heap reports existing errors in OIDC/SDK and unrelated files, with no errors in changed files. The default 2 GB heap ran out of memory.
