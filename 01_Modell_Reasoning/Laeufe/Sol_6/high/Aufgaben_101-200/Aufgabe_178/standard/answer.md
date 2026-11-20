Added optional `ident` support to the `password_hash` filter and both hashing backends. The password lookup now defaults to `2a` for bcrypt and saves the chosen ident beside the salt so later runs reuse it. Other algorithms ignore `ident`.

The affected unit tests pass: **54 passed**. The local system’s `crypt` library rejects the legacy `$2$` variant; passlib supports it.