Added the public `syslog.Conf` type and platform-specific validation in [config/syslog]( /app/config/syslog/types.go ). Updated the app configuration and reporter to use it, and adjusted the existing validation test for Windows behavior.

Verified with `go test ./config/... ./reporter`, a Windows cross compile of the config tests, and `git diff --check`.