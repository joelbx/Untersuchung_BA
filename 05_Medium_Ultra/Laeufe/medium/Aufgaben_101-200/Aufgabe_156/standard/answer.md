Implemented the no_log sanitization changes in [basic.py](/app/lib/ansible/module_utils/basic.py): `remove_values` now masks sensitive text in values without changing keys or scalar types, and the new `sanitize_keys` masks matching keys, respects ignored and `_ansible` keys, and handles deeply nested containers.

The [uri module](/app/lib/ansible/modules/uri.py) now applies key sanitization to its response when `no_log_values` is populated. I also updated date serialization and the relevant test expectations.

**Verification:** 34 relevant tests passed, and `git diff --check` passed.