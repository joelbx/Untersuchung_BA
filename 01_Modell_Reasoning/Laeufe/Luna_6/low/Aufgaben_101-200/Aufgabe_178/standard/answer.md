Implemented BCrypt ident support in the filter and password lookup workflow.

`get_encrypted_password(...)` now passes `ident` through to both hashing backends. BCrypt accepts `2`, `2a`, `2y`, and `2b`; other algorithms ignore the parameter. The lookup defaults to `2a` for BCrypt and persists the ident with the salt metadata.

Verification: the existing encrypt and password lookup unit suites passed (38 tests), and `git diff --check` passed.