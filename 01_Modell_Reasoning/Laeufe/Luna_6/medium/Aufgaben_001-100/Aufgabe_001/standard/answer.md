Added the public `config/syslog.Conf` type and platform-specific `Validate()` methods. Unix validation preserves the existing defaults and checks; Windows returns the required unsupported error when enabled. The existing `config.SyslogConf` name remains available as an alias.

Verification passed: `go test ./config/... ./reporter/...` and `GOOS=windows GOARCH=amd64 go test ./config/syslog`.