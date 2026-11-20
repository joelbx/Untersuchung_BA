# Mail metrics helpers checkpoint

- Task: add `@proton/metrics` to the mail app and implement mailbox label and page size normalization helpers.
- Initial state: working tree clean; mail app has no `metrics` directory.
- Added the mail workspace metrics dependency and matching lockfile entry.
- Added `getLabelID` and `getPageSizeString` with focused tests.
- Jest: helper, label, and paging suites pass (40 tests). ESLint and Prettier pass.
- Mail TypeScript check and final `git diff --check` pass. Work complete.
