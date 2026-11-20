Implemented the `safe_eval` deprecation and deterministic dictionary parsing.

- `safe_eval` records a runtime deprecation for version 2.21. The `AnsibleModule` wrapper delegates to it.
- `check_type_dict` tries JSON, then restricted literal parsing, then strict comma or whitespace separated `key=value` parsing. It returns dictionaries only and raises descriptive `TypeError`s for invalid inputs.
- Added changelog entries for both requested APIs.

**Verification:** 115 existing tests passed; direct checks confirmed parsing behavior and deprecation records from both entry points. `git diff --check` passed.

Files: [validation.py](/app/lib/ansible/module_utils/common/validation.py:42), [basic.py](/app/lib/ansible/module_utils/basic.py:1204), [changelog fragment](/app/changelogs/fragments/deprecate-safe-eval.yml:1).