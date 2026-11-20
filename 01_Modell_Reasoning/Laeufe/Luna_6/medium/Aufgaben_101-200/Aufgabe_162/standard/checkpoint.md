# Checkpoint

Task: resolve FormatString encoding validation for HTTP header configuration.

Initial inspection: repository is `/app`; `rg` is unavailable, so use `find` and `grep` to locate converters and tests. Next: identify String/FormatString implementations, compare validation and existing test coverage, then implement and run focused tests.
