Task: fix list removal with multiple distinct string values.
Status: implementation complete across Redis, MongoDB, and PostgreSQL; regression test added.
Validation: ESLint passed for changed files; existing test/database/list.js passed (20 tests) against a temporary local Redis instance, which was then stopped.
Constraints observed: local code/tests only; git history, index, and harness configuration unchanged.
