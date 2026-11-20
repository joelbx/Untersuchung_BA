Task: fix BSD uptime facts and sysctl parsing in /app.
Status: complete. Shared sysctl parsing handles delimiters, multiline values, warnings, and command failures. Uptime from sysctl -n kern.boottime is integrated into FreeBSD, NetBSD, and OpenBSD hardware facts. Targeted tests: 106 passed, 5 skipped.
