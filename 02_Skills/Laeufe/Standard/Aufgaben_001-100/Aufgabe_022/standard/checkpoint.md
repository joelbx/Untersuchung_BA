# Checkpoint

Task: Fix RPM source filename parsing and epoch handling.
Status: Complete.
Changes: Source RPM parse errors now append a scan warning and preserve the binary package; epoch prefixes in filenames are moved from the source name into its version. Both installed-package and repoquery parsers use the same behavior. Added regression tests for malformed source filenames, epoch filenames, warning collection, and continuation across lines.
Checks:
- `rg -n 'parseInstalledPackagesLine|splitFileName' .` unavailable: `/bin/bash: rg: command not found`; used local grep.
- `GOPROXY=off GOSUMDB=off go test ./scanner -run 'Test_redhatBase_parseInstalledPackages|TestSplitFileNameWithEpoch' -count=1` passed.
- `GOPROXY=off GOSUMDB=off go test ./scanner -count=1` passed.
- `git diff --check` passed.
