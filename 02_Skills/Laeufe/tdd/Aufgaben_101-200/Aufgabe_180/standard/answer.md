Updated the EOL data for Fedora 37, 38, and 40; SUSE Enterprise Desktop and Server 13 and 14; and macOS 11 through 15. Added the requested Windows KB rollups in revision order using named struct literals, and updated regression tests for low and high kernel revisions.

Verification passed: `GOPROXY=off GOSUMDB=off go test ./...` and `git diff --check`.