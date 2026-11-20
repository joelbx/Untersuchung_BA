Implemented BSD uptime gathering through the existing OpenBSD hardware facts path. The collector now omits `uptime_seconds` when the boot time is missing or nonnumeric, and the shared sysctl parser handles `=`, `:`, and whitespace delimiters, preserves indented multiline values, and warns on malformed lines while continuing.

A missing `sysctl` binary raises `ValueError`; execution errors and nonzero exits return an empty dictionary with a warning. The OpenBSD collector already merges uptime with its other hardware facts, so that merge remains intact.

Relevant existing tests passed: **92 passed, 5 skipped**.