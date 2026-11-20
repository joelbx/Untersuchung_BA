# Checkpoint

Task: implement `.well-known` force-disable E2EE policy and integrate it with room creation UI and private room defaults.

Implemented the `.well-known` `force_disable` field and named synchronous policy helper, applied forced-disable precedence to private room defaults, and added the async shared encryption permission decision used by `CreateRoomDialog`. The dialog disables its control until policy resolution, applies an enforced value over props/defaults, and submits the displayed state.

Verification: `yarn test --runInBand test/components/views/dialogs/CreateRoomDialog-test.tsx` passed (10 tests); Prettier check and `git diff --check` passed. `yarn lint:types` is blocked by an unrelated existing error in `src/Unread.ts:167` (`getLastUnthreadedReceiptFor` missing on `Thread`).
