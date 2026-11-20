# Checkpoint

Task: isolate Drive members and internal/external invitations by shareId; add getExistingEmails.

Implemented per-share state and scoped actions in the Zustand members and invitations stores. The member view selects its current share's entries and supplies its shareId for reads and writes. Added getExistingEmails and store regression tests.

TDD: observed three store tests fail because getMembers/getInvitations were missing, then observed the email utility test fail because getExistingEmails was missing; implemented each and reran green.

Verification:
- `node_modules/.bin/jest --config packages/drive-store/jest.config.js --runInBand packages/drive-store/zustand/share/shareStores.test.ts`: passed, 4 tests.
- `node_modules/.bin/jest --config packages/drive-store/jest.config.js --runInBand`: passed, 67 suites, 482 tests, 4 skipped. Existing unrelated console warnings and JPEG/Ed25519 warnings appeared.
- `node_modules/.bin/tsc --noEmit --project packages/drive-store/tsconfig.json`: passed.
- `node_modules/.bin/eslint packages/drive-store/zustand/share/types.ts packages/drive-store/zustand/share/invitations.store.ts packages/drive-store/zustand/share/members.store.ts packages/drive-store/zustand/share/getExistingEmails.ts packages/drive-store/zustand/share/shareStores.test.ts packages/drive-store/store/_views/useShareMemberViewZustand.tsx --quiet`: passed.
- `node_modules/.bin/prettier --check packages/drive-store/zustand/share/types.ts packages/drive-store/zustand/share/invitations.store.ts packages/drive-store/zustand/share/members.store.ts packages/drive-store/zustand/share/getExistingEmails.ts packages/drive-store/zustand/share/shareStores.test.ts packages/drive-store/store/_views/useShareMemberViewZustand.tsx`: passed.
- `git diff --check`: passed.

Environment: `rg` unavailable (`/bin/bash: rg: command not found`); used local `find` and `grep`. No downloads.
