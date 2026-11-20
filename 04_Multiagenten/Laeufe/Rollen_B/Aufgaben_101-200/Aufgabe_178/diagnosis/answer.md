The issue spans three files:

- [core.py](/app/lib/ansible/plugins/filter/core.py:272): `get_encrypted_password` has no `ident` argument to forward.
- [encrypt.py](/app/lib/ansible/utils/encrypt.py:101): neither backend accepts an ident. Passlib currently defaults to `$2b$`. The crypt path hard-codes `2a` and builds a BCrypt salt string without a cost field; it returned `*0` on this host.
- [password.py](/app/lib/ansible/plugins/lookup/password.py:120): the lookup rejects `ident`, stores only `salt`, and forwards only `salt` when hashing.

A fix needs to carry `ident` through the filter and hashing calls, apply it only to BCrypt, and persist the lookup choice alongside the salt while reading existing salt-only files. The lookup’s unspecified BCrypt ident should be `2a`; the filter’s unspecified behavior should stay as it is. Platform support for crypt-backed `$2$` remains uncertain: the system `crypt` on this host returned `*0` for that variant.

The existing relevant unit suites pass (**38 tests**), but none cover ident. I recorded the diagnosis in `.codex-role-output/checkpoint.md`. No project source or tests were changed under this fault-localization scope.