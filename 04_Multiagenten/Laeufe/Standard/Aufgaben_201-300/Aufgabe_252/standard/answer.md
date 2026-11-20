Updated the FreeBSD, NetBSD, and OpenBSD hardware collectors to gather `uptime_seconds` from numeric `sysctl -n kern.boottime` output. The shared sysctl parser now preserves multiline values, accepts the required delimiters, warns on malformed lines, and continues parsing valid entries.

Verification: 106 targeted tests passed, 5 skipped; `git diff --check` passed.