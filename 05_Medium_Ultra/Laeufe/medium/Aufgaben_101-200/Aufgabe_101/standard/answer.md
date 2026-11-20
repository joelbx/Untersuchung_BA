Updated list removal in Redis, MongoDB, and PostgreSQL to accept an array of values, remove each matching element, and preserve the order of the remaining list. Added a regression test that reads the list immediately after removal.

ESLint passed, and the existing list test suite passed: 20 tests.