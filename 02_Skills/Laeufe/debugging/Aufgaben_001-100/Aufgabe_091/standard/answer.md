Implemented `isoneof` and `isnotoneof` for string and numeric constraints. Create and update validation now checks JSON array types and enforces the 100-item limit, with regression tests covering matching, invalid lists, and the limit boundary.

The relevant package tests and `git diff --check` pass.