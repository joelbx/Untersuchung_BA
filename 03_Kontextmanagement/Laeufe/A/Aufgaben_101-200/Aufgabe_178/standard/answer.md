Added optional `ident` support to `password_hash` and the password lookup. BCrypt accepts `2`, `2a`, `2y`, and `2b`; the lookup defaults to `2a` and saves the choice beside the salt for later runs. Non-BCrypt hashes ignore `ident`.

The relevant unit tests pass: **50 passed**. The local `crypt` library does not support `$2$`, so that variant requires passlib on this system.