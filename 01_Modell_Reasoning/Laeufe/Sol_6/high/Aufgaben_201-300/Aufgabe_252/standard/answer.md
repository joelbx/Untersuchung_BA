Updated BSD fact gathering to calculate `uptime_seconds` from numeric `sysctl -n kern.boottime` output, and made the shared sysctl parser retain valid entries, preserve multiline values, and warn on malformed lines or command failures. Added focused tests in [test_sysctl.py](/app/test/units/module_utils/facts/test_sysctl.py).

The focused facts tests passed: **103 passed, 5 skipped**. The broader suite had one timeout test failure unrelated to these changes; that test passed when run alone.

The numeric-only requirement means uptime is omitted if a host returns a structured `kern.boottime` value.