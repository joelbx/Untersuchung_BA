# Checkpoint

Implemented in `roles.go`:
- `Roles.Check` validates each role, rejects repeated role values, and accepts an empty list.
- `Roles.Equals` compares distinct-role sets, so ordering and duplicate counts do not affect equality; nil and empty sets compare equal.
- Included `RoleRemoteProxy` in the valid-role switch because it is a declared built-in role and used by the repository.

Verification: `gofmt -w roles.go` and `git diff --check` passed. `go test ./lib/utils` ran 50 tests successfully but failed `CertsSuite.TestRejectsSelfSignedCertificate` because its fixed certificate expired on 2021-03-16; the environment date is 2026-10-05.
