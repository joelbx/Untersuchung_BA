Fixed the reviewer’s defect: `expand_record` now preserves populated author and contributor `db_name` values. Added regression tests for matching records with different display names in both author and contributor roles.

The reviewer’s exact test commands passed: 14 passed and 1 expected failure; 63 passed; and 57 passed. `git diff --check` passed. TEST_ENVIRONMENT_PROBLEM: none.