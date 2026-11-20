Updated OS lifecycle data and Windows KB mappings. Fedora 37/38 dates are corrected and Fedora 40 is included; SUSE Enterprise versions 13/14 and macOS lifecycle entries are updated. Windows 10 22H2, Windows 11 22H2/23H2, and Server 2022 now include the requested KBs in revision order, with named struct fields. Existing test expectations were updated.

Verification passed: `go test ./config ./scanner`, `gofmt`, and `git diff --check`.

Changes are in [config/os.go](/app/config/os.go), [scanner/windows.go](/app/scanner/windows.go), and their existing tests.