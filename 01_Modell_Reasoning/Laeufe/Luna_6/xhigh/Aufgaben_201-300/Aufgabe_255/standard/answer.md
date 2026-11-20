Implemented the password lookup fix. `_parse_parameters` is now an instance method, `run()` loads plugin options before parsing, and term values override option defaults. `chars` accepts lists or comma separated strings, including escaped literal commas.

Verification: **33 password lookup unit tests passed**; `git diff --check` passed.

Updated [password.py](/app/lib/ansible/plugins/lookup/password.py:285) and [test_password.py](/app/test/units/plugins/lookup/test_password.py:211).