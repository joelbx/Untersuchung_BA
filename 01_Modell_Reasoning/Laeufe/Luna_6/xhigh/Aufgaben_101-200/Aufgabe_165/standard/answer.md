Implemented the `.well-known` force-disable policy. The dialog now keeps encryption controls disabled while policy resolves, applies enforced values over defaults, and submits the effective state.

- Added [`checkUserIsAllowedToChangeEncryption`](</app/src/createRoom.ts:81>) with server-policy precedence and a conflict warning.
- Added [`shouldForceDisableEncryption`](</app/src/utils/room/shouldForceDisableEncryption.ts:25>) and the `force_disable` well-known field. [`privateShouldBeEncrypted`](</app/src/utils/rooms.ts:22>) now honors it first.
- Updated [`CreateRoomDialog`](</app/src/components/views/dialogs/CreateRoomDialog.tsx:95>) to apply the policy and submit its resulting encryption state.

Validation: both relevant Jest suites passed (20 tests); ESLint, Prettier, and `git diff --check` passed. `yarn lint:types` stopped on an unrelated error in `src/Unread.ts:167` (`Thread | Room`).