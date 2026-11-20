BSD fact gathering now calculates `uptime_seconds` from `sysctl -n kern.boottime` when the boot time is numeric. The shared sysctl parser handles multiline values and mixed valid and malformed lines, logging warnings while retaining valid facts.

Verification: 31 relevant tests passed, and `git diff --check` passed.