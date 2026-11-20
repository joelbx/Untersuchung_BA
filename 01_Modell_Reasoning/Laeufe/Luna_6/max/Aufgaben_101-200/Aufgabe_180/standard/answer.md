Updated OS lifecycle data in [config/os.go](/app/config/os.go): Fedora 37/38/40 cutoffs, SUSE Enterprise 13/14 dates, and macOS 11 ended with macOS 15 present.

Extended [scanner/windows.go](/app/scanner/windows.go) with the requested Windows 10 22H2, Windows 11 builds 22621/22631, and Server 2022 KB mappings, ordered by revision and using named struct fields. Updated existing expectations in [config/os_test.go](/app/config/os_test.go) and [windows_test.go](/app/scanner/windows_test.go).

**Verification:** `go test ./config ./scanner` and the focused kernel-version detection test passed. `git diff --check` passed.