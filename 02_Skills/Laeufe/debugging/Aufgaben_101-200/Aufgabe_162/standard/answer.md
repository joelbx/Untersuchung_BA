`FormatString` now accepts an optional `encoding` parameter and raises a validation error during `to_py` when a value cannot be encoded. The user agent setting now requires ASCII; format strings without an encoding constraint retain their previous behavior.

The config type and config data suites passed: **1,138 passed, 10 expected failures**.