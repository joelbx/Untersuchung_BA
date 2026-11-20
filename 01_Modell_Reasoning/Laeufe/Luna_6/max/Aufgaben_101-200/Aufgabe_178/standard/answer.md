Implemented BCrypt `ident` support in the filter, shared hashing backends, and password lookup. Lookup defaults to `2a`, saves the ident beside the salt, and reuses saved idents; non-BCrypt hashes ignore the parameter. Added documentation and regression coverage.

Verification: **52 tests passed** with `PYTHONPATH=/app/lib`; `git diff --check` passed.

Native `crypt` support depends on the system library. On this host it generates `2a`, `2y`, and `2b`, but rejects historical `$2$`; passlib supports all four idents.