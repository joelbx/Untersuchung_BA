# Checkpoint

- Task: add bcrypt `ident` support to the `password_hash` filter and password lookup workflow.
- Initial state: working tree clean; repository instructions found no `AGENTS.md`.
- Implemented `ident` propagation through the filter and both hashing backends, plus lookup parsing, persistence, and BCrypt's `2a` lookup default.
- Added focused tests and filter/lookup documentation.
- Final verification: 63 relevant unit tests passed; `git diff --check` passed.
- Limitation: the local system `crypt` library rejects BCrypt ident `2`; that backend now reports an explicit error when it cannot produce the requested variant. Passlib produced all four requested idents in the local tests.
