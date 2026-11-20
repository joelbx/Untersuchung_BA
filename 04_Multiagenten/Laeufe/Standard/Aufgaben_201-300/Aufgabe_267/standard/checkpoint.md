# Checkpoint

Issue: refresh widget room buttons after initial room load and preserve initial event focus.

Plan: inspect `Action`, `RoomView`, and `RoomViewStore`; update the load dispatch and option computation; run relevant existing tests.

Implemented: `RoomLoaded` is dispatched by `RoomView`; `RoomViewStore` computes `viewRoomOpts` only for that action; `RoomView` retains its current initial event ID when the store has none.

Verification: focused RoomView and RoomViewStore suites passed (64 tests); targeted ESLint and `git diff --check` passed. Full TypeScript check fails on unrelated existing SDK/OIDC and TabbedView type errors; none reference changed files.
