# Checkpoint

Task: Fix `Roles.Check` validation and `Roles.Equals` set equality.

Status: Implementation and regression tests complete.

Changes:
- `Roles.Check` rejects repeated roles while continuing to use `Role.Check` for validity.
- `Roles.Equals` compares distinct-role sets, including nil/empty equivalence.
- Added table-driven tests in `roles_test.go` for valid, unknown, duplicate, reordered, and differing roles.

Checks:
- `gofmt -w roles.go roles_test.go`: completed.
- `go test -mod=vendor . ./lib/utils`: root package passed; `lib/utils` failed in `CertsSuite.TestRejectsSelfSignedCertificate` because a fixture expired on 2021-03-16 and the current date is 2026-10-26. Actual error: `x509: certificate has expired or is not yet valid`; expected: `x509: certificate signed by unknown authority`. The unrelated full suite remains failing.
- `go test -mod=vendor ./lib/utils -check.f '^RolesTestSuite\.'`: passed.
- `git diff --check`: passed.

Environment: `rg` is unavailable (`/bin/bash: rg: command not found`); used local `find` and `grep`.
