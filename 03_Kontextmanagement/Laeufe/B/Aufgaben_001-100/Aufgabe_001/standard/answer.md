Syslog configuration now has a public [syslog.Conf](/app/config/syslog/types.go) with its own validation. Report configuration uses it on Linux and Windows, and a compatibility alias preserves existing callers. Windows validation returns the specified single error when syslog is enabled.

The relevant Linux tests pass, and the Windows syslog and config packages cross compile successfully.