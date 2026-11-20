Implemented BCrypt ident selection through the password hash filter and both hashing backends. The password lookup accepts and persists `ident`, defaults to `2a` when BCrypt is requested without one, and reuses stored metadata on later runs. Other algorithms ignore `ident`.

Verification passed: 51 tests across the encryption and password lookup unit suites; `git diff --check` passed.