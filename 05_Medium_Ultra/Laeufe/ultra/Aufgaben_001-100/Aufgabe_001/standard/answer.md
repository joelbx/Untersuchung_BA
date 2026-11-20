Syslog configuration now lives in [config/syslog.Conf](/app/config/syslog/types.go:3), with public validation that preserves the existing non-Windows rules and rejects enabled syslog on Windows. Config and the reporter use the new type; `config.SyslogConf` remains a compatibility alias.

I delegated the package implementation and a reference audit to two subagents, then integrated and verified their work. Tests passed for `./config/syslog`, `./config`, `./reporter`, and `./subcmds` with downloads disabled. The syslog and config test binaries also cross compiled for Windows.

The Windows reporter cross compile remains blocked by an unrelated existing `config.TrivyOpts` reference in `detector/javadb`.