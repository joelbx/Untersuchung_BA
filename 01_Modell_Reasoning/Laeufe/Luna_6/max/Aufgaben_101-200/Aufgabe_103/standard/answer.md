Implemented the RPM parsing fixes in [redhatbase.go](/app/scanner/redhatbase.go:523). Empty release columns now retain their position in installed package and repoquery output. Source package versions omit a release suffix when it’s empty, and epoch formatting is shared with update candidate parsing.

`splitFileName` now accepts `-src.rpm` filenames, including empty releases, and rejects malformed filename structures. Updated the existing test expectation for a valid hyphenated source RPM in [redhatbase_test.go](/app/scanner/redhatbase_test.go:422).

Verification passed: targeted RPM scanner tests, `go test ./scanner`, and `git diff --check`.