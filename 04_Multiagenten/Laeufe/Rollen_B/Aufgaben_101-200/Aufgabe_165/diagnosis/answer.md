**Diagnosis:** The missing policy handling spans four change points:

- [CreateRoomDialog.tsx](/app/src/components/views/dialogs/CreateRoomDialog.tsx:78) starts with an interactive toggle, checks only whether the server forces encryption on, and does not apply an enforced value to the displayed state. Its submit path sends `true` whenever the toggle is locked, which would submit the wrong value for forced-off encryption.
- [createRoom.ts](/app/src/createRoom.ts:45) lacks the requested `checkUserIsAllowedToChangeEncryption` helper. The SDK’s server check is asynchronous and reports forced-on policy; this helper should combine it with `.well-known` forced-off policy, prefer the server on conflict, and warn.
- [WellKnownUtils.ts](/app/src/utils/WellKnownUtils.ts:29) lacks the `force_disable` field. Its existing E2EE lookup can supply the payload to the proposed `shouldForceDisableEncryption.ts`; that helper should return true only for `force_disable === true`.
- [rooms.ts](/app/src/utils/rooms.ts:21) considers only the `default` field. Forced-off policy needs to take precedence there.

[CreateRoomDialog-test.tsx](/app/test/components/views/dialogs/CreateRoomDialog-test.tsx:49) covers defaults and server forced-on behavior, but not forced-off policy, conflicting policies, initial toggle interactivity, or the submitted forced-off value. Policy behavior on an asynchronous server-check failure is unspecified.

I updated [checkpoint.md](/app/.codex-role-output/checkpoint.md). No project source or tests were edited; this was a fault-localization pass.