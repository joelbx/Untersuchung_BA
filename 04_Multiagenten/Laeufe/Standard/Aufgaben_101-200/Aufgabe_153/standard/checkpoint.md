# Checkpoint

Implemented shareId-keyed member, internal invitation, and external invitation storage in `packages/drive-store/zustand/share`. Updated the Zustand member view to select and write only its active share, and added `getExistingEmails`. Added share isolation regression tests.

Verification: `yarn workspace @proton/drive-store check-types` passed; `yarn workspace @proton/drive-store test --runInBand zustand/share/shareStores.test.ts store/_shares/useShareActions.test.ts` passed (8 tests); `git diff --check` passed.
