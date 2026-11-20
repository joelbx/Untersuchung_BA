Task: Deprecate safe_eval in module_utils and make check_type_dict deterministic and non-evaluating.
Status: complete.
Changes: safe_eval emits Ansible deprecation notice for 2.21; AnsibleModule wrapper is documented deprecated and delegates to it. check_type_dict parses JSON, then safe literals, then validated key=value pairs; invalid and non-dictionary input raises TypeError. Added changelog fragment and regression tests.
Verification: PYTHONPATH=lib python -m pytest -q test/units/module_utils/common/validation test/units/module_utils/basic/test_safe_eval.py (90 passed). git diff --check passed.
