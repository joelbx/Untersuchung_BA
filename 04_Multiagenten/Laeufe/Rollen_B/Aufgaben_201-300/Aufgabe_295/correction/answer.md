The checked-out patch meets the device verification requirements. I found no concrete code defect to correct, so I left the project files unchanged.

The reviewer’s exact Jest command passed (3 suites, 9 tests, 8 snapshots). Targeted ESLint and `git diff --check` passed.

**TEST_ENVIRONMENT_PROBLEM:** The TypeScript check still fails on `matrix-js-sdk` API and type mismatches in files outside this patch. No dependencies were changed or downloaded.