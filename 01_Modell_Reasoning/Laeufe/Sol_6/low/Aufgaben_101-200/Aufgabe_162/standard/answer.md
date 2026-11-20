FormatString now accepts an optional `encoding` parameter and validates input during `to_py`, using the same validation error as String. The user agent setting now requires ASCII; FormatString configurations without an encoding constraint retain their previous behavior.

The relevant existing tests passed: 23 FormatString tests and 31 config data tests.