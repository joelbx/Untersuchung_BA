Task: Fix RoomView initial load dispatch, RoomViewStore widget button options, and initial event focus fallback.
Status: Implemented and verified. RoomLoaded action dispatches after room load; RoomViewStore recomputes button options only on RoomLoaded; initial event ID falls back to RoomView state.
Verification: Focused suites pass (66 tests); RoomView suite passes again after final assertion refinement (30 tests). Prettier, ESLint, and git diff --check pass. Full TypeScript check completes with pre-existing dependency/OIDC and unrelated source errors; no errors reported in changed files.
Constraints: Local repository and tests only; git history, index baseline, and harness configuration untouched.
