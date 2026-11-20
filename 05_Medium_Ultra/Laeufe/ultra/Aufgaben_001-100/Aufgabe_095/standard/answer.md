Added the importable `make_date_string` function and made check-in creation use it. Existing instance calls still work. Added `patron_check_ins.is_valid` to require `id` and either `year` or `data`.

The targeted tests pass: **7 passed**. A read-only subagent reviewed the tests and patch.

This checkout has no patron update request handler, so the new validator is available but is not yet called by a live update endpoint.