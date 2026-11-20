Updated BSD fact gathering to calculate `uptime_seconds` from a numeric `sysctl -n kern.boottime` result. The shared sysctl parser now preserves multiline values, continues after malformed lines, and logs the required warnings.

Relevant tests: **105 passed, 5 skipped**. `git diff --check` passed. No delegation was used.