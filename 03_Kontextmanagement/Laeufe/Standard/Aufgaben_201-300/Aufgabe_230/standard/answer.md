Updated [scripts/affiliate_server.py](/app/scripts/affiliate_server.py) with `PrioritizedIdentifier` for ISBNs and ASINs. Queue items now deduplicate by identifier, serialize all fields, and use `stage_import` to control import staging. The former `PrioritizedISBN(isbn=...)` form remains supported.

Verification: all 20 affiliate server tests pass; Ruff and `git diff --check` pass.