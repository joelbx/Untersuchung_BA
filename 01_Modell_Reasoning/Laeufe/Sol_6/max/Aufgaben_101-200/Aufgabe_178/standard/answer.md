Added optional `ident` support to the [password_hash filter](/app/lib/ansible/plugins/filter/core.py), [hashing backends](/app/lib/ansible/utils/encrypt.py), and [password lookup](/app/lib/ansible/plugins/lookup/password.py). The lookup saves the selected ident with its salt and defaults to `2a` for BCrypt; existing filter defaults remain unchanged.

**Verification:** 68 targeted tests passed, and `git diff --check` passed.

This host’s native `crypt` library rejects ident `2`. That path now raises a clear error instead of returning an invalid hash marker; passlib generates `2` hashes successfully.