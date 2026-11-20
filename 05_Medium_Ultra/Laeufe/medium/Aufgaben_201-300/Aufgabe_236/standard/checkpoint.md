Task: deprecate safe_eval entry points and replace check_type_dict evaluation with deterministic parsing.
Status: completed implementation and tests.
Changes: safe_eval records an Ansible deprecation for version 2.21; AnsibleModule.safe_eval delegates and is documented deprecated; check_type_dict parses JSON, dict literals, then validated key=value pairs; changelog and focused tests added.
Verification: PYTHONPATH=lib pytest -q test/units/module_utils/common/validation test/units/module_utils/basic/test_safe_eval.py (90 passed); git diff --check passed.
Constraints observed: local code/tests only; git history/index and harness config unchanged.
