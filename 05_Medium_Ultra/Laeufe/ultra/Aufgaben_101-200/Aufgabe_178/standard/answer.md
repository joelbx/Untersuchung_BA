Added optional BCrypt `ident` support (`2`, `2a`, `2y`, `2b`) to [password_hash](/app/lib/ansible/plugins/filter/core.py) and both hashing backends. The [password lookup](/app/lib/ansible/plugins/lookup/password.py) now defaults to `2a` for bcrypt and saves the chosen ident with the salt for repeatable runs. Non-BCrypt hashing ignores `ident`.

Hashing, lookup, and independent review were delegated, then integrated and verified. The relevant unit tests passed: **74 passed**. `git diff --check` was clean.

This system’s `crypt` backend cannot generate `$2$`; it now raises an error instead of returning an invalid hash. Passlib produced all four requested prefixes.