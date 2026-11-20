# Checkpoint

Task: add optional bcrypt ident to password_hash and password lookup, preserving defaults and salt/rounds behavior.

Initial state: clean working tree. `rg` is unavailable (`/bin/bash: rg: command not found`); using grep/find for local investigation. Following systematic-debugging phases before edits.

Root cause: `get_encrypted_password` and `passlib_or_crypt` have no ident argument; both hash classes omit it. The lookup rejects `ident`, reads/writes only `salt`, and never passes an ident to `do_encrypt`. The crypt backend also emits an invalid bcrypt salt when rounds are omitted or uses the generic rounds syntax when supplied. Existing passlib default is `$2b$`; lookup requires explicit `$2a$` default.

Pattern comparison: SHA crypt uses `$id$rounds=N$salt`, whereas bcrypt requires `$ident$cost$salt`; passlib's bcrypt handler accepts `ident` as a setting. Local crypt accepts 2a/2y/2b, but rejects `$2$` (`crypt.crypt` returned `*0`); passlib accepts all four. Hypothesis: propagating ident only for bcrypt and formatting its crypt salt with cost will produce requested prefixes without changing other algorithms. Added failing tests and ran `PYTHONPATH=lib:test pytest -q test/units/utils/test_encrypt.py -k 'bcrypt_ident_filter or bcrypt_ident_crypt or ident_ignored_for_sha256'`: 8 expected TypeError failures, exit 1.

Implementation: filter and both hash backends accept ident; bcrypt only validates/uses it. Crypt bcrypt salts use `$ident$cost$salt`, default cost 12. Lookup accepts ident, defaults bcrypt to 2a, persists it after salt, reads it on subsequent runs, and updates metadata if explicitly changed. Filter documentation updated.

Verification: `PYTEST_ADDOPTS='' PYTHONPATH=lib:test pytest -q test/units/utils/test_encrypt.py test/units/plugins/lookup/test_password.py test/units/plugins/filter/test_core.py` exited 0: 60 passed. `git diff --check` exited 0. The local crypt implementation does not support legacy `$2$`; it rejects that variant, so the crypt-only backend cannot generate a valid `$2$` hash on this host. Passlib generated all four requested variants locally. The code passes `$2$` to crypt on systems whose crypt implementation supports it and raises an AnsibleError when crypt rejects it.
