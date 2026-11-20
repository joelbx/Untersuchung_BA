BSD hardware collectors now gather `uptime_seconds` from numeric `sysctl -n kern.boottime` output. The shared [sysctl parser](/app/lib/ansible/module_utils/facts/sysctl.py) also handles platform delimiters, multiline values, malformed lines, and command failures.

Verification: 60 focused tests passed. The broader facts suite passed with one timing-sensitive timeout test excluded; that test passed on its own. One agent added regression tests, and another reviewed the implementation; I integrated and verified their work.

On FreeBSD versions that return a structured boot time instead of a numeric string, the fact is omitted as required by the numeric-only rule.