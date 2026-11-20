VERDICT: FIX

The patch has two issues:

- [CreateRoomDialog.tsx](/app/src/components/views/dialogs/CreateRoomDialog.tsx:106) unlocks encryption if the server policy lookup rejects. That allows a room to be created without the shared helper’s policy decision. Keep creation and the control unavailable until the policy is resolved, or handle the failure through an explicit policy outcome.
- [CreateRoomDialog.tsx](/app/src/components/views/dialogs/CreateRoomDialog.tsx:312) adds a forced-off message that is missing from [en_EN.json](/app/src/i18n/strings/en_EN.json). Add it to the catalog so development builds do not show a missing-translation message.

**Tests:** `yarn test --runInBand --watch=false test/components/views/dialogs/CreateRoomDialog-test.tsx test/utils/room/shouldForceDisableEncryption-test.ts` passed: 2 suites, 18 tests. `git diff --check` passed.

**Separate type-check failure:** `./node_modules/.bin/tsc --noEmit --jsx react --pretty false` failed with TS2339 in unchanged [Unread.ts](/app/src/Unread.ts:167). That failure is unrelated to the reviewed patch and needs a separate correction.