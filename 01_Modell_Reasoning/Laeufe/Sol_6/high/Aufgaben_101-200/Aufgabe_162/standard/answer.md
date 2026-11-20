`FormatString` now accepts an optional `encoding` parameter and validates it during `to_py`. The user agent setting requires ASCII; format strings without an encoding constraint keep their previous behavior.

Tests passed: 1,140 config type/data tests and 206 config file tests. The web settings suite could not complete because `PyQt5.QtWebKit` is unavailable in this environment.