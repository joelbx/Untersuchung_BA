Completed: syslog configuration moved to config/syslog with public Conf and Validate; Windows enabled validation returns the required single error. Main config uses syslog.Conf; config.SyslogConf remains an alias for existing callers.
Verified: focused config validation test, Windows syslog package compile, reporter package build. Full config test result recorded in command output.
