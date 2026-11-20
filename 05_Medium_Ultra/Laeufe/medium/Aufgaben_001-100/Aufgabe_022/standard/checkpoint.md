# RPM source filename parsing

- Inspected `scanner/redhatbase.go` and the existing package-line tests.
- Updated both RPM package-line paths to retain binary metadata and append a scan warning for unparseable source RPM filenames.
- Updated `splitFileName` to move a numeric filename epoch into the source version, without duplicating the epoch already in RPM fields.
- Added parser and scan continuation coverage for the supplied examples.
- Verified: `go test ./scanner -run 'Test_redhatBase_parseInstalledPackages' -count=1` passed; `git diff --check` passed.
