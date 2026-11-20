# Checkpoint

Task: improve message composer room replacement semantics and related cancel/profile/reply accessibility.
Status: inspecting local implementation and tests. Assigned TDD workflow in use.
Tooling: `rg` unavailable (`/bin/bash: rg: command not found`); using `find` and `grep`.

Verification so far:
- Targeted Jest: `./node_modules/.bin/jest --runInBand test/components/views/rooms/MessageComposer-test.tsx test/components/views/messages/DisambiguatedProfile-test.tsx test/components/views/buttons/Cancel-test.tsx` passed (6 tests); pre-existing Browserslist and Node deprecation warnings.
- TypeScript: `./node_modules/.bin/tsc --noEmit --jsx react --pretty false` failed on existing type errors in node_modules/matrix-js-sdk/src/http-api.ts (`IRequest.abort`) and src/components/views/room_settings/AliasSettings.tsx and src/components/views/settings/tabs/room/SecurityRoomSettingsTab.tsx (`MatrixClient.getLocalAliases`). No errors in changed files after fixing CancelButton's inherited size type.
- Full Jest suite currently running.

Final full suite check: `./node_modules/.bin/jest --runInBand --silent --json --outputFile=/tmp/message-composer-jest.json` failed: 169 passed suites, 6 failed suites; 1720 passed tests, 7 failed tests. All failures are snapshots containing newly serialized `Symbol(shapeMode): false` and occur in:
- test/components/views/messages/MLocationBody-test.tsx
- test/components/views/location/SmartMarker-test.tsx
- test/components/views/location/LocationViewDialog-test.tsx
- test/components/views/location/ZoomButtons-test.tsx
- test/components/views/beacon/BeaconMarker-test.tsx
- test/components/views/beacon/BeaconStatus-test.tsx
No changed-component tests failed in the full run. Did not update unrelated snapshots.
ESLint on changed TS/TSX files, stylelint on changed SCSS files, and `git diff --check` passed after fixes.
Final targeted check: `./node_modules/.bin/jest --runInBand --silent test/components/views/rooms/MessageComposer-test.tsx test/components/views/rooms/SearchBar-test.tsx test/components/views/messages/DisambiguatedProfile-test.tsx test/components/views/buttons/Cancel-test.tsx` passed: 4 suites, 10 tests (with existing Node/Browserslist warnings).
