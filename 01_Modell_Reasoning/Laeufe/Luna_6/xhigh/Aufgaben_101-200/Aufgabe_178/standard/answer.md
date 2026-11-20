Implemented bcrypt `ident` support for `2`, `2a`, `2y`, and `2b` across the password hash filter and both hashing backends. The password lookup defaults to `2a` and saves/restores the ident alongside its salt. Updated documentation and added a changelog fragment.

`git diff --check` passed. The focused unit suites passed: **52 tests**.

Key files: [core.py](/app/lib/ansible/plugins/filter/core.py), [encrypt.py](/app/lib/ansible/utils/encrypt.py), [password.py](/app/lib/ansible/plugins/lookup/password.py).