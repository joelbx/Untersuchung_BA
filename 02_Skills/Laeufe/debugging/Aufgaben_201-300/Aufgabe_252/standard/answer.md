Updated the FreeBSD, NetBSD, and OpenBSD fact collectors to calculate `uptime_seconds` from numeric output of `sysctl -n kern.boottime`. The shared sysctl parser now retains valid entries when other lines are malformed, preserves multiline values, and warns on parse or command failures.

Verification: 119 tests passed, 5 skipped; `git diff --check` passed.