Updated [roles.go](/app/roles.go:106) so `Check` rejects duplicate roles while preserving unknown-role validation, and `Equals` compares distinct role sets regardless of order or duplicates. Nil and empty collections compare equal.

Added regression cases in [roles_test.go](/app/lib/utils/roles_test.go:44). The focused role suite passed all 4 tests, and `git diff --check` passed.