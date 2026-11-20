Implemented the password lookup fix. Parameter parsing now lives in `LookupModule`, loads plugin options before parsing, honors inline values first, supports list and comma separated `chars`, and keeps seeded output deterministic. Updated the option docs and added regression coverage.

Verification: `PYTHONPATH=lib:test/units pytest -q test/units/plugins/lookup/test_password.py` passed (33 tests); `git diff --check` passed.

- [password.py](/app/lib/ansible/plugins/lookup/password.py:284)
- [test_password.py](/app/test/units/plugins/lookup/test_password.py:211)