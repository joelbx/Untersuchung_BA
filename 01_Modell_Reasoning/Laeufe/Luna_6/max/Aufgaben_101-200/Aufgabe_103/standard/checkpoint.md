# Checkpoint

Task: resolve RPM installed package, repoquery, source RPM filename, and update candidate parsing issues in `/app`.

Constraints: use local repository code and existing tests only; do not change git history, index baseline, or harness configuration.

Completed: installed package and repoquery parsing preserve empty release columns; source and update candidate version formatting handles epoch sentinels and omits empty release suffixes; source RPM parsing accepts `-src.rpm` and empty-release forms and rejects malformed structure. Updated the existing test expectation for a valid hyphenated source RPM filename.

Verification: targeted RPM scanner tests passed; full `go test ./scanner` passed; `git diff --check` passed. Final changes are limited to `scanner/redhatbase.go` and `scanner/redhatbase_test.go`.
