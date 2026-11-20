# Checkpoint

Implemented a synchronous member action lock in `UserInfo.tsx`, shared by Kick, Ban, and Mute in `RoomAdminToolsContainer`. It starts before confirmation and releases after cancel, success, or failure. The pending controls set `disabled` and `aria-disabled`; failures show one error dialog.

Validation: `./node_modules/.bin/jest --runInBand test/components/views/right_panel/UserInfo-test.tsx --silent` passed 70 tests in the previous run. Added tests cover shared lock, cancel, and failure. `./node_modules/.bin/eslint src/components/views/right_panel/UserInfo.tsx test/components/views/right_panel/UserInfo-test.tsx` and Prettier check passed.

`./node_modules/.bin/tsc --noEmit --jsx react --pretty false` failed with existing repository errors in matrix-js-sdk declarations and unrelated project files. The final type run reported 47 pre-existing errors and no `UserInfo` errors. Examples: `node_modules/matrix-js-sdk/src/crypto/OutgoingRoomKeyRequestManager.ts(17,30): error TS7016: Could not find a declaration file for module 'uuid'` and `src/components/views/dialogs/devtools/RoomState.tsx(61,42): error TS2339: Property 'replaces_state' does not exist on type 'IUnsigned'`. Full output was captured in `/tmp/userinfo-tsc.log`. No dependencies downloaded. `rg` is unavailable (`/bin/bash: rg: command not found`), so local `find` and `grep` were used.
