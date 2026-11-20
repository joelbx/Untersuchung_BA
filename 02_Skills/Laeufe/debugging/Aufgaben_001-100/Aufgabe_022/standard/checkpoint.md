# Checkpoint

Investigating RPM source filename parsing and epoch handling. `rg` is unavailable (`/bin/bash: rg: command not found`); using local grep/find. No fixes yet.

## Root cause and hypothesis
`parseInstalledPackagesLine` returns a source filename parse error before constructing the binary package, so `parseInstalledPackages` aborts. `splitFileName` splits on hyphens and leaves a filename epoch in the parsed name (`1:bar`). Existing source version formatting prefixes the line epoch, so the filename epoch must be stripped from the name and represented once in the version. Existing warning storage is `base.warns []error`, exported through `ScanResult.Warnings`.

## Verification
Before fix: `GOPROXY=off GOSUMDB=off go test ./scanner -run 'Test_redhatBase_(nonstandardSourceRPM|parseInstalledPackagesLine)$' -count=1` failed as expected: non-standard source filename aborted before binary creation; epoch filename produced source name `1:bar`.
After fix: same focused command passed (exit 0). `GOPROXY=off GOSUMDB=off go test ./scanner -count=1` passed (exit 0), including the Amazon repoquery regression. `git diff --check` passed.
