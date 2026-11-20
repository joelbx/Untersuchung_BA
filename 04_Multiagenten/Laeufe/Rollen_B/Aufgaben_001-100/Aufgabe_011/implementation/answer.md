Implemented the fixes in the checked-out repository: `_UNSET` handling, legacy YAML constructors, `None` Templar overrides, lookup messages, deprecation configuration and messaging, Boolean `timedout` results, and early CLI error help text.

Verification: 314 focused unit tests passed, 1 skipped. Direct edge checks passed, and `git diff --check` found no issues.