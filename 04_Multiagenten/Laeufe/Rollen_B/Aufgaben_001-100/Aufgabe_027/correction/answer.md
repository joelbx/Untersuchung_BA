Fixed public session selection so `getLastPersistedLocalID` ignores numeric keys containing empty, array, or incomplete session data. Updated the existing fixtures and added regression coverage for unusable entries.

The reviewer’s exact Jest command passed: **2 suites, 23 tests**. Formatting and `git diff --check` passed. No remaining failures or test environment problems.