Issue: scalar string values targeting []string should split on all whitespace, including for YAML and environment sourced config; empty strings should decode as an empty slice, while arrays and non-string values remain untouched.

Plan: inspect internal/config decoding and tests, update the decode hook with scoped string-to-[]string behavior, add/adjust focused regression tests, and run the relevant existing config tests.
