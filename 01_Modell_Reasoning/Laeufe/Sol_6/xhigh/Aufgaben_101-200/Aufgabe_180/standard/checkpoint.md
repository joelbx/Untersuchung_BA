Task: Align EOL data and Windows KB rollups in /app.
Status: Complete; working tree contains only intended source/test edits.
Changes: Fedora 37/38/40 cutoffs, macOS 11/15 status, SUSE Enterprise and FreeBSD 13/14 cutoffs, Windows 19045/22621/22631/20348 rollups with named fields. Tests cover EOL boundaries and kernel-version KB classification.
Verification: `GOPROXY=off GOSUMDB=off go test ./config ./scanner` passed. `GOPROXY=off GOSUMDB=off go test -run '^$' ./...` passed. `git diff --check` passed.
