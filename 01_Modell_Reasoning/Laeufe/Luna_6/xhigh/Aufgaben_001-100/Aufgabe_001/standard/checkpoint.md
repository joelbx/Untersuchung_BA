# Checkpoint

Task: Reorganize syslog configuration into `config/syslog` and preserve platform-specific validation behavior.

Completed:
- Added public `syslog.Conf` with Protocol, Host, Port, Severity, Facility, Tag, Verbose, and Enabled fields.
- Moved Unix validation and severity/facility parsing into the `config/syslog` package.
- Added Windows validation that rejects enabled syslog with `windows not support syslog` and returns no errors when disabled.
- Updated app config and reporter references to use `syslog.Conf`; Windows config now validates syslog too.
- Updated the existing validation test to use the dedicated type and account for Windows rejection behavior.

Verification:
- `go test ./config/... ./reporter` passed.
- `GOOS=windows GOARCH=amd64 go test -c -o /tmp/vuls-config.test.exe ./config` cross compiled successfully.
- `git diff --check` passed.
