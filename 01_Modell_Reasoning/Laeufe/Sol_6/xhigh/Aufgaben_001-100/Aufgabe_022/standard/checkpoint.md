# Progress

- Updated `scanner/redhatbase.go` to retain binary RPM metadata and append a scan warning when a source RPM filename cannot be parsed, including the repoquery path.
- `splitFileName` now recognizes a numeric epoch before the source name; source versions include that epoch once and retain the `src` architecture and binary links.
- Added regression coverage for malformed source filenames, epoch-prefixed filenames, scan continuation, and source-to-binary links.
- Verified with `GOPROXY=off GOSUMDB=off go test ./scanner -run 'Test_redhatBase_parseInstalledPackages' -count=1`, `GOPROXY=off GOSUMDB=off go test ./scanner -count=1`, and `git diff --check`; all passed.
