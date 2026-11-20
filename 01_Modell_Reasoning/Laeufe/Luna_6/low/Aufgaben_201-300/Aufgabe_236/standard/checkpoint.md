# Checkpoint

Task: Deprecate `safe_eval` and make `check_type_dict` parse dictionaries without evaluation.

Initial state: working tree clean. `rg` is unavailable in this environment; using `find` and `grep` for repository inspection.

Next: inspect implementations/tests/changelog conventions, make targeted edits, run relevant existing tests.

Completed changes:
- Added target 2.21 runtime deprecation records to both `safe_eval` entry points; the `AnsibleModule` wrapper delegates to the global function.
- Updated `check_type_dict` to parse JSON, then safe dictionary literals via `ast.literal_eval`, or deterministic key=value tokens. It returns only dictionaries and raises descriptive `TypeError`s for malformed forms.
- Added `changelogs/fragments/deprecate-safe-eval.yml`.

Verification: `python -m pytest -q test/units/module_utils/common/validation/test_check_type_dict.py test/units/module_utils/basic/test_safe_eval.py` passed (24 tests); `git diff --check` passed.
