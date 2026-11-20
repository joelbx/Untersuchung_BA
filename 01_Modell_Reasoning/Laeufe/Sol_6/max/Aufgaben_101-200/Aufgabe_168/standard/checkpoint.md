# Progress checkpoint

- Traced Kick, Ban, and Mute through confirmation dialogs and Matrix requests.
- Added a synchronous member-scoped lock shared by the three controls, with pending UI state and cleanup on settle.
- Added regression tests for rapid activation, cross-button locking, cancellation, request failures, and switching members.
- Validation: UserInfo Jest suite passed (73 tests); ESLint, Prettier, and `git diff --check` passed.
- Repository-wide TypeScript check remains blocked by pre-existing errors in other files and installed SDK declarations; no diagnostics pointed at the changed files.
