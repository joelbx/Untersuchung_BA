FormatString now accepts an optional `encoding` and raises a validation error during `to_py` when a value cannot be encoded. The user-agent setting now requires ASCII; FormatString settings without an encoding remain unrestricted.

Verification: the targeted config suite passed with **1,140 passed, 10 expected failures**. `git diff --check` passed.