# Checkpoint

Implemented share-keyed member, internal invitation, and external invitation stores in both Drive copies. Updated the Zustand member view to read and write data for the active share. Added `getExistingEmails` and focused isolation tests.

Verification completed:
- `./node_modules/.bin/tsc --noEmit -p applications/drive/tsconfig.json` — exit 0.
- `./node_modules/.bin/tsc --noEmit -p packages/drive-store/tsconfig.json` — exit 0.
- `/app/node_modules/.bin/jest --config jest.config.js src/app/zustand/share/memberInvitations.store.test.ts --runInBand --coverage=false` from `/app/applications/drive` — 3 tests passed.
- `git diff --check` — exit 0.

Additional existing suite running: `/app/node_modules/.bin/jest --config jest.config.js src/app/zustand/share/shares.store.test.ts src/app/zustand/share/memberInvitations.store.test.ts --runInBand --coverage=false` from `/app/applications/drive`.
- The combined existing suite command above produced no output after roughly 90 seconds while consuming CPU; interrupted with Ctrl-C (exit 130). Its result is unknown. The focused new suite completed separately and passed.

Final change: the view now clears its selected share and reloads when `rootShareId` or `linkId` changes, with abort checks before writing fetched data.
Final verification after this change:
- `./node_modules/.bin/tsc --noEmit -p applications/drive/tsconfig.json` — exit 0.
- `./node_modules/.bin/tsc --noEmit -p packages/drive-store/tsconfig.json` — exit 0.
- `/app/node_modules/.bin/jest --config jest.config.js src/app/zustand/share/memberInvitations.store.test.ts --runInBand --coverage=false` from `/app/applications/drive` — 3 tests passed.
