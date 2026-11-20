# Checkpoint

Implemented BCrypt ident support across the password hash filter, both hashing backends, and the password lookup workflow.

- Filter API accepts `ident` and forwards it to the hasher. Omitting it preserves passlib defaults.
- Both passlib and crypt hashing paths support `2`, `2a`, `2y`, and `2b`; non-BCrypt algorithms ignore the option.
- Password lookup defaults omitted BCrypt ident to `2a`, reads and writes ident alongside salt, and reuses stored ident on subsequent runs.
- Added tests for the variant prefixes, invalid values, lookup defaults, and persisted metadata.

Verification: `PYTHONPATH=lib:test python -m pytest -q test/units/utils/test_encrypt.py test/units/plugins/lookup/test_password.py` passed (51 tests); `git diff --check` passed.
