BSD hardware fact gathering now reports `uptime_seconds` from `sysctl -n kern.boottime` when the boot time is numeric. The shared sysctl parser also preserves multiline values, keeps valid facts when other lines are malformed, and logs the required warnings.

The relevant hardware and sysctl tests pass: **28 passed**.