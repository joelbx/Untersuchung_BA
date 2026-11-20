FormatString now validates an optional encoding during `to_py`, using the same validation behavior as String. The [user agent setting](/app/qutebrowser/config/configdata.yml) requires ASCII; FormatString settings without an encoding constraint keep their existing behavior.

The relevant configuration suites passed: **1,137 passed, 10 expected failures**. A final focused run passed all 14 tests.