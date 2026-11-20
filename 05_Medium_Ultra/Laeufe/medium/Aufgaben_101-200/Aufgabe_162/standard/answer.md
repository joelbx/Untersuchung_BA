`FormatString` now accepts an optional encoding and raises a clear validation error during `to_py` when a value cannot be encoded. The user agent setting now requires ASCII; other `FormatString` settings keep their existing behavior.

Verification: 1,138 config tests passed, with 10 expected failures and one deselection. The 15 focused tests passed.