# Checkpoint

Task: Add bcrypt ident selection to password_hash filter, hashing backends, and password lookup.
Status: Implemented and verified.

Changes:
- Added optional ident propagation through filter and hashing helpers; bcrypt accepts 2, 2a, 2y, 2b.
- Crypt backend now formats bcrypt salts with cost and requested ident. For legacy 2 unsupported by system crypt, uses installed passlib when available.
- Password lookup accepts ident, defaults bcrypt to 2a, stores ident with salt, and reuses saved ident.
- Added unit coverage for variants, backends, non-bcrypt behavior, and lookup persistence.

Validation: 52 targeted unit tests passed; git diff --check passed.
