Implemented the dedicated `config/syslog` package with public `Conf` and platform-specific `Validate()` methods. Unix validation preserves the existing defaults and accepted values; Windows returns the required error when syslog is enabled. Kept `config.SyslogConf` as a compatibility alias and added syslog to Windows report validation.

Verification passed:

- `go test ./config/... ./reporter/...`
- `GOOS=windows GOARCH=amd64 go test -exec=true -run '^$' ./config/...`

The checkpoint is in `.codex-role-output/checkpoint.md`.