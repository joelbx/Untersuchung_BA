# Checkpoint

Implemented a synchronous, member-scoped lock for Kick, Ban/Unban, and Mute/Unmute in `RoomAdminToolsContainer`. Each control receives `disabled` and `aria-disabled="true"` while locked. Directly rendered buttons also use a local guard. Confirmation cancellation and operation settlement release the lock; existing request failure dialogs remain in place.

Verification:
- `yarn test test/components/views/right_panel/UserInfo-test.tsx --runInBand` passed (68 tests).
- `yarn eslint src/components/views/right_panel/UserInfo.tsx` passed.
- `git diff --check` passed.
- `yarn lint:types` did not pass due to pre-existing errors in dependencies and unrelated SDK/application files (including missing declarations for `uuid`, `content-type`, and SDK API mismatches); no reported errors in `UserInfo.tsx`.
