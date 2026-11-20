# Checkpoint

Task: fix share-scoped member and invitation state in the Drive member view and add the requested `getExistingEmails` utility.

Completed:
- Invitation and member Zustand stores now keep data by `shareId`, expose getters that return empty arrays for missing shares, and scope every write/update to the requested share.
- The Zustand member view selects and updates the arrays for its active share only; adding invitations appends within the correct share.
- Added and adopted `getExistingEmails` in both member view implementations.

Verification:
- `yarn workspace @proton/drive-store check-types` passed.
- `yarn workspace @proton/drive-store test --runInBand` passed: 66 suites, 478 tests passed, 4 skipped.
- ESLint passed on the six changed source files.
- `git diff --check` passed.
