# Checkpoint

Task: Deprecate `safe_eval` and make `check_type_dict` parse inputs without evaluation.

Status: Implemented deprecation signaling for both safe_eval entry points, deterministic dictionary parsing, changelog fragment, and regression tests.

Checks:
- `PYTHONPATH=lib python -m pytest -q test/units/module_utils/common/validation test/units/module_utils/basic/test_safe_eval.py` passed: 91 tests.
- `git diff --check` passed.
- `PYTHONPATH=lib python -m pytest -q test/units/module_utils/basic` failed: 24 failed, 296 passed. Failures involve shared warning/deprecation state and exit_json expectations. An isolated existing test also fails: `PYTHONPATH=lib python -m pytest -q test/units/module_utils/basic/test_deprecate_warn.py -x --tb=short` reports warnings `warning1`, `warning2` remaining from its preceding test. The broader suite's failures are outside the changed parsing path; their baseline status has not been established.
