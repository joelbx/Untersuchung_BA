Implemented the atomic move permission fix. New files use `_DEFAULT_PERM = 0o0600`; modules that accept `mode` warn at result formatting when it was omitted, and an explicit mode application clears the path from warning tracking.

Verification: **65 unit tests passed** across atomic move, mode setting, and result formatting. `git diff --check` passed.