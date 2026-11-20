The existing patch in [UserInfo.tsx](/app/src/components/views/right_panel/UserInfo.tsx) addresses the rapid activation issue. I found no concrete defect in the reviewer’s patch, so I made no further project code changes.

The exact reviewer checks were rerun: Jest passed (70 tests, 6 snapshots), and ESLint and Prettier passed.

**TEST_ENVIRONMENT_PROBLEM:** TypeScript still fails on missing declarations and SDK API mismatches outside the changed files. No dependencies were downloaded.