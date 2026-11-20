# Checkpoint

Task: implement canonical OS EOL lookup, scan warnings, summary rendering, and shared major version parser.
Status: complete. EOL table contains the specified exact release identifiers and dates. Scan results evaluate EOL at scannedAt; pseudo and raspbian are excluded. Summary prints each warning in evaluation order.
Verification: `GOPROXY=off GOSUMDB=off go test ./config ./util ./scan ./report ./oval ./gost` passed. `git diff --check` passed.
