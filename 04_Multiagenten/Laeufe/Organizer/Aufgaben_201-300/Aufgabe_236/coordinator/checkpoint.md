Task complete: deprecated both safe_eval entry points with 2.21 runtime deprecation from the shared function; check_type_dict now tries JSON, then ast.literal_eval, then strict key=value token parsing, returning only dicts. Added changelog and regression coverage for accepted forms, malformed tokens, non-dicts, non-execution, and deprecation messages.
Validation: PYTHONPATH=lib python -m pytest -q test/units/module_utils/common/validation test/units/module_utils/basic/test_safe_eval.py -> 90 passed. git diff --check passed.
Delegation: none.
