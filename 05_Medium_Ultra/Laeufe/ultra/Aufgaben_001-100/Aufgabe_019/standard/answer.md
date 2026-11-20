Updated [roles.go](/app/roles.go:105) so `Roles.Check` rejects duplicate and unknown roles, and `Roles.Equals` compares distinct role sets regardless of order. Added regression cases in [roles_test.go](/app/lib/utils/roles_test.go:45).

The focused Roles tests, `lib/services` tests, and root package check passed. The full `lib/utils` suite has one unrelated failure: an expired certificate fixture changes the error expected by `CertsSuite.TestRejectsSelfSignedCertificate`.

I delegated a test coverage review to a subagent; it made no edits.