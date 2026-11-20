# Checkpoint

Task: implement `.well-known` force-disable encryption policy for room creation and UI.

Completed:
- Added `IE2EEWellKnown.force_disable` and a strict synchronous helper for the forced-off policy.
- Updated `privateShouldBeEncrypted` to honor force-disable before its existing default behavior.
- Added the shared server and well-known policy resolver with server precedence and conflict warning.
- Updated `CreateRoomDialog` to disable the control while policy resolves, reflect enforced values, and submit its effective state.

Validation:
- Existing room creation and dialog Jest suites passed (20 tests).
- ESLint, Prettier, and `git diff --check` passed.
- `yarn lint:types` stopped on the existing unrelated `src/Unread.ts:167` `Thread | Room` type error.
