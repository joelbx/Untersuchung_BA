# Checkpoint

Task complete: the user info panel now uses a synchronous, member-scoped lock for Kick, Ban, and Mute. All three buttons set disabled and aria-disabled while confirmation or a request is pending; cancellation and failure release the lock, and failures show one action-specific error dialog. Existing request update tracking now awaits settlement.

Validation: UserInfo Jest suite passed (72 tests, 6 snapshots). ESLint for both changed TypeScript files and git diff --check passed. Full TypeScript check still reports 47 existing errors outside UserInfo/UserInfo-test; it reports none in changed files.

Delegation: none.
