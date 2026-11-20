Added optional BCrypt `ident` support to `password_hash`, both hashing backends, and the password lookup. The lookup defaults to `2a`, saves the chosen ident beside the salt, and reads existing salt-only files.

The relevant local suites passed: **56 tests**. This host’s crypt library rejects `$2$`; passlib supports all four requested idents.