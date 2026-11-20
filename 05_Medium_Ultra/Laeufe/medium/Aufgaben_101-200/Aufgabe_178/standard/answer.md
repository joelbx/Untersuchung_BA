Added BCrypt `ident` support to `password_hash` and the password lookup. The filter accepts `2`, `2a`, `2y`, and `2b`; the lookup stores the choice with the salt and defaults to `2a`. Other hash types ignore `ident`.

The relevant tests pass: **54 passed**. A host with neither passlib nor native `$2$` support cannot generate a valid legacy `$2$` hash.