Task: Prevent repeated Kick, Ban, and Mute admin actions in the user info panel.
Status: Implemented and verified.
Changes: Added a synchronous per-member admin action lock shared by the three controls. It begins before confirmation, drives disabled and aria-disabled, and releases after cancel, success, or failure. Network failures show one ErrorDialog. Added regression tests for rapid mouse/keyboard activation, cross-button locking, cancellation, failure recovery, and switching members.
Verification: UserInfo Jest suite passes (73 tests); ESLint and Prettier pass on changed files. Full TypeScript check remains blocked by existing errors in unrelated SDK and repository files; no UserInfo errors reported.
