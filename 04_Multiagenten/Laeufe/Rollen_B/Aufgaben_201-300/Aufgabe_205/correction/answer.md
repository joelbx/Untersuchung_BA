Connected token creation and deletion, bearer authentication, and admin token settings to the indexed token utility. Existing `core.api` tokens are imported with their IDs preserved, and deletion removes their legacy entries so they cannot reappear.

The reviewer’s exact authentication test now passes: **6 passing**. ESLint and `git diff --check` also pass.