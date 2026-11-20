# Checkpoint

Task: restore widget room buttons by dispatching and handling `Action.RoomLoaded`, and preserve initial event focus fallback.

Status: implementation and focused tests updated. `rg` is unavailable (`/bin/bash: rg: command not found`); used local grep/find.

Verification:
- `./node_modules/.bin/jest --runInBand --silent test/stores/RoomViewStore-test.ts test/components/structures/RoomView-test.tsx`: 2 suites, 65 tests, 8 snapshots passed.
- `./node_modules/.bin/eslint --max-warnings 0 src/dispatcher/actions.ts src/stores/RoomViewStore.tsx src/components/structures/RoomView.tsx test/stores/RoomViewStore-test.ts test/components/structures/RoomView-test.tsx`: exit 0.
- `./node_modules/.bin/tsc --noEmit --jsx react`: exit 134, `FATAL ERROR: CALL_AND_RETRY_LAST Allocation failed - JavaScript heap out of memory` at approximately 2 GiB heap. Type status remains unverified pending retry with a larger heap.
- `NODE_OPTIONS=--max-old-space-size=4096 ./node_modules/.bin/tsc --noEmit --jsx react`: exit 2. TypeScript reported 19 errors in existing OIDC/matrix-js-sdk integration and `TabbedView.tsx` files, including missing `NonEmptyArray`, `getAuthIssuer`, and `discoverAndValidateOIDCIssuerWellKnown` exports. No diagnostic names the edited files, but repository-wide type checking remains failing; the exact errors are in the command output.
- `./node_modules/.bin/prettier --check src/dispatcher/actions.ts src/stores/RoomViewStore.tsx src/components/structures/RoomView.tsx test/stores/RoomViewStore-test.ts test/components/structures/RoomView-test.tsx`: exit 0.
- After adding a ViewRoom non-recomputation assertion, `./node_modules/.bin/jest --runInBand --silent test/stores/RoomViewStore-test.ts`: 37 tests, 3 snapshots passed; `./node_modules/.bin/eslint --max-warnings 0 test/stores/RoomViewStore-test.ts`: exit 0.
