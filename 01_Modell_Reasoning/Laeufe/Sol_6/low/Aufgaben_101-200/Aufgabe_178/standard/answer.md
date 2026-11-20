Added optional `ident` support to `password_hash` and the password lookup’s bcrypt workflow. The lookup now stores the selected ident alongside the salt and defaults to `2a` when none is supplied. Non-bcrypt hashing ignores `ident`.

The relevant unit suites passed: **48 tests**. This host’s crypt provider rejects the legacy `2` variant; passlib accepts it.