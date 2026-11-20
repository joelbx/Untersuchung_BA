Task: Fix contact import text date parsing in shared contact property and CSV helpers.
Status: Complete. Added shared text date parser, wired CSV and vCard property conversion, and added regression coverage.
Verification: Targeted Jasmine property specs passed (11 specs); shared package type check, ESLint, Prettier, and git diff --check passed. Karma bundle compiled, but its configured Playwright Chrome binary is absent; targeted specs ran under Node Jasmine instead.
Constraints: Use local repository and existing tests; do not change git history or index baseline.
