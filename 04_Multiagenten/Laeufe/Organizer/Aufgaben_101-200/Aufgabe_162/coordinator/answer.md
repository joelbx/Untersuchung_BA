FormatString now accepts an optional `encoding` and validates it during `to_py`, using the same clear validation error as String. The HTTP user agent setting now requires ASCII. FormatString settings without an encoding constraint still accept Unicode.

Tests passed: 1,139 focused tests and 390 configuration integration tests. The broader suite could not complete: a web settings test requires `PyQt5.QtWebKit`, which is unavailable in this environment.

No delegation was used.