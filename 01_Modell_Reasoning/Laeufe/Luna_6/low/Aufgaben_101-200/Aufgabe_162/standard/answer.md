Added optional `encoding` validation to `FormatString`, using the same validation and error messages as `String`. The user agent setting now requires ASCII, and tests cover both rejection and the unconstrained default.

Validation: `pytest -q tests/unit/config/test_configtypes.py` — 1105 passed, 10 xfailed. `git diff --check` passed.