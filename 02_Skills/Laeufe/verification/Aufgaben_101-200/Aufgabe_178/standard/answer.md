Added optional bcrypt `ident` support to `password_hash` and both hashing backends. The password lookup now saves the selected ident beside the salt, reuses it on later runs, and defaults to `2a` for bcrypt. Documentation and regression tests were updated.

Verification: **59 relevant tests passed**; `git diff --check` passed.

This host’s native `crypt` rejects the legacy `$2$` variant, so that variant requires a backend that supports it. Passlib generated `$2$` successfully.