Task: Fix widget room buttons and initial event focus in RoomView/RoomViewStore.
Status: Implemented RoomLoaded action and RoomView dispatch, moved widget option recomputation to RoomViewStore's RoomLoaded handler, and added initial-event fallback. Updated relevant tests. RoomView and RoomViewStore suites pass (66 tests); ESLint, Prettier, and git diff check pass. Full TypeScript check completed with unrelated existing errors in OIDC code and installed matrix-js-sdk types.
Constraints: Use local repository and existing tests only; preserve git history, index, and harness configuration.
