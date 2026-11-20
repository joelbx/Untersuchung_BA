Added optional BCrypt `ident` support to the `password_hash` filter and hashing backends. The password lookup now defaults `encrypt=bcrypt` to `2a` and saves the selected ident alongside the salt so later runs reuse it. Non BCrypt hashes ignore `ident`.

Verification: 52 relevant unit tests passed, and `git diff --check` passed.