Added the public `config/syslog.Conf` type and platform-specific `Validate()` methods. Unix validation preserves the existing defaults and rules; Windows returns the specified single error when syslog is enabled. `config.SyslogConf` remains available as a compatibility alias.

Verified with `go test ./config/...`, a Windows cross compile of `config/syslog`, and `git diff --check`.