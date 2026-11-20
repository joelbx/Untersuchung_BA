# Checkpoint

Task complete: `safe_eval` deprecation and deterministic `check_type_dict` parsing are implemented.

Changes:
- Global `safe_eval` records a runtime deprecation for version 2.21; the `AnsibleModule` wrapper documents deprecation and delegates to it.
- `check_type_dict` tries JSON, then `ast.literal_eval`, and accepts strict comma or whitespace separated key=value pairs. Every parsed result must be a dictionary; malformed tokens raise descriptive `TypeError`s.
- Added changelog entries for both requested entry points.

Verification:
- `pytest -q test/units/module_utils/common/validation test/units/module_utils/common/parameters test/units/module_utils/basic/test_safe_eval.py`: 115 passed.
- Direct checks exercised JSON, Python dictionary literals, quoted key=value values, malformed/non-dictionary inputs, a non-executed expression, and 2.21 deprecations from both entry points.
- `git diff --check` passed.
