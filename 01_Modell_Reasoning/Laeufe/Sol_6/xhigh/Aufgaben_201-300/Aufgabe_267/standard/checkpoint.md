# Checkpoint

Task: Fix widget room buttons and initial event focus in `/app`.

Plan: inspect `Action`, `RoomView`, and `RoomViewStore`; update the room-loaded dispatch and option recomputation; run the existing focused tests.

Status: implemented `Action.RoomLoaded`, its dispatch from `RoomView.onRoomLoaded`, store option recomputation on that action only, and the initial event fallback. Focused Jest suites pass (66 tests, 8 snapshots). ESLint, Prettier, and `git diff --check` pass. Full TypeScript check completes with errors in unchanged SDK/OIDC and other files, and no errors in edited files.
