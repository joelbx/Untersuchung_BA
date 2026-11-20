# Checkpoint

Task: implement `.well-known` forced encryption disable for new rooms, expose the policy helper, wire it into room defaults and `CreateRoomDialog`, and run relevant existing tests.

Constraints: use repository code and tests only; preserve the working tree's existing state; do not alter git history, index baseline, or harness configuration.

Completed:
- Added `force_disable` to the E2EE well-known type and a strict synchronous `shouldForceDisableEncryption` helper.
- Made `privateShouldBeEncrypted` honor forced disable before the E2EE default.
- Added `AllowedEncryptionSetting` and `checkUserIsAllowedToChangeEncryption`, including server precedence and a conflict warning.
- Updated `CreateRoomDialog` to disable the control while policy resolves, apply forced values over defaults, and submit its displayed encryption state.
- Existing dialog tests pass; formatting and ESLint checks pass for modified source files.

Verification note: the full TypeScript check reports an unrelated existing error in `src/Unread.ts:167` (`getLastUnthreadedReceiptFor` is not available on `Thread | Room`).
