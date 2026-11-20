# Checkpoint

Task: Deprecate `safe_eval` and make `check_type_dict` parse user input without evaluation.

Completed:
- Added a runtime 2.21 deprecation warning to global `safe_eval`; `AnsibleModule.safe_eval` delegates to it and documents its deprecation.
- Replaced `check_type_dict`'s `safe_eval` fallback with JSON parsing, safe Python literal parsing via `ast.literal_eval`, and validated key=value parsing. Invalid and non-dictionary inputs raise descriptive `TypeError`s.
- Added changelog deprecation entries for both public paths.
- Existing focused tests passed: 24 tests across dictionary validation and `safe_eval`.
- `git diff --check` passed.
