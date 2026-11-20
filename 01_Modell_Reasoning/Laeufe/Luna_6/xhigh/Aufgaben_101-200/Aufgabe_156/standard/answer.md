Implemented the no_log sanitization changes:

- [basic.py](/app/lib/ansible/module_utils/basic.py:460): `remove_values` masks sensitive substrings in values only, preserves keys and scalar values, and traverses deeply nested containers iteratively. Added `sanitize_keys` for recursive key masking, exact-match sentinel replacement, `_ansible` keys, and ignored keys.
- [uri.py](/app/lib/ansible/modules/uri.py:394): sanitizes responses only when `module.no_log_values` is set, using `NO_MODIFY_KEYS`.
- [converters.py](/app/lib/ansible/module_utils/common/text/converters.py:262): preserves date serialization after `remove_values` stopped converting date objects.
- Updated the focused unit tests for the new behavior.

**Verification:** Focused tests passed: 32 passed. Compilation and `git diff --check` passed. The full `test/units/module_utils/basic` run had 22 failures; the first failure reports warnings left by earlier argument-spec tests, and later tests see accumulated warning/deprecation output.