# Checkpoint

Task complete: BCrypt `ident` support is implemented for the `password_hash` filter and password lookup.

Changes: added optional ident propagation through the filter and shared passlib/crypt hasher; supported `2`, `2a`, `2y`, and `2b`; preserved passlib defaults when omitted and ignored ident for non-BCrypt hashes. The password lookup defaults new BCrypt requests to `2a`, saves ident beside salt, and restores stored idents while remaining compatible with salt-only files. Added documentation and regression tests.

Verification: `PYTHONPATH=/app/lib python -m pytest -q test/units/utils/test_encrypt.py test/units/plugins/lookup/test_password.py` passed (52 passed). `git diff --check` passed. Also exercised real crypt-backed output for idents `2a`, `2y`, and `2b` with salt and rounds; all prefixes matched.
