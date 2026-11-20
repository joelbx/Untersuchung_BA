Updated [BSD hardware fact gathering](/app/lib/ansible/module_utils/facts/hardware/freebsd.py) to calculate `uptime_seconds` from a numeric `sysctl -n kern.boottime` result. FreeBSD, DragonFly, NetBSD, OpenBSD, and Darwin now include the fact when that result is valid. The [shared sysctl parser](/app/lib/ansible/module_utils/facts/sysctl.py) now handles `=`, `:`, and space delimiters, preserves multiline values, and warns while continuing past malformed lines.

All 35 focused tests pass. The full facts suite had one timeout test failure; that test passed when rerun alone.

**Limitation:** Structured `kern.boottime` output, including output FreeBSD may produce, is omitted under the requested numeric-only rule.