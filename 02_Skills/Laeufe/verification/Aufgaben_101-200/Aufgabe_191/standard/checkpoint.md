# Checkpoint

Task: Add registration token support to InteractiveAuth, including stable and unstable stage identifiers, UI, and verification.

Status: Implemented a registration token entry stage and mapped both stable and unstable auth identifiers to it. Added localized English strings and focused tests.

Verification:
- `./node_modules/.bin/jest test/components/views/dialogs/InteractiveAuthDialog-test.tsx --runInBand --silent` passed: 1 suite, 5 tests. This includes stable and unstable identifier flows, form behavior, and the success callback's third argument.
- `./node_modules/.bin/eslint src/components/views/auth/InteractiveAuthEntryComponents.tsx test/components/views/dialogs/InteractiveAuthDialog-test.tsx` exited 0.
- `./node_modules/.bin/prettier --check src/components/views/auth/InteractiveAuthEntryComponents.tsx test/components/views/dialogs/InteractiveAuthDialog-test.tsx src/i18n/strings/en_EN.json` exited 0.
- `git diff --check` exited 0.

Type check limitation: `./node_modules/.bin/tsc --noEmit --jsx react` exited 2 with existing SlidingSync API errors in `src/SlidingSyncManager.ts`, `src/components/views/rooms/RoomSublist.tsx`, `src/hooks/useSlidingSyncRoomSearch.ts`, `src/stores/room-list/SlidingRoomListStore.ts`, and corresponding tests. Representative errors: `Property 'getListParams' does not exist on type 'SlidingSync'` and `Argument of type 'string' is not assignable to parameter of type 'number'`. No diagnostics referenced the changed files. Repository-wide type correctness remains unverified because of those unrelated errors.
