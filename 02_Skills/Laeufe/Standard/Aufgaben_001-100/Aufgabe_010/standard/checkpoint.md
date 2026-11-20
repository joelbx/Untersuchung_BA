# Checkpoint

Resolved the Message Composer replacement notice and related reply/cancel/profile UI:
- Tombstoned rooms render the inactive status and replacement link in paragraphs; decorative icon has empty alt text.
- Added `CancelButton` with configurable string size (default `16`), native button semantics, accessible label, and shared icon styling. Used it in reply preview, search bar, and dial pad close controls.
- Reply preview names the message sender and offers a labeled cancel action. Reply profiles can render as spans inside preview links.
- Updated the composer test and added a reply preview cancellation test.

Verification:
- `./node_modules/.bin/jest --runInBand test/components/views/rooms/MessageComposer-test.tsx test/components/views/rooms/ReplyPreview-test.tsx test/components/views/rooms/BasicMessageComposer-test.tsx test/components/views/rooms/SendMessageComposer-test.tsx` passed: 4 suites, 18 tests.
- ESLint on changed TS/TSX files passed.
- Stylelint on changed SCSS files passed (before final selector-only change).
- `git diff --check` passed.
- `./node_modules/.bin/tsc --noEmit --jsx react --pretty false` failed with existing unrelated errors: `node_modules/matrix-js-sdk/src/http-api.ts` lines 830, 885, 886: `Property 'abort' does not exist on type 'IRequest'`; `src/components/views/room_settings/AliasSettings.tsx` line 144 and `src/components/views/settings/tabs/room/SecurityRoomSettingsTab.tsx` line 223: `Property 'getLocalAliases' does not exist on type 'MatrixClient'`. No TypeScript errors were reported in changed files after the size prop fix. Overall project typecheck remains uncertain due to those errors.
- `rg` is unavailable (`/bin/bash: rg: command not found`); used local `find`/`grep`.
