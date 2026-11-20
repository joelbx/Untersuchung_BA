# Fault-localization checkpoint

Inspected filter, encryption utility, password lookup, and existing unit/integration tests. No project source or tests edited.

- `get_encrypted_password` in `lib/ansible/plugins/filter/core.py:272-284` has no `ident` argument; it maps `blowfish` to `bcrypt` then calls `passlib_or_crypt`.
- `passlib_or_crypt`, `PasslibHash.hash/_hash`, `CryptHash.hash/_hash`, and `do_encrypt` in `lib/ansible/utils/encrypt.py` have no ident propagation. Passlib's bcrypt default produces `$2b$`; direct passlib `using(ident=...)` accepts 2, 2a, 2y, 2b here. CryptHash hard-codes bcrypt crypt_id 2a but its generic saltstring omits bcrypt cost in the required position, so current crypt-backed bcrypt returns `*0` on this host. Direct system crypt accepts 2a, 2y, 2b, but returns `*0` for 2 here, showing platform support uncertainty.
- Lookup `VALID_PARAMS` in `lib/ansible/plugins/lookup/password.py:120` rejects ident. `_parse_content` / `_format_content` (222-263) only persist salt; `LookupModule.run` (310-355) only forwards salt via `do_encrypt`.
- Existing relevant tests cover salts/rounds and lookup file behavior but no ident. Baseline targeted unit suites: 38 passed.

Likely fix scope: optional ident in filter and all hashing dispatch signatures; apply only for bcrypt in both backends, preserving default filter behavior and valid bcrypt cost formatting in crypt path; lookup term parsing/default `2a` for bcrypt, metadata read/write, and forwarding. Handle old salt-only files and non-bcrypt ident without changing existing results. Verify idents, default behavior, salt/rounds composition, repeat lookup, and backend differences. No implementation made due specialist scope.
