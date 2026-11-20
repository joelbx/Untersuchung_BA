# Checkpoint

Task: add bcrypt `ident` support to password hashing filter, backends, and password lookup.

Initial environment: `/app`; `rg` is unavailable (`/bin/bash: rg: command not found`). Used local `grep`/`find` instead.

Implemented: optional `ident` propagation from `password_hash` and password lookup through passlib and crypt hashers; bcrypt lookup metadata stores and reuses `ident`, defaulting to `2a`. Added relevant tests and documentation.

Verification: `PYTHONPATH=lib:test python -m pytest -q test/units/utils/test_encrypt.py test/units/plugins/lookup/test_password.py test/units/plugins/filter/test_core.py` exited 0 with 59 passed. `git diff --check` exited 0.

Host limitation: Python `crypt.crypt('foo', '$2$12$123456789012345678901u')` returned `*0` in a local probe; this host's native crypt cannot generate the legacy `$2$` variant. The crypt path passes the requested `$2$` salt and raises an error if native crypt rejects it. Passlib generated `$2$` successfully. No downloads were attempted.
