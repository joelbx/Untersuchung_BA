# Checkpoint

Implemented the `.well-known` `force_disable` field and synchronous policy helper, applied it to private room encryption defaults, and added the async server/well-known policy resolver used by `CreateRoomDialog`. The dialog now disables the toggle until policy resolution, applies forced values, and submits the displayed encryption state.

Verification: existing `CreateRoomDialog` and `createRoom` Jest suites pass (20 tests). `yarn lint:types` remains blocked by a pre-existing unrelated error in `src/Unread.ts:167` (`Thread | Room` lacks `getLastUnthreadedReceiptFor`).
