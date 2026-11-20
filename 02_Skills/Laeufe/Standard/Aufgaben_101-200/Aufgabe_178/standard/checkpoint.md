# Checkpoint

Implemented optional bcrypt `ident` through the password_hash filter, shared passlib/crypt hasher, and password lookup. The lookup persists `ident` with `salt` and defaults to `2a` for bcrypt. Added documentation and focused tests.

Verification: `PYTHONPATH=lib:test pytest -q test/units/utils/test_encrypt.py test/units/plugins/lookup/test_password.py` — 50 passed. `git diff --check` — passed.

Local platform limitation: its native `crypt.crypt` supports `2a`, `2y`, and `2b`, but returns `*0` for `2`. The crypt backend now raises an AnsibleError for unsupported variants instead of returning that invalid marker. Passlib supports all four variants and was tested locally.
