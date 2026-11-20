# Share member view isolation

- Updated the Drive and drive-store invitation/member Zustand stores to keep separate arrays for each share ID, with scoped getters and actions.
- Updated the new member view to resolve the current link's share ID before selecting members or invitations, and to pass that ID through updates and removals.
- Added `getExistingEmails` and regression coverage for multiple shares and both invitation types.
- Verification: Drive and drive-store TypeScript checks passed; targeted Jest suites passed (21 tests); Prettier, ESLint, and `git diff --check` passed.
