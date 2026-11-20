Syslog configuration now has a public [Conf](/app/config/syslog/types.go) type and `Validate()` method in `config/syslog`. The existing value rules and defaults are preserved. Windows validation returns the requested single error when syslog is enabled.

Both platform configurations and the reporter use the new type. `config.SyslogConf` remains an alias for existing callers.

Verification passed: `go test ./config ./config/syslog ./reporter`, Windows config cross compilation, and `git diff --check`.