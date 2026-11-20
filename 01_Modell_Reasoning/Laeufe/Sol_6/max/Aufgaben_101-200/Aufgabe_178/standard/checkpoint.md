Task: Add BCrypt ident support to password_hash and password lookup.

Progress: Implemented ident propagation through the filter, shared hasher, and password lookup; added BCrypt metadata persistence, documentation, changelog, and unit tests. Final targeted suite: 68 passed. git diff --check passed.

Remaining platform limitation: This host's native crypt library rejects ident 2, so the crypt path raises a clear error instead of returning an invalid hash marker. Passlib generates ident 2 successfully.
