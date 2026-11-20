# Checkpoint

Task: Deprecate `safe_eval`, remove its use from dictionary validation, and add a safe deterministic parser for JSON and simple key=value input.

Initial state: Repository inspection started in `/app`. `rg` is unavailable in this environment, so use `find` and `grep` for local source/test discovery.

Constraints: Use repository code and existing tests only; do not alter git history, index baseline, or harness configuration.

Implementation complete:
- `safe_eval` now records a 2.21 deprecation; `AnsibleModule.safe_eval` documents the deprecated compatibility wrapper and delegates to it.
- `check_type_dict` tries JSON, then `ast.literal_eval`, then validated key=value parsing. Only dictionaries are returned from JSON/literal parsing; malformed pairs raise descriptive `TypeError`s.
- Added changelog entries for both deprecated entry points.

Verification: `python -m pytest -q test/units/module_utils/common/validation/test_check_type_dict.py test/units/module_utils/basic/test_safe_eval.py` passed (24 tests). `git diff --check` passed.
