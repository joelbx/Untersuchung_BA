Task: Add BCrypt ident selection to password_hash filter and password lookup workflow.

Plan: Trace filter/hash implementations and lookup metadata; preserve existing defaults except lookup bcrypt's required 2a default; implement propagation across passlib and crypt backends; update/add existing tests and run targeted tests.
