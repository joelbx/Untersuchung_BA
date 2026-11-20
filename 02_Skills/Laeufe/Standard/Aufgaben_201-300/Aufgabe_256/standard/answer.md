Fixed `Play` so `load` no longer derives or changes `name`. `get_name` now derives it from the current `hosts` value, and `_validate_hosts` raises the specified parser errors for invalid values.

Added regression tests. The full playbook unit suite passed: **248 tests**.