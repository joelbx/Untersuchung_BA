# Checkpoint

Task: Add optional bcrypt ident support to password_hash and password lookup.
Status: Implemented filter and backend propagation, BCrypt cost formatting for crypt, lookup parsing/persistence/default 2a, documentation, and focused tests.
Verification: PYTHONPATH=lib:test python -m pytest -q test/units/utils/test_encrypt.py test/units/plugins/lookup/test_password.py (54 passed); git diff --check passed.
Platform note: Local crypt rejects the legacy 2 ident; passlib supports it. Crypt path passes the requested ident to crypt and reports unsupported variants rather than returning an invalid hash.
