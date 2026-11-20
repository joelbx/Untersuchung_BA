Task: Fix widget room buttons and initial event focus on room load.
Status: Implemented Action.RoomLoaded, RoomView dispatch after load, RoomViewStore option refresh on that action, and initial event fallback. Updated focused tests. No delegation used.
Verification: RoomView and RoomViewStore Jest suites passed (64 tests); Prettier and git diff --check passed. Full TypeScript check reached unrelated pre-existing SDK/OIDC/TabbedView errors after increasing Node heap.
