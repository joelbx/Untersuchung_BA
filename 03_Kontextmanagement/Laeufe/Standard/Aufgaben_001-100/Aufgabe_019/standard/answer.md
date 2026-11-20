Updated [roles.go](/app/roles.go) so `Check` rejects duplicate and unknown roles, and `Equals` compares distinct roles regardless of order or repetition. Added regression cases in [roles_test.go](/app/lib/utils/roles_test.go).

The focused role suite passes. The full `lib/utils` suite has one unrelated failure: a certificate fixture expired in 2021.