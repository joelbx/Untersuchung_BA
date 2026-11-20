`FormatString` now accepts an optional encoding and raises a clear validation error during `to_py` when a value cannot be encoded. The user agent setting requires ASCII; other format strings remain unrestricted.

Verification: 1,139 configuration tests passed, with 10 expected failures.