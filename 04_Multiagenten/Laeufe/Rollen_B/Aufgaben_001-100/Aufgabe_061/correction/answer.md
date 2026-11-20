Fixed the reviewed RPM ownership defect. A process is now associated with a stored package only when its version, release, and architecture all match. Added regression cases for each mismatch in [redhatbase_test.go](/app/scan/redhatbase_test.go).

Verification passed: `GOPROXY=off GOSUMDB=off go test ./scan` and `git diff --check`.