FormatString now accepts an optional `encoding` and rejects characters it cannot encode during `to_py`, with a validation error. The user agent setting requires ASCII; FormatString settings without an encoding constraint keep their existing behavior.

Verification: the config type and config data suites passed (1,139 passed, 10 expected failures).