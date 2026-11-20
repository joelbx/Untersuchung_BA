# RPM scanner fix

- Located RPM parsing in `scanner/redhatbase.go` and its existing tests in `scanner/redhatbase_test.go`.
- Source RPM parse failures now append a scan warning and leave the binary package available in both RPM and repoquery paths.
- `splitFileName` now separates a numeric epoch prefix from the source name and carries it into the source version.
- Added line, scan continuation, repoquery, and filename regression cases.
- Focused scanner tests passed: `GOPROXY=off GOSUMDB=off go test ./scanner -run 'Test_redhatBase_parseInstalledPackages|TestSplitFileName' -count=1`.
- `git diff --check` passed.
