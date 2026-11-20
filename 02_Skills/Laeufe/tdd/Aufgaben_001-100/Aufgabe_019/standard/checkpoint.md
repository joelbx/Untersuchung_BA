# Checkpoint

Task: fix Roles.Check validation and Roles.Equals set equality using test-driven development.

Changes: `roles_test.go` adds validation and set-equality regressions. `roles.go` rejects duplicate roles and compares distinct-role sets.

TDD: `GOPROXY=off go test -mod=vendor . -run 'TestRoles(Check|EqualsUsesDistinctRoles)$' -count=1` failed as expected before implementation (duplicate accepted; duplicate-aware equality wrong), then passed after implementation.

Full suite: `GOPROXY=off go test -mod=vendor ./...` is still running. It has reported pre-existing vet errors in `lib/backend/test/suite.go` at lines 402 and 666: conversion from OpType (int) to string yields one rune, not decimal digits. It also reported a C compiler warning in vendored sqlite3.

Tooling: `rg` is unavailable (`/bin/bash: rg: command not found`); used local fallback searches.

Relevant existing tests: `GOPROXY=off go test -mod=vendor ./lib/utils -run '^TestUtils$' -check.f 'RolesTestSuite' -count=1` passed.

`GOPROXY=off go test -mod=vendor ./lib/utils -run 'Test.*Roles|Test' -count=1` failed in `CertsSuite.TestRejectsSelfSignedCertificate`: expected unknown-authority error, got expired-certificate error because the test certificate expired on 2021-03-16 and the current date is 2026-10-26.

The repository-wide `GOPROXY=off go test -mod=vendor ./...` run was interrupted after it reported vet errors in `lib/backend/test/suite.go`; it did not finish, so its remaining packages are unverified. The current result is exit code 2 from interruption. `git diff --check` passed.
