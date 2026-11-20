Task: Resolve voice broadcast liveness mapping and update behavior.
Status: Implemented info-state liveness utility and routed playback liveness updates through setInfoState. No delegation used.
Constraints: Keep liveness derived only from infoState; run relevant existing tests.
Verification: Focused Jest suites passed (50 tests); ESLint and Prettier passed. Full TypeScript check reports existing MatrixClient API errors in unrelated files.
