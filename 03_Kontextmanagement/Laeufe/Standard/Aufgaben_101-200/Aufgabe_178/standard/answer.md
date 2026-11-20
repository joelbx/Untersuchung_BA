Added optional `ident` support to `password_hash` and the password lookup. BCrypt accepts `2`, `2a`, `2y`, and `2b`; the lookup defaults to `2a` and saves the choice with the salt so later runs reproduce it. Non-BCrypt hashes ignore `ident`.

**Verification:** 49 relevant unit tests passed, and `git diff --check` passed.

The local system’s `crypt` library rejects legacy `$2$` hashes. Passlib generates them; the crypt-backed path reports an error when the system library rejects that variant.