# Checkpoint

Resolved: `useShouldMoveOut` now navigates back only after element loading finishes and the active ID is absent from the supplied element IDs. `MailboxContainer` passes the IDs and loading state to both detail views. `ConversationView` selects message ID for labels classified by `isAlwaysMessageLabels`, and conversation ID otherwise. Cache and label-membership exit heuristics were removed.

TDD: New hook tests failed before implementation for missing/empty/outside IDs and loading transition. New conversation-view test failed before implementation for the message-level-label ID choice. Both passed after the patch.

Verification:
- `../../node_modules/.bin/tsc --noEmit --pretty false` from `applications/mail`: passed.
- `../../node_modules/.bin/jest --runInBand --coverage=false --forceExit` from `applications/mail`: 92 suites passed; 832 tests passed, 1 skipped. Existing tests emitted React/jsdom warnings and crypto asm.js warnings.
- Changed-file `eslint --quiet`: passed.

Tooling: `rg` unavailable (`/bin/bash: rg: command not found`); used local `find`/`grep`.
