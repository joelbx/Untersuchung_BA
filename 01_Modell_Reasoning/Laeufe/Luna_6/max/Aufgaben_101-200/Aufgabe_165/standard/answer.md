Implemented `.well-known` forced encryption disable for room creation. The dialog now follows the shared policy decision, applies enforced values over defaults, stays non-interactive while the decision loads, and submits the encryption state it displays.

Added the `force_disable` field and [shouldForceDisableEncryption.ts](/app/src/utils/room/shouldForceDisableEncryption.ts). `privateShouldBeEncrypted` now honors forced disable before the default.

**Verification:** The existing CreateRoomDialog suite passed (10 tests); Prettier, ESLint, and `git diff --check` passed. The full TypeScript check reports an unrelated error in [Unread.ts](/app/src/Unread.ts:167): `getLastUnthreadedReceiptFor` is unavailable on `Thread | Room`.