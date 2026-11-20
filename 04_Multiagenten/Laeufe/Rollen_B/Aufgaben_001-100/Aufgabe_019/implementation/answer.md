Updated [roles.go](/app/roles.go) so `Check` rejects duplicate roles and `Equals` compares sets of distinct roles. Added regression cases in [roles_test.go](/app/lib/utils/roles_test.go).

The focused roles tests pass. The full `lib/utils` suite has one unrelated failure: a certificate fixture expired in 2021.