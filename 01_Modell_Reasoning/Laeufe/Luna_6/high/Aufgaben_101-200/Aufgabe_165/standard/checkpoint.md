# Checkpoint

Implemented `.well-known` E2EE `force_disable` support.

- Added the documented `IE2EEWellKnown.force_disable` field and the named synchronous `shouldForceDisableEncryption(client)` helper.
- Updated `privateShouldBeEncrypted` so force-disable takes precedence over the existing default setting.
- Added the exported `AllowedEncryptionSetting` contract and async `checkUserIsAllowedToChangeEncryption(client, chatPreset)` policy helper. It checks both server force-enable and `.well-known` force-disable, prefers server force-enable on conflict, and warns once for conflicts.
- Updated `CreateRoomDialog` to keep encryption disabled while policy loads, apply any enforced value over defaults, and submit the effective state displayed in the dialog.

Verification:
- Existing focused Jest suites passed: 3 suites, 23 tests.
- ESLint and Prettier checks passed for all changed source files.
- `yarn lint:types` has one existing error in `src/Unread.ts:167` (`Thread | Room` lacks `getLastUnthreadedReceiptFor`); no errors remain in the changed files.
- `git diff --check` passed.
