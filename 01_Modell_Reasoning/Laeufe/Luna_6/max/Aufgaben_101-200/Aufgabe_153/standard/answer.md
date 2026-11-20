Implemented share scoped state. Members, internal invitations, and external invitations are stored by `shareId`; reads return an empty array for shares without data, and updates affect only the specified share. The member view now selects data for its active share.

Added `getExistingEmails` and used it in both member view implementations: [share.ts](/app/packages/drive-store/utils/share.ts:3).

Verification passed: TypeScript check, ESLint on changed files, and Drive store tests (66 suites passed; 478 tests passed, 4 skipped). `git diff --check` passed.