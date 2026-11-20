Task: Reorganize syslog configuration into config/syslog with public Conf and Validate.
Status: Complete. Added public Conf and platform-specific validation in config/syslog, retained config.SyslogConf alias, and updated configuration/reporter to use the dedicated type. Added focused validation tests.
Verification: GOPROXY=off GOTOOLCHAIN=local go test ./config/syslog ./config ./reporter passed. Windows cross-compilation of config/syslog and config test binaries passed. git diff --check passed.
Constraints: Local repository and tests only; no history/index/harness changes.
