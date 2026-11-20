# Checkpoint

Task: prevent repeated Kick, Ban, and Mute activations in the user info panel.

Status: investigating root cause and existing tests. No fix attempted yet.

Root cause: Kick and Ban await confirmation before calling startUpdating; Mute also has no synchronous guard. The parent update counter is a spinner indicator, not a lock, and no button receives disabled state. A second activation can enter the handler while the first dialog or request is pending. Existing AccessibleButton sets both disabled and aria-disabled when given disabled=true.

Hypothesis: a synchronous shared lock in RoomAdminToolsContainer, entered before any dialog and released in finally, prevents duplicate and cross-action entry; individual buttons need a local fallback for standalone rendering.

Implementation: shared synchronous ref guard and pending state in room admin container, keyed by room/member; individual buttons use the same hook when rendered alone. Guard starts before confirmation and releases in finally after cancel, success, or failure. Kick/Ban/Mute now await the network operation; one error dialog comes from the guard on failure.

Verification: initial regression failed as expected (three dialogs opened). Focused Jest suite passed (72 tests) before final test-type cleanup. `./node_modules/.bin/tsc --noEmit --jsx react --pretty false` exits 2 with 51 lines of diagnostics, including missing declarations in matrix-js-sdk (`uuid`, `content-type`, `sdp-transform`) and existing OIDC API mismatches. A later run also found two new test typing errors; those were fixed and require recheck. No dependencies downloaded. ESLint and Prettier checks passed after the return type correction.

Final verification: `./node_modules/.bin/jest test/components/views/right_panel/UserInfo-test.tsx --runInBand --silent` passed, 72/72 tests and 6/6 snapshots. `./node_modules/.bin/eslint src/components/views/right_panel/UserInfo.tsx test/components/views/right_panel/UserInfo-test.tsx`, `./node_modules/.bin/prettier --check src/components/views/right_panel/UserInfo.tsx test/components/views/right_panel/UserInfo-test.tsx`, and `git diff --check` passed. `./node_modules/.bin/tsc --noEmit --jsx react --pretty false` exits 2 with 47 existing diagnostics (for example TS7016 missing uuid declarations in matrix-js-sdk and TS2724 missing OidcClientConfig in src/utils/AutoDiscoveryUtils.tsx). No diagnostics mention UserInfo.tsx or UserInfo-test.tsx. Whole-repository type status remains uncertain until those external/baseline errors are resolved.
