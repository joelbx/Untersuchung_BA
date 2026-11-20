# Checkpoint

Task: Add selectable bcrypt idents to the password_hash filter and password lookup workflow.

Implemented:
- Added optional `ident` to `get_encrypted_password`, passlib and crypt hashing, and `do_encrypt`.
- Supported bcrypt identifiers `2`, `2a`, `2y`, and `2b`; non-bcrypt algorithms ignore ident. Omitted ident retains the filter backend's previous default.
- Password lookup accepts `ident`, defaults new bcrypt hashes to `2a`, and stores/restores the ident with its salt.
- Updated filter and lookup docs, added a changelog fragment, and added coverage for variant selection, lookup defaults, and persisted metadata.

Verification: `git diff --check` passed. `PYTHONPATH=lib:test python -m pytest -q test/units/utils/test_encrypt.py test/units/plugins/lookup/test_password.py` passed (52 tests).
