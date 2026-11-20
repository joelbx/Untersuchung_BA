Implemented BCrypt `ident` support across the `password_hash` filter and password lookup.

The filter accepts `2`, `2a`, `2y`, and `2b`, passes the choice through both hashing backends, and preserves existing behavior when omitted. The lookup defaults bcrypt to `2a` and saves the ident with the salt so later runs can reproduce it. Added filter documentation and coverage for both backends and lookup metadata.

Verified with `PYTHONPATH=lib python -m pytest -q test/units/utils/test_encrypt.py test/units/plugins/lookup/test_password.py`: **41 passed**. `git diff --check` also passed.